---
type: paper_note
title: Open X-Embodiment
category: Robot Data / Evaluation
status: queue
read_mode: Scan
phase: 2026-10_to_2026-11
linked_project: [[embodied-ai-mini-stack]]
---

# Open X-Embodiment

## 一句话 Takeaway

Open X-Embodiment 的核心价值是展示机器人数据跨任务、跨机器人、跨实验室整合后，能支撑更 general 的 robot policy，但也暴露 schema、质量、评测和 embodiment 差异问题。

## 重点问题

- 多来源 robot data 如何统一。
- observation/action schema 如何处理 embodiment 差异。
- eval 如何避免只看单一任务 demo。
- 数据规模化后系统工程问题是什么。

## 和 Mini-Stack 的连接

这是 DB / 存储背景最容易迁移的方向：trajectory schema、metadata、failure index、dataset versioning、replay 和 eval 都可以对齐这个问题域。

