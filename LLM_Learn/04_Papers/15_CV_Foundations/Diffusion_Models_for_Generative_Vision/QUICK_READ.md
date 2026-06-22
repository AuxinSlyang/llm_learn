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

本模块只做 awareness scan，不插队 `CNN -> LeNet-5 -> AlexNet -> ResNet -> ViT -> CLIP` 主线。Diffusion 后续统一追踪入口见：`../../25_Diffusion_Flow_and_Action_Generation/README.md`。

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

## 2026-06-18 校准：Diffusion / Flow 作为 VLA Action Generation 支撑线

用户校准：除了 LoRA / QLoRA / vLLM / DeepSeek-R1 / FlashAttention 这条 LLM 工程线，也要把 diffusion 系列经典论文纳入后续分析。这里不新开完整 diffusion 专题，先作为 `pi0 / Diffusion Policy / robot action generation` 的支撑线。

### 推荐第一轮顺序

| 顺序 | 材料 | 读法 | 只回答什么 |
|---|---|---|---|
| 1 | DDPM | 30-45m awareness | forward noising / reverse denoising 是什么，为什么可以从 noise 生成样本 |
| 2 | DDIM | 20-30m scan | 为什么 sampling 可以更快，为什么不必严格按长 Markov chain |
| 3 | Score SDE | 30-45m awareness | score / continuous-time / SDE 视角如何统一 diffusion |
| 4 | Flow Matching / Rectified Flow 方向 | 30-45m bridge | 为什么 pi0 会用 flow matching action expert；它和 diffusion denoising 有什么关系 |
| 5 | Latent Diffusion | 30-45m awareness | 为什么在 latent space 做 diffusion 更工程可行，和 Stable Diffusion 的关系 |
| 6 | Diffusion Policy | structured read | 如何把 `observation + noisy action sequence -> denoised action sequence` 用作 robot policy |

### 和当前 VLA 主线的关系

```text
OpenVLA / RT-2:
  action-as-token / language-model-style output

pi0:
  VLM backbone + flow matching action expert

pi0-FAST:
  continuous action sequence -> action tokens

Diffusion Policy:
  observation-conditioned action sequence denoising
```

第一轮目标不是推公式，而是能解释三种 action generation 表达：

- tokenized action：把 action 当成 token 预测。
- diffusion action：从 noisy action sequence 逐步去噪。
- flow action：学习从简单分布到 action distribution 的连续变换路径。

### 暂不做

- 不训练 Stable Diffusion。
- 不复现 DDPM / DDIM。
- 不深挖 ELBO、SDE 推导、score matching 公式细节。
- 不让 diffusion 抢 `OpenVLA / pi0 / pi0-FAST / LeRobot` 当前阅读主线。

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
