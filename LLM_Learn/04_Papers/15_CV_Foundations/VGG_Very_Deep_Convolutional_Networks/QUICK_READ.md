---
type: paper_note
title: Very Deep Convolutional Networks for Large-Scale Image Recognition
short_name: VGG
arxiv_id: "1409.1556"
url: https://arxiv.org/abs/1409.1556
pdf_url: https://arxiv.org/pdf/1409.1556
local_pdf: ./VGG_Very_Deep_Convolutional_Networks.pdf
track: CV foundation
read_mode: Background Structured Scan
status: quick_read_done
created: 2026-06-09
started: 2026-06-14
completed: 2026-06-14
---

# VGG - QUICK READ

## Position

VGG 的核心是用很多小的 `3x3` convolution 堆出更深的网络，展示 depth 对视觉表征的重要性。

## Key Ideas

- 小卷积核堆叠可以扩大 receptive field，同时保留简洁结构。
- 网络更深通常带来更强视觉表征，但训练难度也上升。

## Why For VLM/VLA

VGG 帮助理解 CNN backbone 的基本层级结构：从低级边缘纹理到高级语义特征。近期只需扫读。

## 2026-06-14 Structured Quick Read 收尾

### One-sentence takeaway

VGG 用统一的 `3x3 conv` stack 证明了 `depth matters`：在可控的 CNN architecture family 里，把网络加深到 16-19 个 weight layers 能显著提升 ImageNet 表征质量。

### Abstract / Introduction

- 本文要研究的是 ConvNet depth 对 large-scale image recognition accuracy 的影响。
- AlexNet 之后已有很多改进，例如 smaller first-layer receptive field、dense testing、multi-scale testing；VGG 把问题收窄到 architecture depth。
- 关键设计判断：固定大多数架构变量，逐步增加 depth，用小 `3x3` filters 让深度增加变得参数可控。

### Architecture / Configurations

- 所有配置共享统一模板：`224x224 RGB -> repeated conv3 + ReLU -> 5x maxpool -> FC-4096 -> FC-4096 -> FC-1000 -> softmax`。
- `conv3-64` 表示 `3x3` kernel、64 个输出 channels；同一层多个 filters 增加 channels，不扩大单点 receptive field。
- receptive field 主要由连续多层 conv 和 pooling 累积扩大：三个连续 `3x3 conv` 可形成约 `7x7` effective receptive field。
- A-E 是 controlled comparison：
  - A：11 weight layers，baseline。
  - A-LRN：测试 AlexNet 风格 LRN 是否有用。
  - B：13 layers，增加 depth。
  - C：16 layers，加入 `1x1 conv`，增加 non-linearity 但不扩大 spatial receptive field。
  - D：16 layers，全部用 `3x3 conv`，即常见 VGG-16。
  - E：19 layers，即常见 VGG-19。

### Training / Testing Framework

- Training 是标准 supervised classification：resize 到 training scale `S`，random crop `224x224`，flip / RGB shift，softmax + cross entropy，SGD + momentum。
- `scale jittering` 是训练时随机采样 `S in [256, 512]`，让模型见到不同尺度的物体。
- Testing 里的 `Q` 是 test scale，可与训练 scale `S` 不同。
- `multi-crop evaluation`：显式裁多个 `224x224` crops，每个 crop 独立跑原始 VGG，最后平均 softmax outputs。
- `dense evaluation`：把 FC 等价改成 conv，整张 resize 图一次前向，得到 `H x W x 1000` score map，再沿空间位置平均成 `1000` 类预测。
- `dense + multi-crop` 是两种 evaluation outputs 的融合，不是只把 crop 输入 dense 模型。

### Experiments

- LRN 没有带来收益，后续深配置不用。
- depth 增加整体降低 error，证明更深的 CNN 表征更强。
- C 优于 B，说明额外 non-linearity 有用；D 优于 C，说明 `3x3` 的 spatial context 比只用 `1x1` 更重要。
- training scale jittering、test-time multi-scale evaluation、dense/multi-crop combination、model ensemble 都能继续提升结果，但它们是辅助技巧。

### Historical Position

```text
LeNet: CNN + backprop 的早期范式
AlexNet: CNN + GPU + ImageNet 的现代起点
VGG: depth matters，小卷积堆叠形成强 visual backbone
ResNet: 解决 plain deep CNN 继续加深后的 optimization / degradation problem
ViT: image patches as tokens，进入 Transformer vision 范式
```

VGG 的价值不是复杂模块，而是把 CV 社区的注意力推向“堆叠简单模块形成深层层级表征”。它自然引出 ResNet：既然 depth 有用，为什么不能继续堆到 50/101/152 层，以及如何让这种深度可训练。

## 2026-06-14 45m Focus

今天只做 `AlexNet -> VGG -> ResNet` 中间桥，不扩成完整 CV 全科。

### 必须回答

- 为什么 VGG 用大量 `3x3 conv`，而不是继续依赖 AlexNet 那种较大的 early kernels？
- 多个 `3x3 conv` 堆叠如何扩大 effective receptive field，同时增加 nonlinearity？
- VGG 证明了 depth 很重要，但为什么也自然暴露出后续 ResNet 要解决的训练难度？

### 45m 读法

- 10m：Abstract / Introduction，只抓 `depth` 和 `small filters`。
- 20m：看 architecture configs，重点理解 repeated `3x3 conv + max-pool`。
- 10m：看 results，只确认 depth 带来的收益，不背表格。
- 5m：写 3 句 takeaway，并停止，回 SO-ARM101 / LeRobot 拼装。
