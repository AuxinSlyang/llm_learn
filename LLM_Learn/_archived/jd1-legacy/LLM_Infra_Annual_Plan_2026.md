---
type: roadmap
title: 2026 LLM Inference / Serving 转岗倒排计划
role_target: Junior LLM Inference / Serving Engineer
time_budget: 10-15h/week
tags: [llm, inference, serving, kv-cache, vllm, sglang, annual-plan]
---

# 2026 LLM Inference / Serving 转岗倒排计划

> 起点假设：你有 `存储 / cache / HBM / 系统工程` 背景，但 `AI / GPU / LLM` 基础还不扎实。  
> 当前设备：本地 `Mac` 做笔记与轻量阅读，远端 `V100` 做最小实验。  
> 主线目标：在 `2026-09 ~ 2026-10` 具备投递并竞争 `LLM Inference / Serving` 初级工程师岗位的能力。  
> 保底窗口：如果工程证据沉淀速度不够，保底转岗窗口顺延到 `2027-02 ~ 2027-03`。

## 目标定义

今年的目标不是“学完所有 AI 知识”，而是拿到下面 4 种真实能力：

1. `概念能力`
   你能把 `token / logits / generate / prefill / decode / KV cache / TTFT / TPOT` 讲清楚。
2. `框架能力`
   你至少能跑通一个主流推理引擎（`vLLM` 或 `SGLang`），并能解释关键指标。
3. `工程能力`
   你能做一次像样的 benchmark / profiling / 实验记录，而不是只停留在跑通。
4. `迁移表达`
   你能把原有的 `HBM / 存储 / cache / 系统工程` 背景翻译成面向 `KV cache / 调度 / 资源管理 / 稳定性` 的工程叙事。

## 你适合的方向

你更适合从下面这条路径切入：

- `KV cache / 多级存储 / 数据路径 / memory hierarchy`
- 再进入 `推理指标 / benchmark / profiling`
- 再进入 `vLLM / SGLang / serving 代码路径`
- 再逐步进入 `调度 / 资源编排 / 稳定性`

这比一开始直接冲资源调度、容器编排、超大规模在线系统更稳。

## 你已有的资产

- `HBM / memory` 经验：有利于理解显存容量、带宽、memory-bound 问题。
- `存储 / cache` 经验：有利于理解 `KV cache` 的命中、回收、碎片、分层和迁移。
- `系统工程` 经验：有利于理解调度、隔离、稳定性、可观测性、故障恢复。

## 你需要补的断层

1. `最小 AI / ML / DL 基础`
   `embedding / logits / cross entropy / backward / optimizer.step / generate`
2. `最小 LLM 主流程`
   `token -> embedding -> attention -> logits -> generate`
3. `推理视角`
   `prefill / decode / KV cache / TTFT / TPOT / throughput / 显存`
4. `推理系统工程`
   `vLLM / SGLang / benchmark / profiling / 调度 / 资源管理`

## 关键时间窗口

### 主窗口：2026-09 ~ 2026-10

适合投递的前提是：

- 至少 1 个主流推理引擎跑通过
- 至少 1 份 benchmark 报告
- 至少 1 份 profiling / 性能分析记录
- 至少 1 个可讲清的小项目或专题
- 至少 1 套成体系的笔记与表达

### 保底窗口：2027-02 ~ 2027-03

如果到 2026-09 仍缺：

- 工程证据
- 框架实战
- 项目/PR/分析记录

那就把节奏转为“继续沉淀证据，到明年春招冲更稳的窗口”。

## 总体节奏

按现在的状态，更合理的半年路线不是“平均学所有东西”，而是这 5 个阶段：

1. `阶段 1：补最小基础`
2. `阶段 2：补最小 LLM`
3. `阶段 3：补推理视角`
4. `阶段 4：补框架与实验`
5. `阶段 5：补工程证据与求职表达`

下面按月份倒排。

---

## 2026-03：补齐最小 AI / DL / LLM 基础

### 月目标

- 完成 `makemore` 核心理解
- 完成最小 LLM 主流程理解
- 建立 `训练 vs 推理` 的最小边界

### 必须讲清的概念

- `embedding`
- `logits`
- `cross entropy`
- `backward`
- `optimizer.step`
- `generate`
- `token / attention / next-token prediction`

### 当月 Milestone

1. `Milestone A`
   完成 `makemore` 基础笔记，能用自己的话解释 5 个概念。
2. `Milestone B`
   完成一页 `训练 vs 推理` 笔记。
3. `Milestone C`
   完成一页 `最小 LLM 主流程` 笔记。

### 当月产出

- `makemore 基础笔记`
- `训练 vs 推理` 笔记
- `最小 LLM 主流程` 笔记

### 周计划模板

- `Week 1-2`：只做 `makemore`
- `Week 3`：只做最小 LLM 流程
- `Week 4`：只做回顾、串联、收口

### 过关标准

- 你能不看资料讲清 `embedding / logits / loss / generate`
- 你能画出 `token -> embedding -> attention -> logits -> generate`

---

## 2026-04：补齐推理视角和最小实验闭环

### 月目标

- 把模型基础接到 inference 语境
- 跑通最小本地推理闭环
- 留下第一批实验记录

### 必须讲清的概念

- `prefill`
- `decode`
- `KV cache`
- `TTFT`
- `TPOT`
- `throughput`
- `显存变化`

### 当月 Milestone

1. `Milestone D`
   完成 `KV cache / prefill / decode` 一页笔记。
2. `Milestone E`
   完成 `TTFT / TPOT / 显存 / 吞吐` 一页笔记。
3. `Milestone F`
   跑通最小 `transformers` 推理，并记录两类 prompt 的结果。

### 当月产出

- `KV cache` 笔记
- `metrics` 笔记
- `最小本地推理记录`
- `V100 环境说明文档`

### 周计划模板

- `Week 1`：`KV cache`
- `Week 2`：`metrics`
- `Week 3`：最小实验（两类 prompt）
- `Week 4`：文档收口与复盘

### 过关标准

- 你能解释为什么长上下文更贵
- 你能解释 `TTFT` 和 `TPOT` 分别对应哪段开销

---

## 2026-05：跑通第一个推理框架

### 月目标

- 选 `vLLM` 为主线先跑通
- 建立“服务化推理”和“naive 本地推理”的差异认识

### 当月 Milestone

1. `Milestone G`
   安装并跑通 `vLLM`。
2. `Milestone H`
   用一个小模型跑通 OpenAI 风格服务接口。
3. `Milestone I`
   写一页笔记：`vLLM 相对 naive 推理多了什么系统组件`

### 当月产出

- `vLLM 启动脚本`
- `首个服务调用记录`
- `vLLM 初印象笔记`

### 周计划模板

- `Week 1`：安装、环境兼容性确认
- `Week 2`：跑通服务、固定模型和 workload
- `Week 3`：熟悉 metrics 和接口
- `Week 4`：收口文档

### 过关标准

- 你能独立启动一个 `vLLM` 服务并打出结果
- 你知道它和本地 `transformers` 推理的关键差异

---

## 2026-06：做第一份 benchmark 报告

### 月目标

- 定义稳定 workload
- 固定指标
- 留下第一份能展示的 benchmark 报告

### 当月 Milestone

1. `Milestone J`
   定义 2 类 prompt、2 档长度、2-3 档并发。
2. `Milestone K`
   用统一脚本采集结果。
3. `Milestone L`
   写完 `Benchmark Report #1`

### 当月产出

- `benchmark 脚本 v1`
- `workload 定义文档`
- `Benchmark Report #1`

### 报告至少应包含

- 模型
- prompt 类型
- context length
- output length
- TTFT
- TPOT / token latency
- 吞吐
- 显存观察
- 你的解释

### 过关标准

- 你第一次具备“不是只会跑，而是会记录和解释”的证据

---

## 2026-07：开始 profiling 和源码路径理解

### 月目标

- 能对一次实验做基本 profiling
- 能读懂推理引擎最小代码路径

### 当月 Milestone

1. `Milestone M`
   完成一份最小 profiling 记录。
2. `Milestone N`
   写出 `vLLM` 最小代码路径导航。
3. `Milestone O`
   解释一个性能现象：更像算力瓶颈还是 memory / IO 瓶颈。

### 当月产出

- `Profiling Note #1`
- `vLLM 代码地图 v1`
- `性能现象解释` 笔记

### 过关标准

- 你能说“时间花在哪”
- 你能说“为什么这个现象会发生”

---

## 2026-08：形成一个小专题或小项目

### 月目标

- 围绕你的背景优势做一个专题
- 让它成为简历/面试可讲素材

### 推荐专题方向

1. `KV cache / 多级缓存 / 长上下文`
2. `TTFT / TPOT / 显存 / workload` 关系
3. `naive 推理 vs vLLM` 的系统差异
4. `memory-bound vs compute-bound` 的初步判断

### 当月 Milestone

1. `Milestone P`
   确定专题题目。
2. `Milestone Q`
   完成实验或分析主体。
3. `Milestone R`
   写出一份可讲解的专题报告。

### 当月产出

- `专题笔记 / 小项目`
- `图表 + 结论`
- `可讲 10 分钟的讲稿提纲`

### 过关标准

- 你能围绕一个问题连续讲 10 分钟，而不是只背名词

---

## 2026-09：求职准备月

### 月目标

- 让前 6 个月的学习转成求职材料
- 判断是否进入主窗口投递

### 当月 Milestone

1. `Milestone S`
   整理简历：把存储/HBM 经验翻译到 `KV cache / 推理系统` 语境。
2. `Milestone T`
   整理项目表达：至少 2 个能讲清的项目/专题。
3. `Milestone U`
   整理知识表达：至少 10 个常见面试问题的答案。

### 当月产出

- `转岗版简历`
- `项目讲稿`
- `面试问题清单`
- `岗位对照表`

### 判断是否进入 9-10 月主窗口

如果满足下面 4 条，可以开始主窗口投递：

- [ ] 有 1 份 benchmark 报告
- [ ] 有 1 份 profiling 或性能分析记录
- [ ] 有 1 个小专题或小项目
- [ ] 有 1 套成体系的笔记和表达

如果这 4 条不够完整，就转入保底窗口，继续沉淀到 `2027-02 ~ 2027-03`。

---

## 2026-10 ~ 2027-03（保底窗口规划）

如果 9-10 月未满足主窗口条件，后续重点不是换方向，而是补强证据：

1. `10-11 月`
   补一个 `SGLang` 对照组，形成第二套框架认知。
2. `11-12 月`
   做一次更完整的 profiling 或源码分析。
3. `12-01 月`
   尝试 1 次社区贡献：PR / issue analysis / 文档贡献。
4. `02-03 月`
   用更新后的证据冲春招窗口。

## 周计划生成规则

从现在开始，每周都按下面 4 个问题来生成：

1. `本周唯一主线是什么？`
2. `本周最低完成线是什么？`
3. `本周必须留下的可见产物是什么？`
4. `这个产物对 9-10 月求职有什么帮助？`

如果一个周计划回答不了第 4 个问题，说明它还不够面向转岗目标。

## 日计划生成规则

每天的任务不再按“材料列表”生成，而按下面结构生成：

1. `今天只推进一个主问题`
2. `今天只要求一个最小输出`
3. `今天必须能回写到周计划`

你当前适合的日计划节奏：

- 工作日：`45m 阅读 + 15m 整理 + 30-45m 动手`
- 周末：集中留给实验、文档、复盘

## 2026 年结束时至少应具备的证据

- [ ] `makemore / 最小 LLM / KV cache / metrics` 基础笔记完整
- [ ] `最小本地推理记录`
- [ ] `V100 环境说明文档`
- [ ] `vLLM` 或 `SGLang` 跑通记录
- [ ] `Benchmark Report #1`
- [ ] `Profiling Note #1`
- [ ] `1 个专题或小项目`
- [ ] `1 套可用于简历和面试的表达`

## 最后判断标准

到 `2026-09`，如果你能做到下面这些，就具备比较现实的初级岗位竞争力：

- 讲清最小推理主流程
- 讲清 `KV cache / TTFT / TPOT`
- 跑通过至少一个推理框架
- 有 benchmark / profiling / 文档证据
- 能把你的 `存储 / HBM / cache` 经验翻译成推理系统语境

这才是这份计划真正要服务的目标。
