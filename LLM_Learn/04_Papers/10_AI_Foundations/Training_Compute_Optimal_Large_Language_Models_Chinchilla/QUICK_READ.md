---
type: paper_note
title: Training Compute-Optimal Large Language Models
category: 10_AI_Foundations
status: queue
read_mode: Quick Read
phase: 2026-05 / post-GPT lineage
source_url: https://arxiv.org/abs/2203.15556
arxiv: 2203.15556
pdf_url: https://arxiv.org/pdf/2203.15556
doi: https://doi.org/10.48550/arXiv.2203.15556
local_pdf: Training_Compute_Optimal_Large_Language_Models.pdf
submitted: 2022-03-29
subjects:
  - cs.CL
  - cs.LG
---

# Training Compute-Optimal Large Language Models (Chinchilla)

## 为什么现在读

- 回答 Scaling Laws 后的修正问题：固定 compute 下，参数和训练 token 应该如何配平。
- 帮助理解现代 LLM 不是单纯参数越大越好，数据量和训练充分性同样关键。
- 阅读顺序上它应该接在 Kaplan Scaling Laws 后面；SFT/RLHF 对应的是下一篇 `Training language models to follow instructions with human feedback`，不应跳过 compute-optimal 这层。

## 接读定位

- Kaplan 2020：建立 `L/N/D/C` 的经验幂律和 compute-optimal 问题框架。
- Chinchilla 2022：重算 fixed compute 下的最优 `N/D` 配比，指出很多大模型是 **undertrained**。
- InstructGPT/RLHF：在预训练 base LM 之后，通过 SFT + reward model + RLHF 改善指令跟随和人类偏好。

## 官方来源记录（2026-05-31）

- arXiv abs: https://arxiv.org/abs/2203.15556
- arXiv PDF: https://arxiv.org/pdf/2203.15556
- DOI: https://doi.org/10.48550/arXiv.2203.15556
- 提交时间：2022-03-29
- 分类：`cs.CL`（Computation and Language），`cs.LG`（Machine Learning）
- 作者：Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre
- 本地 PDF：[Training_Compute_Optimal_Large_Language_Models.pdf](/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Training_Compute_Optimal_Large_Language_Models_Chinchilla/Training_Compute_Optimal_Large_Language_Models.pdf)

## Abstract 快速抓手

- 研究问题：在固定训练 compute 下，Transformer LM 的最优模型参数量和训练 token 数应该如何选择。
- 关键判断：当时很多大模型显著 **undertrained**，原因是模型参数持续变大，但训练数据量没有同步增加。
- 实验规模：训练 400+ 个模型，覆盖约 70M 到 16B+ 参数、5B 到 500B tokens。
- 主要结论：compute-optimal 训练下，模型大小和训练 token 数应该大致等比例增长；模型翻倍时，训练 token 也应翻倍。
- 验证方式：训练 Chinchilla，使用与 Gopher 接近的 compute，但选择 70B 参数并使用约 4 倍更多数据。
- 结果意义：Chinchilla 在大量下游任务上超过更大的 Gopher/GPT-3/Jurassic-1/MT-NLG，并且更小模型也降低了 fine-tuning 和 inference 成本。

## Abstract & Introduction 理解（2026-05-31）

- 这篇的第一问题不是“怎么训练一个给定模型”，而是：**训练预算 `C` 已知时，应该选多大的模型 `N`、看多少训练 token `D`，才能让最终 pretraining loss 最低**。
- Abstract 直接给出答案：很多当时的大模型是 **undertrained**，即参数量不断变大，但训练 token 数没有同步增长；因此它们没有在同等 compute 下达到最优 loss。
- 它对 Kaplan 的修正很具体：Kaplan 也认为 compute-optimal 时大模型不必训到最低 loss，但 Kaplan 推荐的配比偏向更快增加模型大小、较慢增加训练 token。Chinchilla 认为 token 增长应该更多，近似和参数量等比例增长。
- Introduction 先从工程约束出发：大模型训练 compute/energy 成本很高，训练预算通常提前确定（多少 accelerator、跑多久），而大模型往往只能训练一次，所以必须在训练前估算好超参和规模配置。
- Introduction 中的核心对比：Kaplan 认为 compute 增加 `10x` 时，模型大小约增加 `5.5x`，训练 token 只增加约 `1.8x`；Chinchilla 的结论是模型大小和 token 数应以接近相同比例增加。
- 论文观察到 GPT-3/Gopher 等一批大模型大多训练在约 `300B` tokens 左右；Chinchilla 则选择更小的 `70B` 参数，并训练约 `1.4T` tokens，用同等 compute 换更低 loss 和更好下游表现。
- 形式化问题：把最终 pretraining loss 写成 `L(N, D)`，compute 约束写成 `FLOPs(N, D) = C`，目标就是在这个约束下最小化 `L`。
- 从读法上看，Abstract/Introduction 已经把全文主线交代完：`fixed FLOPs budget -> choose N/D -> many LLMs undertrained -> train Chinchilla to validate the revised optimum`。

## 今日学习入口

1. 先读 Abstract：只抓住 `fixed compute -> N/D tradeoff -> undertrained -> Chinchilla validation`。
2. 再读 Introduction：看它如何批评 Kaplan 式配比，以及为什么很多大模型数据不够。
3. 最后只看 scaling law 结论图/公式：先不陷入全部拟合细节，只回答“为什么 tokens 要跟着参数一起涨”。

## 第 3 章：N/D 关系是怎么估计出来的

- 这篇不是严格数学证明，而是 **三套经验估计方法互相验证**。共同问题是：给定固定 compute `C`，找到让 loss 最低的 `N_opt(C)` 和 `D_opt(C)`。
- 形式化目标：
  - `N_opt(C), D_opt(C) = argmin L(N, D)` subject to `FLOPs(N, D) = C`
  - 近似 compute 约束：`FLOPs(N, D) ≈ 6 N D`
- Approach 1：固定一组模型大小，改变训练 token 数 / 训练步数。对每条训练曲线做平滑和插值，在每个 FLOPs 点上找 loss 最低的模型大小和 token 数；再拟合 `N_opt ∝ C^a`、`D_opt ∝ C^b`，得到 `a≈0.50`、`b≈0.50`。
- Approach 2：IsoFLOP profiles。固定若干 FLOPs budget，训练不同模型大小；因为 `C≈6ND`，模型大时 token 少，模型小时 token 多。对每个固定 compute 画 `loss vs N`，找到 loss 最低的 valley，再拟合最优 `N/D` 随 compute 的幂律，得到 `a≈0.49`、`b≈0.51`。
- Approach 3：直接拟合参数化 loss 函数：
  - `L_hat(N, D) = E + A / N^α + B / D^β`
  - `E` 表示数据分布本身不可避免的熵/极限 loss；`A/N^α` 表示模型容量不足带来的误差；`B/D^β` 表示训练 token/优化步数有限带来的误差。
  - 在 `FLOPs(N,D)≈6ND=C` 约束下最小化 `L_hat`，得到闭式 efficient frontier：
    - `N_opt(C)=G(C/6)^a`
    - `D_opt(C)=G^{-1}(C/6)^b`
    - `a=β/(α+β)`，`b=α/(α+β)`
  - 该方法得到 `a≈0.46`、`b≈0.54`。
- 三种方法的结论一致：`a` 和 `b` 都接近 `0.5`，所以 compute 增大时，最优参数量和最优训练 token 数都应近似按 `sqrt(C)` 增长。直觉上就是：**compute 翻 4 倍，参数约翻 2 倍，tokens 也约翻 2 倍**。
- 与 Kaplan 对比：Kaplan 给出的指数约为 `N_opt ∝ C^0.73`、`D_opt ∝ C^0.27`，更偏向增大模型而不是增大 token；Chinchilla 认为这导致很多大模型 undertrained。

## 明日导读问题

1. 为什么很多旧模型被认为是 undertrained？
2. Chinchilla 的 compute-optimal 结论和 Kaplan scaling law 有什么差异？
3. 对后续自己做 nanoGPT / 小模型实验有什么启发？

## 明日最低产出

- 写清 `fixed compute -> parameters/tokens tradeoff -> compute-optimal training` 主链路。
- 写清“模型大”和“训练够”之间的区别。

## 通读 Takeaway

- **一句话**：Chinchilla 把 Kaplan 的 scaling-law 框架推进到 fixed-compute 训练预算配置：给定 `C`，不要只堆参数，`N` 和 `D` 应该近似一起增长。
- **最重要结论**：compute-optimal 区域里，`N_opt ∝ C^0.5`，`D_opt ∝ C^0.5`。也就是 compute 翻 4 倍，参数和训练 tokens 都大约翻 2 倍。
- **对 Kaplan 的修正**：Kaplan 更偏向 `N_opt ∝ C^0.73`、`D_opt ∝ C^0.27`，导致策略上更容易训练“过大的欠训练模型”；Chinchilla 认为很多当时的大模型就是 undertrained。
- **验证案例**：Chinchilla 用和 Gopher 接近的训练 compute，但选择 `70B` 参数和约 `1.4T` tokens；相比 `280B` Gopher，它更小、训练更充分、下游效果更好，并且 fine-tuning/inference 成本更低。
- **方法论**：这篇不是理论证明，而是三套经验估计互相验证：training-curve envelope、IsoFLOP profiles、parametric loss fitting。
- **可跳过细节**：暂时不需要细抠所有下游 benchmark 表格、优化器超参、完整 bootstrap 区间；先保留主结论和推导框架即可。
- **后续连接**：下一篇应读 InstructGPT/RLHF。Chinchilla 解决“base LM 如何训练得更 compute-optimal”，InstructGPT 解决“base LM 如何变得更会听指令/符合人类偏好”。

## 对 nanoGPT / AI Infra 的启发

- 小模型实验也不要只问“模型再大点会不会更好”，还要问“当前 token 数是否足够把这个模型训充分”。
- 评估模型时不能只看参数规模，要同时看训练 token 数、compute budget、是否 undertrained。
- 对推理系统来说，Chinchilla 方向很重要：在相同能力下，更小但训练更充分的模型可能带来更低 inference/fine-tuning 成本。
