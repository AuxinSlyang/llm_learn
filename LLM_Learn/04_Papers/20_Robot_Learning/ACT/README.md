---
type: paper_note
title: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA / ACT)
category: Robot Learning / Imitation Learning
status: downloaded
read_mode: Structured Read
phase: 2026-W24
linked_project: [[so-arm101-lerobot-first-loop]]
arxiv: 2304.13705
source_url: https://arxiv.org/abs/2304.13705
pdf_url: https://arxiv.org/pdf/2304.13705
authors: Tony Z. Zhao; Vikash Kumar; Sergey Levine; Chelsea Finn
submitted: 2023-04-23
---

# ALOHA / ACT

## 一句话 Takeaway

ACT 把高频动作预测压成 action chunks，降低长时序 manipulation imitation learning 的难度，并把数据采集、policy、eval 组织成一个工程闭环。

## 为什么现在读

它直接对齐 2026-09/10 的 manipulation BC pipeline，是从 classic-control demo 进入 robot learning 的关键论文之一。

## 8 问

- 任务是什么？双臂精细操作的 imitation learning。
- observation 是什么？视觉和机器人状态。
- action 是什么？一段未来动作 chunk。
- 数据怎么采？teleoperation / demonstration。
- policy / model 输出什么？action chunk。
- eval 怎么做？真实任务成功率和长程任务表现。
- failure mode 是什么？数据质量、时序误差、视觉泛化和 compounding error。
- 产品化需要什么支撑？数据版本、policy runtime、latency、failure replay、安全兜底。

## 和 Mini-Stack 的连接

- `trajectory schema` 需要能表达 action chunk。
- `policy_runner` 要能处理 chunked action 和 replanning frequency。
