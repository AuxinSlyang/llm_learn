---
type: paper_note
title: Diffusion Policy
category: Robot Learning / Imitation Learning
status: queue
read_mode: Structured Read
phase: 2026-09_to_2026-10
linked_project: [[embodied-ai-mini-stack]]
---

# Diffusion Policy

## 一句话 Takeaway

Diffusion Policy 把机器人动作序列建模为条件去噪生成问题，适合表达多模态动作分布，但也带来 inference latency 和 closed-loop control 频率问题。

## 为什么现在读

它是 manipulation policy 的核心路线之一，能帮助理解为什么 robot learning 不只是分类或回归。

## 8 问

- 任务是什么？从 observation 生成机器人动作序列。
- observation 是什么？视觉、低维状态或二者结合。
- action 是什么？连续动作序列。
- 数据怎么采？demonstration trajectories。
- policy / model 输出什么？通过 denoising 生成 action sequence。
- eval 怎么做？任务成功率、泛化、失败样例。
- failure mode 是什么？latency、distribution shift、长时序稳定性。
- 产品化需要什么支撑？runtime profiling、fallback、action validation、eval harness。

## 和 Mini-Stack 的连接

- 11 月的 latency report 可以专门讨论 diffusion-style policy 的部署挑战。
- `policy_runtime` 需要区分 model inference latency 和 control loop frequency。

