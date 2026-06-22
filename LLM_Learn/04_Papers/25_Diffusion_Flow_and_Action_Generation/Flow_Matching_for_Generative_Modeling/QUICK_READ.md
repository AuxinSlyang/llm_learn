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
