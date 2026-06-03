---
type: paper_note
title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
authors:
  - Rafael Rafailov
  - Archit Sharma
  - Eric Mitchell
  - Stefano Ermon
  - Christopher D. Manning
  - Chelsea Finn
arxiv: "2305.18290"
source_url: "https://arxiv.org/abs/2305.18290"
pdf_url: "https://arxiv.org/pdf/2305.18290"
local_pdf: "/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Direct_Preference_Optimization/Direct_Preference_Optimization.pdf"
published: "2023-05-29"
updated: "2024-07-29"
categories:
  - cs.LG
  - cs.AI
  - cs.CL
status: quick_read_done
read_mode: Quick Scan
---

# Direct Preference Optimization

## Metadata

- 论文：Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- 作者：Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn
- arXiv：2305.18290
- 官方来源：https://arxiv.org/abs/2305.18290
- PDF：https://arxiv.org/pdf/2305.18290
- 本地 PDF：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Direct_Preference_Optimization/Direct_Preference_Optimization.pdf`

## Why Now

刚读完 Llama 2 之后，需要把 `SFT -> Reward Model -> PPO/RLHF` 这条后训练链路进一步拆开。DPO 关心的问题是：是否可以不用显式训练 reward model、也不用 PPO，直接用 preference pairs 优化语言模型。

## Reading Questions

1. RLHF + PPO 的复杂点到底在哪里？
2. DPO 怎么把 reward model 重新参数化成 policy likelihood ratio？
3. “language model is secretly a reward model” 的工程含义是什么？
4. DPO 和 InstructGPT / Llama 2 的 RLHF 流程是什么关系？

## Abstract + Introduction Understanding

### 问题

预训练 LM 学到大量知识，但行为不可控。现有做法通常收集人类偏好数据，先训练 reward model，再用 RL/PPO 调整语言模型。但这条链路有三个工程成本：

- 需要单独训练 reward model；
- PPO 训练不稳定、调参成本高；
- fine-tuning 时需要从模型采样并做 RL 更新，系统复杂度高。

### 核心想法

DPO 不把“人类偏好”先变成一个显式 reward model，再间接优化 policy；它直接把偏好对 `(chosen, rejected)` 变成一个分类式目标：让模型更偏向 chosen response，同时用 reference model 控制不要偏离太远。

### 一句话直觉

如果某个回答被人类选中，另一个回答被拒绝，那么 DPO 直接提高当前 policy 相对 reference policy 对 chosen 的概率优势，降低 rejected 的概率优势。

## Method

### 传统 RLHF 链路

```text
SFT model
  -> collect preference pairs
  -> train reward model
  -> PPO optimize policy with KL constraint
  -> aligned assistant
```

### DPO 链路

```text
SFT/reference model
  -> collect preference pairs
  -> optimize policy with DPO loss
  -> aligned assistant
```

### 关键对象

- `π_ref`：reference policy，通常是 SFT 后的模型，用来提供 KL 约束基准。
- `π_θ`：当前要优化的 policy。
- `β`：控制偏离 reference model 的强度；越大越强调偏好分离，越小越保守。
- preference pair：同一个 prompt 下的 `chosen response` 和 `rejected response`。

### 今日理解记录

- `π_θ(y|x)` 是当前训练模型在 prompt `x` 下生成整条回答 `y` 的概率；实现上通常用 response token 的 log-prob 求和，而不是直接把概率连乘。
- `π_ref` 是冻结的 SFT/reference model；它不反向传播，但它给出固定 baseline，决定当前模型的 chosen/rejected margin 要超过什么基准。
- DPO 的隐式 reward 定义为 `r_hat_θ(x, y) = β * log(π_θ(y|x) / π_ref(y|x))`。它不是显式 reward model，而是由当前 policy 相对 reference 的 log-prob ratio 得到的偏好分数。
- DPO loss 不是让所有回答 reward 都更高，而是让 `r_hat_θ(x, y_w) > r_hat_θ(x, y_l)`，即 chosen 的隐式 reward 高于 rejected。
- DPO 没有硬阈值保证模型绝不极端；它主要靠 `-log sigmoid` 的梯度饱和、`π_ref` 基准、`β` 和训练工程监控降低过优化风险。
- 更精确的表述：DPO 不是把 PPO 直接“变成”一个 loss，而是在 KL-constrained RLHF 目标和 Bradley-Terry preference model 下，把 `显式 reward model + PPO/RL policy optimization` 这条链路重参数化成 `reference-anchored pairwise log-prob loss`。

## Experiments

先扫结论：论文声称 DPO 在 sentiment control、summarization、single-turn dialogue 等任务上达到或超过 PPO-style RLHF，同时训练更简单、更轻量。

后续阅读重点：

- baselines 是否公平；
- 用了哪些 model size；
- DPO 的稳定性来自目标函数本身，还是来自更少的训练自由度；
- 是否仍然依赖高质量 SFT / preference 数据。

## Takeaway

DPO 是把 RLHF 的“显式 reward model + PPO”压缩成“reference-constrained preference classification”的后训练方法。它不替代 SFT，也不替代 preference 数据；它主要替代复杂的 PPO 优化环节。

一句话收口：DPO 是 RLHF 的轻量化重参数化，用 `chosen/rejected` 偏好对和 reference model，直接训练 policy 的相对 log-prob margin，替代显式 reward model + PPO。

## Robot Learning / Runtime Connection

对当前路线的意义不是马上训练模型，而是理解“偏好优化”可以怎样工程化：未来做机器人策略或 VLA 行为对齐时，`成功/失败轨迹偏好`、`人类纠偏`、`安全约束` 都可能转化为类似 preference optimization 的训练信号。

## Open Questions

- DPO 对 noisy preference data 的鲁棒性如何？
- 多轮对话和 long-context preference 是否仍然简单？
- 如果 reward 不是语言偏好，而是机器人任务成功率，DPO-style objective 能否迁移到 trajectory-level preference？
