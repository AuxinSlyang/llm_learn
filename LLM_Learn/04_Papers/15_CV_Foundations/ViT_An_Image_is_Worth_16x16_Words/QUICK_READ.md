---
type: paper_note
title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
short_name: ViT
arxiv_id: "2010.11929"
url: https://arxiv.org/abs/2010.11929
pdf_url: https://arxiv.org/pdf/2010.11929
local_pdf: ./ViT_An_Image_is_Worth_16x16_Words.pdf
track: CV foundation
read_mode: Structured Read
status: queued_for_2026_W25
created: 2026-06-09
---

# ViT - QUICK READ

## Position

ViT 把图片切成 patch，把 patch 当成 token，用 Transformer encoder 做图像分类。CLIP / BLIP-2 / LLaVA 这类模型经常使用 ViT 系视觉编码器。

## Core Question

Transformer 能不能少用 CNN inductive bias，直接在图像 patch 序列上学习视觉表征？

## Key Idea

```text
image
-> split into 16x16 patches
-> patch embeddings + position embeddings
-> Transformer encoder
-> image representation
```

ViT 的重点不是“图片天然就是语言”，而是把图像转成 token sequence 后，可以复用 Transformer 的序列建模能力。

## Why For VLM/VLA

多模态模型经常需要把 visual tokens 接到 language tokens / connector 上。ViT 是理解 `visual token` 的最直接入口。

近期建议结构化读：patch embedding / class token / position embedding / scaling with data。

## 2026-06-11 Preview Focus

今天先不把 ViT 当唯一主槽位；它放在 ResNet 之后做 preview，只回答三个问题，不扩成完整 CV 专项：

- 图像如何被切成 patch，并变成类似 token sequence 的输入？
- Transformer attention 从文本迁移到视觉时，少了哪些 CNN inductive bias，又换来了什么 scaling / representation 能力？
- 对后续 `camera image -> visual tokens -> VLM/VLA/policy` 有什么直接启发？

preview 最低输出：

- [ ] 一句话解释 `image patch as token`。
- [ ] 一句话解释 `ViT` 和 `ResNet` 的差别。
- [ ] 一句话连接到 `CLIP / BLIP-2 / LLaVA / VLA visual encoder`。

## 2026-W25 Reading Target

本周把 ViT 作为休息日 paper sprint 的硬目标之一，但不让它抢 `SO-ARM101 + LeRobot` 首闭环。

### Must Answer

- 图像如何被切成 fixed-size patches，并通过 linear projection 变成 patch embeddings？
- `class token` 和 `position embedding` 分别解决什么问题？
- ViT 相比 ResNet 少了哪些 CNN inductive bias，又为什么需要更大的数据规模？
- 为什么 ViT 是理解 CLIP / BLIP-2 / LLaVA / VLA visual encoder 的入口？
- 对 SO-ARM101 来说，`camera image -> visual tokens -> policy/VLA` 这条链路如何落到 observation schema？

### Output

- 3-5 条 structured takeaway。
- 一段 `ResNet -> ViT -> CLIP/VLA visual encoder` 桥接说明。
- 一句和 LeRobot 数据字段的连接：`observation.images.<camera>` 后续如何进入视觉 encoder。
