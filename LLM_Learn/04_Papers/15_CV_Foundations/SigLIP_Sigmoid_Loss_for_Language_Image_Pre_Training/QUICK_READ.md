---
type: paper_note
paper: Sigmoid Loss for Language Image Pre-Training
short_name: SigLIP
arxiv_id: "2303.15343"
url: https://arxiv.org/abs/2303.15343
pdf_url: https://arxiv.org/pdf/2303.15343
local_pdf: ./SigLIP_Sigmoid_Loss_for_Language_Image_Pre_Training.pdf
authors: Xiaohua Zhai; Basil Mustafa; Alexander Kolesnikov; Lucas Beyer
status: pdf_downloaded
track: CV foundation / OpenVLA visual encoder support
---

# QUICK_READ - SigLIP

## Why Now

OpenVLA 使用 DINOv2 + SigLIP fused visual encoder。SigLIP 这一侧主要用于理解 image-text alignment、language grounding 和 open-vocabulary semantic visual features 为什么对 VLA 有价值。

## Read Questions

- SigLIP 和 CLIP 都做 image-text pretraining，它把 loss 从 softmax contrastive loss 改成 sigmoid pairwise loss，核心收益是什么？
- SigLIP 解决的是视觉语义对齐问题，还是机器人动作控制问题？
- 对 OpenVLA 来说，SigLIP 提供的是哪类 visual feature？
- 为什么 language instruction grounding 需要这类 image-text aligned encoder？

## OpenVLA Connection

```text
camera image + language instruction
-> SigLIP semantic / language-aligned visual features
-> concatenate with DINOv2 spatial / dense visual features
-> projector
-> Llama 2
-> action tokens
```

## Status

- PDF downloaded.
- 后续读法：Structured Quick Read，只看 abstract / intro / loss intuition / representation claim，不深挖所有 benchmark。
