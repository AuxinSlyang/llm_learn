---
type: paper_note
title: Language Models are Unsupervised Multitask Learners
category: 10_AI_Foundations
status: queue
read_mode: Quick Read
phase: 2026-05 / GPT lineage
source_url: https://cdn.openai.com/better-language-models/language-models.pdf
local_pdf: GPT2_Language_Models_are_Unsupervised_Multitask_Learners.pdf
---

# GPT-2 - Language Models are Unsupervised Multitask Learners

## 为什么现在读

- GPT-2 把 GPT-1 的路线从“预训练后任务微调”推进到“足够大的语言模型可以在无显式监督下表现出多任务能力”。
- 当前只通读设计思想，不追所有 benchmark。

## 今日导读问题

1. GPT-2 为什么强调 language modeling 本身就是多任务学习？
2. 它相对 GPT-1 主要改变了什么：数据、规模、训练/评估范式？
3. zero-shot / prompting 的雏形在哪里出现？
4. 它如何为 GPT-3 的 in-context learning 铺路？

## 今日最低产出

- 写清 `larger WebText LM -> unsupervised multitask behavior -> zero-shot task framing` 主链路。

## 通读 Takeaway

- 一句话：GPT-2 把 GPT-1 的“预训练后再微调”往前推进一步，尝试证明足够大的语言模型在 WebText 这种自然文本上训练后，可以直接通过上下文里的任务描述/示例做 zero-shot task transfer，不再为每个任务改架构或做监督 fine-tuning。
- 核心问题意识：传统 NLP 系统是 narrow expert，需要为每个任务收集标注数据、设计目标并监督训练；GPT-2 追求的是一个更 general 的 language model。
- 关键转变：
  - GPT-1：`pretrain -> supervised fine-tune`
  - GPT-2：`larger LM on WebText -> prompt/task framing -> zero-shot evaluation`
- 重要直觉：语言本身可以同时承载 task specification、input 和 output；例如翻译任务可以写成 `translate to french, english text, french text`。
- 论文的核心判断：如果语言模型足够大、数据足够自然且多样，那么 next-token objective 可能会在训练中隐式学习很多任务格式。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-27 | Quick Read | planned | GPT 设计演化第二站：无监督多任务 / 零样本 |
