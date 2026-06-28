---
type: paper_note
title: Denoising Diffusion Implicit Models
short_name: DDIM
authors:
  - Jiaming Song
  - Chenlin Meng
  - Stefano Ermon
arxiv_id: "2010.02502"
url: https://arxiv.org/abs/2010.02502
pdf_url: https://arxiv.org/pdf/2010.02502
local_pdf: ./DDIM_Denoising_Diffusion_Implicit_Models.pdf
track: diffusion / sampling acceleration / action generation support
read_mode: Scan
status: downloaded
created: 2026-06-28
---

# DDIM - QUICK READ

## Why now

DDIM 是 DDPM 之后的第一篇加速采样入口。我们读它不是为了完整推导，而是理解：

```text
同样训练目标
-> 是否能用更少 sampling steps 生成样本
-> 这对 robot policy runtime latency 有什么意义
```

## 本轮只回答

- DDPM 为什么采样慢。
- DDIM 如何在不重新训练的情况下改变采样过程。
- deterministic / non-Markovian sampling 的直觉是什么。
- sampling steps 减少后，质量和速度如何 trade off。
- 对 robot action generation：少步采样是否能降低 policy latency。

## 一句话预期 takeaway

DDIM 说明 diffusion 模型不一定只能按原始 DDPM 的长 Markov chain 慢慢采样；在相同训练目标下，可以构造更快的采样过程，用更少 steps 换取实用 latency。

## Robot connection

```text
Diffusion Policy / action diffusion:
  sampling steps too many
  -> policy latency too high
  -> need DDIM-style acceleration or alternative flow/action expert
```

## 待读后填充

- DDPM bottleneck:
- DDIM sampling idea:
- deterministic vs stochastic:
- speed / quality tradeoff:
- policy runtime connection:
- one_sentence:

