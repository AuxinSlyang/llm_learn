# Paper Reading Workflow

## 目标

论文阅读要服务三个目标：

1. 建立 AI / Robotics 的长期判断力。
2. 给 `Embodied AI mini-stack` 提供可迁移的系统设计 idea。
3. 服务 [[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]：课程阶段、仿真实验、runtime/data loop、JD mapping。

不追求每天完整精读一篇。默认先做 structured pass，先抓论文位置、问题、方法结构和证据，再决定是否精读。

## 新 Session 启动入口

新开论文阅读 session 时，优先读：

1. [[00_Paper_Session_Context]]：当前论文主线、已读关键论文、下一篇论文。
2. [[01_Reading_Index]]：队列状态和当前 paper slot。
3. 当前 sprint / paper note，例如 [[CV_Foundation_Sprint_2026-W24]] 或具体论文的 `QUICK_READ.md`。

这样新 session 不需要依赖聊天历史，也能接上当前主线。

## 标准 6-Pass 流程

| Pass | 目标 | 输出 |
|---|---|---|
| 0 Metadata / Position | 确认标题、作者、venue、arXiv/DOI/PDF/code；判断为什么现在读 | 元信息 + 阅读模式 |
| 1 Abstract + Introduction | 读懂问题、动机、核心 insight、贡献 | 段落级解释 + 本文要证明什么 |
| 2 Structure Map | 看章节和图表，建立全局地图 | section map + figures/tables 清单 |
| 3 Method | 拆模型、算法、系统或机器人任务 | task/obs/action/model/loss/reward/train/inference |
| 4 Experiments | 看证据是否支撑 claim | baseline/metric/main result/ablation/failure |
| 5 Synthesis | 连接当前路线和项目 | takeaway + robot learning/runtime 连接 |

不要在 Pass 1 前直接写最终总结。用户说“不懂”时，优先解释当前概念，而不是继续推进。

## 每日 Paper Slot

默认节奏：

| 时间 | 内容 | 产出 |
|---|---|---|
| 白天碎片 20-40m | 读 1 篇论文的 abstract / intro / method overview / figures / conclusion | 一句话 takeaway + 1 个项目连接 |
| 晚上 1.5h | 当前周主线学习 / 实验 / 笔记 | Weekly / Monthly 硬产出 |
| 周五 20-30m | 汇总本周 3-4 篇 paper slot | 本周 paper takeaways |
| 周末可选 | 精读当前 Phase 关键论文 | 结构化 paper note |

## 阅读深度分级

| Level | 适用场景 | 标准 |
|---|---|---|
| Scan | 非当前主线，但值得知道 | 能讲清论文解决什么问题和一个 takeaway |
| Structured Read | 当前阶段相关 | 完成 8 问模板，能连接到 mini-stack |
| Deep Read | 当前 Phase 核心论文 | 读方法细节、实验设置、失败模式，必要时看代码 |
| Reproduce | 项目强相关 | 复现最小代码或把 idea 放入 mini-stack |

## 不同类型论文的抓手

### AI / Robot Learning

- 任务是什么
- observation 是什么
- action 是什么
- 数据怎么采
- policy / model 输出什么
- loss / reward / objective 是什么
- eval 怎么做
- failure mode 是什么
- 如果产品化，需要什么 software / data / runtime 支撑

### Systems / USENIX / OSDI / SOSP

- workload 和假设是什么
- 系统架构是什么
- 核心 abstraction / data structure / protocol 是什么
- scheduler / resource management / fault handling 怎么做
- evaluation workload、metric、baseline 是否有说服力
- 可以迁移到 robot runtime / policy serving 的点是什么

### VLA / Foundation Policy

- language / vision / action 分别如何表示
- 训练数据来自哪里
- action head 或 policy 输出是什么
- 推理路径和延迟瓶颈是什么
- 是否需要 high-level planner + low-level controller 分层
- 数据闭环和失败回放如何设计

## 文件命名约定

- `QUICK_READ.md`：通读笔记，记录核心问题、主线结构、takeaway、历史位置和后续连接。
- `DEEP_READ.md`：精读笔记，记录逐节细节、公式 / 算法推导、训练与推理过程、实验设置、疑问和代码映射。
- `README.md`：只用于目录或资源介绍；不要把逐步学习笔记默认写成 `README.md`。
- 对于刚进入视野的论文，先维护 `QUICK_READ.md`；只有进入当前主线精读时，再新增 `DEEP_READ.md`。

## 每篇论文只先回答 8 个问题

- 任务是什么？
- observation 是什么？
- action 是什么？
- 数据怎么采？
- policy / model 输出什么？
- eval 怎么做？
- failure mode 是什么？
- 如果我要产品化，需要什么 software / data / runtime 支撑？

## Abstract / Introduction 导读模板

```text
1. 这篇论文开头认为领域里现在卡在哪里？
2. 它认为旧方法为什么不够？
3. 它提出的核心 insight 是什么？
4. 它声称贡献了哪几件事？
5. 后续 method/experiment 需要验证哪些 claim？
6. 对当前 Robot Learning Full-Stack 路线有什么用？
```

## Daily Note 回写格式

`start-my-day` 生成计划时，应在 Daily Note 写入：

```text
## 今日论文槽位

- 候选论文：
- 阅读模式：Scan / Structured Read / Deep Read
- 今日目标：一句 takeaway + 一个和 mini-stack 的连接
- 输出位置：
```

完成后，在 `今日总结` 或论文目录的 `QUICK_READ.md` / `DEEP_READ.md` 里补：

```text
- 今日论文 takeaway：
- 和 mini-stack 的连接：
- 后续 idea：
```

## 指定明天论文

如果当天晚上突然想指定某篇论文，写入：

```text
04_Papers/99_Overrides/YYYY-MM-DD.md
```

第二天 `start-my-day` 会优先使用 override，不再从默认队列取第一篇。

推荐对话方式：

```text
明天论文指定：arXiv:xxxx.xxxxx，帮我从 arXiv 抓一下，明天 paper slot 读它。
```

如果只给标题，也可以先创建 override；能确认 arXiv 身份时再补 `arxiv` 和 `source_url`。

## 不做什么

- 不把 paper slot 变成当天主任务，除非它就是本周主线。
- 不默认下载和管理 PDF。
- 不为了覆盖数量牺牲理解质量。
- 不读完就结束，必须留下 takeaway 或项目连接。
