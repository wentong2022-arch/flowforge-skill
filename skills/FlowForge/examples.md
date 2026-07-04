# Examples

## Index of example files

Read the `.drawio` file matching your diagram type directly — they are real, working files (open them in draw.io to see the result). The XML is not duplicated here.

| File | Type | Theme | Demonstrates |
|------|------|-------|--------------|
| `examples/flow-cicd.drawio` | `flow` | tech-blue | 4-node linear flow, bound arrows with exit/entry points |
| `examples/compare-monolith-vs-micro.drawio` | `compare` | morandi | Header + 3 rich-node rows per side, VS badge |
| `examples/loop-ml-training.drawio` | `loop` | mint | 4 nodes clockwise, return arrow routed outside |
| `examples/tree-storage-decision.drawio` | `tree` | mint | Decision diamonds, labeled yes/no branches |
| `examples/hub-agent-capabilities.drawio` | `hub` | indigo | 6 spokes from lookup table, decorative rays (`endArrow=none`) |
| `examples/timeline-llm-history.drawio` | `timeline` | terracotta | Axis + ticks as unbound `mxPoint` edges, alternating events |

## Coordinate-calculation walkthroughs

How the layout formulas produce concrete coordinates — follow the same arithmetic for your own diagram, then cross-check the file.

### Walkthrough 1: `flow` (flow-cicd.drawio)

```
n = 4, NODE_W = 160, NODE_H = 50, GAP_H = 60, CANVAS_PAD = 40, TITLE_H = 28, GAP_V = 50

x[0] = 40
x[1] = 40 + 1×(160+60) = 260
x[2] = 40 + 2×(160+60) = 480
x[3] = 40 + 3×(160+60) = 700

y = 40 + 28 + 50 = 118

CANVAS_W = 40×2 + 4×160 + 3×60 = 900
CANVAS_H = 40×2 + 28 + 50 + 50 = 208
```

### Walkthrough 2: `compare` (compare-monolith-vs-micro.drawio)

```
NODE_W = 160, NODE_H_RICH = 90, GAP_H = 60, VS_W = 50, CANVAS_PAD = 40

Left x   = 40
VS x     = 40 + 160 + 60 = 260
Right x  = 260 + 50 + 60 = 370

Header y  = 40 + 28 + 50 = 118
Row y[0]  = 118 + 50 + 25 = 193
Row y[1]  = 193 + 90 + 25 = 308
Row y[2]  = 308 + 90 + 25 = 423

CANVAS_W = 40 + 370 + 160 + 40 = 610
CANVAS_H = 423 + 90 + 40 = 553
```

### Walkthrough 3: `tree` (tree-storage-decision.drawio)

The core tree rule: lay out the deepest level first, then center each parent over the span of its children.

```
Root + 4 rich children (NODE_W = 160, NODE_H_RICH = 90), CANVAS_PAD = 40, TITLE_H = 28

Children first (compact sibling gap GAP_H/3 = 20 because rich nodes are wide):
  x[j] = 40 + j × (160 + 20)  →  40, 220, 400, 580
  y    = 190

Children span: 40 … (580 + 160) = 740  →  span center = (40 + 740) / 2 = 390

Root centered over that span (root widened to 240 for emphasis):
  root x = 390 - 240/2 = 270
  root y = 58   (directly below title; children top 190 - root bottom 108 = 82 ≈ GAP_V × 1.5)

CANVAS_W = 40 + 700 + 40 = 780
CANVAS_H = 190 + 90 + 40 = 320
```

For multi-level trees apply the same rule bottom-up: each subtree's width = max(sum of child subtree widths + gaps, NODE_W); each parent centers over its own children's span, not over the whole canvas.

### Walkthrough 4: `loop` (loop-ml-training.drawio)

```
NODE_W = 160, NODE_H = 50, GAP_H = 120, GAP_V = 80, CANVAS_PAD = 40, TITLE_H = 28

Positions (clockwise):
  node_1 (top-left):     x=40,  y=118
  node_2 (top-right):    x=320, y=118
  node_3 (bottom-right): x=320, y=248
  node_4 (bottom-left):  x=40,  y=248

CANVAS_W = 40 + 320 + 160 + 40 = 560
CANVAS_H = 248 + 50 + 40 = 338
```
