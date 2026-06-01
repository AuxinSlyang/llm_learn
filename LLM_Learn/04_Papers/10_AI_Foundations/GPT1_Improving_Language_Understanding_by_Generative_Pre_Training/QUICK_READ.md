---
type: paper_note
title: Improving Language Understanding by Generative Pre-Training
category: 10_AI_Foundations
status: queue
read_mode: Quick Read
phase: 2026-05 / GPT lineage
source_url: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
local_pdf: GPT1_Improving_Language_Understanding_by_Generative_Pre_Training.pdf
---

# GPT-1 - Improving Language Understanding by Generative Pre-Training

## 为什么现在读

- 这是 GPT 路线的起点：decoder-only Transformer + generative pre-training + supervised fine-tuning。
- 当前只通读设计思想，不追完整 benchmark 细节。

## 今日导读问题

1. 为什么用语言模型预训练来做 NLU？
2. 为什么选择 Transformer decoder / left-to-right LM？
3. 预训练目标和下游微调目标如何衔接？
4. 它和原始 Transformer encoder-decoder 结构删改了哪些部分？

## 今日最低产出

- 写清 `unlabeled text -> LM pretraining -> task-specific fine-tuning` 主链路。
- 写清 GPT-1 如何把 Transformer 从翻译架构改造成通用语言理解预训练架构。

## 通读 Takeaway

- 一句话：用 **decoder-only Transformer** 做 **left-to-right language modeling** 的生成式预训练（BooksCorpus），再用 **最小架构改动** 在各个 NLU 任务上做判别式微调，证明“预训练 + 微调”可以替代大量任务专用结构。
- 两段式训练范式：
  - Unsupervised pre-training：语言模型目标在大规模无标注文本上学通用表示
  - Supervised fine-tuning：在下游任务上用对应监督目标微调
- 关键工程设计：**task-aware input transformations**
  - 把不同任务的输入（单句/句对/多选 QA 等）统一转成“一个连续 token 序列”（必要时加分隔 token）
  - 输出端尽量复用同一模型主体，只换很薄的 task head
- 模型规格（用于建立直觉，而非背参数）：12-layer decoder-only Transformer、masked self-attention、768 hidden、12 heads；BPE（40k merges）；训练序列长度 512；Adam，max lr 2.5e-4（细节见 paper 的 setup 段落）。
- 你应该带走的主线：**Transformer（decoder-only）+ next-token LM objective** 能学到足够通用的语言表示；“怎么把任务输入拼成序列”是微调能否有效迁移的关键杠杆之一。

## 核心 idea（给 nanoGPT/推理系统的连接）

- GPT-1 视角里，NLU 不一定要从“判别式特征工程/专用结构”开始：先把 LM 预训练做强，再把任务当作“在同一模型上加一个薄壳”。
- “任务统一成 token 序列”这个动作，和后续 serving/runtime 的现实是强绑定的：最终都回到 **prompt -> tokens -> forward -> logits** 这条链路，只是 downstream head 不同。

## 完整流程总结

- 核心贡献：不是发明 Transformer，而是把 `large-scale LM pre-training -> task-specific fine-tuning` 这条路线系统化验证出来。
- 模型主体：`token embedding + position embedding -> 12-layer decoder-only Transformer -> hidden states`。
- 预训练阶段：
  - 数据：BooksCorpus 这类大规模无标注连续文本。
  - 目标：left-to-right language modeling，给前文预测下一个 token。
  - 输出：`hidden state -> LM head -> vocab logits -> next-token cross entropy`。
  - 更新：GPT 主体参数 + LM head。
- 微调阶段：
  - 数据：具体任务的有标注样本，例如文本蕴含、问答、相似度、分类。
  - 输入：把结构化任务输入改写成一段 token sequence，例如 `premise <delimiter> hypothesis`。
  - 输出：`final hidden state -> task head -> label logits -> supervised cross entropy`。
  - 更新：task head + GPT 主体；同时保留一个辅助 LM loss。
- 一句话 takeaway：GPT-1 证明了“会做 next-token prediction 的 decoder-only Transformer”不只是会续写，它的 hidden states 可以通过少量监督微调迁移到多种语言理解任务。

## Supervised fine-tuning 怎么求解

- 有标注数据集记作 `C`，每条样本包含输入 token 序列 `x1...xm` 和标签 `y`。
- 把 `x1...xm` 输入预训练好的 GPT，取最后一层最后位置的 hidden state `h_m`。
- 在 `h_m` 后面加一个线性分类头 `W_y`，用 softmax 得到 `P(y | x1...xm)`。
- 监督目标是最大化所有标注样本的 log likelihood：让正确标签的概率变大。
- 论文还在 fine-tuning 时加入辅助 LM objective：`task loss + λ * language modeling loss`，用于改善泛化和加速收敛；实验中 `λ=0.5`。
- 额外参数很少：主要是任务输出头 `W_y` 和 delimiter token embedding；Transformer 主体继续参与微调。

## Task input transformation

- 文本分类：输入文本可直接送入 GPT，再接 classifier。
- 文本蕴含：`premise <delimiter> hypothesis -> label`。
- 相似度：两个句子没有天然顺序，所以两种顺序都跑一遍，再合并表示。
- 多选问答：`context <delimiter> question <delimiter> answer_candidate`，每个候选答案独立打分，再对候选答案做 softmax。

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-05-27 | Quick Read | planned | GPT 设计演化第一站：预训练 + 微调 |
