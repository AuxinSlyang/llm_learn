---
type: paper_note
title: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger)
category: Robot Learning / Imitation Learning
status: queue
read_mode: Scan
phase: 2026-08_to_2026-09
linked_project: [[embodied-ai-mini-stack]]
arxiv_id: "1011.0686"
arxiv_url: https://arxiv.org/abs/1011.0686
pdf_url: https://arxiv.org/pdf/1011.0686.pdf
authors:
  - Stephane Ross
  - Geoffrey J. Gordon
  - J. Andrew Bagnell
submitted: "2010-11-02"
last_revised: "2011-03-16"
subjects:
  - cs.LG
  - cs.AI
  - stat.ML
---

# DAgger

## Metadata

- Title: `A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning`
- arXiv: `1011.0686`（cs.LG / cs.AI / stat.ML）
- Authors: Stephane Ross, Geoffrey J. Gordon, J. Andrew Bagnell
- PDF: https://arxiv.org/pdf/1011.0686.pdf
- Notes: DAgger（Dataset Aggregation）是本文提出/系统化的核心算法之一（常用来指代这一类 imitation learning 迭代数据聚合方法）。

## 一句话 Takeaway

BC 的核心风险是训练数据分布和 policy 自己运行时遇到的状态分布不一致，DAgger 用数据聚合把 learner 访问到的状态重新标注进训练集。

## 为什么现在读

它解释了为什么一个仿真 BC demo 可能训练 loss 很好，但一接回 closed-loop evaluation 就失败。

## 8 问

- 任务是什么？降低 imitation learning 中的 covariate shift。
- observation 是什么？由具体任务定义，重点是 learner 实际访问到的状态。
- action 是什么？expert 在这些状态下给出的动作。
- 数据怎么采？让当前 policy 运行，收集访问状态，再由 expert 标注。
- policy / model 输出什么？动作或动作分布。
- eval 怎么做？closed-loop task performance，而不是只看 supervised loss。
- failure mode 是什么？expert query 成本高，真实机器人上探索不安全。
- 产品化需要什么支撑？safe data collection、rollback、human/expert labeling、failure replay。

## 和 Mini-Stack 的连接

- 在 BC eval 失败后，把失败 episode 加入下一轮 dataset。
- `failure_reason` 和 replay 工具可以服务 DAgger-style 数据迭代。
