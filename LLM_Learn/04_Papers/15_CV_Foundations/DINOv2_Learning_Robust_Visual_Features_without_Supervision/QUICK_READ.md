---
type: paper_note
paper: DINOv2: Learning Robust Visual Features without Supervision
short_name: DINOv2
arxiv_id: "2304.07193"
url: https://arxiv.org/abs/2304.07193
pdf_url: https://arxiv.org/pdf/2304.07193
local_pdf: ./DINOv2_Learning_Robust_Visual_Features_without_Supervision.pdf
authors: Maxime Oquab et al.
status: pdf_downloaded
track: CV foundation / OpenVLA visual encoder support
---

# QUICK_READ - DINOv2

## Why Now

OpenVLA 使用 DINOv2 + SigLIP fused visual encoder。DINOv2 这一侧主要用于理解 robust visual features、空间结构、局部细节和 dense visual representation 为什么对机器人控制有价值。

## Read Questions

- DINOv2 的 self-supervised visual representation 和 supervised ImageNet / CLIP-style representation 有什么差异？
- 它为什么能作为 all-purpose visual feature？
- 它对 robot observation 的帮助更接近 semantic recognition，还是 spatial / dense feature？
- OpenVLA 为什么要把 DINOv2 和 SigLIP 拼起来，而不是只用一个 visual encoder？

## OpenVLA Connection

```text
camera image
-> DINOv2 spatial / dense visual features
-> concatenate with SigLIP semantic / language-aligned features
-> projector
-> Llama 2
-> action tokens
```

## Status

- PDF downloaded.
- 后续读法：Structured Quick Read，只看 abstract / intro / method overview / representation claim，不深挖所有 benchmark。
