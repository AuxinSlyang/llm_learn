---
type: paper_note
title: Diffusion Models for Generative Vision
short_name: Diffusion Models
track: CV foundations / generative vision / robot learning bridge
read_mode: Awareness Scan
status: queued
created: 2026-06-11
---

# Diffusion Models for Generative Vision - QUICK READ

## Position

Diffusion models 是现代视觉生成模型的核心路线之一。它们和 CNN / ViT / CLIP 的位置不同：

```text
CNN / ViT: image -> representation
CLIP / BLIP-2 / LLaVA: image <-> language / multimodal reasoning
Diffusion models: noise -> image, or noisy image -> clean image
Diffusion Policy: noisy action sequence -> action sequence
```

本模块只做 awareness scan，不插队 `CNN -> LeNet-5 -> AlexNet -> ResNet -> ViT -> CLIP` 主线。

## Core Intuition

扩散模型的基本直觉：

```text
training:
clean image -> gradually add noise -> noisy image
model learns: noisy image + timestep -> predict noise / denoise

sampling:
random noise -> repeated denoising -> generated image
```

它不是一次性生成图片，而是通过多步 denoising 从噪声里“还原”出样本。

## Suggested Paper Ladder

| Order | Paper | arXiv | 为什么看 |
|---|---|---|---|
| 1 | Denoising Diffusion Probabilistic Models | `2006.11239` | 现代 DDPM 入口：把图像生成建模成逐步加噪 / 逐步去噪。 |
| 2 | Denoising Diffusion Implicit Models | `2010.02502` | DDIM：理解为什么 diffusion sampling 可以加速，不必死守很长 Markov chain。 |
| 3 | Score-Based Generative Modeling through SDEs | `2011.13456` | score-based / SDE 视角，把 diffusion 和连续时间生成建模统一起来。 |
| 4 | Improved DDPM | `2102.09672` | 改进 likelihood / sample quality / sampling speed 的工程路线。 |
| 5 | Latent Diffusion Models | `2112.10752` | Stable Diffusion 系列关键思想：在 latent space 里做 diffusion，降低高分辨率生成成本。 |
| 6 | Diffusion Policy | `2303.04137` | 机器人桥接：把 action sequence generation 建模成条件扩散。 |

## Official Links

- DDPM: https://arxiv.org/abs/2006.11239
- DDIM: https://arxiv.org/abs/2010.02502
- Score SDE: https://arxiv.org/abs/2011.13456
- Improved DDPM: https://arxiv.org/abs/2102.09672
- Latent Diffusion Models: https://arxiv.org/abs/2112.10752
- Diffusion Policy: https://arxiv.org/abs/2303.04137

## Why For Robot Learning

对当前路线有两层意义：

### 1. Generative vision

理解视觉模型不只可以做 classification / detection / representation，也可以生成、编辑、补全、修复图像。

这对 synthetic data、simulation asset、data augmentation、scene imagination 后续可能有用。

### 2. Action generation

Diffusion Policy 把同样的 denoising 思想迁移到 robot action sequence：

```text
observation + noisy action sequence
-> denoise
-> plausible action sequence
```

这解释了为什么 diffusion 不只是“画图模型”，也能成为机器人策略模型的一类。

## First-pass Scope

第一轮只需要回答：

- 什么是 forward noising / reverse denoising？
- 为什么 diffusion 生成质量强，但推理通常多步、较慢？
- 为什么 Latent Diffusion 要在 latent space 做？
- Diffusion Policy 和图像 diffusion 的共同点是什么？

第一轮不做：

- ELBO / score matching / SDE 公式深挖。
- Stable Diffusion 工程栈细节。
- 训练或复现 diffusion model。

## Current Status

- [ ] DDPM awareness scan
- [ ] LDM awareness scan
- [ ] Diffusion Policy 和 robot action generation 对照
