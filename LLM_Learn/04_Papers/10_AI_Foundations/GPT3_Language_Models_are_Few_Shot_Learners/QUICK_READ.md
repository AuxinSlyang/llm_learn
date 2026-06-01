---
type: paper_note
title: Language Models are Few-Shot Learners
category: 10_AI_Foundations
status: queue
read_mode: Quick Read
phase: 2026-05 / GPT lineage
source_url: https://arxiv.org/abs/2005.14165
arxiv: 2005.14165
pdf_url: https://arxiv.org/pdf/2005.14165
local_pdf: GPT3_Language_Models_are_Few_Shot_Learners.pdf
---

# GPT-3 - Language Models are Few-Shot Learners

## 为什么现在读

- GPT-3 把 GPT-2 的路线推到规模化，核心现象是 in-context learning / few-shot prompting。
- 当前只通读设计思想，不追 75 页所有实验细节。

## 今日导读问题

1. few-shot / one-shot / zero-shot 在 GPT-3 里分别是什么意思？
2. 它如何把任务适配从参数更新转成上下文示例？
3. 模型规模、数据规模和能力涌现之间的主张是什么？
4. 它和 GPT-1/GPT-2 的连续性是什么？

## 今日最低产出

- 写清 `large autoregressive LM -> in-context examples -> task behavior without gradient update` 主链路。

## 通读 Takeaway

- 一句话：GPT-3 把 GPT-2 的 `larger LM -> zero-shot task behavior` 继续规模化，核心是证明一个 175B autoregressive language model 可以在 **不更新参数、不做 fine-tuning** 的情况下，只通过 prompt 里的任务说明和少量示例完成大量 NLP 任务。
- 关键转变：
  - GPT-1：`pretrain -> supervised fine-tune`
  - GPT-2：`larger WebText LM -> zero-shot task framing`
  - GPT-3：`much larger LM -> in-context examples -> few-shot task behavior without gradient update`
- few-shot / one-shot / zero-shot 的区别：
  - zero-shot：只给任务说明，不给样例。
  - one-shot：给 1 个输入输出示例。
  - few-shot：在上下文里给少量输入输出示例。
- GPT-3 的重点不是新增 task head，也不是对每个任务微调参数，而是把任务适配从 “改参数” 变成 “写上下文”。
- 核心主张：模型规模扩大后，task-agnostic few-shot performance 明显改善；但论文也明确指出它仍有失败任务和大规模网页语料带来的方法论/污染问题。

## 核心流程

- 训练阶段：继续训练一个 autoregressive LM，目标仍然是 next-token prediction。
- 使用阶段：
  - 把任务说明、若干示例、待回答输入都写进 prompt。
  - 模型根据 prompt 继续生成后续 token。
  - 没有梯度更新，没有 task-specific head，没有 supervised fine-tuning。
- 一句话公式：`prompt = task instruction + examples + query`，`model output = next-token continuation`。

## 和 GPT-1/GPT-2 的连续性

- GPT-1 证明 LM pretraining 的 hidden states 可以迁移到下游任务。
- GPT-2 证明 larger LM 可以在 zero-shot 设置下表现出一些无监督多任务能力。
- GPT-3 进一步证明：当模型足够大，少量示例可以直接放在上下文里，让模型在推理时“临时适配”任务。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-27 | Quick Read | planned | GPT 设计演化第三站：规模化 + in-context learning |
