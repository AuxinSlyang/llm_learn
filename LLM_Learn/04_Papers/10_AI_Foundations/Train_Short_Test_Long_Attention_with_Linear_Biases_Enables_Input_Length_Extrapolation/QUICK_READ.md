---
type: paper_note
title: "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation"
authors:
  - Ofir Press
  - Noah A. Smith
  - Mike Lewis
arxiv: "2108.12409"
source_url: "https://arxiv.org/abs/2108.12409"
pdf_url: "https://arxiv.org/pdf/2108.12409"
local_pdf: "/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Train_Short_Test_Long_Attention_with_Linear_Biases_Enables_Input_Length_Extrapolation/ALiBi.pdf"
published: "2021-08-27"
categories:
  - cs.LG
  - cs.CL
status: quick_read_done
read_mode: Quick Scan
phase: LLM support line -> position bias / context extrapolation
linked_project: "[[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]"
---

# ALiBi

## 一句话 Takeaway

- `ALiBi` 不给 token 加 positional embedding，而是在 attention score 里加一个随 query-key 距离线性变负的 bias；它用“越远惩罚越大”的 recency inductive bias 支持 `train short, test long` 的长度外推。

## 为什么现在读

- 这篇是 `RoPE` 的对照组：它回答的是不用显式位置 embedding，而是在 attention score 里直接加线性 bias，能不能做到 `train short, test long`。

## Metadata

- Title: Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation
- Authors: Ofir Press, Noah A. Smith, Mike Lewis
- Venue / Date: arXiv / submitted 2021-08-27, latest version 2022-04-22
- Source URL: https://arxiv.org/abs/2108.12409
- PDF URL: https://arxiv.org/pdf/2108.12409
- Local PDF: /Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Train_Short_Test_Long_Attention_with_Linear_Biases_Enables_Input_Length_Extrapolation/ALiBi.pdf
- Categories: cs.CL
- Code / Project: https://github.com/ofirpress/attention_with_linear_biases
- Reading mode: Quick Scan

## Abstract + Introduction 理解

- 问题：Transformer 训练时通常固定一个 context length `L`，但推理时往往希望处理更长上下文；训练长上下文很贵，训练短上下文又容易在长上下文推理时外推失败。
- 旧方法为什么不够：
  - learned positional embedding 只能覆盖训练长度内的位置。
  - sinusoidal position embedding 有定义但外推能力弱。
  - 一些相对位置方法能改善外推，但可能更慢、额外耗内存或引入参数。
- 核心 insight：不要把位置 embedding 加到 word embedding；直接在 `q_i K^T` 的 attention score 上加一个非学习的线性距离惩罚。
- 贡献：
  - 提出 Attention with Linear Biases（ALiBi）。
  - 不使用 positional embedding。
  - 每个 head 使用固定 slope，距离越远 attention score 被惩罚越大。
  - 训练短序列，推理长序列时保持较好 perplexity，同时训练更快、省内存。
- 后续要验证的 claim：`train short, test long` 是否真的成立，以及线性 bias 是否比 RoPE/T5 bias/sinusoidal 更高效。

## 章节地图

| Section | 作用 | 首轮是否精读 |
|---|---|---|
| Abstract / Intro | 长度外推问题定义 | 是 |
| Method | attention linear bias 怎么加 | 是 |
| Results | WikiText-103 / Books / 1.3B 设置上的外推结果 | 选读 |
| Analysis | early token curse 解释 | 是 |
| Conclusion | 简单、无参数、低成本的位置方法 | 快速扫 |

## 论文写作骨架

```text
1. Abstract / Introduction:
   长 context 训练贵，但推理长 context 有用。
   问题定义为 train short, test long。

2. Method:
   不加 positional embedding。
   在 q_i K^T 后加 head-specific linear bias。

3. Results:
   在 WikiText-103、BookCorpus、1.3B/461GB 数据设置上验证外推。
   对比 sinusoidal、RoPE、T5 bias 等位置方法。

4. Analysis:
   分析为什么更长 eval length 会降低 perplexity。
   关键概念是 early token curse。

5. Conclusion:
   ALiBi 是简单、无额外参数、几行代码可实现的位置方法。
```

## 8 问

- 任务是什么？改善 Transformer LM 的位置表示，使短上下文训练的模型能外推到更长上下文推理。
- observation 是什么？token sequence，进入模型后是 token embeddings、q/k/v hidden states。
- action 是什么？不适用；类比输出是 next-token logits。
- 数据怎么采？使用语言建模数据集，如 WikiText-103 等。
- policy / model 输出什么？语言模型输出 next-token distribution；ALiBi 只改变 attention score。
- eval 怎么做？perplexity、训练速度、显存、不同 test context length 下的外推性能。
- failure mode 是什么？训练长度太短时，外推超过一定倍数后性能仍会下降；recency bias 可能不适合所有需要均匀远程访问的任务。
- 如果我要产品化，需要什么 software / data / runtime 支撑？attention mask/bias 实现、不同 head slope 生成、KV cache 下 position distance 的正确处理、长上下文 eval。

## 方法结构

### 1. 标准 attention score

对第 `i` 个 query：

```text
softmax(q_i K^T)
```

causal LM 中，`q_i` 只能 attend 到前面 `1..i` 的 keys。

### 2. ALiBi 的修改

ALiBi 不加 positional embedding：

```text
x_i = token_embedding_i
```

它只在 attention score 上加 bias：

```text
softmax(q_i K^T + m * [-(i-1), ..., -2, -1, 0])
```

这里：

```text
i: 当前 query 位置
key 距离 query 越远，bias 越负
m: 当前 head 的 slope
```

如果 key 就在当前位置，距离是 0，bias 是 0；如果 key 很远，bias 是负数，attention score 被压低。

### 3. 多头不同 slope

每个 attention head 使用不同斜率：

```text
head 1: 惩罚远距离更强
head 2: 惩罚远距离较弱
...
```

直觉：

```text
大 slope: 更关注近处
小 slope: 可以保留更远距离
```

这和 RoPE 的多频率有相似的多尺度味道，但 ALiBi 是加在 score 上的线性 bias，不是旋转 q/k。

### 4. 和 RoPE 的对比

```text
RoPE:
q/k 旋转
score = (R_m q_m)^T (R_n k_n)

ALiBi:
q/k 不旋转
score = q_m^T k_n - slope_head * distance(m,n)
```

RoPE 是 geometric transformation；ALiBi 是 explicit attention bias。

## 实验与证据

- Baselines: sinusoidal PE、T5 bias、RoPE 等位置方法。
- Metrics: perplexity、training speed、memory usage、不同上下文长度下的 extrapolation。
- Main results:
  - 1.3B LM 在 `L=1024` 训练，用 ALiBi 外推到 `2048`，达到和 sinusoidal `L=2048` 训练相近 perplexity。
  - 作者报告该设置训练更快、内存更省。
  - 在 WikiText-103 上，ALiBi 的 recency bias 对比多种位置方法表现强。
- Ablations: slope 设置、不同 context length、不同数据集和模型大小。
- Failure / limitations:
  - performance peak 约在训练长度的两倍附近，继续拉长仍会下降。
  - ALiBi 是强 recency prior，对需要远距离精确检索的任务未必总是最优。
  - Analysis 部分显示：ALiBi 外推带来的 perplexity 改善，很大一部分可能来自减少 `early token curse`，不一定说明模型真正高效利用了超过训练长度的长程依赖。

## Analysis: early token curse

论文后半部分有一个关键校准：作者不只报外推结果，还分析为什么外推时 perplexity 会变好。

问题来自 non-overlapping evaluation：

```text
长文本被切成多个窗口
每个窗口开头的 token 几乎没有前文
这些 early tokens 更难预测
perplexity 被拉高
```

这就是 `early token curse`。

如果模型能用更长 evaluation window：

```text
每个窗口开头 token 的比例下降
更多 token 能看到足够上下文
整体 perplexity 下降
```

作者用 stride=1 的 sliding window evaluation 做分析。这个设置让每个预测都尽量看到最大上下文。结果显示：ALiBi 在这个设置下，随着 evaluation length 变长，perplexity 大体保持平，而不是继续显著改善。

这说明：

```text
ALiBi 的外推收益
部分来自它允许更长 evaluation window
从而减少 early token curse
不一定代表模型充分利用了超过训练长度的远程依赖
```

这个分析很重要：它降低了 ALiBi 的神秘感，也提醒我们不要把 `train short, test long` 直接等同于“学会超长程推理”。

## 系统 / 工程启发

- ALiBi 把“位置信息”改成 attention score 上的 inductive bias，这对理解长上下文外推为什么可能成立很有帮助。
- 它非常工程化：少参数、少改代码、不需要位置 embedding table，也避免了 learned PE 的扩表问题。
- 它的工程价值来自降低训练 context length 需求：如果能用短窗口训练、长窗口推理达到相近 perplexity，就能省训练时间和显存。
- 但它不解决 attention 的 `O(N^2)` 计算，也不自动解决长程精确检索。

## 和 Robot Learning / Runtime 的连接

- 对当前路线的意义主要是支撑 runtime/context 线：理解长度外推、context cost 和位置编码替代方案。
- 更一般的启发：很多系统优化不是让模型“无限强”，而是把成本结构重新分配。ALiBi 把长 context 的部分成本从训练侧转移到推理侧，并用 bias 保持外推稳定。

## 可以转成的实验 Idea

- 在 `RoPE vs ALiBi` 对照表里只回答三件事：位置怎么注入、是否利于外推、后续扩窗路线怎么接。
- 在 nanoGPT 中把 learned positional embedding 替换为 ALiBi mask/bias，做一个 tiny train-short/test-long toy eval。

## 疑问

- ALiBi 的 recency bias 为什么在语言模型上有效，但在需要长程精确 retrieval 的任务上是否会过度惩罚远处 token？
- 现代 LLM 更常用 RoPE 而不是 ALiBi，原因需要结合 LLaMA/Qwen/GPT-NeoX 等后续实现对比。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-06-07 | Quick Scan | done | ALiBi method、train short test long、head-specific slopes、early-token curse 和 RoPE 对比 |
