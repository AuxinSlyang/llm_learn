---
type: reading_map
track: multimodal / VLM / VLA
status: draft
created: 2026-06-09
linked_project: [[so-arm101-lerobot-first-loop]]
---

# Multimodal Model Map

## 一句话

多模态模型的核心不是“把图片和文字硬塞进同一个模型”，而是设计一条稳定路径，让不同模态先变成可对齐、可交互、可生成或可行动的 representation。

## 典型路线

```text
1. Dual encoder alignment
   image encoder + text encoder -> shared embedding space
   代表：CLIP

2. Vision-to-language bridge
   frozen vision encoder -> connector -> frozen LLM -> text generation
   代表：BLIP-2

3. Visual instruction tuning
   vision encoder -> projector -> LLM -> assistant-style response
   代表：LLaVA

4. Vision-language-action
   image/state/task -> VLM/VLA backbone -> action token / action head
   代表：RT-2

5. VLA engineering stack
   data schema -> config -> post-training -> eval -> deployment
   代表：LingBot-VLA / OpenVLA / LeRobot ecosystem
```

## 四个关键问题

### 1. 不同模态怎么表示？

```text
image -> CNN / ViT / vision encoder -> visual features
text  -> tokenizer + Transformer -> text features
audio / state / action -> modality-specific encoder -> features
```

第一步永远是把原始输入变成模型能处理的向量序列或向量。

### 2. 不同模态怎么对齐？

CLIP 代表的是 `alignment`：

```text
image embedding
text embedding
-> contrastive learning
-> matched pairs close, unmatched pairs far
```

它强在 open-vocabulary semantic matching，但不是生成模型。

### 3. 视觉信息怎么进入 LLM？

BLIP-2 / LLaVA 代表的是 `connector`：

```text
vision encoder output
-> Q-Former / projector / resampler / adapter
-> LLM-compatible token embeddings
-> generation
```

这一步把“可匹配的视觉语义”推进到“可被语言模型消费的上下文”。

### 4. 语言输出怎么变成动作？

VLA 代表的是 `action interface`：

```text
image + robot state + task
-> policy / VLA
-> action token / continuous action / action chunk
-> robot runtime
```

对 SO-ARM101 来说，后续重点不是先追模型大小，而是先把 observation / state / action / eval / failure log 记录规范。

## 和当前阅读顺序的关系

```text
CLIP       -> 图文语义对齐
BLIP-2    -> frozen vision encoder 和 frozen LLM 之间的 Q-Former 桥
LLaVA     -> visual instruction tuning
RT-2      -> action-as-token / VLA
LingBot   -> LeRobot-style VLA 工程流程
```

## CV backbone 补课位置

CLIP / BLIP-2 / LLaVA / VLA 都会反复提到 `vision encoder`。这里需要最小 CV 基础：

```text
AlexNet -> VGG -> Inception -> ResNet -> ViT
```

当前只需要理解它们在视觉表征里的角色，不需要马上复现完整 CV 训练。

