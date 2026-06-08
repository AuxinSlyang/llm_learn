---
type: paper_note
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
authors:
  - Patrick Lewis
  - Ethan Perez
  - Aleksandara Piktus
  - Fabio Petroni
  - Vladimir Karpukhin
  - Naman Goyal
  - Heinrich Kuttler
  - Mike Lewis
  - Wen-tau Yih
  - Tim Rocktaschel
  - Sebastian Riedel
  - Douwe Kiela
arxiv: "2005.11401"
source_url: "https://arxiv.org/abs/2005.11401"
pdf_url: "https://arxiv.org/pdf/2005.11401"
local_pdf: "/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Retrieval_Augmented_Generation_for_Knowledge_Intensive_NLP_Tasks/RAG.pdf"
published: "2020-05-22"
categories:
  - cs.CL
  - cs.LG
status: quick_read_done
read_mode: Quick Scan
phase: LLM support line -> retrieval / external memory
linked_project: "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
---

# Retrieval-Augmented Generation

## 一句话 Takeaway

- RAG 的核心不是“把搜索结果塞进 prompt”这么简单，而是把外部可检索记忆接进生成模型：原论文用 `DPR retriever + Wikipedia dense index + BART generator`，通过最终答案 likelihood 联合训练 query encoder 和 generator。

## 为什么现在读

- 这篇用来回答：当参数记忆不够时，生成模型怎么接外部检索，把 `knowledge retrieval -> generation` 变成一条可训练链路。

## Metadata

- Title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- Authors: Patrick Lewis et al.
- Venue / Date: arXiv / 2020-05-22
- Source URL: https://arxiv.org/abs/2005.11401
- PDF URL: https://arxiv.org/pdf/2005.11401
- Local PDF: /Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Retrieval_Augmented_Generation_for_Knowledge_Intensive_NLP_Tasks/RAG.pdf
- Code / Project:
- Reading mode: Quick Scan

## Abstract + Introduction 理解

- 问题：预训练 LM 的参数里确实存了大量事实知识，但这些知识不容易精确访问、更新和溯源；在 knowledge-intensive tasks 上，纯参数模型容易 hallucinate，也不如检索式系统可靠。
- 旧方法为什么不够：纯 seq2seq / parametric-only model 只能依赖参数记忆；已有 retrieval-augmented work 更多集中在 extractive QA，还没有把检索式 non-parametric memory 系统地接到通用 seq2seq generation。
- 核心 insight：把两类记忆结合起来：`parametric memory = BART 参数里的语言/知识能力`，`non-parametric memory = Wikipedia dense vector index`。先检索外部文档，再基于问题和文档生成答案。
- 贡献：提出通用 RAG fine-tuning recipe；比较 `RAG-Sequence` 和 `RAG-Token` 两种把 retrieved documents 纳入生成概率的方式；在 open-domain QA、fact verification 和 generation 任务上验证检索增强的收益。
- 后续要验证的 claim：RAG 是否真的让答案更 factual / specific / diverse；联合训练是否比单纯 fixed retriever + generator 更有效；这种原始联合训练范式在现代工程里是否仍是主流。

## 章节地图

| Section | 作用 | 首轮是否精读 |
|---|---|---|
| Abstract / Intro | 为什么参数记忆不够，为什么要检索 | 是 |
| Method | retriever + generator 如何结合 | 是 |
| Experiments | open-domain QA / factual generation 结果 | 选读 |

## 8 问

- 任务是什么？在知识密集 NLP 任务中，给定 query / input，生成答案、声明判断或自然语言输出。
- observation 是什么？输入 `x` 加上 retriever 找到的 top-k passages `z1...zk`。
- action 是什么？不是 RL action；模型行为是检索文档并生成 token 序列。
- 数据怎么采？训练数据是普通 `(query, answer)` pair，没有 gold document supervision；外部知识库是 Wikipedia passages 的 dense index。
- policy / model 输出什么？Retriever 输出 `p(z | x)` 和 top-k documents；generator 输出 `p(y | x, z)` 或 token probabilities。
- eval 怎么做？open-domain QA、abstractive QA、Jeopardy question generation、FEVER 等任务；首轮不深读具体表格。
- failure mode 是什么？检索错误、错误文档污染生成、知识库缺失、联合训练成本高、现代工程中常被简化成 pipeline RAG。
- 如果我要产品化，需要什么 software / data / runtime 支撑？文档 ingestion、chunking、index、retriever、reranker/filters、source attribution、permission control、generation prompt/context packing、retrieval eval。

## 方法结构

### 组件

```text
query x
-> DPR query encoder
-> query embedding
-> dense vector index / MIPS
-> top-k passages z1...zk
-> BART generator reads x + zi
-> answer y
```

- `Retriever = DPR`：负责把 query 编成向量，并在 Wikipedia dense index 里找 top-k passages。
- `Generator = BART-large`：完整的 seq2seq 生成模型，读取 `query + retrieved passage` 后逐 token 生成答案。
- `Vector DB / document index`：非参数记忆。原论文中 document encoder 和 index 基本固定，主要训练 query encoder 和 generator。

### RAG-Sequence

`RAG-Sequence` 假设整段答案由同一个 retrieved document 支撑：

```text
p(y | x) = sum_z p(z | x) * p(y | x, z)
```

直觉：每篇候选文档都尝试解释完整答案，最后按 retriever 权重把贡献加起来。

### RAG-Token

`RAG-Token` 假设每个 output token 都可以从不同 document 获得支持：

```text
p(y | x) = product_i sum_z p(z | x) * p(y_i | x, z, y_<i)
```

直觉：生成每个 token 时，都重新混合 top-k 文档的贡献；粒度更细，更适合多文档、多事实融合，但解码更复杂。

### 训练

训练数据只有 `(x, y)`，没有 gold document。

```text
x
-> retrieve top-k z
-> BART computes p(gold y | x, zi)
-> combine with p(zi | x)
-> p(y | x) = sum_i p(zi | x) * p(y | x, zi)
-> loss = -log p(y | x)
-> update query encoder + BART generator
```

这里 `p(y | x, zi)` 是 BART 对 gold answer 序列的 autoregressive likelihood：

```text
p(y | x, zi) = product_t p(y_t | x, zi, y_<t)
```

训练会同时推动：

- query encoder 更容易召回能帮助生成正确答案的文档；
- BART 更会利用检索文档生成正确答案。

### 推理

推理时没有 gold answer，不算 loss，不更新参数。

```text
question x
-> query encoder
-> vector index top-k
-> retrieved passages
-> BART decode
-> final answer
```

- `RAG-Sequence`：对每个 document 生成完整答案候选，再用 `p(z | x) * p(answer | x, z)` 给候选答案重打分。
- `RAG-Token`：每生成一个 token，都综合 top-k documents 下该 token 的概率。

## 实验与证据

- Baselines: parametric-only seq2seq model、retrieve-and-extract architectures、task-specific systems。
- Metrics: open-domain QA accuracy / EM、generation 任务指标、人评 factuality / specificity / diversity 等。
- Main results: 论文声称 RAG 在多个 open-domain QA 任务上达到 SOTA，在 generation 任务上比 parametric-only BART 更 factual、specific、diverse。
- Ablations: 首轮未细读。
- Failure / limitations: 首轮重点不在实验表格；现代工程里原始 joint training 并不是默认做法，更多是 retrieval pipeline + prompt/context injection。

## 系统 / 工程启发

- 如果把参数看成“内置记忆”，RAG 解决的是“外部知识库怎么在推理时动态接进来”，这对未来 tool use、agent memory、robot knowledge grounding 都有参考价值。
- 现代工程要区分两层：
  - RAG 思想很通用：外部 memory grounding。
  - 原始 RAG 的 retriever-generator joint training 不一定是默认生产做法。
- 现在更常见的生产形态是 `fixed retriever / hybrid search / reranker / prompt injection / strong LLM`，而不是每个私域库都做原论文式联合训练。
- Search API 也可以看成 retrieval tool；RAG 更适合受控 corpus，例如私域知识库、代码库、文档、日志、runbook、robot memory。

## 和 Robot Learning / Runtime 的连接

- 它不是低层控制论文，但对机器人系统里的 `external memory / retrieval / task knowledge grounding` 有直接启发。
- 对未来机器人系统，可以把以下对象看成可检索外部 memory：
  - task memory
  - environment map
  - skill library
  - failure logs
  - policy eval history
  - runbook
  - fleet telemetry
- 核心不是 embedding 本身，而是：模型参数之外的动态知识如何被可靠检索、约束、引用，并接入生成或决策过程。

## 可以转成的实验 Idea

- 把 `RAG / Toolformer / ReAct` 整理成一张表：分别解决 `检索 / 调工具 / reasoning-acting loop` 哪一层问题。

## 疑问

- 现代 agent 是否应该固定走 RAG，还是把 search / DB / code search / log search 都作为工具按需调用？
- 对公开互联网知识，Google/Bing/search tool 可能比自建 RAG 更合理；对私域知识，controlled RAG 更有价值。
- 原始 RAG 的 joint training 在当前通用 LLM API 时代是否还值得复现？还是只需要理解其概率建模思想？
- 对机器人系统，retrieval memory 应该服务 high-level planner、failure analysis，还是也能进入 policy runtime？

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-06-04 | Quick Scan | Abstract / Introduction / Methods 主线 | 首轮 quick read 完成；后续不继续展开实验，主线切回 tokenizer |
