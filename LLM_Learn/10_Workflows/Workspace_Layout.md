---
type: workflow_doc
topic: workspace_layout
status: active
---

# Workspace Layout

## 设计原则

- 长期目标由“单一 LLM 学习”升级为“机器人足球 / 具身智能系统 + AI Infra 支撑”
- 长期计划和短期执行分层
- 高价值沉淀与日常推进分层
- 年 / 月 / 周 / 日各自回答不同问题
- 工作流与模板单独保留，先作为过渡层，后续再逐步迁入 OpenClaw 原生流程

## 当前目录职责

### `01_DailyNotes/`

- 结构：`年 / 月 / 日`
- 例子：`01_DailyNotes/2026/2026-03/2026-03-31.md`
- 作用：
  - 今天做什么
  - 今天实际完成了什么
  - 今天卡在哪里
  - 明天唯一主线

### `02_WeeklyNotes/`

- 结构：`年 / 起始月 / 周文件`
- 例子：`02_WeeklyNotes/2026/2026-03/2026-W14.md`
- 作用：
  - 本周唯一主线
  - 本周最低完成线
  - 本周任务清单
  - 本周复盘
  - 本周对整体目标的推进情况

### `07_MonthlyPlans/`

- 结构：`00_Roadmap/ + 年 / 月计划文件`
- 例子：
  - `00_Roadmap/03_Annual_Plan_2026.md`
  - `07_MonthlyPlans/2026/2026-03_月计划.md`
- 作用：
  - 长期 roadmap
  - 月主题
  - 月最低完成线
  - 月关键产出
  - 与周计划的映射关系

### `03_Projects/`

- 用于项目化 / 专题化学习对象
- 当前包括：
  - `micrograd/`
  - `makemore/`
  - `nanogpt-from-scratch/`
  - `robotics-foundations/`
  - `modern-robotics/`
- 作用：
  - 承接跨日、跨周持续推进的学习主题
  - 沉淀专题笔记、代码、实验和阶段总结
  - 把 `LLM / AI Infra` 与 `机器人系统 / 控制 / 仿真` 都放进同一个长期学习框架

### `04_Papers/`

- 用于长期经典论文库和每天 paper slot
- 按主题分类，每篇重要论文一个目录
- 作用：
  - 承接 `start-my-day` 的每日论文槽位
  - 沉淀一句 takeaway、系统启发和可进入项目的 idea
  - 区分轻量 Scan、结构化阅读和真正精读
  - 避免把论文阅读混进 Daily 里变成不可复用碎片
  - 通过 `99_Overrides/YYYY-MM-DD.md` 支持临时指定某天论文

### `08_Insights/`

- 用于收纳高价值学习总结、阶段性判断、路线修正和精加工材料
- 不与 Daily Note 混在一起
- 只保留值得长期复用和回看的内容

### `10_Workflows/`

- 工作流设计文档
- 命令规格
- 旧命令与脚本入口
- 作为当前过渡层保留，后续逐步迁入 OpenClaw 原生流程
- 不作为长期知识沉淀主目录；长期知识仍应进入 Daily / Weekly / Monthly / Projects / Insights

### `99_Templates/`

- Daily / Weekly / Project 模板
- 后续若学习节奏调整，优先先改模板，而不是每次临时改笔记结构

## 文件层级回答的问题

- Roadmap / Annual：`我要去哪`
- Monthly：`这个月重点是什么`
- Weekly：`这周怎么做`
- Daily：`今天做什么`
- Projects：`哪些专题值得持续推进`
- Papers：`哪些经典论文值得反复回看，它们给项目什么启发`
- Insights：`哪些认知值得长期保留`

## 当前状态

- 目录已收敛到学习主骨架
- 冗余 project / reference / archive-like 目录已删除或迁出
- roadmap 已收入口到 `00_Roadmap/`
- 高价值学习总结已开始收敛到 `08_Insights/`
- 当前正在从 `LLM-only` 学习仓库过渡为 `具身智能 + AI Infra` 长期成长系统

## 后续重点

- 强化机器人系统 / Modern Robotics / 控制 / ROS2 / 仿真的项目化入口
- 继续规范 `07_MonthlyPlans/` 的文件命名与使用方式
- 明确 `08_Insights/` 的准入规则
- 将 `10_Workflows/` 中可稳定复用的流程逐步迁入 OpenClaw 原生能力
- 调整 `99_Templates/`，使之更贴合当前学习节奏与目标
- 维护 `04_Papers/01_Reading_Index.md`，让 daily paper slot 有稳定来源

## 当前命令约定

当前工作区仍保留旧命令语义：

- 语义命令：`/start-my-day [time_budget]`
- 实际入口：`zsh 10_Workflows/bin/start-my-day`

注意：
- `/start-my-day` 目前仍是工作区内部语义，不是宿主原生命令
- 后续等 OpenClaw 原生流程接住后，再逐步迁移并清理旧入口
