---
type: paper_note
title: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
category: 10_AI_Foundations
status: quick_read_done
read_mode: Quick Read
phase: 2026-05 / post-GPT lineage
source_url: https://arxiv.org/abs/2201.11903
arxiv: 2201.11903
pdf_url: https://arxiv.org/pdf/2201.11903
local_pdf: Chain_of_Thought_Prompting_Elicits_Reasoning_in_Large_Language_Models.pdf
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

## 为什么现在读

- 回答 GPT-3 few-shot 之后的问题：为什么给中间推理步骤会显著改善复杂任务表现。
- 理解 prompt 不只是任务格式，也可以提供“解题过程格式”。

## 明日导读问题

1. CoT prompt 和普通 few-shot prompt 的区别是什么？
2. 为什么 CoT 主要在大模型上更有效？
3. 它释放的是 reasoning 能力，还是更好的输出格式约束？

## 明日最低产出

- 写清 `few-shot examples -> intermediate reasoning steps -> better multi-step task performance` 主链路。
- 写清 CoT 和 GPT-3 in-context learning 的关系。

## 通读 Takeaway

- CoT 的核心 insight 不是训练新模型，而是在足够大的语言模型上，通过 few-shot in-context prompting 把示例从 `question -> answer` 改成 `question -> intermediate reasoning -> answer`，从而诱导模型在回答前显式生成中间推理 token。
- 这说明普通 `Q -> A` prompt 只是大模型能力的一个 lower bound；大模型可能在预训练中已经学到大量解释、推导、解题过程和步骤化文本模式，只是直接问答不一定会触发这些模式。
- CoT prompting 本身更像一个发现/探针，而不是生产级完整方案：示例难选、prompt 敏感、只在大模型上明显有效，且生成的 reasoning path 不保证 faithful 或正确。
- 对后续 LLM 推理能力的真正影响是：它把“显式中间推理过程”确立为可利用的行为格式，后续可以进入 reasoning SFT、synthetic CoT data、verifier / PRM、tool use、self-consistency 和 reasoning RL。
- 学习上不再继续深挖 CoT 原论文细节；保留这个 takeaway，后续统一阅读 CoT 系列论文时再看 self-consistency、STaR、process supervision、ReAct / tool use 和 reasoning RL。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-31 | Quick Read | done | 形成 `few-shot examples -> intermediate reasoning -> answer` 主线 |
