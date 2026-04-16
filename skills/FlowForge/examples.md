# Complete Examples

3 full, copy-pasteable draw.io XML examples. Each demonstrates a different diagram type and theme. Open any of these directly in draw.io or app.diagrams.net.

---

## Example 1: Linear Flow (`flow`, `tech-blue`)

**"CI/CD Pipeline"** — 4 nodes, left-to-right.

### Coordinate Calculations

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

### XML

```xml
<mxfile host="app.diagrams.net">
    <diagram name="CI/CD Pipeline" id="cicd_001">
        <mxGraphModel dx="0" dy="0" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="900" pageHeight="208" background="none" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <!-- Title -->
                <mxCell id="title_main" value="CI/CD Pipeline" style="text;html=1;fontSize=18;fontColor=#2D3748;align=center;verticalAlign=middle;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="40" y="10" width="820" height="28" as="geometry"/>
                </mxCell>
                <!-- Nodes -->
                <mxCell id="node_1" value="Code Commit" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F0FE;strokeColor=#5B8DEF;strokeWidth=1.2;arcSize=10;fontSize=13;fontColor=#2D3748;" parent="1" vertex="1">
                    <mxGeometry x="40" y="118" width="160" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_2" value="Build" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D6E4F9;strokeColor=#5B8DEF;strokeWidth=1.2;arcSize=10;fontSize=13;fontColor=#2D3748;" parent="1" vertex="1">
                    <mxGeometry x="260" y="118" width="160" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_3" value="Test" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D6E4F9;strokeColor=#5B8DEF;strokeWidth=1.2;arcSize=10;fontSize=13;fontColor=#2D3748;" parent="1" vertex="1">
                    <mxGeometry x="480" y="118" width="160" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_4" value="Deploy" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF0E5;strokeColor=#E8A87C;strokeWidth=1.2;arcSize=10;fontSize=13;fontColor=#2D3748;" parent="1" vertex="1">
                    <mxGeometry x="700" y="118" width="160" height="50" as="geometry"/>
                </mxCell>
                <!-- Arrows -->
                <mxCell id="arr_1_2" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor=#A0AEC0;strokeWidth=0.8;endSize=5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="node_1" target="node_2" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="arr_2_3" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor=#A0AEC0;strokeWidth=0.8;endSize=5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="node_2" target="node_3" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="arr_3_4" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor=#A0AEC0;strokeWidth=0.8;endSize=5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="node_3" target="node_4" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

---

## Example 2: Comparison (`compare`, `morandi`)

**"Monolith vs Microservices"** — 2 columns, 3 comparison dimensions.

### Coordinate Calculations

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

### XML

```xml
<mxfile host="app.diagrams.net">
    <diagram name="Monolith vs Microservices" id="compare_001">
        <mxGraphModel dx="0" dy="0" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="610" pageHeight="553" background="none" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <!-- Title -->
                <mxCell id="title_main" value="Monolith vs Microservices" style="text;html=1;fontSize=18;fontColor=#4A4A4A;align=center;verticalAlign=middle;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="40" y="10" width="530" height="28" as="geometry"/>
                </mxCell>
                <!-- Headers -->
                <mxCell id="node_h1" value="Monolith" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D8E2EA;strokeColor=#92A8BC;strokeWidth=1.2;arcSize=10;fontSize=14;fontColor=#4A4A4A;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="40" y="118" width="160" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_vs" value="VS" style="text;html=1;fontSize=14;fontColor=#7B6B8A;align=center;verticalAlign=middle;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="260" y="118" width="50" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_h2" value="Microservices" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2D8E6;strokeColor=#B5A3BC;strokeWidth=1.2;arcSize=10;fontSize=14;fontColor=#4A4A4A;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="370" y="118" width="160" height="50" as="geometry"/>
                </mxCell>
                <!-- Row 0: Deployment -->
                <mxCell id="node_l1" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D8E2EA;strokeColor=#92A8BC;strokeWidth=1.2;arcSize=10;" parent="1" vertex="1">
                    <mxGeometry x="40" y="193" width="160" height="90" as="geometry"/>
                </mxCell>
                <mxCell id="node_l1_t" value="&lt;b&gt;Deployment&lt;/b&gt;" style="text;html=1;fontSize=13;fontColor=#4A4A4A;align=center;verticalAlign=middle;" parent="1" vertex="1">
                    <mxGeometry x="40" y="198" width="160" height="22" as="geometry"/>
                </mxCell>
                <mxCell id="node_l1_b" value="&amp;bull; Single deployable unit&lt;br&gt;&amp;bull; All-or-nothing release&lt;br&gt;&amp;bull; Simple CI/CD" style="text;html=1;fontSize=10;fontColor=#7A7A7A;align=left;verticalAlign=top;spacingLeft=8;" parent="1" vertex="1">
                    <mxGeometry x="50" y="223" width="140" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_r1" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2D8E6;strokeColor=#B5A3BC;strokeWidth=1.2;arcSize=10;" parent="1" vertex="1">
                    <mxGeometry x="370" y="193" width="160" height="90" as="geometry"/>
                </mxCell>
                <mxCell id="node_r1_t" value="&lt;b&gt;Deployment&lt;/b&gt;" style="text;html=1;fontSize=13;fontColor=#4A4A4A;align=center;verticalAlign=middle;" parent="1" vertex="1">
                    <mxGeometry x="370" y="198" width="160" height="22" as="geometry"/>
                </mxCell>
                <mxCell id="node_r1_b" value="&amp;bull; Independent deploys&lt;br&gt;&amp;bull; Per-service releases&lt;br&gt;&amp;bull; Complex orchestration" style="text;html=1;fontSize=10;fontColor=#7A7A7A;align=left;verticalAlign=top;spacingLeft=8;" parent="1" vertex="1">
                    <mxGeometry x="380" y="223" width="140" height="50" as="geometry"/>
                </mxCell>
                <!-- Row 1: Scaling -->
                <mxCell id="node_l2" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D8E2EA;strokeColor=#92A8BC;strokeWidth=1.2;arcSize=10;" parent="1" vertex="1">
                    <mxGeometry x="40" y="308" width="160" height="90" as="geometry"/>
                </mxCell>
                <mxCell id="node_l2_t" value="&lt;b&gt;Scaling&lt;/b&gt;" style="text;html=1;fontSize=13;fontColor=#4A4A4A;align=center;verticalAlign=middle;" parent="1" vertex="1">
                    <mxGeometry x="40" y="313" width="160" height="22" as="geometry"/>
                </mxCell>
                <mxCell id="node_l2_b" value="&amp;bull; Scale entire app&lt;br&gt;&amp;bull; Vertical scaling&lt;br&gt;&amp;bull; Resource wasteful" style="text;html=1;fontSize=10;fontColor=#7A7A7A;align=left;verticalAlign=top;spacingLeft=8;" parent="1" vertex="1">
                    <mxGeometry x="50" y="338" width="140" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_r2" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2D8E6;strokeColor=#B5A3BC;strokeWidth=1.2;arcSize=10;" parent="1" vertex="1">
                    <mxGeometry x="370" y="308" width="160" height="90" as="geometry"/>
                </mxCell>
                <mxCell id="node_r2_t" value="&lt;b&gt;Scaling&lt;/b&gt;" style="text;html=1;fontSize=13;fontColor=#4A4A4A;align=center;verticalAlign=middle;" parent="1" vertex="1">
                    <mxGeometry x="370" y="313" width="160" height="22" as="geometry"/>
                </mxCell>
                <mxCell id="node_r2_b" value="&amp;bull; Scale per service&lt;br&gt;&amp;bull; Horizontal scaling&lt;br&gt;&amp;bull; Resource efficient" style="text;html=1;fontSize=10;fontColor=#7A7A7A;align=left;verticalAlign=top;spacingLeft=8;" parent="1" vertex="1">
                    <mxGeometry x="380" y="338" width="140" height="50" as="geometry"/>
                </mxCell>
                <!-- Row 2: Complexity -->
                <mxCell id="node_l3" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D8E2EA;strokeColor=#92A8BC;strokeWidth=1.2;arcSize=10;" parent="1" vertex="1">
                    <mxGeometry x="40" y="423" width="160" height="90" as="geometry"/>
                </mxCell>
                <mxCell id="node_l3_t" value="&lt;b&gt;Complexity&lt;/b&gt;" style="text;html=1;fontSize=13;fontColor=#4A4A4A;align=center;verticalAlign=middle;" parent="1" vertex="1">
                    <mxGeometry x="40" y="428" width="160" height="22" as="geometry"/>
                </mxCell>
                <mxCell id="node_l3_b" value="&amp;bull; Simple codebase&lt;br&gt;&amp;bull; Easy to understand&lt;br&gt;&amp;bull; Hard to maintain at scale" style="text;html=1;fontSize=10;fontColor=#7A7A7A;align=left;verticalAlign=top;spacingLeft=8;" parent="1" vertex="1">
                    <mxGeometry x="50" y="453" width="140" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_r3" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2D8E6;strokeColor=#B5A3BC;strokeWidth=1.2;arcSize=10;" parent="1" vertex="1">
                    <mxGeometry x="370" y="423" width="160" height="90" as="geometry"/>
                </mxCell>
                <mxCell id="node_r3_t" value="&lt;b&gt;Complexity&lt;/b&gt;" style="text;html=1;fontSize=13;fontColor=#4A4A4A;align=center;verticalAlign=middle;" parent="1" vertex="1">
                    <mxGeometry x="370" y="428" width="160" height="22" as="geometry"/>
                </mxCell>
                <mxCell id="node_r3_b" value="&amp;bull; Distributed complexity&lt;br&gt;&amp;bull; Steep learning curve&lt;br&gt;&amp;bull; Better long-term agility" style="text;html=1;fontSize=10;fontColor=#7A7A7A;align=left;verticalAlign=top;spacingLeft=8;" parent="1" vertex="1">
                    <mxGeometry x="380" y="453" width="140" height="50" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

---

## Example 3: Cycle (`loop`, `mint`)

**"ML Training Loop"** — 4 nodes in a clockwise rectangle.

### Coordinate Calculations

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

### XML

```xml
<mxfile host="app.diagrams.net">
    <diagram name="ML Training Loop" id="loop_001">
        <mxGraphModel dx="0" dy="0" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="560" pageHeight="338" background="none" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <!-- Title -->
                <mxCell id="title_main" value="ML Training Loop" style="text;html=1;fontSize=18;fontColor=#1A3A3A;align=center;verticalAlign=middle;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="40" y="10" width="480" height="28" as="geometry"/>
                </mxCell>
                <!-- Nodes (clockwise) -->
                <mxCell id="node_1" value="Prepare Data" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E0F5F0;strokeColor=#6DBFAB;strokeWidth=1.2;arcSize=10;fontSize=13;fontColor=#1A3A3A;" parent="1" vertex="1">
                    <mxGeometry x="40" y="118" width="160" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_2" value="Train Model" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CCF0E8;strokeColor=#2A9D8F;strokeWidth=1.2;arcSize=10;fontSize=13;fontColor=#1A3A3A;" parent="1" vertex="1">
                    <mxGeometry x="320" y="118" width="160" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_3" value="Evaluate" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CCF0E8;strokeColor=#2A9D8F;strokeWidth=1.2;arcSize=10;fontSize=13;fontColor=#1A3A3A;" parent="1" vertex="1">
                    <mxGeometry x="320" y="248" width="160" height="50" as="geometry"/>
                </mxCell>
                <mxCell id="node_4" value="Tune Hyperparams" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF4E6;strokeColor=#E9A84C;strokeWidth=1.2;arcSize=10;fontSize=13;fontColor=#1A3A3A;" parent="1" vertex="1">
                    <mxGeometry x="40" y="248" width="160" height="50" as="geometry"/>
                </mxCell>
                <!-- Arrows (clockwise) -->
                <mxCell id="arr_1_2" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor=#9DC0B7;strokeWidth=0.8;endSize=5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="node_1" target="node_2" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="arr_2_3" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor=#9DC0B7;strokeWidth=0.8;endSize=5;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" parent="1" source="node_2" target="node_3" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="arr_3_4" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor=#9DC0B7;strokeWidth=0.8;endSize=5;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="node_3" target="node_4" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="arr_4_1" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;strokeColor=#9DC0B7;strokeWidth=0.8;endSize=5;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" parent="1" source="node_4" target="node_1" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```
