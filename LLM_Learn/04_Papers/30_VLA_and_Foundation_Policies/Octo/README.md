---
type: paper_note
title: Octo
category: VLA / Open Generalist Robot Policy
status: queue
read_mode: Scan
phase: 2026-11_to_2026-12
linked_project: [[embodied-ai-mini-stack]]
---

# Octo

## 一句话 Takeaway

Octo 的价值在于理解 open generalist robot policy 如何组织多任务、多机器人、多模态输入和动作输出。

## 重点问题

- 不同 embodiment 的 observation/action 如何统一。
- policy interface 如何设计。
- 数据混合和任务泛化如何处理。
- 开源模型如何落到本地 runtime / eval。

## 和 Mini-Stack 的连接

用于启发 `robot_interface` 和 `policy_runner` 的接口设计，尤其是不同 observation/action schema 的兼容边界。

