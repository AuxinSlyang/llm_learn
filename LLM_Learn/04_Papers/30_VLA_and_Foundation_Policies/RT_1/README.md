---
type: paper_note
title: RT-1
category: VLA / Foundation Robot Policy
status: queue
read_mode: Scan
phase: 2026-11
linked_project: [[embodied-ai-mini-stack]]
---

# RT-1

## 一句话 Takeaway

RT-1 代表了用大规模真实机器人数据训练 language-conditioned robot policy 的早期系统化路线。

## 重点问题

- language instruction 如何进入 policy。
- 数据规模和任务多样性如何影响泛化。
- action representation 如何被离散化或结构化。
- eval 如何覆盖任务、环境和泛化。

## 和 Mini-Stack 的连接

2026 年只需要理解其系统结构，不做复现。重点放在 `language instruction -> policy input -> action -> eval` 这条链路。

