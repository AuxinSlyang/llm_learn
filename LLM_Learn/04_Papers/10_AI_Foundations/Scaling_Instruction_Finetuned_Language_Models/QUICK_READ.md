---
type: paper_note
title: Scaling Instruction-Finetuned Language Models
category: 10_AI_Foundations
status: quick_read_done
read_mode: Quick Read
phase: 2026-05 / post-GPT lineage
source_url: https://arxiv.org/abs/2210.11416
arxiv: 2210.11416
submitted: 2022-10-20
last_revised: 2022-12-06
subjects:
  - cs.LG
  - cs.CL
doi: 10.48550/arXiv.2210.11416
pdf_url: https://arxiv.org/pdf/2210.11416
local_pdf: Scaling_Instruction_Finetuned_Language_Models.pdf
authors:
  - Hyung Won Chung
  - Le Hou
  - Shayne Longpre
  - Barret Zoph
  - Yi Tay
  - William Fedus
  - Yunxuan Li
  - Xuezhi Wang
  - Mostafa Dehghani
  - Siddhartha Brahma
  - Albert Webson
  - Shixiang Shane Gu
  - Zhuyun Dai
  - Mirac Suzgun
  - Xinyun Chen
  - Aakanksha Chowdhery
  - Alex Castro-Ros
  - Marie Pellat
  - Kevin Robinson
  - Dasha Valter
  - Sharan Narang
  - Gaurav Mishra
  - Adams Yu
  - Vincent Zhao
  - Yanping Huang
  - Andrew Dai
  - Hongkun Yu
  - Slav Petrov
  - Ed H. Chi
  - Jeff Dean
  - Jacob Devlin
  - Adam Roberts
  - Denny Zhou
  - Quoc V. Le
  - Jason Wei
---

# Scaling Instruction-Finetuned Language Models (FLAN)

## 为什么现在读

- 回答 instruction tuning 和 scale 如何叠加：在大量任务上指令微调后，模型是否更会泛化到未见任务。
- 和 InstructGPT/RLHF 一起区分 SFT、多任务 instruction tuning、人类偏好对齐。

## 明日导读问题

1. instruction tuning 和 GPT-3 few-shot prompting 有什么关系？
2. 扩大任务数、模型规模、CoT 数据分别带来什么提升？
3. 它和 RLHF 的关注点有什么不同？

## 明日最低产出

- 写清 `many instruction tasks -> instruction-finetuned LM -> better unseen-task generalization` 主链路。
- 写清 FLAN / InstructGPT / CoT 三者的边界。

## 通读 Takeaway

- FLAN 的核心不是 RLHF，也不是新架构，而是证明大规模 instruction-style SFT 可以把 pretrained LM 变成更会按自然语言任务说明完成新任务的模型。
- 它把任务写成 instruction/input/output 格式，在大量任务上做多任务指令微调，目标是提升 unseen-task generalization。
- 模型规模、任务数量和 CoT/rationale 数据会共同影响效果：如果希望模型输出推理过程，SFT 数据里必须包含对应的推理轨迹。
- 和 InstructGPT 的边界：InstructGPT 关注真实用户指令和人类偏好对齐；FLAN 更关注多任务 instruction tuning 的泛化能力。
- 和 CoT 的边界：CoT 是 prompt 格式诱导推理；FLAN 可以把 CoT/rationale 数据放进 finetuning 数据，让推理格式成为模型行为的一部分。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-06-02 | Quick Read | done | 形成 `many instruction tasks -> instruction-tuned LM -> unseen-task generalization` 主线 |
