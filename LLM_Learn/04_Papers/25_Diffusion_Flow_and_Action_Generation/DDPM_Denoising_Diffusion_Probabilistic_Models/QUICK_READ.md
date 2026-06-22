---
type: paper_note
title: Denoising Diffusion Probabilistic Models
short_name: DDPM
authors:
  - Jonathan Ho
  - Ajay Jain
  - Pieter Abbeel
arxiv_id: "2006.11239"
url: https://arxiv.org/abs/2006.11239
pdf_url: https://arxiv.org/pdf/2006.11239
local_pdf: ./DDPM_Denoising_Diffusion_Probabilistic_Models.pdf
track: diffusion / generative modeling / robot action generation support
read_mode: Awareness
status: downloaded
created: 2026-06-22
---

# DDPM - QUICK READ

## Why now

DDPM 是理解 diffusion 的入口，只为后续读 Diffusion Policy、Flow Matching 和 pi0 服务。

## 本轮只回答

- forward noising：`data -> noisy data -> noise` 是什么？
- reverse denoising：`noise -> data` 是怎么学习的？
- 模型训练时预测的是 noise / denoising target 的哪种形式？
- 为什么 sampling 通常需要多步？
- 这个机制如何迁移到 `noisy action sequence -> clean action sequence`？

## 一句话预期 takeaway

DDPM 把生成问题变成一个逐步去噪问题：训练时给 clean data 加噪，学习 reverse process；生成时从随机噪声反向采样得到 data-like sample。

## Robot connection

```text
image diffusion:
  noisy image -> clean image

action diffusion:
  noisy action chunk -> clean action chunk
```

## 待读后填充

- forward process:
- reverse process:
- training target:
- inference cost:
- 和 Diffusion Policy 的连接:
