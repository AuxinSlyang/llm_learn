---
type: paper_note
title: Flow Matching for Generative Modeling
short_name: Flow Matching
authors:
  - Yaron Lipman
  - Ricky T. Q. Chen
  - Heli Ben-Hamu
  - Maximilian Nickel
  - Matt Le
arxiv_id: "2210.02747"
url: https://arxiv.org/abs/2210.02747
pdf_url: https://arxiv.org/pdf/2210.02747
local_pdf: ./Flow_Matching_for_Generative_Modeling.pdf
track: flow matching / generative modeling / pi0 support
read_mode: Bridge
status: downloaded
created: 2026-06-22
last_session: 2026-06-28
---

# Flow Matching for Generative Modeling - QUICK READ

## Why now

Flow Matching 是理解 pi0 action expert 的关键底座。第一轮不推公式，只抓 `probability path` 和 `vector field`。

## 本轮只回答

- probability path 是什么：noise distribution 到 data distribution 的中间路径。
- vector field 是什么：中间样本应该如何移动。
- Flow Matching 训练目标为什么是 regression over vector fields？
- 它和 diffusion / score matching 的关系是什么？
- 为什么适合 continuous action chunk generation？

## 一句话预期 takeaway

Flow Matching 学习从简单噪声分布到真实数据分布的连续速度场；采样时从噪声出发，沿着 learned vector field 移动到 data-like sample。

## Robot connection

```text
noise action chunk distribution
-> learned vector field conditioned on observation
-> demonstration action chunk distribution
```

## 待读后填充

- probability path:
- vector field:
- training objective:
- sampling:
- 和 DDPM / Diffusion Policy 的区别:
- 和 pi0 的连接:

## 2026-06-28 Study Session

### Pass 0：定位

- 论文：`Flow Matching for Generative Modeling`
- 领域：generative modeling / continuous normalizing flows / diffusion alternatives
- 读法：Bridge Scan，不做公式深推，只建立 `probability path -> vector field -> sampling ODE` 的直觉。
- 为什么今天读：它是理解 `pi0` 里 flow action expert 的支撑论文。我们只关心它如何把 `noise action chunk` 推到 `demonstration action chunk`。

### Pass 1：Abstract / Introduction 先抓什么

这篇论文的主问题：

- Diffusion 模型训练稳定、可扩展，但路径形式较受限，采样往往需要很多步。
- Continuous Normalizing Flows 理论上能表达更一般的连续概率路径，但传统训练要跑 ODE 或处理难积分，不够 scalable。
- Flow Matching 的目标是：不通过模拟整条 ODE 训练，而是直接回归一个目标 vector field。

一句话理解：

```text
给定一条从 noise distribution 到 data distribution 的路径，
Flow Matching 训练一个神经网络预测“当前位置 x 在时间 t 应该往哪里走”。
采样时从 noise 出发，沿着这个 learned vector field 积分，就得到 data-like sample。
```

### 今天只看三个问题

1. `probability path`：从简单噪声分布到数据分布，中间每个时间点的分布是什么。
2. `vector field`：在路径上的某个时间点，每个样本点应该朝哪个方向、以多快速度移动。
3. `Conditional Flow Matching`：为什么不用知道全局复杂 vector field，只用每个 data sample 对应的 conditional path 也能训练。

### 和 robot action 的连接

```text
image/state/language condition
+ noisy future action chunk
-> model predicts vector field / velocity
-> integrate or step along the field
-> clean future action chunk
```

对 SO-ARM101 / LeRobot 的直接要求：

- 未来记录 episode 时必须知道 action dim、control frequency、action horizon。
- 否则无法判断 flow / diffusion / ACT action chunk 这几种 action generation 方法到底在生成什么。
