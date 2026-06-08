---
type: paper_queue
name: TOREAD LLM Papers
updated: 2026-06-07
phase: LLM end-to-end closure before Robot Learning
---

# TOREAD LLM Papers

> 目的：把 LLM 从 `pretraining -> tokenizer/nanoGPT -> instruction following -> reasoning/tool/context/runtime` 的通路补完整。  
> 约束：这是 LLM 扩展阅读队列，不替代 W24 起的 Robot Learning 主线；每篇默认 Quick Read，只有直接影响代码/系统理解时再 Deep Read。

## 当前已读 / 收口中

| 状态 | 论文 / 材料 | 作用 |
|---|---|---|
| 已读 | Scaling Laws for Neural Language Models | 理解参数量、数据量、compute 与 loss 的可预测关系 |
| 已读 | Training Compute-Optimal Large Language Models (Chinchilla) | 理解 fixed compute 下参数量和 token 数的配平 |
| 已读 | Training Language Models to Follow Instructions with Human Feedback (InstructGPT) | 理解 SFT + RM + RLHF 的 assistant 对齐范式 |
| 已读 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | 理解 few-shot CoT 如何释放推理过程 |
| 已读 | Scaling Instruction-Finetuned Language Models (FLAN) | 理解多任务 instruction tuning、CoT 数据和 unseen-task generalization |

## 第一阶段总结前最后一篇

| 优先级 | 论文 / 材料 | 链接 | 读法 | 读完要回答的问题 |
|---|---|---|---|---|
| 已看过 | Llama 2: Open Foundation and Fine-Tuned Chat Models | https://arxiv.org/abs/2307.09288 | Structured Read | 现代 open LLM 如何组织 pretraining、SFT、RLHF、safety、eval 和 release |

`Llama 2` 已具备阅读笔记后，先写第一阶段总结：

```text
现代 LLM 是怎么训练出来的：
data/tokenizer -> pretraining -> SFT/instruction tuning -> preference optimization/RLHF -> safety/eval -> serving/runtime
```

阶段判断：

- 到 `InstructGPT + CoT + FLAN + Llama 2` 为止，LLM 已经基本具备可用的 instruction following、assistant 行为和显式推理范式。
- 但它还不够稳定、便宜、长上下文、工具化、可高效微调、可高吞吐服务，所以后续论文分别在这些方向做优化。

## 后续扩展队列

### A. Post-training / Preference / Reasoning

| 优先级 | 论文 / 材料 | 链接 | 价值 |
|---|---|---|---|
| 已读 | Direct Preference Optimization (DPO) | https://arxiv.org/abs/2305.18290 | 从 PPO/RLHF 转到直接 preference optimization，理解现代偏好优化主线 |
| 已读 | Self-Consistency Improves Chain of Thought Reasoning | https://arxiv.org/abs/2203.11171 | 理解多条 CoT reasoning path + answer voting 的 test-time compute 思路 |
| P2 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | https://arxiv.org/abs/2501.12948 | 理解 reasoning RL、verifiable reward、distillation 和 thinking model 训练路线 |

### B. Agent / Tool / External Memory

| 优先级 | 论文 / 材料 | 链接 | 价值 |
|---|---|---|---|
| 已读 | ReAct: Synergizing Reasoning and Acting in Language Models | https://arxiv.org/abs/2210.03629 | 理解 reasoning/action/observation 交替，是 tool agent 和 embodied agent 的桥 |
| 已读 | Toolformer: Language Models Can Teach Themselves to Use Tools | https://arxiv.org/abs/2302.04761 | 理解模型如何学习何时调用工具、传参、使用返回结果 |
| 已读 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | https://arxiv.org/abs/2005.11401 | 理解参数记忆之外的外部检索记忆路线 |

### C. Context Window / Position / Long Context

| 优先级 | 论文 / 材料 | 链接 | 价值 |
|---|---|---|---|
| 已读 | RoFormer / RoPE | https://arxiv.org/abs/2104.09864 | 理解 rotary position embedding 和相对位置信息如何进入 attention |
| 已读 | ALiBi | https://arxiv.org/abs/2108.12409 | 作为 RoPE 对照，理解 train short test long 的位置偏置路线 |
| P2 | Transformer-XL | https://arxiv.org/abs/1901.02860 | 理解固定 context window 的历史限制和 recurrence memory |
| P1 | Position Interpolation | https://arxiv.org/abs/2306.15595 | 理解 RoPE 模型如何通过位置插值扩展上下文 |
| P1 | YaRN | https://arxiv.org/abs/2309.00071 | 理解更高效的 RoPE context extension |
| P2 | LongRoPE | https://arxiv.org/abs/2402.13753 | 理解超长上下文扩展路线和短上下文能力恢复 |
| P2 | RULER | https://arxiv.org/abs/2404.06654 | 理解标称上下文长度和真实可用上下文长度的差异 |

### D. Efficient Finetuning / Runtime / Serving

| 优先级 | 论文 / 材料 | 链接 | 价值 |
|---|---|---|---|
| P1 | LoRA | https://arxiv.org/abs/2106.09685 | 理解冻结大模型、只训练低秩 adapter 的参数高效微调 |
| P2 | QLoRA | https://arxiv.org/abs/2305.14314 | 理解 4-bit quantization + LoRA 低显存微调路线 |
| P1 | FlashAttention | https://arxiv.org/abs/2205.14135 | 理解 attention 的 IO bottleneck 和 exact attention 加速 |
| P2 | FlashAttention-2 | https://arxiv.org/abs/2307.08691 | 理解更好的并行和 work partitioning |
| P1 | PagedAttention / vLLM | https://arxiv.org/abs/2309.06180 | 理解 KV cache 的 paging 管理和高吞吐 serving |

### E. Transformer Theory / Interpretability Support

| 优先级 | 论文 / 材料 | 链接 | 价值 |
|---|---|---|---|
| P2 | Transformers are Inherently Succinct | https://openreview.net/forum?id=Yxz92UuPLQ | 从 succinctness / expressivity 角度理解 Transformer 为什么能紧凑表达复杂模式，以及 attention 架构为什么能迁移到非文本 token |

## 推荐阅读顺序

1. `FLAN` 收口：写清 instruction tuning / CoT / InstructGPT 的边界。
2. `Llama 2`：补现代 LLM 工程全流程。
3. 第一阶段总结：写 `LLM phase 1 总结.md` 或并入 `LLM end-to-end path v0`。
4. `Tokenizer / BPE + nanoGPT`：跟 Karpathy 视频，把 text 到 logits/generate 的代码通路打通。
5. `DPO -> Self-Consistency -> ReAct`：已完成第一轮，后续只在 agent/runtime 汇总时回看。
6. `RoPE -> ALiBi`：已完成第一轮；context/runtime 线后续从 `Position Interpolation -> FlashAttention -> PagedAttention` 继续。

## 每篇默认输出

- 一句话 takeaway。
- 解决什么问题。
- 它接在前一篇论文哪里。
- 方法主链路。
- 对 `LLM end-to-end path` 或 `Robot Learning / VLA runtime` 的意义。
