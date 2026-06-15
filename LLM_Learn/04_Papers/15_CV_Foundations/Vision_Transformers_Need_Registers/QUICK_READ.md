---
type: paper_note
title: Vision Transformers Need Registers
short_name: ViT Registers
arxiv_id: "2309.16588"
url: https://arxiv.org/abs/2309.16588
pdf_url: https://arxiv.org/pdf/2309.16588
openreview: https://openreview.net/forum?id=2dnO3LLiJ1
local_pdf: ./Vision_Transformers_Need_Registers.pdf
venue: ICLR 2024
award: ICLR 2024 Outstanding Paper
track: CV foundations / transformer interpretability / VLM-VLA support
read_mode: Follow-up Quick Read
status: queued
created: 2026-06-11
---

# Vision Transformers Need Registers QUICK_READ

## 为什么放进来

这篇是 `ICLR 2024 Outstanding Paper`，适合作为 `Transformer attention / interpretability / visual tokens` 的支撑线阅读。

它不改变当前主线：`SO-ARM101 + LeRobot` 首闭环仍优先。后续阅读时只回答一个问题：

```text
Transformer attention map 到底能不能解释模型？
如果不能，register tokens 暴露了什么内部计算机制？
这对 robot observation / visual tokens / VLA 有什么启发？
```

## 元信息

- Paper：`Vision Transformers Need Registers`
- Authors：Timothee Darcet, Maxime Oquab, Julien Mairal, Piotr Bojanowski
- arXiv：`2309.16588`
- arXiv URL：`https://arxiv.org/abs/2309.16588`
- PDF：`https://arxiv.org/pdf/2309.16588`
- OpenReview：`https://openreview.net/forum?id=2dnO3LLiJ1`
- Local PDF：`./Vision_Transformers_Need_Registers.pdf`

## 预期 takeaway

- ViT 的 attention / feature maps 中可能出现高范数 artifact tokens，尤其出现在低信息背景区域。
- 这些 token 可能被模型复用为内部计算空间，而不是直接代表图像语义。
- 加入额外 learnable register tokens 可以给模型一个显式“内部工作区”，从而改善 feature map / attention map 的可读性和下游 dense prediction 表现。

## 阅读问题

- [ ] 什么是 high-norm artifact token？
- [ ] 为什么 artifact 往往出现在低信息背景区域？
- [ ] register token 和 `[CLS] token` / patch token 的职责区别是什么？
- [ ] 为什么 attention map 不能直接等价为解释？
- [ ] 对 `camera image -> visual tokens -> policy / VLA` 有什么启发？

## 和当前项目的连接

- SO-ARM101 第一阶段会从 `camera image` 得到 visual observation；后续不应天真把 attention heatmap 当成可靠解释。
- 对 VLA / robot policy 来说，Transformer token 可以表示 patch、state、action chunk、object slot、language instruction；attention 是信息路由机制，不天然保证语义可解释。
- 如果后续做 robot visual encoder / VLA runtime 解释，应该关注 token 表征、干预、ablation 和 failure case，而不是只看 attention visualization。

## 当前状态

- [x] PDF 已下载到本地
- [x] Quick read note 已创建
- [ ] 后续安排 30-45m quick read
- [ ] 读完后写一句 mini-stack connection
