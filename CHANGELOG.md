# Changelog

All notable changes to FlowForge will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
