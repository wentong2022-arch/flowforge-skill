# XML Reference

## Canvas Boilerplate

```xml
<mxfile host="app.diagrams.net">
    <diagram name="{DIAGRAM_TITLE}" id="{UNIQUE_ID}">
        <mxGraphModel dx="0" dy="0" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="{CANVAS_W}" pageHeight="{CANVAS_H}" background="none" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <!-- content elements here -->
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

Compute `CANVAS_W` and `CANVAS_H` from the layout algorithm's formulas in SKILL.md.

---

## Element ID Convention

- Nodes: `node_1`, `node_2`, `node_3`, ...
- Arrows: `arr_1_2` (arrow from node_1 to node_2)
- Groups: `group_a`, `group_b`
- Title: `title_main`
- Labels: `label_1`, `label_2`

---

## Element Templates

### Diagram title

```xml
<mxCell id="title_main" value="Diagram Title" style="text;html=1;fontSize=18;fontColor=#2D3748;align=center;verticalAlign=middle;fontStyle=1;" parent="1" vertex="1">
    <mxGeometry x="{x}" y="10" width="{CANVAS_W - CANVAS_PAD*2}" height="28" as="geometry"/>
</mxCell>
```

### Simple node (single label)

```xml
<mxCell id="node_1" value="Node Label" style="rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=1.2;arcSize=10;fontSize=13;fontColor={titleColor};" parent="1" vertex="1">
    <mxGeometry x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" as="geometry"/>
</mxCell>
```

### Rich node (title + content list)

```xml
<mxCell id="node_1" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=1.2;arcSize=10;" parent="1" vertex="1">
    <mxGeometry x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H_RICH}" as="geometry"/>
</mxCell>
<mxCell id="node_1_title" value="&lt;b&gt;Module Title&lt;/b&gt;" style="text;html=1;fontSize=13;fontColor={titleColor};align=center;verticalAlign=middle;" parent="1" vertex="1">
    <mxGeometry x="{x}" y="{y+5}" width="{NODE_W}" height="22" as="geometry"/>
</mxCell>
<mxCell id="node_1_body" value="&amp;bull; Item one&lt;br&gt;&amp;bull; Item two&lt;br&gt;&amp;bull; Item three" style="text;html=1;fontSize=10;fontColor={bodyColor};align=left;verticalAlign=top;spacingLeft=8;" parent="1" vertex="1">
    <mxGeometry x="{x+10}" y="{y+30}" width="{NODE_W-20}" height="50" as="geometry"/>
</mxCell>
```

### Arrow (bound to source/target)

```xml
<mxCell id="arr_1_2" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor={arrowColor};strokeWidth=0.8;endSize=5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="node_1" target="node_2" edge="1">
    <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Arrow with label

```xml
<mxCell id="arr_1_2" value="&lt;span style=&quot;font-size:9px;color:{keywordColor}&quot;&gt;label text&lt;/span&gt;" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor={arrowColor};strokeWidth=0.8;endSize=5;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" parent="1" source="node_1" target="node_2" edge="1">
    <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Dashed group box

```xml
<mxCell id="group_a" value="Group Name" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor={groupStroke};strokeWidth=1.0;dashed=1;fontSize=10;fontColor={annotationColor};verticalAlign=top;align=left;spacingLeft=8;spacingTop=4;" parent="1" vertex="1">
    <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>
</mxCell>
```

### Diamond (decision node)

```xml
<mxCell id="node_d1" value="Condition?" style="rhombus;whiteSpace=wrap;html=1;fillColor={accentFill};strokeColor={accentStroke};strokeWidth=1.2;fontSize=11;fontColor={titleColor};" parent="1" vertex="1">
    <mxGeometry x="{x}" y="{y}" width="{DIAMOND_W}" height="{DIAMOND_H}" as="geometry"/>
</mxCell>
```

### Cylinder (database/storage)

```xml
<mxCell id="node_db1" value="Database" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=8;fillColor={storageFill};strokeColor={storageStroke};strokeWidth=1.2;fontSize=12;fontColor={titleColor};" parent="1" vertex="1">
    <mxGeometry x="{x}" y="{y}" width="120" height="60" as="geometry"/>
</mxCell>
```

---

## Arrow Exit/Entry Direction Reference

| Direction | exitX | exitY | entryX | entryY |
|-----------|-------|-------|--------|--------|
| Right → | 1 | 0.5 | 0 | 0.5 |
| Left ← | 0 | 0.5 | 1 | 0.5 |
| Down ↓ | 0.5 | 1 | 0.5 | 0 |
| Up ↑ | 0.5 | 0 | 0.5 | 1 |

**Important:** `exitX/exitY` defines where the arrow leaves the source node, `entryX/entryY` defines where it enters the target node. Values are ratios (0–1) of the node's bounding box. Always include `exitDx=0;exitDy=0;entryDx=0;entryDy=0` to disable offsets.

**Why `edgeStyle=orthogonalEdgeStyle`:** This forces draw.io to route edges using only horizontal and vertical segments. Without it, arrows between non-aligned nodes (e.g., branching/merging flows) render as diagonals. Always include this in every arrow — it has no effect on already-aligned arrows.
