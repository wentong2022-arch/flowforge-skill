# Color Themes

5 themes available. Default: **tech-blue**.

All values are contrast-audited against a white canvas: text roles ≥ 4.5:1 (WCAG AA),
arrow lines ≥ 3:1, node strokes ≥ 2.5:1 (`group` borders are decorative and exempt).
Keep `scripts/validate.py` in sync when editing any value.

## Semantic Color Roles

### Base 4 — Use these for 80%+ of nodes

| Role | Usage |
|------|-------|
| **primary** | Starting/ending points, user input, final output |
| **process** | Core processing steps, main flow (the default for most nodes) |
| **accent** | 1-2 key turning points only — use sparingly |
| **neutral** | Background modules, data sources, external inputs |

### Extended 6 — Use only when genuinely needed

| Role | Usage |
|------|-------|
| **success** | Positive results, completed states |
| **warning** | Decision points, pending, needs attention |
| **error** | Pain points, failures, error paths |
| **secondary** | Auxiliary steps, optional paths |
| **storage** | Databases, caches, external services |
| **group** | Dashed group box fill and border |

### Background Tints — bg-1 … bg-5

Ultra-light large-area backgrounds: section/region backdrops behind node clusters,
swimlane zebra striping, and filled group boxes. Rules:
- Backgrounds only — never as node fills; nodes placed on top must use regular fills.
- Draw bg rectangles BEFORE the nodes they contain (z-order).
- No text directly on a bg tint except via the annotation/title text colors.
- Adjacent regions: pick tints of different hue (e.g. bg-1 next to bg-3), not neighbors in lightness.

---

## `tech-blue` — 科技蓝灰 (Default)

Blue-gray primary with warm accents. Clean, modern, ideal for technical content.

| Role | Fill | Stroke |
|------|------|--------|
| primary | `#E8F0FE` | `#5B8DEF` |
| process | `#D6E4F9` | `#5B8DEF` |
| accent | `#FFF0E5` | `#E29057` |
| neutral | `#EDF2F7` | `#95A5B9` |
| success | `#E6F5EC` | `#5BA87C` |
| warning | `#FFF8E1` | `#CC9C2F` |
| error | `#FDE8E8` | `#D05050` |
| secondary | `#EDE8F5` | `#8B7EC4` |
| storage | `#E8F4F2` | `#5BA8A0` |
| group | `#F5F7FA` | `#CBD5E0` |

| Text Role | Color |
|-----------|-------|
| title | `#2D3748` |
| body | `#68778D` |
| keyword | `#3F72D9` |
| success-label | `#45815F` |
| error-label | `#CE4848` |
| arrow | `#8496AE` |
| annotation | `#68778D` |

| Background Tint | Color | Hue family |
|-----------------|-------|-----------|
| bg-1 | `#F1F5FB` | primary |
| bg-2 | `#FBF5F1` | accent |
| bg-3 | `#F2FAF5` | success |
| bg-4 | `#F5F3FA` | secondary |
| bg-5 | `#F3F9F8` | storage |

---

## `morandi` — 莫兰迪

Muted sage-green + smoky purple + warm gray. Sophisticated, understated.

| Role | Fill | Stroke |
|------|------|--------|
| primary | `#D8E2EA` | `#8FA5BA` |
| process | `#E2D8E6` | `#B09DB8` |
| accent | `#EDE8E1` | `#AFA190` |
| neutral | `#DDE6DB` | `#90AB8C` |
| success | `#D6E4D8` | `#88AD8B` |
| warning | `#E8E2D2` | `#B5A172` |
| error | `#E8D6D6` | `#B89090` |
| secondary | `#DBD8E6` | `#A098B5` |
| storage | `#D4DFD8` | `#8DA898` |
| group | `#EDEAE6` | `#C5BFB8` |

| Text Role | Color |
|-----------|-------|
| title | `#4A4A4A` |
| body | `#767676` |
| keyword | `#7B6B8A` |
| success-label | `#5B7F5D` |
| error-label | `#A26666` |
| arrow | `#9C9387` |
| annotation | `#767676` |

| Background Tint | Color | Hue family |
|-----------------|-------|-----------|
| bg-1 | `#F3F6F9` | primary |
| bg-2 | `#F9F7F3` | accent |
| bg-3 | `#F3F9F4` | success |
| bg-4 | `#F5F3F9` | secondary |
| bg-5 | `#F9F3F3` | error |

---

## `mint` — 薄荷清新

Mint green primary with warm yellow accents. Fresh, airy.

| Role | Fill | Stroke |
|------|------|--------|
| primary | `#E0F5F0` | `#54B49D` |
| process | `#CCF0E8` | `#2A9D8F` |
| accent | `#FFF4E6` | `#E3921F` |
| neutral | `#E8F0ED` | `#71AF9D` |
| success | `#D4F0D8` | `#4AAE5C` |
| warning | `#FFF2D6` | `#D19A34` |
| error | `#FCE4E4` | `#C85050` |
| secondary | `#E0E8F0` | `#7AA0C0` |
| storage | `#D8F0EE` | `#4AADA5` |
| group | `#F0F7F5` | `#B0D0C5` |

| Text Role | Color |
|-----------|-------|
| title | `#1A3A3A` |
| body | `#5A7A7A` |
| keyword | `#238377` |
| success-label | `#368545` |
| error-label | `#C74E4E` |
| arrow | `#6A9F91` |
| annotation | `#5E7C76` |

| Background Tint | Color | Hue family |
|-----------------|-------|-----------|
| bg-1 | `#F2FBF8` | primary |
| bg-2 | `#FBF7F1` | accent |
| bg-3 | `#F2FAF3` | success |
| bg-4 | `#F3F6F9` | secondary |
| bg-5 | `#FBF1F1` | error |

---

## `terracotta` — 暖陶商务

Earthy tones — clay and sand. Warm, grounded, suits business and strategy content.

| Role | Fill | Stroke |
|------|------|--------|
| primary | `#FAF0E4` | `#D4956A` |
| process | `#F0E0CC` | `#B07D4F` |
| accent | `#E8DDD0` | `#A89279` |
| neutral | `#F5EDE3` | `#BD9E74` |
| success | `#E8ECDA` | `#8EA06A` |
| warning | `#F5ECD0` | `#C39F3E` |
| error | `#F0DCD0` | `#B07060` |
| secondary | `#E8E0D8` | `#A89088` |
| storage | `#E8E4DA` | `#9A9478` |
| group | `#F5F0E8` | `#D0C4B0` |

| Text Role | Color |
|-----------|-------|
| title | `#3D2C1E` |
| body | `#87725E` |
| keyword | `#996D45` |
| success-label | `#657E44` |
| error-label | `#A05040` |
| arrow | `#B28D5C` |
| annotation | `#897259` |

| Background Tint | Color | Hue family |
|-----------------|-------|-----------|
| bg-1 | `#FBF7F1` | primary |
| bg-2 | `#F8F9F3` | success |
| bg-3 | `#FBF9F1` | warning |
| bg-4 | `#FBF5F1` | error |
| bg-5 | `#F9F6F3` | secondary |

---

## `indigo` — 靛蓝深邃

Indigo + violet, higher saturation. Bold, authoritative.

| Role | Fill | Stroke |
|------|------|--------|
| primary | `#DBEAFE` | `#3B82F6` |
| process | `#DDD6FE` | `#7C3AED` |
| accent | `#E0E7FF` | `#4F62B0` |
| neutral | `#E8ECF4` | `#7C8DB5` |
| success | `#D4F0E0` | `#3AA06A` |
| warning | `#FEF3C7` | `#D29820` |
| error | `#FEE2E2` | `#DC2626` |
| secondary | `#E0D8F0` | `#6B50B0` |
| storage | `#D8E8F0` | `#4080A0` |
| group | `#EEF0F8` | `#A0AAC8` |

| Text Role | Color |
|-----------|-------|
| title | `#1E293B` |
| body | `#64748B` |
| keyword | `#7C3AED` |
| success-label | `#29864E` |
| error-label | `#DC2626` |
| arrow | `#8596AE` |
| annotation | `#637895` |

| Background Tint | Color | Hue family |
|-----------------|-------|-----------|
| bg-1 | `#F1F5FB` | primary |
| bg-2 | `#FBF9F1` | warning |
| bg-3 | `#F2FAF5` | success |
| bg-4 | `#F5F2FA` | secondary |
| bg-5 | `#F2F7FA` | storage |


---

## Color Rhythm — Worked Examples

**Bad** (rainbow — every node a different color):
```
[neutral] 数据源 → [process] 采集 → [warning] 检查 → [success] 清洗 → [error] 告警 → [storage] 入库
```

**Bad** (wall of one color — 9 nodes all the same):
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
