---
type: paper_note
title: Learning Transferable Visual Models From Natural Language Supervision
short_name: CLIP
arxiv_id: "2103.00020"
url: https://arxiv.org/abs/2103.00020
pdf_url: https://arxiv.org/pdf/2103.00020
local_pdf: ./CLIP_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision.pdf
track: VLM foundation
read_mode: Mini Scan
status: downloaded
created: 2026-06-08
---

# CLIP - QUICK READ

## Position

CLIP 是这条线的第一块地基：它不直接把图像塞进 LLM 里生成文本，而是用大规模 image-text pairs 学出一个共享语义空间，让 image encoder 和 text encoder 的表示能对齐。

在 `LLM -> VLM -> VLA` 链条里，CLIP 回答的是：

```text
image representation <-> text representation
```

## Why Now

我们后面读 BLIP-2、LLaVA、RT-2、LingBot-VLA 时，会反复看到 `vision encoder`、`image-text alignment`、`visual token`、`projector/adapter`。CLIP 负责建立最小直觉：图像不是天然能被语言模型理解，必须先有一种跨模态对齐方式。

## Tonight's Scan Questions

- 图像和文字如何被放到同一个语义空间？
- contrastive learning 在这里到底预测什么？
- zero-shot image classification 为什么可以从自然语言 prompt 得到？
- CLIP 缺什么，导致它还不是 VLM chat，也不是 VLA？

## Rough Takeaway

CLIP 的核心不是机器人动作，而是 `image-text alignment`。它让模型能把图像和语言概念对齐，但它本身不解决多轮对话、复杂推理和动作输出。

## 2026-06-09 Reading Notes

今天读到 abstract / introduction / method framing，先不继续展开实验。

### 核心理解

- 传统视觉模型多数是固定 label space：`image -> fixed class id`。
- CLIP 把监督空间换成开放的 natural language space：`image embedding <-> text embedding`。
- natural language 提供开放概念表达能力，contrastive learning 负责把图像表示训练到能和文本表示比较的位置。
- CLIP 不是 `image -> text generation`，而是 `image-text matching / alignment`。
- ResNet / ViT 都只是 image encoder 选项；重点是 image encoder 和 text Transformer 输出到同一个 embedding space。

### Method 粗框架

```text
image -> ResNet / ViT -> image feature -> projection -> image embedding
text  -> Transformer -> text feature -> projection -> text embedding

similarity = image_embeddings @ text_embeddings.T
loss = symmetric cross entropy(image->text, text->image)
```

batch 里 `N` 个图文 pair 会形成 `N x N` 相似度矩阵。对角线是真实匹配，非对角线是 batch 内负样本。

### 和后续论文的连接

- CLIP：图文语义对齐，不能生成回答。
- BLIP-2 / LLaVA：把视觉表示接入 LLM，开始生成/对话。
- RT-2：把输出从 text response 推到 action-as-token / VLA。
- LingBot-VLA：把 VLA 变成 LeRobot-style data/config/eval/deploy 工程流程。

### 明天继续

- 早上 1 小时只粗扫 BLIP-2 / LLaVA / RT-2 / LingBot-VLA。
- 重点问题：`image embedding` 如何进入 LLM？`text output` 如何进一步变成 `action output`？

## Bridge To Robotics

对 SO-ARM101 第一阶段，它不直接可用；但未来任何 VLA/VLM policy 里的视觉前端，都绕不开“视觉表征如何对齐语言任务”的问题。

```text
camera image
-> vision encoder
-> aligned visual representation
-> VLM/VLA policy
```

## Tomorrow / Later

- CLIP 当前只需要保留 abstract、intro、method 图和 contrastive objective。
- 不需要深挖 400M 数据、所有 benchmark、模型 scaling 细节。
