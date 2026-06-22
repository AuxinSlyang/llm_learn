# llm-learner

`llm-learner` 是一个长期学习知识库与执行系统，当前服务于具身智能、机器人系统、语言智能和 AI Infra 的持续学习。

目录名和部分历史文件仍保留 `LLM` 语义，但项目主线已经升级为：

```text
Robot Learning Full-Stack
-> robot system / perception / policy / data loop
-> VLA / multimodal / language intelligence
-> inference / serving / runtime / AI Infra
```

## 项目定位

短期目标：成长为具身智能系统构建者，并以具身智能软件、Robot Learning Infra、Policy Runtime、机器人全栈工程作为现实第一跳。

长期目标：成长为机器人全栈工程师 / roboticist，能够打通机器人本体、感知决策、运动控制、多机器人协作、语言智能与 AI Infra。

这个仓库不是单一代码项目，而是一个带有执行节奏的学习系统。它负责沉淀路线规划、论文阅读、项目实验、日计划、周复盘、月计划和工作流。

## 当前主线

当前学习主线是 `Robot Learning Full-Stack`：

- SO-ARM101 / LeRobot 首闭环
- robot learning data loop：teleop、record、replay、dataset、eval、failure log
- CV foundation：ResNet、ViT、CLIP/VLM/VLA visual encoder
- VLA / foundation policy：ACT、Diffusion Policy、OpenVLA、SmolVLA、pi0
- LLM / multimodal：作为机器人语言理解、高层任务分解和协作智能的子能力
- AI Infra / runtime：作为 VLA / policy runtime / edge inference 的工程底座

## 目录结构

```text
.
├── AGENTS.md                 # 当前 workspace 的角色、边界和协作规则
├── MEMORY.md                 # 长期记忆和事实来源原则
├── WORKSPACE_MAP.md          # workspace 结构索引
├── skills/                   # 当前实际启用的本地工作流 skill
├── memory/                   # 日常持久记忆
└── LLM_Learn/                # 长期学习知识库主体
```

`LLM_Learn/` 是主要知识资产：

```text
LLM_Learn/
├── 00_Roadmap/               # 年度路线、阶段目标、能力地图
├── 01_DailyNotes/            # 日计划和当天执行记录
├── 02_WeeklyNotes/           # 周计划和周复盘
├── 03_Projects/              # 项目化学习与实验记录
├── 04_Papers/                # 论文阅读队列和 structured notes
├── 07_MonthlyPlans/          # 月计划
├── 08_Insights/              # 高价值总结和阶段性 insight
├── 10_Workflows/             # 工作流说明和命令规范
└── 99_Templates/             # Daily / Weekly / Paper / Project 模板
```

## 使用方式

日常节奏遵循：

```text
年度计划 -> 月计划 -> 周计划 -> Daily Note -> 阅读 / 实验 / 复盘
```

常用入口：

- 今天做什么：先看 `LLM_Learn/01_DailyNotes/`
- 本周目标：先看 `LLM_Learn/02_WeeklyNotes/`
- 本月目标：先看 `LLM_Learn/07_MonthlyPlans/`
- 当前阶段方向：先看 `LLM_Learn/00_Roadmap/`
- 论文阅读：先看 `LLM_Learn/04_Papers/01_Reading_Index.md`
- 项目实验：先看 `LLM_Learn/03_Projects/`

常用工作流：

- `skills/start-my-day/`：生成当天学习计划并回写 Daily Note
- `skills/end-of-this-week/`：周复盘和下周衔接
- `skills/llm-reading-queue/`：阅读队列整理
- `skills/llm-experiment-logbook/`：实验记录
- `skills/llm-learn-devbox/`：远端学习实验环境相关记录

## 知识库维护原则

- 优先复用既有 Daily / Weekly / Monthly / Roadmap / Templates 体系。
- 不在没有 review 的情况下重建平行目录。
- 长期价值内容要沉淀为结构化笔记，而不是散落在聊天记录里。
- 临时日志、重复内容和历史噪音先标记和归类，后续单独清理。
- 学习与实验事实优先来自本地笔记和实际环境，不依赖模糊记忆。

## 当前边界

适合这个仓库处理：

- 具身智能、机器人系统、VLA、robot learning、CV foundation、LLM / multimodal、AI Infra 学习
- 论文 / 博客 / 开源项目阅读与总结
- SO-ARM101 / LeRobot / policy runtime 相关实验记录
- Daily / Weekly / Monthly 计划和复盘
- 知识库结构维护和工作流整理

不适合这个仓库处理：

- TokaDB 主业务
- 平台治理任务
- 股票项目维护
- 与当前机器人 / 语言智能 / AI Infra 主线无关的主题扩张

## 当前阶段的判断标准

新增学习内容时，优先回答三个问题：

1. 它是否服务 `Robot Learning Full-Stack` 主线？
2. 它能否沉淀到现有 Daily / Weekly / Paper / Project 结构？
3. 它是否能连接到机器人系统里的 observation、action、policy、eval、runtime 或 data loop？

如果答案不清楚，先放入候选队列，不打断当前阶段主线。
