---
type: paper_note
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
authors:
  - Timo Schick
  - Jane Dwivedi-Yu
  - Roberto Dessì
  - Roberta Raileanu
  - Maria Lomeli
  - Luke Zettlemoyer
  - Nicola Cancedda
  - Thomas Scialom
arxiv: "2302.04761"
source_url: "https://arxiv.org/abs/2302.04761"
pdf_url: "https://arxiv.org/pdf/2302.04761"
local_pdf: "/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/Toolformer.pdf"
published: "2023-02-09"
categories:
  - cs.CL
  - cs.AI
status: quick_read_done
read_mode: Quick Scan
phase: LLM support line -> tool use / agent / runtime
linked_project: "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
---

# Toolformer

## 一句话 Takeaway

- Toolformer 的核心是用少量人工 API 示例引导模型在普通语料里自举 tool-use 标注，再用 loss improvement 筛选真正有帮助的调用样本，最后 finetune LM，让模型学会“什么时候调工具、怎么传参、如何把结果接回后续 token prediction”。

## 为什么现在读

- 昨天已经把 `ReAct` 放回 `Thought -> Action -> Observation` 的 runtime 协议里；今天补 `Toolformer`，是为了回答“模型本身如何学会何时调用工具、传什么参数、以及如何把工具结果接回后续 token prediction”。

## Metadata

- Title: Toolformer: Language Models Can Teach Themselves to Use Tools
- Authors: Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- Venue / Date: arXiv / 2023-02-09
- Source URL: https://arxiv.org/abs/2302.04761
- PDF URL: https://arxiv.org/pdf/2302.04761
- Local PDF: /Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/Toolformer.pdf
- Code / Project:
- Reading mode: Quick Scan

## Abstract + Introduction 理解

- 问题：普通 LM 可以在文本里学到很多知识，但算术、事实检索、翻译、日历/时间等能力不稳定；外部工具能补强这些能力，但模型默认不知道何时调用、如何调用、如何利用返回结果。
- 旧方法为什么不够：纯 prompt / few-shot tool use 依赖人工写示例，难以规模化；专门为工具调用收集监督数据成本高；ReAct 更像 inference-time reasoning/action 协议，不直接解决模型如何从大规模语料中学习 tool-use 行为。
- 核心 insight：如果一次工具调用能降低 LM 对后续 token 的预测 loss，说明这个调用对建模有用；可以用这个信号从自生成 API 调用中筛出训练数据。
- 贡献：提出一套自监督 tool-use 数据构造流程；覆盖 calculator、QA、search、translation、calendar 等工具；把筛选后的调用样本混入 LM finetune，使模型保留语言能力的同时获得工具调用能力。
- 后续要验证的 claim：loss improvement 是否足够代表“工具调用真的有用”；工具 API 质量、调用格式和返回结果噪声会怎样影响最终行为；这种方法在现代 function calling / agent runtime 里是否仍值得复现。

## 章节地图

| Section | 作用 | 首轮是否精读 |
|---|---|---|
| Abstract / Intro | 问题定义、工具调用动机、自监督构造数据 | 是 |
| Method | API 插入、筛选、训练目标 | 是 |
| Experiments | 算术、问答、检索、翻译、日历等任务收益 | 选读 |

## 8 问

- 任务是什么？让 LM 在生成文本时学会按需插入 API call，并把 API result 纳入后续 token prediction。
- observation 是什么？普通文本上下文，加上候选 API 调用位置、API 参数和工具返回结果。
- action 是什么？高层语言 action：选择是否调用工具、调用哪个工具、传入什么参数，以及在文本中如何接续使用返回结果。
- 数据怎么采？先用少量人工示例 prompt 让模型在语料中采样 API calls，再执行工具得到结果，用带/不带工具结果的 token prediction loss 差异筛选样本。
- policy / model 输出什么？最终模型输出普通文本和特殊 API 调用片段；不是低层 robot action，而是 tool-use 行为。
- eval 怎么做？在问答、算术、翻译、时间/日历等任务上比较 vanilla LM、tool-augmented baselines 和 Toolformer。
- failure mode 是什么？错误调用、参数不合法、工具结果无用但被模型采用、调用过多、工具覆盖范围有限、runtime 没有 timeout / retry / logging 时难以产品化。
- 如果我要产品化，需要什么 software / data / runtime 支撑？tool schema、parser、executor、sandbox、timeout、权限控制、结果注入格式、调用日志、失败恢复和离线评估集。

## 方法结构

- 方法主链路：

```text
少量人工 API 示例
-> prompt LM 在普通语料中采样候选 API calls
-> 执行 API，拿到返回结果
-> 比较带工具结果 vs 不带工具结果的后续 token loss
-> 只保留能显著降低 loss 的调用样本
-> 用筛选后的 tool-use 数据 finetune LM
-> 推理时模型自己决定何时插入 API call
```

- 关键点不是工具本身，而是筛选标准：如果工具结果能提升后续文本预测，它才被当成有监督信号。
- 和 ReAct 的区别：ReAct 主要是 `Thought -> Action -> Observation` 的交互式 runtime 格式；Toolformer 主要是构造 tool-use finetuning 数据，让模型内化工具调用行为。
- 和 RAG 的区别：RAG 专注 retrieval memory；Toolformer 把 search、calculator、translator、calendar 等都视为可调用工具。

## 实验与证据

- Baselines: 原始 LM、不同工具使用 baselines、无工具版本等。
- Metrics: 各任务准确率 / generation quality；首轮不深读表格。
- Main results: 论文声称 Toolformer 在多个外部工具相关任务上提升明显，同时尽量保留原始语言建模能力。
- Ablations: 首轮未细读。
- Failure / limitations: API 调用格式依赖 prompt 和工具设计；工具结果错误会污染生成；方法主要处理文本/API 层工具，不解决 agent 长时规划、权限、安全和 runtime 可靠性。

## 系统 / 工程启发

- 如果把工具调用看成高层 action，Toolformer 关心的是 `什么时候 call tool`，而不是低层控制；这正好适合作为未来 VLA / robot high-level planner 的语言智能支撑线。

## 和 Robot Learning / Runtime 的连接

- 对当前路线的价值不是复现论文，而是先建立一个清晰分层：`LLM/tool-use` 负责任务分解、外部知识与 API 使用，`policy/runtime` 负责高频动作执行、timeout、fallback、logging 和 replay。

## 可以转成的实验 Idea

- 把 `Toolformer / ReAct / RAG` 三篇整理成一张 `tool use / retrieval / runtime` 对照表，只回答它们分别解决什么、在系统里处于哪一层。

## 疑问

- 现代 function calling 已经有显式 tool schema 和 runtime，Toolformer 的自监督数据筛选思想是否仍可用于构造 tool-use SFT 数据？
- 对机器人系统，哪些能力应该让 LLM tool-use 层处理，哪些必须下沉到 deterministic runtime / policy controller？
- loss improvement 能否筛出“看起来有帮助但语义上错误”的工具调用？

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-06-04 | Quick Scan | Abstract / Intro / Method 主线 | 首轮理解完成；和 `ReAct / RAG` 对齐为 tool use / retrieval / runtime 支撑线 |
