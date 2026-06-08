# 2026-06-07 论文阅读状态 Review

> 目的：进入 `tokenizer / nanoGPT` 前，把本地已学论文从待读队列中清出，避免继续扩散论文树。

## 已完成：Transformer 前传与 GPT 主线

| 状态 | 论文 / 材料 | 当前 takeaway |
|---|---|---|
| skimmed | Finding Structure in Time | RNN 用内部状态处理变长序列，但串行且长距离依赖困难。 |
| skimmed | Long Short-Term Memory | LSTM 用 gates 和 cell state 缓解普通 RNN 的长期记忆问题。 |
| done | Sequence to Sequence Learning with Neural Networks | Seq2Seq 把输入序列压成 encoder state，再让 decoder 条件生成目标序列。 |
| done | Neural Machine Translation by Jointly Learning to Align and Translate | Bahdanau attention 让 decoder 每步动态读取 source states，缓解 fixed vector bottleneck。 |
| done | Attention Is All You Need | Transformer 把 attention 从辅助模块升级为主计算机制；GPT 继承 decoder-only causal self-attention 路径。 |
| done | GPT-1 | `pretrain -> supervised fine-tune`，证明 decoder-only LM hidden states 可迁移到 NLU 任务。 |
| done | GPT-2 | `larger LM -> zero-shot task framing`，自然文本中的任务格式开始成为能力来源。 |
| done | GPT-3 | `in-context examples -> few-shot behavior without gradient update`，任务适配从改参数转向构造上下文。 |

## 已完成：Scaling / Post-Training / Reasoning

| 状态 | 论文 / 材料 | 当前 takeaway |
|---|---|---|
| done | Scaling Laws | `N/D/C` 与 loss 呈稳定幂律关系，scale 可以进入训练预算规划。 |
| done | Chinchilla | 固定 compute 下不要只堆参数，模型参数和训练 tokens 应近似一起增长。 |
| done | InstructGPT / RLHF | `base LM -> SFT -> RM -> PPO/RLHF`，能力、听话、好用、安全不是同一件事。 |
| done | Chain-of-Thought Prompting | CoT 通过中间推理 token 诱导大模型释放复杂任务能力，但不保证 faithful。 |
| done | FLAN | 多任务 instruction tuning 提升 unseen-task generalization；CoT 数据会塑造推理输出格式。 |
| done | Llama 2 | 现代 open LLM 是 `pretraining -> SFT/RLHF -> safety/eval/release` 的工程闭环。 |
| done | DPO | 用 reference-constrained preference loss 替代显式 reward model + PPO。 |
| done | Self-Consistency | test-time 多路径 CoT + answer voting，用推理成本换更稳定答案。 |
| done | ReAct | `Thought -> Action -> Observation` 是高层 agent/runtime loop，而不是低层控制算法。 |
| done | Toolformer | 用 loss improvement 自举 tool-use 数据，让模型学会何时调用工具和使用结果。 |
| done | RAG | 把外部可检索记忆接入生成模型，核心是 external memory grounding。 |

## 已完成：Position / Context 补充线

| 状态 | 论文 / 材料 | 当前 takeaway |
|---|---|---|
| done | RoFormer / RoPE | 对 q/k 按位置旋转，让 `q_m · k_n` 自然携带相对距离 `m-n`。 |
| done | ALiBi | 在 attention logits 上加 head-specific 距离惩罚，是稳定外推的 soft local-attention bias。 |

## 暂不继续展开

- `DeepSeek-R1`：reasoning RL / verifiable reward / distillation，后续看，不抢 tokenizer。
- `Transformer-XL / Position Interpolation / YaRN / LongRoPE / RULER`：长上下文线后续从 Position Interpolation 重新进入。
- `LoRA / QLoRA / FlashAttention / PagedAttention / vLLM`：AI Infra 支撑线，等 nanoGPT 主链路讲清后再看。
- `DAgger / ACT / Diffusion Policy / RT-1 / RT-2 / Open X-Embodiment / Octo / OpenVLA / PI0`：W24 起按 Robot Learning 主线逐步进入。

## 下一步

当前不再开新论文。下一步切到 tokenizer：

```text
raw text -> UTF-8 bytes -> BPE merge -> token ids -> embedding lookup -> transformer blocks -> logits/loss/generate
```
