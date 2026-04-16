---
name: FlowForge
description: >
  TRIGGER when: user asks to draw, illustrate, or visualize anything — "画个流程图", "draw an architecture diagram",
  "帮我画个对比图", "visualize this process", "make a diagram for this doc", or mentions 流程图/架构图/示意图/对比图.
  Also trigger when user provides a document/article and asks for illustrations or diagrams.
  DO NOT trigger for: chart/plot requests (bar charts, line graphs — those need a charting library, not draw.io).
---

# FlowForge — Draw.io Diagram Skill

Generate professional diagrams as draw.io XML files. Supports flowcharts, architecture diagrams, comparisons, mind maps, timelines, and more.

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

### Step 1: Understand Requirements

**If given a document:**
1. Read the full document
2. Identify 1–3 places that benefit from a diagram
3. For each, list:
   - Insert position (after which section)
   - Diagram topic (one sentence)
   - Recommended diagram type (see Diagram Type Reference below)
4. **Wait for user confirmation**

**If given a concept directly:**
1. Confirm the core message to convey
2. Choose diagram type
3. Proceed to Step 2

### Step 2: Confirm Theme

If the user hasn't specified `--theme`, state:

> Default theme: **tech-blue** (科技蓝灰). Other options: morandi, mint, terracotta, indigo. Want a different one?

Proceed after user confirms. For full theme definitions, see [themes.md](themes.md).

### Step 3: Design Sketch (ASCII)

Produce an ASCII sketch showing:
- All nodes with labels
- Arrow directions and labels
- Grouping/regions
- Color role assignments (e.g., `[primary]`, `[accent]`, `[neutral]`)
- Approximate dimensions and layout direction

Example sketch:
```
Direction: left-to-right | Nodes: 4 | Type: flow

[primary] Code Commit  →  [process] Build  →  [process] Test  →  [accent] Deploy
                                                    ↓ (fail)
                                              [error] Alert
```

**STOP — Wait for user confirmation or revision before proceeding to XML generation.**

### Step 4: Generate draw.io XML

1. Select layout algorithm for the chosen type (see Layout System below)
2. Compute all coordinates using the formulas and constants
3. Apply theme colors from [themes.md](themes.md)
4. Use element templates from [xml-reference.md](xml-reference.md)
5. Reference complete examples in [examples.md](examples.md) for pattern matching
6. Fix any issues found

### Step 5: Save & Deliver

Save the `.drawio` file. Default path:
```
./diagrams/{diagram-name}.drawio
```

Or user-specified path. After saving, report:
- File path
- How to open: draw.io desktop app or https://app.diagrams.net

### Iteration

If the user wants changes after viewing:
1. Read the current `.drawio` file
2. Modify the XML per feedback
3. Save as `{name}_v2.drawio` (preserve previous version)

---

## Layout System

### Global Constants

```
CANVAS_PAD    = 40       # padding from content to canvas edge
NODE_W        = 160      # default node width
NODE_H        = 50       # single-label node height
NODE_H_RICH   = 90       # node with title + bullet list
TITLE_H       = 28       # diagram title height
GAP_H         = 60       # horizontal gap between nodes
GAP_V         = 50       # vertical gap between nodes
DIAMOND_W     = 120      # decision diamond width
DIAMOND_H     = 80       # decision diamond height
GROUP_PAD     = 20       # padding inside dashed group boxes
FONT_TITLE    = 18       # diagram title font size
FONT_NODE     = 13       # node title font size
FONT_BODY     = 10       # node body/list font size
FONT_ARROW    = 9        # arrow label font size
STROKE_NODE   = 1.2      # node border stroke width
STROKE_ARROW  = 0.8      # arrow stroke width
ARC_SIZE      = 10       # rounded rect arc size
ARROW_SIZE    = 5        # arrowhead size
```

Adjust constants when needed:
- If nodes > 6 in a flow, reduce `NODE_W` to 140 or `GAP_H` to 40
- If labels are long, increase `NODE_W` up to 200
- Rich nodes (title + list): use `NODE_H_RICH` instead of `NODE_H`

### Layout Algorithms by Type

#### `flow` — Linear Flow (left-to-right)

```
x[i] = CANVAS_PAD + i × (NODE_W + GAP_H)
y    = CANVAS_PAD + TITLE_H + GAP_V

Canvas width  = CANVAS_PAD × 2 + n × NODE_W + (n-1) × GAP_H
Canvas height = CANVAS_PAD × 2 + TITLE_H + GAP_V + NODE_H
```

If n > 5, use **snake layout** — wrap to next row flowing right-to-left:
```
Row 0 (L→R): nodes 0..4
Row 1 (R→L): nodes 5..9
Row 2 (L→R): nodes 10..14

y[row] = CANVAS_PAD + TITLE_H + GAP_V + row × (NODE_H + GAP_V)
x[i] in even row = CANVAS_PAD + col × (NODE_W + GAP_H)
x[i] in odd row  = CANVAS_PAD + (4-col) × (NODE_W + GAP_H)
```

#### `flow-vertical` — Linear Flow (top-to-bottom)

```
x    = CANVAS_PAD + (Canvas width / 2) - NODE_W / 2
y[i] = CANVAS_PAD + TITLE_H + GAP_V + i × (NODE_H + GAP_V)
```

#### `compare` — Left-Right Comparison

```
VS_W = 50   # width of "VS" badge

Left column x  = CANVAS_PAD
Right column x = CANVAS_PAD + NODE_W + GAP_H + VS_W + GAP_H
VS badge x     = CANVAS_PAD + NODE_W + GAP_H

Header y = CANVAS_PAD + TITLE_H + GAP_V
Row y[j] = Header y + NODE_H + GAP_V/2 + j × (NODE_H + GAP_V/2)
```

Each side has a header node (title) and content rows below.

#### `layers` — Layer Stack

```
LAYER_W = 400

x = CANVAS_PAD + (canvas center offset)
y[i] = CANVAS_PAD + TITLE_H + GAP_V + i × (NODE_H_RICH + GAP_V/3)

Canvas width  = CANVAS_PAD × 2 + LAYER_W
Canvas height = CANVAS_PAD × 2 + TITLE_H + GAP_V + n × NODE_H_RICH + (n-1) × GAP_V/3
```

Layers span full width. Top layer = highest abstraction.

#### `loop` — Cycle / Feedback Loop

Arrange N nodes in a rectangular path (clockwise):

For 4 nodes (most common):
```
Positions:
  [0] top-left:     (CANVAS_PAD, CANVAS_PAD + TITLE_H + GAP_V)
  [1] top-right:    (CANVAS_PAD + NODE_W + GAP_H × 2, same y)
  [2] bottom-right: (same x as [1], y + NODE_H + GAP_V)
  [3] bottom-left:  (same x as [0], same y as [2])

Arrows: 0→1 (top), 1→2 (right), 2→3 (bottom, R→L), 3→0 (left, bottom→top)
```

For N nodes: distribute evenly across 4 sides of a rectangle.

#### `tree` — Tree / Hierarchy

```
Level spacing = GAP_V × 1.5
Sibling spacing = NODE_W + GAP_H / 2

Root: centered at top
Children: evenly distributed below parent, centered under parent

Subtree width = max(sum of children subtree widths, NODE_W)
Parent x = leftmost child x + (rightmost child x + NODE_W - leftmost child x) / 2 - NODE_W / 2
```

#### `hub` — Hub and Spoke (Center Radiate)

Center node at canvas center. Spokes at equal angles.

**Lookup table** (use these positions instead of computing cosines):

| N spokes | Positions relative to center (dx, dy) |
|----------|---------------------------------------|
| 3 | (0, -R), (R×0.87, R×0.5), (-R×0.87, R×0.5) |
| 4 | (0, -R), (R, 0), (0, R), (-R, 0) |
| 5 | (0, -R), (R×0.95, -R×0.31), (R×0.59, R×0.81), (-R×0.59, R×0.81), (-R×0.95, -R×0.31) |
| 6 | (0, -R), (R×0.87, -R×0.5), (R×0.87, R×0.5), (0, R), (-R×0.87, R×0.5), (-R×0.87, -R×0.5) |

Where `R = 180` (radius). Spoke node position:
```
x[i] = cx + dx[i] - NODE_W / 2
y[i] = cy + dy[i] - NODE_H / 2
```

#### `columns` — Parallel Columns

```
Column x[i] = CANVAS_PAD + i × (NODE_W + GAP_H)
Header y     = CANVAS_PAD + TITLE_H + GAP_V
Item y[j]    = Header y + NODE_H + GAP_V/2 + j × (NODE_H + GAP_V/3)
```

Each column has a header node (colored) and vertically stacked item nodes below.

#### `matrix` — Comparison Matrix

```
CELL_W = 140
CELL_H = 45
HEADER_H = 40

Col header x[c] = CANVAS_PAD + HEADER_W + GAP_H/3 + c × (CELL_W + GAP_H/3)
Row header y[r] = CANVAS_PAD + TITLE_H + HEADER_H + GAP_V/3 + r × (CELL_H + GAP_V/3)
Cell (r,c): x = Col header x[c], y = Row header y[r]
```

#### `funnel` — Funnel

```
MAX_W = 360
MIN_W = 120

w[i] = MAX_W - i × ((MAX_W - MIN_W) / (n - 1))
x[i] = CANVAS_PAD + (MAX_W - w[i]) / 2
y[i] = CANVAS_PAD + TITLE_H + GAP_V + i × (NODE_H + GAP_V / 3)
```

Centered, decreasing-width bands stacked vertically.

#### `timeline` — Timeline

```
LINE_Y = canvas vertical center
Node spacing = NODE_W + GAP_H

Event nodes alternate above and below the timeline:
  Above: y = LINE_Y - NODE_H - GAP_V/2
  Below: y = LINE_Y + GAP_V/2
  x[i]  = CANVAS_PAD + i × (NODE_W + GAP_H)

Draw a horizontal line at LINE_Y spanning full width.
Draw vertical ticks from line to each node.
```

#### `sequence` — Sequence Diagram

```
LIFELINE_GAP = 180
MESSAGE_GAP  = 50
PARTICIPANT_Y = CANVAS_PAD + TITLE_H + GAP_V
PARTICIPANT_W = 140
PARTICIPANT_H = 40

Participant x[i] = CANVAS_PAD + i × LIFELINE_GAP
Lifeline: vertical dashed line from bottom of participant box downward

Message y[j] = PARTICIPANT_Y + PARTICIPANT_H + GAP_V + j × MESSAGE_GAP
Messages: horizontal arrows between lifelines
```

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

### Selection Guide

| Content Pattern | Recommended Type |
|----------------|-----------------|
| Sequential steps | `flow` or `flow-vertical` |
| Two things compared | `compare` |
| 3+ parallel concepts | `columns` or `hub` |
| Layered system | `layers` |
| Iterative/cyclical process | `loop` |
| One core, many branches | `hub` or `tree` |
| Components communicating | `sequence` |
| Change over time | `timeline` |
| Multi-criteria evaluation | `matrix` |
| Progressive filtering | `funnel` |

---

## Quality Checks

**Before delivering the `.drawio` file, verify ALL of the following. Fix any failures before saving.**

### Layout Checks

1. **No overlapping nodes** — For every pair of nodes, their bounding boxes must not intersect. Verify: `|x1 - x2| >= width` OR `|y1 - y2| >= height`.
2. **Canvas large enough** — No node extends beyond: `max(x + w) + CANVAS_PAD <= CANVAS_W` and `max(y + h) + CANVAS_PAD <= CANVAS_H`.
3. **Consistent spacing** — Gaps between adjacent nodes should match `GAP_H` / `GAP_V` (±10px tolerance).
4. **Alignment** — Nodes in the same row share the same `y`. Nodes in the same column share the same `x`.

### Text Checks

5. **Text fits in node** — Estimate: Chinese characters ≈ 14px each at font 13; English characters ≈ 8px each. If text width > node width - 20px padding, either widen the node, reduce font, or add `<br>` line breaks.
6. **Minimum readability** — No font size below 9px. No node smaller than 80×30.

### XML Checks

7. **All arrow targets exist** — Every `source="X"` and `target="Y"` must match an `id="X"` / `id="Y"` defined as a vertex.
8. **Unique IDs** — Every `id` attribute is unique across the entire XML.
9. **Correct parent** — All content elements have `parent="1"` unless intentionally grouped.
10. **Valid XML** — Well-formed, all attributes quoted, HTML entities escaped (`&lt;` `&gt;` `&amp;` `&quot;`).

### Style Checks

11. **Theme consistency** — All fill/stroke/font colors come from the selected theme. No ad-hoc hex values.
12. **Arrow routing** — Arrows use orthogonal routing only (horizontal + vertical). No diagonal arrows. Return arrows route around the outside, never crossing through unrelated nodes.

---

## Color Usage Principles

**This is the most important section for visual quality.**

### The 4+6 Rule

Each theme has **4 base colors** and **6 extended colors**:

- **Base 4**: `primary`, `process`, `accent`, `neutral`
- **Extended 6**: `success`, `warning`, `error`, `secondary`, `storage`, `group`

Blue (primary + process) should always be the dominant color family, but the amount of non-blue accents should scale with diagram size.

### Color Budget by Diagram Size

| Node Count | Target Colors | Guideline |
|------------|--------------|-----------|
| 3-5 nodes | 2-3 colors | Blue dominates. At most 1 accent node. |
| 6-8 nodes | 3-4 colors | Blue ~60%. Add 1-2 non-blue at semantic turning points. |
| 9+ nodes | 4-5 colors | Blue ~50%. Distribute 2-3 non-blue for visual rhythm. |

**6+ colors almost always looks bad regardless of diagram size.**

### Color Assignment Strategy

1. **Blue dominates** — `primary` and `process` should cover the largest visual area and the biggest nodes.

2. **Accent is a scalpel, not a paintbrush** — Use `accent` for at most 1-2 key highlights. Never on the largest node.

3. **Scale with length** — A 4-node flow with 2 colors looks clean. A 9-node flow with only 2 colors is a monotonous wall. Add non-blue colors at natural semantic boundaries to create rhythm.

4. **3-consecutive guideline** — Avoid more than 3 adjacent nodes in the same color. If you spot 4+ consecutive blue nodes, promote the most semantically distinctive one to a non-blue color.

5. **Distribute spatially** — Non-blue nodes should be spread across the diagram (top/middle/bottom), not clustered in one region.

### Semantic Color Heuristics

When deciding which nodes get non-blue colors, use this table:

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

### Examples

**Bad** (rainbow — every node a different color):
```
[neutral] 数据源 → [process] 采集 → [warning] 检查 → [success] 清洗 → [error] 告警 → [storage] 入库
```

**Bad** (wall of blue — 9 nodes all the same):
```
[primary] 提问 → [process] 校验 → [process] 评估 → [process] 翻译 → [process] 执行 → [process] 解读 → [process] 可视化 → [process] 标注 → [primary] 返回
```

**Good** (short flow, 2-3 colors):
```
[neutral] 数据源 → [process] 采集 → [process] 检查 → [process] 清洗 → [primary] 入库
                                        ↓ (异常)
                                  [accent] 告警处理
```

**Good** (long flow, 4-5 colors with rhythm):
```
[primary] 提问 → [process] 校验 → [warning] 评估 → [secondary] 翻译 → [process] 执行 → [process] 解读 → [accent] 可视化 → [process] 标注 → [success] 返回
```

---

## Design Principles

1. **Narrative titles** — Use "How OAuth 2.0 Authorizes a User" not "OAuth 2.0 Diagram".
2. **Bilingual labels** — Use the user's language. Technical abbreviations (API, LLM, CI/CD) stay in English regardless.
3. **Orthogonal arrows only** — All arrows run horizontally or vertically, no diagonals. Always include `edgeStyle=orthogonalEdgeStyle;` in every arrow's style attribute.

---

## Gotchas — Common Failure Points

These are the most common mistakes when generating draw.io XML. Check for these first when debugging.

1. **Rich node text overflow** — The `<b>Title</b>` inside a rich node uses a separate text cell. If you put the title in the `value` attribute of the background rect AND in a text cell, the title renders twice. Use `value=""` on the background rect.

2. **Arrow ignores exit/entry points** — If you omit `exitX/exitY/entryX/entryY` from the arrow style, draw.io auto-routes, which often looks wrong. Always specify explicit exit/entry points.

3. **HTML entities in value attributes** — `value` attributes use HTML, so `<` must be `&lt;`, `>` must be `&gt;`, `&` must be `&amp;`. Missing escapes break the entire XML. The most common miss: `&bull;` in bulleted lists — use `&amp;bull;` when inside an attribute.

4. **Dashed group box covers its children** — If a dashed group box is defined AFTER its child nodes in the XML, it renders on top and hides them. Always define group boxes BEFORE their child elements.

5. **Canvas too small** — `pageWidth`/`pageHeight` that are too small cause nodes to be cut off in the exported image. Always compute from layout formulas: `max(x + w) + CANVAS_PAD`.

6. **Forgetting `parent="1"`** — Every content element must have `parent="1"`. Missing this silently breaks the node.

7. **Diamond text overflow** — Diamond/rhombus shapes have less usable area than rectangles. Keep labels to 2-3 short words. Use font size 11 instead of 13.

8. **Snake layout wrong arrow direction** — In snake layouts (flow with >5 nodes), the wrap-around arrow must exit from the bottom of the last node in row N and enter the top of the first node in row N+1, not go sideways.

9. **Cycle arrow goes through center** — In `loop` diagrams, the return arrow (last→first) must route along the outside of the rectangle, not diagonally through the center.

10. **Coordinate calculation off-by-one** — When computing `n` items: there are `n` nodes but `n-1` gaps. Canvas width = `PAD×2 + n×NODE_W + (n-1)×GAP_H`, not `n×GAP_H`.

11. **Diagonal arrows on branching/merging** — When a centered node branches to two side-by-side targets, exit/entry points are not aligned vertically. Without `edgeStyle=orthogonalEdgeStyle;` in the style, draw.io renders these as diagonal lines. Always include it in every arrow.

---

## Initial Setup

On first invocation, check if `config.json` exists in the skill directory. If not, ask the user:

1. **Default theme** — Which color theme to use by default? (tech-blue / morandi / mint / terracotta / indigo)
2. **Output directory** — Where to save `.drawio` files? (default: `./diagrams/`)
3. **Language** — Primary language for labels? (zh / en / auto-detect)

Save responses to `config.json`:
```json
{
  "defaultTheme": "tech-blue",
  "outputDir": "./diagrams",
  "language": "auto"
}
```

On subsequent invocations, read `config.json` and apply defaults. User can override per-invocation with `--theme`, `--lang` flags.

---

## Supporting Files

The skill directory contains these files. Read them when needed — don't load everything upfront.

| File | When to read |
|------|-------------|
| [themes.md](themes.md) | When applying colors — has all 5 themes with 10 semantic colors + 7 text colors each |
| [xml-reference.md](xml-reference.md) | When writing XML — canvas boilerplate, 8 element templates, arrow direction table |
| [examples.md](examples.md) | When generating a diagram — 3 complete XML examples with coordinate calculations |

| `config.json` | On every invocation — user preferences (created on first run, see Initial Setup) |

### Example `.drawio` files (in `examples/`)

These are real, working `.drawio` files you can read as reference when generating similar diagram types:

- `examples/flow-cicd.drawio` — Linear flow, 4 nodes, tech-blue theme
- `examples/compare-monolith-vs-micro.drawio` — Comparison, 2 columns × 3 rows, morandi theme
- `examples/loop-ml-training.drawio` — Cycle, 4 nodes clockwise, mint theme
