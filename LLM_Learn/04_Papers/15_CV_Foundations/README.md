---
type: reading_index
track: CV foundations for VLM/VLA
status: draft
created: 2026-06-09
---

# 15 CV Foundations

本目录只服务 VLM / VLA 的视觉 backbone 补课，不把当前主线切换成完整 CV 专项。

当前执行计划：[[CV_Foundation_Sprint_2026-W24]]

## 最小阅读顺序

| Order | Paper | Why |
|---|---|---|
| 0 | CNN Primer | 先理解 convolution、locality、weight sharing、feature map、pooling |
| 1 | LeNet-5 | 早期 CNN 完整形态：convolution + subsampling + classifier |
| 2 | AlexNet | 现代深度 CNN 在 ImageNet 上的起点 |
| 3 | VGG | 用小卷积堆深度，理解 depth 对视觉表征的影响 |
| 4 | GoogLeNet / Inception | 多尺度卷积和计算效率 |
| 5 | ResNet | residual connection，现代视觉 backbone 的核心基础 |
| 6 | ViT | 把 image patches 当 token，用 Transformer 做视觉表征 |
| 7 | Vision Transformers Need Registers | 理解 ViT attention / feature map artifact，以及 attention visualization 的解释边界 |

## 当前读法

- `2026-06-11` 升级：硬件工具未到的等待期可以完整读一轮代表性 CV foundation 论文，但限定为 `AlexNet -> VGG -> Inception -> ResNet -> ViT -> Registers -> CLIP/BLIP-2/LLaVA`，目标是快速理解视觉 backbone、visual token、image-text alignment 和 attention interpretability。
- `2026-06-11` 补充：AlexNet 前先看 `00_CNN_Primer.md` 和 LeNet-5，用 30-45m 搞清 CNN 的基本语法和早期完整架构，再进入 ImageNet 时代。
- `2026-06-11` 校准：如果 CV 基础薄，不直接从 `ViT` 精读开始；先用 10-15m 看 `AlexNet` 背景，再用 `ResNet` 建立 CNN backbone / residual connection 直觉，最后再读 `ViT` 的 patch-as-token 和 attention 迁移。
- `ResNet` 和 `ViT` 是近期必读，因为 CLIP/BLIP-2/LLaVA 都会反复使用 CNN/ViT 视觉编码器。
- `Vision Transformers Need Registers` 是后续 30-45m 支撑线阅读，用来校准 attention map / visual token 的可解释性，不抢 SO-ARM101 bring-up 主线。
- `AlexNet / VGG / Inception` 只做背景扫读，帮助理解 ResNet 为什么重要。
- 不进入 detection / segmentation / self-supervised vision 细节；这些后续按项目需要补。

## 和 VLM/VLA 的连接

```text
camera image
-> CV backbone / vision encoder
-> visual features
-> connector / projector / Q-Former
-> LLM / VLA / policy
```

所以这里读 CV，不是为了做传统图像分类，而是为了理解“视觉特征从哪里来、形状是什么、为什么能被接到多模态模型里”。
