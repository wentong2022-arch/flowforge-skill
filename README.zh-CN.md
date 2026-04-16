# FlowForge

> 一个 Claude Code skill，把自然语言转换成专业的 draw.io 图表 — 流程图、架构图、对比图等。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-orange.svg)](https://code.claude.com)

[English](README.md) | **中文**

<p align="center">
  <img src="assets/screenshots/05-llm-full-stack-architecture.png" alt="大模型全栈技术架构 — FlowForge 生成" width="800"/>
</p>

---

## FlowForge 是什么？

FlowForge 是一个 [Claude Code](https://code.claude.com) skill，可以根据自然语言描述生成专业的 `.drawio` 图表文件。你只需描述想要的内容 — 一个 CI/CD 流水线、一个系统架构、一个算法对比 — FlowForge 就会生成一份布局规整的 draw.io XML 文件，可直接在 [draw.io 桌面版](https://www.drawio.com/) 或 [app.diagrams.net](https://app.diagrams.net) 中打开。

### 为什么用 draw.io XML？

- **可编辑** — 生成后可以在任何 draw.io 编辑器中继续调整
- **跨平台** — 浏览器、桌面应用、VS Code 插件、Confluence 等都支持
- **生成可控** — 绝对坐标 + 显式样式，让 Claude 输出稳定可预测的布局

## 特性

- **11 种布局算法** — `flow`、`flow-vertical`、`compare`、`layers`、`loop`、`tree`、`hub`、`columns`、`matrix`、`funnel`、`timeline`、`sequence`
- **5 套配色主题** — `tech-blue`（默认）、`morandi`、`mint`、`terracotta`、`indigo`
- **智能配色原则** — 自适应色彩预算；蓝色主导 + 关键节点点缀，避免"彩虹色"反模式
- **正交箭头路由** — 横平竖直的折线，没有斜线
- **中英文双语** — 标签使用中文，技术缩写保留英文
- **草图先行** — 生成 XML 前先用 ASCII 草图与你确认结构

## 安装

### 方式 1：作为 Claude Code 插件（推荐）

```bash
# 在 Claude Code 中
/plugin install https://github.com/winstonyoyo/flowforge-skill
```

或先添加到你的插件市场再安装。

### 方式 2：手动安装 Skill

克隆仓库并复制到 Claude Code 的 skills 目录：

```bash
git clone https://github.com/winstonyoyo/flowforge-skill.git
cp -r flowforge-skill/skills/FlowForge ~/.claude/skills/
# 或仅安装到当前项目：
cp -r flowforge-skill/skills/FlowForge ./.claude/skills/
```

## 使用方式

在 Claude Code 中直接描述你要画什么：

```
画一个用户注册流程图
帮我画 RAG 的检索流程
对比一下 PPO、DPO、GRPO 算法
draw a microservices architecture diagram
```

或显式调用 `/FlowForge` 命令：

```
/FlowForge "OAuth 2.0 授权码流程"
/FlowForge path/to/design-doc.md --type layers --theme morandi
```

### 工作流程

1. **描述需求**
2. **确认配色**（或使用默认 `tech-blue`）
3. **审查 ASCII 草图** — FlowForge 在生成 XML 前会先展示规划好的结构
4. **在 draw.io 中打开** `.drawio` 文件，按需调整

## 配色主题

| 主题 | 风格 | 适用场景 |
|------|------|----------|
| `tech-blue` | 蓝灰为主 + 暖色点缀 | 技术内容、系统文档（默认） |
| `morandi` | 灰绿 + 烟紫 | 设计作品集、品牌方案 |
| `mint` | 薄荷绿 + 暖黄 | 产品流程、用户旅程 |
| `terracotta` | 陶土 + 沙色 | 商业策略、运营流程 |
| `indigo` | 靛蓝 + 紫罗兰 | 技术演示、产品发布 |

## 图表类型

| 类型 | 代号 | 适用场景 |
|------|------|----------|
| 线性流程 | `flow` | A → B → C 顺序步骤 |
| 纵向流程 | `flow-vertical` | 自上而下的流程 |
| 左右对比 | `compare` | A vs B 并列对比 |
| 层级堆叠 | `layers` | 多层架构 |
| 循环 | `loop` | 迭代过程（CI/CD、训练循环） |
| 树形 | `tree` | 层级、分类 |
| 中心辐射 | `hub` | 一个核心 + 多个分支 |
| 并列列 | `columns` | 3+ 并列概念 |
| 矩阵 | `matrix` | 多维度对比 |
| 漏斗 | `funnel` | 筛选、转化 |
| 时间轴 | `timeline` | 版本演进 |
| 序列图 | `sequence` | 组件交互 |

## 示例画廊

FlowForge 生成的 9 个示例图，覆盖全部 5 套主题和最常用的图表类型 — 源文件见 `gallery/`。

### 多层架构（`layers` × `tech-blue` + 多色）

<p align="center">
  <img src="assets/screenshots/03-platform-architecture.png" alt="经济数据平台架构" width="700"/>
</p>

### 算法对比（`columns` + 循环 × `tech-blue`）

<p align="center">
  <img src="assets/screenshots/04-ppo-dpo-grpo-comparison.png" alt="PPO vs DPO vs GRPO" width="800"/>
</p>

### 决策树（`tree` × `mint`）

<p align="center">
  <img src="assets/screenshots/07-storage-decision-tree-mint.png" alt="数据存储选型决策树" width="650"/>
</p>

### 中心辐射（`hub` × `indigo`）

<p align="center">
  <img src="assets/screenshots/08-agent-capabilities-hub-indigo.png" alt="Agent 能力中心" width="500"/>
</p>

### 时间轴（`timeline` × `terracotta`）

<p align="center">
  <img src="assets/screenshots/09-llm-history-timeline-terracotta.png" alt="大模型发展简史" width="800"/>
</p>

### 完整索引

| # | 图表 | 类型 | 主题 |
|---|------|------|------|
| 01 | 数据采集入库流程 | `flow-vertical` + 分支 | `tech-blue` |
| 02 | 智能问数查询流程 | `flow-vertical`（长流程 + 色彩节奏） | `tech-blue` |
| 03 | 经济数据平台架构 | `layers`（5 层） | 每层独立配色 |
| 04 | PPO vs DPO vs GRPO 算法 | `columns`（横向 × 纵向对比，含循环） | `tech-blue` + 强调色 |
| 05 | 大模型全栈架构 | `layers`（6 层 + 横切关注点） | 全色板 |
| 06 | 传统 vs AI 增强数据团队 | `compare` | `morandi` |
| 07 | 数据存储选型决策树 | `tree` | `mint` |
| 08 | Agent 能力中心 | `hub`（6 辐射） | `indigo` |
| 09 | 大模型发展简史 | `timeline`（上下交替） | `terracotta` |

> 在 [app.diagrams.net](https://app.diagrams.net) 中打开任意 `.drawio` 文件即可查看或编辑。

## 项目结构

```
flowforge-skill/
├── .claude-plugin/
│   └── plugin.json           # 插件元数据
├── skills/
│   └── FlowForge/
│       ├── SKILL.md          # Skill 主入口
│       ├── themes.md         # 5 套配色定义
│       ├── xml-reference.md  # XML 元素模板
│       ├── examples.md       # 完整参考示例
│       └── examples/         # 参考 .drawio 文件
├── gallery/                  # 展示示例
├── assets/screenshots/       # README 截图
├── README.md                 # 英文 README
├── README.zh-CN.md           # 中文 README
├── LICENSE                   # MIT
└── CHANGELOG.md
```

## 设计理念

- **布局确定性** — 每种图表类型都有显式坐标公式，不是"让 AI 猜位置"
- **颜色语义化** — 每种颜色对应一种含义（主流程/强调/警告等），不做装饰性使用
- **节制优于装饰** — 大部分节点使用主导色系，强调色是手术刀而非刷子
- **双语标签** — 自然使用用户语言，技术术语（API、LLM、RAG）保留英文

## 贡献

欢迎提交 PR！特别欢迎以下方向的贡献：

- 新的图表类型布局（甘特图、思维导图、ER 图等）
- 更多配色主题
- 不同领域的画廊示例
- 翻译（`README.{lang}.md`）

## 致谢

参考了 Anthropic 的 [Thariq Shihipar](https://x.com/trq212) 的文章 [《构建 Claude Code 的经验：我们如何使用 Skills》](https://baoyu.io/translations/2026-03-17/claude-code-skills-lessons) 中的设计原则。

## 协议

[MIT](LICENSE) © 2026 [winstonyoyo](https://github.com/winstonyoyo)
