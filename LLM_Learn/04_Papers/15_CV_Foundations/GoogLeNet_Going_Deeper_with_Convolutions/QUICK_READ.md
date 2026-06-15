---
type: paper_note
title: Going Deeper with Convolutions
short_name: GoogLeNet / Inception
arxiv_id: "1409.4842"
url: https://arxiv.org/abs/1409.4842
pdf_url: https://arxiv.org/pdf/1409.4842
local_pdf: ./GoogLeNet_Going_Deeper_with_Convolutions.pdf
track: CV foundation
read_mode: Background Scan
status: downloaded
created: 2026-06-09
---

# GoogLeNet / Inception - QUICK READ

## Position

GoogLeNet / Inception 关注的是在可控计算量下做更深、更宽的卷积网络，并用多尺度分支捕获不同尺度的视觉特征。

## Key Ideas

- Inception module：并行使用不同卷积核 / pooling 分支，再 concat。
- 用 `1x1` convolution 降维，控制计算成本。
- 视觉 backbone 不只是堆深，也要考虑计算效率。

## Why For VLM/VLA

对机器人 runtime 来说，视觉 encoder 的计算成本很重要。Inception 这条线可以作为效率意识的背景。

