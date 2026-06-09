---
type: paper_note
title: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
short_name: BLIP-2
arxiv_id: "2301.12597"
url: https://arxiv.org/abs/2301.12597
pdf_url: https://arxiv.org/pdf/2301.12597
local_pdf: ./BLIP_2_Bootstrapping_Language_Image_Pretraining.pdf
track: VLM bridge
read_mode: Mini Scan
status: downloaded
created: 2026-06-08
---

# BLIP-2 - QUICK READ

## Position

BLIP-2 是 `LLM -> VLM` 的桥接论文之一。它的核心不是从零训练一个巨大多模态模型，而是把 frozen image encoder 和 frozen LLM 用一个轻量的 Q-Former 接起来。

```text
frozen image encoder
-> Q-Former / visual query bottleneck
-> frozen LLM
-> text generation
```

## Why Now

我们要理解 VLA，先要理解图像如何进入语言模型。BLIP-2 的价值是把 `vision encoder / connector / LLM` 这个模块化结构讲得很清楚。

## Tonight's Scan Questions

- 为什么 frozen image encoder + frozen LLM 之间需要 Q-Former？
- Q-Former 输出的是怎样的视觉表示？
- 两阶段 pre-training 分别解决什么问题？
- 这种结构离机器人动作输出还差什么？

## Rough Takeaway

BLIP-2 的关键是用一个小模块补上模态鸿沟：图像编码器擅长视觉，LLM 擅长语言生成，中间的 Q-Former 负责把视觉信息整理成 LLM 能消费的形式。

## 2026-06-09 Reading Entry

### 它解决什么问题

从零端到端训练大规模 VLM 很贵。BLIP-2 的思路是复用两个现成强模块：

```text
frozen pre-trained image encoder
frozen large language model
```

然后只训练中间的轻量桥接模块 `Q-Former`，把视觉特征变成 LLM 能消费的表示。

### 和 CLIP 的差异

```text
CLIP:
image encoder + text encoder
-> image/text embedding matching
-> no generation

BLIP-2:
frozen image encoder + Q-Former + frozen LLM
-> image-to-text generation
```

### Q-Former 的直觉

Q-Former 可以先粗略理解成一组 learnable queries 去“询问” frozen image encoder 的 visual features，抽取少量、紧凑、和语言相关的 visual tokens。

```text
visual features
<- cross-attention from learnable query tokens
query outputs
-> projected into LLM input space
```

它的意义是避免把整张图的所有视觉 patch 直接塞给 LLM，而是用一个小模块完成视觉信息压缩和对齐。

### 两阶段训练

```text
Stage 1: vision-language representation learning
frozen image encoder + train Q-Former
目标：让 Q-Former 学会从图像特征中抽取和文本相关的视觉表示

Stage 2: vision-to-language generative learning
frozen LLM + train Q-Former / projection
目标：让 Q-Former 输出能作为 LLM 的 visual prompt，支持 caption / VQA / instruction-like generation
```

### 对 VLA 的启发

后续 VLA 也会反复出现这个结构：

```text
frozen or pre-trained perception backbone
-> trainable connector / adapter
-> language or policy backbone
-> output text / action
```

所以 BLIP-2 最值得学的不是 benchmark，而是 `frozen backbones + connector` 这个工程范式。

## Bridge To Robotics

后续看 VLA 时要盯住同一个位置：

```text
vision/state/task
-> connector / adapter
-> language backbone
-> action head / action tokens
```

BLIP-2 还没有 action；它只说明 image-to-language bridge。

## Tomorrow / Later

- 读 abstract、intro、Fig. 1/2、Q-Former 设计。
- 暂时跳过完整 benchmark 表。
