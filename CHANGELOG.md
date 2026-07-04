# Changelog

All notable changes to FlowForge will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-07-04

### Added
- **Background tints (`bg-1`…`bg-5`)** per theme: 25 hue-distinct ultra-light colors for region backdrops, swimlane zebra striping, and filled group boxes — closes the gap where large diagrams invented off-theme pastels (seen in gallery/05); validator recognizes them
- `tree` coordinate walkthrough in examples.md (bottom-up: children first, parent centered over children's span) — the last diagram family without a worked example

### Changed
- **Contrast audit**: all 5 themes re-tuned against WCAG targets — text roles ≥ 4.5:1, arrow lines ≥ 3:1, node strokes ≥ 2.5:1 (`group` borders exempt as decorative). 36 values darkened one step in the same hue; theme identities preserved. Biggest fixes: arrow colors (were 2.0–2.6:1 across all themes) and morandi's stroke family
- Bundled example `.drawio` files recolored attribute-aware (edge strokes → new arrow colors, vertex strokes / font colors → their role's new values); all six re-validate clean
- `tree` layout algorithm clarified in references/layouts.md (subtree width includes gaps; explicit bottom-up ordering)
- Swimlane zebra striping now uses `bg-*` tints instead of `group`/`neutral` fills

## [1.1.0] - 2026-07-04

### Added
- `scripts/validate.py` — deterministic validator run on every generated file: XML well-formedness, unique ids, dangling arrow references, orthogonal edge style, canvas bounds, node overlap, z-order (containers before children), font sizes, text-fit estimates, theme color compliance
- `scripts/render.sh` — PNG export via draw.io CLI, enabling a visual self-check step (model inspects the rendered image before delivering)
- `swimlane` diagram type (13th): flat lane bands + per-role step columns
- 3 more example files covering `tree`, `hub`, and `timeline` (promoted from gallery)
- XML templates for lane bands and coordinate-anchored decorative lines (timeline axis/ticks, hub rays)

### Changed
- SKILL.md slimmed from 530 to 240 lines: layout algorithms moved to `references/layouts.md` (read on demand), color-rhythm examples moved to `themes.md`
- Workflow: three confirmation stops merged into one combined proposal (type + theme + ASCII sketch); confirmation skipped when the request is unambiguous or no human is in the loop
- Configuration moved from `config.json` inside the skill directory to optional per-project `./.flowforge.json`; first-run interview removed
- Orthogonal-routing rule clarified: applies to flow arrows; `endArrow=none` decorative connectors (hub rays, timeline axes) may run straight
- Trigger description: added negative triggers for artistic image requests (logos, mascots)
- `examples.md` deduplicated — coordinate walkthroughs only, XML lives in the `.drawio` files

### Removed
- `config.json` runtime state inside the skill directory (broke read-only installs and dirtied git status)

## [1.0.0] - 2026-04-16

### Added
- Initial release of FlowForge skill
- 11 diagram type layouts: `flow`, `flow-vertical`, `compare`, `layers`, `loop`, `tree`, `hub`, `columns`, `matrix`, `funnel`, `timeline`, `sequence`
- 5 color themes: `tech-blue` (default), `morandi`, `mint`, `terracotta`, `indigo`
- Color usage principles with size-adaptive color budget (2-3 colors for short flows, 4-5 for long flows)
- Layout system with 13 global constants and per-type coordinate algorithms
- 8 XML element templates (rich nodes, simple nodes, arrows, diamonds, cylinders, dashed groups, etc.)
- Orthogonal arrow routing (`edgeStyle=orthogonalEdgeStyle`) for clean right-angle bends
- Bilingual support (Chinese + English labels)
- 5 gallery examples spanning data pipelines, architecture diagrams, and algorithm comparisons
- 12-item gotchas list documenting common XML generation pitfalls
- Plugin metadata (`.claude-plugin/plugin.json`) for one-click installation
