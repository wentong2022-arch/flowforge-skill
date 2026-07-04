#!/usr/bin/env python3
"""FlowForge draw.io validator.

Deterministically checks a .drawio file against FlowForge's quality rules:
well-formed XML, unique ids, dangling arrow references, orthogonal edge style,
canvas bounds, node overlap, z-order (containers before children), font sizes,
text-fit estimates, and theme color compliance.

Usage:
    python3 validate.py <file.drawio> [--theme tech-blue|morandi|mint|terracotta|indigo]

Exit code 0 = no errors (warnings allowed), 1 = errors found, 2 = cannot read/parse.
Stdlib only — no dependencies.
"""

import argparse
import html
import re
import sys
import xml.etree.ElementTree as ET

# ---------------------------------------------------------------- themes ----
# Keep in sync with themes.md. Sets contain every fill/stroke/text/bg color of a theme.
THEMES = {
    "tech-blue": {
        "#2D3748", "#3F72D9", "#45815F", "#5B8DEF", "#5BA87C", "#5BA8A0", "#68778D", "#8496AE", "#8B7EC4", "#95A5B9", "#CBD5E0", "#CC9C2F", "#CE4848", "#D05050", "#D6E4F9", "#E29057", "#E6F5EC", "#E8F0FE", "#E8F4F2", "#EDE8F5", "#EDF2F7", "#F1F5FB", "#F2FAF5", "#F3F9F8", "#F5F3FA", "#F5F7FA", "#FBF5F1", "#FDE8E8", "#FFF0E5", "#FFF8E1",
    },
    "morandi": {
        "#4A4A4A", "#5B7F5D", "#767676", "#7B6B8A", "#88AD8B", "#8DA898", "#8FA5BA", "#90AB8C", "#9C9387", "#A098B5", "#A26666", "#AFA190", "#B09DB8", "#B5A172", "#B89090", "#C5BFB8", "#D4DFD8", "#D6E4D8", "#D8E2EA", "#DBD8E6", "#DDE6DB", "#E2D8E6", "#E8D6D6", "#E8E2D2", "#EDE8E1", "#EDEAE6", "#F3F6F9", "#F3F9F4", "#F5F3F9", "#F9F3F3", "#F9F7F3",
    },
    "mint": {
        "#1A3A3A", "#238377", "#2A9D8F", "#368545", "#4AADA5", "#4AAE5C", "#54B49D", "#5A7A7A", "#5E7C76", "#6A9F91", "#71AF9D", "#7AA0C0", "#B0D0C5", "#C74E4E", "#C85050", "#CCF0E8", "#D19A34", "#D4F0D8", "#D8F0EE", "#E0E8F0", "#E0F5F0", "#E3921F", "#E8F0ED", "#F0F7F5", "#F2FAF3", "#F2FBF8", "#F3F6F9", "#FBF1F1", "#FBF7F1", "#FCE4E4", "#FFF2D6", "#FFF4E6",
    },
    "terracotta": {
        "#3D2C1E", "#657E44", "#87725E", "#897259", "#8EA06A", "#996D45", "#9A9478", "#A05040", "#A89088", "#A89279", "#B07060", "#B07D4F", "#B28D5C", "#BD9E74", "#C39F3E", "#D0C4B0", "#D4956A", "#E8DDD0", "#E8E0D8", "#E8E4DA", "#E8ECDA", "#F0DCD0", "#F0E0CC", "#F5ECD0", "#F5EDE3", "#F5F0E8", "#F8F9F3", "#F9F6F3", "#FAF0E4", "#FBF5F1", "#FBF7F1", "#FBF9F1",
    },
    "indigo": {
        "#1E293B", "#29864E", "#3AA06A", "#3B82F6", "#4080A0", "#4F62B0", "#637895", "#64748B", "#6B50B0", "#7C3AED", "#7C8DB5", "#8596AE", "#A0AAC8", "#D29820", "#D4F0E0", "#D8E8F0", "#DBEAFE", "#DC2626", "#DDD6FE", "#E0D8F0", "#E0E7FF", "#E8ECF4", "#EEF0F8", "#F1F5FB", "#F2F7FA", "#F2FAF5", "#F5F2FA", "#FBF9F1", "#FEE2E2", "#FEF3C7",
    },
}

HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}\b")


class Cell:
    def __init__(self, el, index):
        self.el = el
        self.index = index  # document order = render order (later paints on top)
        self.id = el.get("id")
        self.parent = el.get("parent")
        self.style = el.get("style") or ""
        self.value = el.get("value") or ""
        self.is_vertex = el.get("vertex") == "1"
        self.is_edge = el.get("edge") == "1"
        self.source = el.get("source")
        self.target = el.get("target")
        geo = el.find("mxGeometry")
        self.geo = None
        if geo is not None and geo.get("relative") != "1":
            try:
                self.geo = (
                    float(geo.get("x", 0)), float(geo.get("y", 0)),
                    float(geo.get("width", 0)), float(geo.get("height", 0)),
                )
            except (TypeError, ValueError):
                self.geo = None
        self.style_map = {}
        for token in self.style.split(";"):
            if "=" in token:
                k, _, v = token.partition("=")
                self.style_map[k] = v

    @property
    def is_text_label(self):
        return self.style.startswith("text;")

    @property
    def fill(self):
        return self.style_map.get("fillColor")

    @property
    def is_filled_shape(self):
        # Vertices that paint an opaque area. Text cells and fillColor=none don't.
        return self.is_vertex and not self.is_text_label and self.fill != "none"

    @property
    def is_decorative_line(self):
        # Thin horizontal rules (e.g. timeline axis) — exempt from size/text checks.
        if not self.geo:
            return False
        _, _, w, h = self.geo
        return h <= 6 or "shape=line" in self.style


def abs_bbox(cell, cells_by_id, _depth=0):
    """Resolve absolute (x, y, w, h); child coordinates are relative to parent."""
    if cell.geo is None or _depth > 10:
        return None
    x, y, w, h = cell.geo
    parent = cells_by_id.get(cell.parent)
    while parent is not None and parent.id not in ("0", "1") and _depth <= 10:
        if parent.geo:
            x += parent.geo[0]
            y += parent.geo[1]
        parent = cells_by_id.get(parent.parent)
        _depth += 1
    return (x, y, w, h)


def strip_html(value):
    text = re.sub(r"<[^>]+>", "\n", value)
    return html.unescape(text)


def est_text_width(line, font_size):
    w = 0.0
    for ch in line:
        w += font_size * (1.05 if ord(ch) >= 0x2E80 else 0.5)
    return w


def main():
    ap = argparse.ArgumentParser(description="Validate a FlowForge .drawio file")
    ap.add_argument("file")
    ap.add_argument("--theme", choices=sorted(THEMES), default=None,
                    help="verify all colors belong to this theme")
    args = ap.parse_args()

    errors, warnings = [], []

    def err(cid, msg):
        errors.append(f"  ERROR [{cid}] {msg}")

    def warn(cid, msg):
        warnings.append(f"  WARN  [{cid}] {msg}")

    try:
        tree = ET.parse(args.file)
    except (ET.ParseError, OSError) as e:
        print(f"FATAL: cannot parse {args.file}: {e}")
        print("Hint: unescaped <, >, & or &bull; inside value attributes is the usual cause.")
        sys.exit(2)

    model = tree.getroot().find(".//mxGraphModel")
    root = model.find("root") if model is not None else None
    if root is None:
        print("FATAL: no mxGraphModel/root element found")
        sys.exit(2)

    try:
        page_w = float(model.get("pageWidth"))
        page_h = float(model.get("pageHeight"))
    except (TypeError, ValueError):
        page_w = page_h = None
        warn("canvas", "pageWidth/pageHeight missing — canvas bounds not checked")

    cells = [Cell(el, i) for i, el in enumerate(root.findall("mxCell"))]
    cells_by_id = {}

    # --- ids unique, parents exist -------------------------------------------
    for c in cells:
        if c.id is None:
            err("?", "mxCell without id")
            continue
        if c.id in cells_by_id:
            err(c.id, "duplicate id")
        cells_by_id[c.id] = c
    for c in cells:
        if c.id in ("0", "1"):
            continue
        if c.parent is None or c.parent not in cells_by_id:
            err(c.id, f'parent="{c.parent}" does not exist')
    if "0" not in cells_by_id or "1" not in cells_by_id:
        err("root", 'missing base cells <mxCell id="0"/> and <mxCell id="1" parent="0"/>')

    content = [c for c in cells if c.id not in ("0", "1")]
    vertices = [c for c in content if c.is_vertex]
    edges = [c for c in content if c.is_edge]

    # --- edges ---------------------------------------------------------------
    for e in edges:
        geo_el = e.el.find("mxGeometry")
        for attr, ref in (("source", e.source), ("target", e.target)):
            if ref is None:
                # Unbound side is fine if anchored to an explicit coordinate
                # (decorative lines: timeline axis, ticks).
                has_point = geo_el is not None and geo_el.find(
                    f'mxPoint[@as="{attr}Point"]') is not None
                if not has_point:
                    err(e.id, f"edge has no {attr} (bind a node or add an mxPoint {attr}Point)")
            elif ref not in cells_by_id:
                err(e.id, f'{attr}="{ref}" does not exist')
            elif not cells_by_id[ref].is_vertex:
                err(e.id, f'{attr}="{ref}" is not a vertex')
        # Flow arrows must route orthogonally; arrowhead-less connectors
        # (hub rays, axis lines) are decorative and may run straight.
        if "endArrow=none" in e.style:
            continue
        if "edgeStyle=orthogonalEdgeStyle" not in e.style:
            err(e.id, "missing edgeStyle=orthogonalEdgeStyle (arrow may render diagonal)")

    # --- vertex geometry -----------------------------------------------------
    boxes = {}
    for v in vertices:
        if v.geo is None:
            err(v.id, "vertex has no usable mxGeometry")
            continue
        bb = abs_bbox(v, cells_by_id)
        boxes[v.id] = bb
        x, y, w, h = bb
        if page_w is not None:
            if x < 0 or y < 0 or x + w > page_w + 0.5 or y + h > page_h + 0.5:
                err(v.id, f"outside canvas: bbox=({x:.0f},{y:.0f},{w:.0f},{h:.0f}) "
                          f"canvas=({page_w:.0f}x{page_h:.0f}) — enlarge pageWidth/pageHeight")
        if v.is_filled_shape and not v.is_decorative_line and (w < 80 or h < 30):
            warn(v.id, f"node smaller than 80x30 ({w:.0f}x{h:.0f})")

    # --- overlap & z-order (filled shapes only; containment is allowed) ------
    filled = [v for v in vertices if v.is_filled_shape and v.id in boxes]
    for i, a in enumerate(filled):
        ax, ay, aw, ah = boxes[a.id]
        for b in filled[i + 1:]:
            bx, by, bw, bh = boxes[b.id]
            ix = min(ax + aw, bx + bw) - max(ax, bx)
            iy = min(ay + ah, by + bh) - max(ay, by)
            if ix <= 2 or iy <= 2:
                continue  # disjoint or merely touching
            a_in_b = ax >= bx and ay >= by and ax + aw <= bx + bw and ay + ah <= by + bh
            b_in_a = bx >= ax and by >= ay and bx + bw <= ax + aw and by + bh <= ay + ah
            if a_in_b or b_in_a:
                outer, inner = (b, a) if a_in_b else (a, b)
                if outer.index > inner.index:
                    err(outer.id, f"filled container drawn AFTER its child '{inner.id}' "
                                  f"— it will hide it; move it before in the XML")
            else:
                err(a.id, f"overlaps node '{b.id}' — adjust coordinates")

    # --- fonts & text fit ----------------------------------------------------
    for c in content:
        fs = c.style_map.get("fontSize")
        if fs:
            try:
                if float(fs) < 9:
                    err(c.id, f"fontSize {fs} below minimum 9")
            except ValueError:
                pass
        for m in re.finditer(r"font-size\s*:\s*(\d+(?:\.\d+)?)px", c.value):
            if float(m.group(1)) < 9:
                warn(c.id, f"inline font-size {m.group(1)}px below 9 in value")

    for v in vertices:
        if not v.value or v.id not in boxes or v.is_decorative_line:
            continue
        _, _, w, h = boxes[v.id]
        try:
            fs = float(v.style_map.get("fontSize", 13))
        except ValueError:
            fs = 13
        usable = (w * 0.6 if "rhombus" in v.style else w) - 4
        for line in (ln.strip() for ln in strip_html(v.value).splitlines()):
            if line and est_text_width(line, fs) > usable and "whiteSpace=wrap" not in v.style:
                warn(v.id, f'text "{line[:30]}…" (~{est_text_width(line, fs):.0f}px) may not fit '
                           f"in {usable:.0f}px — widen node, shrink font, or add <br>")
                break

    # --- theme compliance ----------------------------------------------------
    if args.theme:
        # White is always allowed: badge text on colored chips, card backgrounds.
        palette = THEMES[args.theme] | {"#FFFFFF"}
        for c in content:
            for key in ("fillColor", "strokeColor", "fontColor"):
                val = c.style_map.get(key)
                if val and val != "none" and val.upper() not in {p.upper() for p in palette}:
                    err(c.id, f'{key}={val} is not in theme "{args.theme}" — use themes.md values')
            for m in HEX_RE.finditer(c.value):
                if m.group(0).upper() not in {p.upper() for p in palette}:
                    warn(c.id, f'color {m.group(0)} inside value is not in theme "{args.theme}"')

    # --- report ----------------------------------------------------------------
    for line in errors:
        print(line)
    for line in warnings:
        print(line)
    print(f"\n{args.file}: {len(errors)} error(s), {len(warnings)} warning(s)"
          + (f" [theme={args.theme}]" if args.theme else ""))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
