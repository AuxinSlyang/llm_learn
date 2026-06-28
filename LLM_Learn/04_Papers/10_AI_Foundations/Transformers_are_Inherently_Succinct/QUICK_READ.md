---
type: paper_note
title: Transformers are Inherently Succinct
short_name: Transformer Succinctness
arxiv_id: "2510.19315"
url: https://arxiv.org/abs/2510.19315
pdf_url: https://arxiv.org/pdf/2510.19315
openreview: https://openreview.net/forum?id=Yxz92UuPLQ
local_pdf: ./Transformers_are_Inherently_Succinct.pdf
authors: Pascal Bergstrasser; Ryan Cotterell; Anthony W. Lin
submitted: 2025-10-22
last_revised: 2026-05-15
subjects: Formal Languages and Automata Theory (cs.FL); Machine Learning (cs.LG); Logic in Computer Science (cs.LO)
venue: ICLR 2026
award: ICLR 2026 Outstanding Paper
track: AI foundations / transformer theory / expressivity
read_mode: Theory Scan
status: selected_for_2026-06-23
created: 2026-06-11
---

# Transformers are Inherently Succinct QUICK_READ

## 为什么放进来

这篇是 `ICLR 2026 Outstanding Paper / Oral`，适合作为 Transformer 理论支撑线阅读。

它不改变当前主线：`SO-ARM101 + LeRobot` 首闭环仍优先。后续读它只回答一个问题：

```text
Transformer 为什么能用很紧凑的结构表达某些复杂模式？
这种“succinctness”如何帮助理解 attention 架构为什么能迁移到语言、视觉、轨迹、动作和机器人状态？
```

## 元信息

- Paper：`Transformers are Inherently Succinct`
- Authors：Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- arXiv：`2510.19315`
- arXiv URL：`https://arxiv.org/abs/2510.19315`
- PDF：`https://arxiv.org/pdf/2510.19315`
- OpenReview：`https://openreview.net/forum?id=Yxz92UuPLQ`
- Local PDF：`./Transformers_are_Inherently_Succinct.pdf`
- Venue：`ICLR 2026`
- Submitted：`2025-10-22`
- Last revised：`2026-05-15` (`v3`)
- Subjects：`Formal Languages and Automata Theory (cs.FL); Machine Learning (cs.LG); Logic in Computer Science (cs.LO)`
- Official arXiv metadata：`https://arxiv.org/abs/2510.19315`

## Official arXiv Abstract Summary

论文把 `succinctness` 作为 Transformer 表达能力的度量：不是只问能不能表达某类语言，而是问同样语言是否能用更小的模型描述。官方 arXiv 摘要给出的主张是：fixed-precision Transformer 对某些形式语言可以比 LTL、RNN / SSM、finite automata 更紧凑；这种紧凑性也带来 verification 难度，例如 emptiness / equivalence 这类问题达到很高复杂度。

## 当前定位

这不是一篇工程论文，也不是常规 mechanistic interpretability 论文。它更像是：

```text
Transformer theory / expressivity
-> succinctness
-> formal languages / automata / LTL / RNN comparison
-> verification complexity
```

第一轮不追证明细节，只建立概念地图。

## 预期 takeaway

- 论文用 `succinctness` 衡量表达能力：不是问 Transformer 能不能表达某类语言，而是问它能否比其他形式系统用更小描述表达同一类模式。
- 论文主张 fixed-precision Transformer 可以比 LTL、RNN / state-space models、finite automata 更紧凑地表达某些形式语言。
- 这解释了一个直觉：attention 不只是 NLP 技巧，而是一种可以在 token 集合上做紧凑信息路由和模式组合的通用计算结构。
- 代价是形式验证可能很难；论文提到相关验证问题达到 `EXPSPACE-complete`。

## 阅读问题

- [ ] `succinctness` 和普通 `expressivity` 有什么区别？
- [ ] 为什么论文选择 finite automata、LTL、RNN / state-space models 作为比较对象？
- [ ] fixed-precision Transformer 在理论上限制了什么，又为什么更贴近现实硬件？
- [ ] 论文里的“更紧凑”是否等价于“更容易训练”？如果不是，差别在哪里？
- [ ] 对 `attention 可迁移到视觉 / action / trajectory / robot state` 的启发是什么？

## 和当前路线的连接

- 对 LLM/nanoGPT：帮助解释为什么 `token -> attention routing -> FFN composition` 可以成为通用序列建模骨架。
- 对 ViT/VLA：如果 image patches、robot states、action chunks 都 token 化，attention 的紧凑组合能力可以迁移到非文本结构。
- 对 robot runtime：这篇不直接给工程方案，但提醒我们不要只把 Transformer 当“大模型里的文本模块”；它更像一种通用 token 计算架构。
- 对可解释性：succinctness 不等于可解释性。表达很紧凑的模型可能更难验证、更难解释；后续要和 `Vision Transformers Need Registers` 分开读。

## 建议读法

第一轮 30-60m：

1. 读 Abstract / Introduction，只抓 `succinctness` 和比较对象。
2. 看 main theorem statements，不追完整证明。
3. 找出作者如何连接 fixed-precision transformers、automata、LTL、RNN。
4. 写一句：它如何改变我对 attention 可迁移性的理解。

暂不做：

- 不深挖所有 proof。
- 不展开成形式语言专项。
- 不让它抢掉 SO-ARM101 bring-up / LLM phase 1 closure。

## 当前状态

- [x] PDF 已下载到本地
- [x] Quick read note 已创建
- [x] 2026-06-23 已提升为今日 theory scan 主槽
- [ ] 读完后写一句 mini-stack connection

## 2026-06-23 优先级校准

今天把它设为理论主读，因为它才是 ICLR 2026 Outstanding Paper；`Transformer Is Inherently a Causal Learner` 保留为 causal / world-model radar。

本轮只读：

1. `succinctness` 和普通 `expressivity` 的区别。
2. 为什么 fixed-precision Transformer 可以比 LTL、RNN / SSM、finite automata 更紧凑。
3. 为什么这种紧凑表达能力会让 verification 变得困难。
4. 这对 `tokenized vision / action chunk / robot trajectory` 的启发是什么。
