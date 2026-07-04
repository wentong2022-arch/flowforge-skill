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

### Walkthrough 3: `loop` (loop-ml-training.drawio)

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
