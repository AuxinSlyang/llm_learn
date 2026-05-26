---
type: paper_note
title: RT-2
category: VLA / Foundation Robot Policy
status: queue
read_mode: Scan
phase: 2026-11
linked_project: [[embodied-ai-mini-stack]]
---

# RT-2

## 一句话 Takeaway

RT-2 的核心看点是把 web-scale VLM 的知识迁移到机器人动作预测，让模型不仅看懂图像和语言，还能输出可执行动作。

## 重点问题

- VLM pretraining knowledge 如何迁移到 robot action。
- action 如何 tokenized 或序列化。
- 高层语义推理和低层动作控制如何分层。
- 真实机器人 eval 如何定义。

## 和 Mini-Stack 的连接

帮助写清 11 月 `语言智能在机器人系统中的位置说明`：LLM/VLM/VLA 更适合高层任务理解和动作意图，不直接替代高频控制器。

