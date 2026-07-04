# Layout Algorithms

Read the section for your chosen diagram type, then compute every coordinate from the formulas before writing XML. All formulas share the Global Constants below.

**Contents:** [Constants](#global-constants) · [flow](#flow) · [flow-vertical](#flow-vertical) · [compare](#compare) · [layers](#layers) · [loop](#loop) · [tree](#tree) · [hub](#hub) · [columns](#columns) · [matrix](#matrix) · [funnel](#funnel) · [timeline](#timeline) · [sequence](#sequence) · [swimlane](#swimlane)

## Global Constants

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

---

## `flow` — Linear Flow (left-to-right) {#flow}

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

## `flow-vertical` — Linear Flow (top-to-bottom) {#flow-vertical}

```
x    = CANVAS_PAD + (Canvas width / 2) - NODE_W / 2
y[i] = CANVAS_PAD + TITLE_H + GAP_V + i × (NODE_H + GAP_V)
```

## `compare` — Left-Right Comparison {#compare}

```
VS_W = 50   # width of "VS" badge

Left column x  = CANVAS_PAD
Right column x = CANVAS_PAD + NODE_W + GAP_H + VS_W + GAP_H
VS badge x     = CANVAS_PAD + NODE_W + GAP_H

Header y = CANVAS_PAD + TITLE_H + GAP_V
Row y[j] = Header y + NODE_H + GAP_V/2 + j × (NODE_H + GAP_V/2)
```

Each side has a header node (title) and content rows below.

## `layers` — Layer Stack {#layers}

```
LAYER_W = 400

x = CANVAS_PAD + (canvas center offset)
y[i] = CANVAS_PAD + TITLE_H + GAP_V + i × (NODE_H_RICH + GAP_V/3)

Canvas width  = CANVAS_PAD × 2 + LAYER_W
Canvas height = CANVAS_PAD × 2 + TITLE_H + GAP_V + n × NODE_H_RICH + (n-1) × GAP_V/3
```

Layers span full width. Top layer = highest abstraction.

## `loop` — Cycle / Feedback Loop {#loop}

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

## `tree` — Tree / Hierarchy {#tree}

```
Level spacing = GAP_V × 1.5
Sibling spacing = NODE_W + GAP_H / 2

Root: centered at top
Children: evenly distributed below parent, centered under parent

Subtree width = max(sum of children subtree widths, NODE_W)
Parent x = leftmost child x + (rightmost child x + NODE_W - leftmost child x) / 2 - NODE_W / 2
```

## `hub` — Hub and Spoke (Center Radiate) {#hub}

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

Hub rays (center→spoke connectors) are decorative straight lines: use `endArrow=none` and no `edgeStyle` — the orthogonal-routing rule applies only to flow arrows.

## `columns` — Parallel Columns {#columns}

```
Column x[i] = CANVAS_PAD + i × (NODE_W + GAP_H)
Header y     = CANVAS_PAD + TITLE_H + GAP_V
Item y[j]    = Header y + NODE_H + GAP_V/2 + j × (NODE_H + GAP_V/3)
```

Each column has a header node (colored) and vertically stacked item nodes below.

## `matrix` — Comparison Matrix {#matrix}

```
CELL_W = 140
CELL_H = 45
HEADER_H = 40

Col header x[c] = CANVAS_PAD + HEADER_W + GAP_H/3 + c × (CELL_W + GAP_H/3)
Row header y[r] = CANVAS_PAD + TITLE_H + HEADER_H + GAP_V/3 + r × (CELL_H + GAP_V/3)
Cell (r,c): x = Col header x[c], y = Row header y[r]
```

## `funnel` — Funnel {#funnel}

```
MAX_W = 360
MIN_W = 120

w[i] = MAX_W - i × ((MAX_W - MIN_W) / (n - 1))
x[i] = CANVAS_PAD + (MAX_W - w[i]) / 2
y[i] = CANVAS_PAD + TITLE_H + GAP_V + i × (NODE_H + GAP_V / 3)
```

Centered, decreasing-width bands stacked vertically.

## `timeline` — Timeline {#timeline}

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

The axis line and ticks are unbound edges anchored with explicit `mxPoint` coordinates (`sourcePoint`/`targetPoint`) and `endArrow=none` — see `examples/timeline-llm-history.drawio`.

## `sequence` — Sequence Diagram {#sequence}

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

## `swimlane` — Swimlane Process (roles × steps) {#swimlane}

Use flat lane-band rectangles, not draw.io's native swimlane container — absolute coordinates keep generation and validation simple.

```
LANE_H       = 130   # lane band height
LANE_LABEL_W = 110   # left strip reserved for the role label

Lane band i:
  x = CANVAS_PAD
  y = CANVAS_PAD + TITLE_H + GAP_V + i × LANE_H
  w = LANE_LABEL_W + GAP_H/2 + n_steps × (NODE_W + GAP_H/2)
  h = LANE_H

Step node (lane i, column j):
  x = CANVAS_PAD + LANE_LABEL_W + GAP_H/2 + j × (NODE_W + GAP_H/2)
  y = lane_y + (LANE_H - NODE_H) / 2
```

Rules:
- Define ALL lane bands before any step node — filled containers drawn after their children hide them.
- Alternate lane fills between `group` and `neutral` for zebra striping; lane label goes in the left strip as a text cell.
- Each process step occupies its own column j (a global step counter), so the flow reads left-to-right even as it crosses lanes; cross-lane arrows run vertically at the column of the target step.
