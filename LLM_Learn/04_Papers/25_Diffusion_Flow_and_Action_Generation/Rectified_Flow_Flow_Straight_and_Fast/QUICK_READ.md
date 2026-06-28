---
type: paper_note
title: "Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow"
short_name: Rectified Flow
authors:
  - Xingchao Liu
  - Chengyue Gong
  - Qiang Liu
arxiv_id: "2209.03003"
url: https://arxiv.org/abs/2209.03003
pdf_url: https://arxiv.org/pdf/2209.03003
local_pdf: ./Flow_Straight_and_Fast_Learning_to_Generate_and_Transfer_Data_with_Rectified_Flow.pdf
track: rectified flow / flow matching / fast generation
read_mode: Optional Bridge
status: downloaded
created: 2026-06-28
---

# Rectified Flow - QUICK READ

## Why now

Rectified Flow 是 Flow Matching 附近的重要支线。我们读它只为理解一个问题：

```text
如果从 noise 到 data 的路径更直，采样是否可以更快、更稳定？
```

## 本轮只回答

- rectified flow 里的 straight path 直觉是什么。
- 它和 diffusion 的曲线路径有什么区别。
- 为什么 straight / fast 对 sampling steps 有帮助。
- 和 Flow Matching 的关系是什么。
- 对 pi0 / action expert：continuous action chunk 是否也希望走更短路径。

## 一句话预期 takeaway

Rectified Flow 关注把从 noise 到 data 的传输路径拉直，让生成过程更接近直接沿速度场移动，从而有机会减少采样步数。

## Robot connection

```text
noisy action chunk
-> straight / rectified velocity field
-> clean action chunk with fewer steps
```

## 待读后填充

- straight path intuition:
- objective:
- relation to diffusion:
- relation to Flow Matching:
- sampling efficiency:
- robot action connection:
- one_sentence:

