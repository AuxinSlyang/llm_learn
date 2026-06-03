---
type: paper_note
title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
authors:
  - Xuezhi Wang
  - Jason Wei
  - Dale Schuurmans
  - Quoc Le
  - Ed Chi
  - Sharan Narang
  - Aakanksha Chowdhery
  - Denny Zhou
arxiv: "2203.11171"
source_url: "https://arxiv.org/abs/2203.11171"
pdf_url: "https://arxiv.org/pdf/2203.11171"
local_pdf: "/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Self_Consistency_Improves_Chain_of_Thought_Reasoning/Self_Consistency_Improves_Chain_of_Thought_Reasoning.pdf"
published: "2022-03-21"
updated: "2023-03-07"
venue: ICLR 2023
categories:
  - cs.CL
  - cs.AI
status: quick_read_done
read_mode: Quick Scan
---

# Self-Consistency Improves Chain of Thought Reasoning

## Metadata

- 论文：Self-Consistency Improves Chain of Thought Reasoning in Language Models
- 作者：Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou
- arXiv：2203.11171
- 官方来源：https://arxiv.org/abs/2203.11171
- PDF：https://arxiv.org/pdf/2203.11171
- 本地 PDF：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Self_Consistency_Improves_Chain_of_Thought_Reasoning/Self_Consistency_Improves_Chain_of_Thought_Reasoning.pdf`

## Why Now

Llama 2 让我们看到 post-training 怎样把 base model 调成 assistant；DPO 继续拆 preference optimization。Self-Consistency 这篇补的是 reasoning/test-time compute：不是训练阶段改变模型，而是在推理阶段采样多条 CoT 路径，再用答案一致性做选择。

## Reading Questions

1. Greedy Chain-of-Thought 为什么不稳？
2. 多条 reasoning paths + answer voting 为什么能提升准确率？
3. 哪些任务最适合 self-consistency？
4. 它和 ReAct / agent / 工具调用链路有什么关系？

## Reading Prep

- 本地 PDF 已就绪：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Self_Consistency_Improves_Chain_of_Thought_Reasoning/Self_Consistency_Improves_Chain_of_Thought_Reasoning.pdf`
- 推荐读法：Quick Scan（20-30m），重点看 `Abstract / Introduction / Method / Main Results`。
- 今日只抓一个问题：为什么 `多条 CoT 路径 + final answer voting` 比一次 greedy CoT 更稳。
- 不展开方向：不把它变成 decoding 大专题，也不追所有 benchmark 细节。

## Section Map

| Section | 读什么 | 第一遍是否必读 |
|---|---|---|
| Abstract + Introduction | 问题设定：greedy CoT 只相信一条推理路径，复杂问题容易走错 | 必读 |
| Method | self-consistency 的三步：sample reasoning paths、extract answers、aggregate/vote | 必读 |
| Experiments | 看 GSM8K / SVAMP / AQuA / StrategyQA 等 benchmark 上的提升幅度 | 扫读 |
| Analysis / Ablation | 看采样条数、temperature、模型规模对收益的影响 | 可选 |
| Related Work / Appendix | 只在需要补背景时看 | 可跳 |

## Third Paper Choice

- 第三篇建议：`ReAct: Synergizing Reasoning and Acting in Language Models`。
- 选择理由：DPO 补 `post-training / preference optimization`，Self-Consistency 补 `reasoning / test-time sampling`，ReAct 正好补 `reasoning + acting + observation`，能连接到 agent / tool use / robot runtime。
- 暂缓：`DeepSeek-R1` 会打开 reasoning RL / distillation 大线；`Toolformer` 会打开工具调用训练数据构造线，今天都容易扩散。

## Abstract + Introduction Understanding

### 问题

Chain-of-Thought prompting 能让大模型显式写出推理步骤，但如果只用 greedy decoding，就等于只相信一条最可能的推理路径。复杂问题经常存在多条有效推理路径，单一路径很容易局部出错。

### 核心想法

Self-Consistency 用采样替代 greedy decoding：对同一个问题采样多条 reasoning paths，然后忽略具体过程差异，统计最终答案，选择最一致的答案。

### 一句话直觉

让模型“多想几遍”，如果多条不同推理路径都收敛到同一个答案，这个答案更可信。

## Method

```text
prompt with CoT examples
  -> sample multiple reasoning paths
  -> extract final answer from each path
  -> aggregate / vote / marginalize
  -> choose most consistent final answer
```

关键点：

- 它是 decoding strategy，不是新模型架构。
- 它增加的是 test-time compute。
- 它依赖答案可聚合：数学题、常识问答这类 final answer 较清晰的任务更合适。

## Experiments

官方摘要中报告 self-consistency 在多个 reasoning benchmark 上显著提升，例如 GSM8K、SVAMP、AQuA、StrategyQA、ARC-challenge。后续需要确认：

- 采样条数和温度如何影响收益；
- 成本提升和准确率提升是否匹配；
- 对开放式生成任务是否仍然有效。

## Takeaway

Self-Consistency 是 CoT 的推理时增强：它不靠一次 greedy 推理，而是用多样化 reasoning samples 的最终答案一致性来提升可靠性。

## Quick Read Summary

- 核心问题：标准 CoT 通常只生成一条 reasoning path，复杂问题中单条路径容易局部出错。
- 核心方法：把 greedy / single-path CoT 改成 `sample multiple CoT paths -> extract final answers -> vote / marginalize -> choose the most consistent answer`。
- 方法性质：它是 inference-time / decoding strategy，不改模型参数，也不是新的训练算法。
- 关键直觉：正确答案往往能由多条不同推理路径收敛得到；错误答案更容易分散。
- 成本与边界：需要多次采样，推理成本更高；更适合 final answer 清晰、可抽取、可投票的任务；开放式生成、多步行动或机器人任务需要额外 verifier / environment check。
- 今日一句话：Self-Consistency 是 CoT 的 test-time ensemble，用更多推理样本换更稳定的最终答案。

## Robot Learning / Runtime Connection

对机器人/VLA 的关系在高层任务规划：当机器人面对“先做什么、再做什么”的语言推理时，可以让 LLM 生成多条候选计划，再用一致性、可执行性、环境约束或 simulator check 做筛选。这是 agent/runtime 层的 test-time decision pattern。

## Open Questions

- 多轮工具调用或行动序列能否像 final answer 一样投票？
- 如果多个答案都可行，self-consistency 是否会压低探索性？
- 在机器人任务里，vote 应该基于语言答案、计划结构，还是模拟执行结果？
