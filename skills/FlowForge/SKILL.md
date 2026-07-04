---
name: FlowForge
description: >
  TRIGGER when: user asks to draw, illustrate, or visualize any process, structure, or concept — "画个流程图",
  "draw an architecture diagram", "帮我画个对比图", "visualize this process", "make a diagram for this doc",
  or mentions 流程图/架构图/示意图/对比图/时序图/泳道图/时间线.
  Also trigger when user provides a document/article and asks for illustrations or diagrams.
  DO NOT trigger for: chart/plot requests (bar charts, line graphs — those need a charting library, not draw.io),
  or artistic image requests (logos, mascots, drawings of objects/people — those need an image tool).
---

# FlowForge — Draw.io Diagram Skill

Generate professional diagrams as draw.io XML files. Supports 13 diagram types: flows, comparisons, layer stacks, cycles, trees, hub-and-spoke, columns, matrices, funnels, timelines, sequence diagrams, and swimlanes.

## Usage

```bash
/FlowForge "OAuth 2.0 authorization code flow"
/FlowForge path/to/design-doc.md
/FlowForge "CI/CD pipeline" --type loop
/FlowForge "Monolith vs Microservices" --type compare --theme morandi
/FlowForge "System Architecture" --lang en
```

---

## Workflow

### Step 1: Understand & Propose (one confirmation, not three)

**If given a document:** read it fully, identify 1–3 places that benefit from a diagram, and for each note the insert position, the topic (one sentence), and the recommended type (see Diagram Type Reference).

**If given a concept directly:** identify the core message and pick the type via the Selection Guide.

Then present **one combined proposal** and ask for confirmation **once**. The proposal contains:
- Diagram type and theme (default: **tech-blue**; other options: morandi, mint, terracotta, indigo)
- An ASCII sketch: all nodes with labels, arrow directions and labels, grouping, color-role tags, layout direction

Example sketch:
```
Direction: left-to-right | Nodes: 4 | Type: flow | Theme: tech-blue

[primary] Code Commit  →  [process] Build  →  [process] Test  →  [accent] Deploy
                                                    ↓ (fail)
                                              [error] Alert
```

**Skip the confirmation entirely** when the request already pins everything down (user gave `--type`/`--theme` or an unambiguous description), or when no human can respond (subagent, batch, CI). In that case proceed with defaults and state your assumptions in the final report.

### Step 2: Generate draw.io XML

1. Read [references/layouts.md](references/layouts.md) — the layout algorithm for the chosen type — and compute all coordinates from its formulas
2. Apply theme colors from [themes.md](themes.md)
3. Use element templates from [xml-reference.md](xml-reference.md)
4. For an unfamiliar type, read the matching example file listed in [examples.md](examples.md)

### Step 3: Validate (mandatory)

```bash
python3 {skill_dir}/scripts/validate.py <file.drawio> --theme <theme>
```

This deterministically checks: XML well-formedness, unique ids, dangling arrow references, orthogonal edge style, canvas bounds, node overlap, z-order (containers before children), font sizes, text-fit estimates, and theme color compliance. **Fix every ERROR and re-run until clean.** WARNs are heuristics — judge each one, fix the real ones.

### Step 4: Visual self-check (when draw.io CLI is available)

```bash
bash {skill_dir}/scripts/render.sh <file.drawio>   # writes a .png next to the file
```

If the script reports draw.io is not installed, skip this step (the user can enable it once with `brew install --cask drawio`). Otherwise **Read the PNG and inspect it with fresh eyes**: text overflowing nodes, crowded regions, arrows colliding with nodes, color rhythm, overall balance. Fix and re-render until it looks right — this catches what rules can't.

### Step 5: Save & Deliver

Save the `.drawio` file to the output directory (see Configuration). After saving, report:
- File path (and the rendered PNG path if Step 4 ran)
- How to open: draw.io desktop app or https://app.diagrams.net

### Iteration

If the user wants changes after viewing:
1. Read the current `.drawio` file
2. Modify the XML per feedback
3. Save as `{name}_v2.drawio` (preserve previous version), then re-run Steps 3–4

---

## Configuration

Optional per-project config file `./.flowforge.json` (in the working directory, **never inside the skill directory** — the skill directory may be read-only or shared across projects):

```json
{
  "defaultTheme": "tech-blue",
  "outputDir": "./diagrams",
  "language": "auto"
}
```

If the file is absent, use exactly these defaults — do not interview the user. `"language": "auto"` means match the user's language; technical abbreviations (API, LLM, CI/CD) stay in English regardless. Per-invocation flags (`--theme`, `--lang`) override config.

---

## Diagram Type Reference

### Core Types

| Type | Code | Best For | Example |
|------|------|----------|---------|
| Linear Flow | `flow` | Sequential steps A→B→C | API call flow, data pipeline |
| Vertical Flow | `flow-vertical` | Top-down processes | Decision process, approval chain |
| Comparison | `compare` | A vs B side by side | Traditional vs AI approach |
| Layer Stack | `layers` | Tech stack, tiers | System architecture layers |
| Cycle | `loop` | Iterative processes | ML training loop, CI/CD |
| Tree | `tree` | Hierarchies, taxonomies | Org chart, decision tree |
| Hub & Spoke | `hub` | Core concept + branches | Product feature map |

### Extended Types

| Type | Code | Best For |
|------|------|----------|
| Parallel Columns | `columns` | 3+ parallel concepts |
| Matrix | `matrix` | Multi-dimension comparison |
| Funnel | `funnel` | Filtering, conversion |
| Timeline | `timeline` | Version evolution, history |
| Sequence | `sequence` | Component interactions |
| Swimlane | `swimlane` | Cross-role processes (who does what) |

### Selection Guide

| Content Pattern | Recommended Type |
|----------------|-----------------|
| Sequential steps | `flow` or `flow-vertical` |
| Two things compared | `compare` |
| 3+ parallel concepts | `columns` or `hub` |
| Layered system | `layers` |
| Iterative/cyclical process | `loop` |
| One core, many branches (incl. mind-map style) | `hub` or `tree` |
| Components communicating | `sequence` |
| Change over time | `timeline` |
| Multi-criteria evaluation | `matrix` |
| Progressive filtering | `funnel` |
| Steps owned by different roles/systems | `swimlane` |

---

## Color Usage Principles

**This is the most important section for visual quality.**

### The 4+6 Rule

Each theme has **4 base colors** (`primary`, `process`, `accent`, `neutral`) and **6 extended colors** (`success`, `warning`, `error`, `secondary`, `storage`, `group`). The primary family should always dominate; the amount of non-primary accents scales with diagram size.

### Color Budget by Diagram Size

| Node Count | Target Colors | Guideline |
|------------|--------------|-----------|
| 3-5 nodes | 2-3 colors | Primary family dominates. At most 1 accent node. |
| 6-8 nodes | 3-4 colors | Primary ~60%. Add 1-2 non-primary at semantic turning points. |
| 9+ nodes | 4-5 colors | Primary ~50%. Distribute 2-3 non-primary for visual rhythm. |

**6+ colors almost always looks bad regardless of diagram size.**

### Color Assignment Strategy

1. **Primary dominates** — `primary` and `process` cover the largest visual area and the biggest nodes.
2. **Accent is a scalpel, not a paintbrush** — at most 1-2 key highlights, never the largest node.
3. **Scale with length** — a 4-node flow with 2 colors looks clean; a 9-node flow with 2 colors is a monotonous wall. Add non-primary colors at natural semantic boundaries to create rhythm.
4. **3-consecutive guideline** — if you spot 4+ adjacent same-color nodes, promote the most semantically distinctive one.
5. **Distribute spatially** — non-primary nodes spread across the diagram, not clustered in one region.

### Semantic Color Heuristics

| Node Type | Recommended Color |
|-----------|------------------|
| User input / starting point | `primary` |
| Standard processing step | `process` |
| Decision / branching point | `warning` or `accent` |
| Domain-specific / translation step | `secondary` |
| Key transformation / highlight | `accent` |
| Data source / external system | `neutral` |
| Error path / fallback | `accent` or `error` |
| Successful output / endpoint | `success` or `primary` |
| Database / storage | `storage` |

Good/bad worked examples of color rhythm are at the bottom of [themes.md](themes.md).

---

## Design Principles

1. **Narrative titles** — Use "How OAuth 2.0 Authorizes a User" not "OAuth 2.0 Diagram".
2. **Bilingual labels** — Use the user's language. Technical abbreviations (API, LLM, CI/CD) stay in English regardless.
3. **Orthogonal flow arrows** — Every arrow between nodes includes `edgeStyle=orthogonalEdgeStyle;` so it runs horizontal/vertical only. Exception: decorative connectors with `endArrow=none` (hub rays, timeline axis/ticks) may run straight.

---

## Gotchas — Common Failure Points

The validator (Step 3) catches most geometry/reference mistakes after the fact, but knowing these saves a fix cycle:

1. **Rich node title duplication** — the title lives in a separate text cell; keep `value=""` on the background rect or it renders twice.
2. **Arrow ignores exit/entry points** — always specify `exitX/exitY/entryX/entryY`; otherwise draw.io auto-routes, usually badly.
3. **HTML entities in value attributes** — `value` is HTML inside an XML attribute: `&lt;` `&gt;` `&amp;`, and `&amp;bull;` for bullets. One missing escape breaks the whole file *(validator: parse error)*.
4. **Filled boxes drawn after their children hide them** — define lane bands and any filled container BEFORE the nodes inside them *(validator: z-order check)*.
5. **Canvas too small** — compute `pageWidth`/`pageHeight` from the layout formulas: `max(x + w) + CANVAS_PAD` *(validator: bounds check)*.
6. **Forgetting `parent="1"`** — every content element needs it unless intentionally grouped *(validator: parent check)*.
7. **Diamond text overflow** — rhombus shapes have ~60% usable width; keep labels to 2-3 short words, font 11.
8. **Snake layout wrap arrows** — the wrap-around arrow exits the BOTTOM of the last node in a row and enters the TOP of the next row's first node, not sideways.
9. **Cycle return arrow** — in `loop` diagrams, route the last→first arrow around the outside of the rectangle, never through the center.
10. **Off-by-one in widths** — `n` nodes have `n-1` gaps: canvas width = `PAD×2 + n×NODE_W + (n-1)×GAP_H` *(validator: bounds/overlap)*.
11. **Branch/merge arrows go diagonal** — when exit/entry points aren't aligned, only `edgeStyle=orthogonalEdgeStyle;` keeps them orthogonal — include it in every flow arrow *(validator: style check)*.

---

## Supporting Files

Read them when the workflow step calls for them — don't load everything upfront.

| File | When to read |
|------|-------------|
| [references/layouts.md](references/layouts.md) | Step 2, before computing coordinates — global constants + all 13 layout algorithms |
| [themes.md](themes.md) | Step 2, when applying colors — 5 themes × 10 semantic colors + 7 text colors, color-rhythm examples |
| [xml-reference.md](xml-reference.md) | Step 2, when writing XML — canvas boilerplate, element templates, arrow direction table |
| [examples.md](examples.md) | Step 2 — coordinate-calculation walkthroughs + index of example files |
| `scripts/validate.py` | Step 3 — run on every generated file (don't read it, run it) |
| `scripts/render.sh` | Step 4 — export PNG for the visual self-check |

### Example `.drawio` files (in `examples/`)

Real, working files to read as reference when generating a similar type:

- `examples/flow-cicd.drawio` — Linear flow, 4 nodes, tech-blue
- `examples/compare-monolith-vs-micro.drawio` — Comparison, 2 columns × 3 rows, morandi
- `examples/loop-ml-training.drawio` — Cycle, 4 nodes clockwise, mint
- `examples/tree-storage-decision.drawio` — Decision tree with diamonds, mint
- `examples/hub-agent-capabilities.drawio` — Hub & spoke, 6 spokes with rays, indigo
- `examples/timeline-llm-history.drawio` — Timeline with axis + ticks, terracotta
