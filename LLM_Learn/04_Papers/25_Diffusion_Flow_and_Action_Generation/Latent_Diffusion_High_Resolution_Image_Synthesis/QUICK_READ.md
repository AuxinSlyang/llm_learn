---
type: paper_note
title: High-Resolution Image Synthesis with Latent Diffusion Models
short_name: Latent Diffusion
authors:
  - Robin Rombach
  - Andreas Blattmann
  - Dominik Lorenz
  - Patrick Esser
  - Bjorn Ommer
arxiv_id: "2112.10752"
url: https://arxiv.org/abs/2112.10752
pdf_url: https://arxiv.org/pdf/2112.10752
project_page: https://github.com/CompVis/latent-diffusion
local_pdf: ./High_Resolution_Image_Synthesis_with_Latent_Diffusion_Models.pdf
track: latent diffusion / generative vision / engineering efficiency
read_mode: Awareness
status: downloaded
created: 2026-06-28
---

# Latent Diffusion - QUICK READ

## Why now

Latent Diffusion 解释 diffusion 为什么能从理论模型变成工程上可用的大规模图像生成系统。它不是当前机器人动作生成主线，但有助于理解 VLA / perception / generative vision 的工程取舍。

## 本轮只回答

- 为什么 pixel space diffusion 成本高。
- latent space diffusion 如何降低计算量。
- autoencoder / latent representation 在链路中处于什么位置。
- conditioning 如何进入 diffusion。
- 对机器人：是否能类比到 action latent / trajectory latent。

## 一句话预期 takeaway

Latent Diffusion 把 diffusion 从像素空间搬到压缩后的 latent space 中运行，用更低计算成本获得高分辨率生成能力。

## Robot connection

```text
image generation:
  pixel -> latent -> diffusion in latent -> decode image

robot learning analogy:
  high-dimensional observation / trajectory
  -> compact representation
  -> generative policy / planner
```

## 待读后填充

- pixel-space bottleneck:
- latent representation:
- conditioning:
- inference cost:
- VLA / perception connection:
- one_sentence:

