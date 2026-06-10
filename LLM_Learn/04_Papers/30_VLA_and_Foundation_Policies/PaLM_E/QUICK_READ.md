---
type: paper_note
title: "PaLM-E: An Embodied Multimodal Language Model"
short_name: PaLM-E
arxiv_id: "2303.03378"
url: https://arxiv.org/abs/2303.03378
pdf_url: https://arxiv.org/pdf/2303.03378
local_pdf: ./PaLM_E_An_Embodied_Multimodal_Language_Model.pdf
track: embodied multimodal model
read_mode: Awareness
status: downloaded
created: 2026-06-09
---

# PaLM-E - QUICK READ

## Position

PaLM-E 是 embodied multimodal language model 入口：把视觉、语言和机器人状态等多模态输入接入大语言模型，用于机器人任务推理和规划。

## Why Later

它对理解 `embodied multimodal reasoning` 很重要，但本周优先级低于 LeRobot / ACT / RT-2，因为当前必须先把 SO-ARM101 的真实 observation/action 闭环建起来。

## Read Questions

- 机器人状态如何进入语言模型？
- multimodal tokens 如何和 language tokens 融合？
- 它输出的是语言计划、动作，还是中间指令？
- 和 RT-2 / VLA 的区别是什么？

