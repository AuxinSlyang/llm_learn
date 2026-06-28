---
type: paper_note
title: Score-Based Generative Modeling through Stochastic Differential Equations
short_name: Score SDE
authors:
  - Yang Song
  - Jascha Sohl-Dickstein
  - Diederik P. Kingma
  - Abhishek Kumar
  - Stefano Ermon
  - Ben Poole
arxiv_id: "2011.13456"
url: https://arxiv.org/abs/2011.13456
pdf_url: https://arxiv.org/pdf/2011.13456
local_pdf: ./Score_Based_Generative_Modeling_through_Stochastic_Differential_Equations.pdf
track: diffusion / score matching / continuous-time generative modeling
read_mode: Awareness
status: downloaded
created: 2026-06-28
---

# Score SDE - QUICK READ

## Why now

Score SDE 是从离散 DDPM 走向 continuous-time diffusion / ODE-SDE 视角的桥。后面理解 Flow Matching、Rectified Flow、pi0 flow action expert 时，需要知道为什么 diffusion 可以被看成连续时间的概率路径。

## 本轮只回答

- score 是什么：`grad_x log p_t(x)` 的直觉。
- SDE 视角如何统一不同 diffusion / score-based models。
- reverse-time SDE / probability flow ODE 的直觉是什么。
- 为什么 continuous-time 视角连接后续 flow / vector field。
- 对 robot action generation：连续时间采样和 latency / control frequency 有什么关系。

## 一句话预期 takeaway

Score SDE 把 diffusion 建模提升到连续时间框架：通过学习每个噪声水平下的 score，可以用 reverse SDE 或 probability flow ODE 从噪声生成数据。

## Robot connection

```text
noisy action distribution over time
-> score / reverse dynamics / probability flow
-> action chunk distribution
```

## 待读后填充

- score intuition:
- forward SDE:
- reverse SDE:
- probability flow ODE:
- relation to Flow Matching:
- robot runtime connection:
- one_sentence:

