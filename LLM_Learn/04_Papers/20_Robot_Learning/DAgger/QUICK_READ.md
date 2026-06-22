---
type: paper_note
paper: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning
short_name: DAgger
arxiv_id: 1011.0686
url: https://arxiv.org/abs/1011.0686
pdf_url: https://arxiv.org/pdf/1011.0686
local_pdf: ./DAgger_A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No_Regret_Online_Learning.pdf
authors: Stephane Ross; Geoffrey J. Gordon; J. Andrew Bagnell
submitted: 2010-11-02
last_revised: 2011-03-16
categories: cs.LG; cs.AI; stat.ML
status: pdf_downloaded
---

# QUICK_READ — DAgger (1011.0686)

## 元信息

- Title：A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning
- Authors：Stephane Ross, Geoffrey J. Gordon, J. Andrew Bagnell
- arXiv：`1011.0686`
- URL：`https://arxiv.org/abs/1011.0686`
- PDF：`https://arxiv.org/pdf/1011.0686`
- Local PDF：`./DAgger_A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No_Regret_Online_Learning.pdf`
- 日期：submitted `2010-11-02`，last revised `2011-03-16`
- 分类：`cs.LG / cs.AI / stat.ML`
- 官方来源：arXiv

## 摘要要点（待读后复核）

- imitation learning 这类 sequential prediction 不满足普通监督学习的 i.i.d. 假设，因为后续 observation 会依赖前面的 action。
- 这会造成 behavior cloning 在 closed-loop 下错误累积，也就是 covariate shift。
- DAgger 的核心是用迭代数据聚合，让 learner 在自己诱导出的状态分布上继续收集 expert label，从而训练一个更适合 closed-loop 执行的 stationary deterministic policy。

## 读前问题（2-3min）

- 我想用这篇论文回答什么：为什么 BC 在 closed-loop 下会崩？如何用数据迭代缓解？
- 我希望带走什么：一个最小 DAgger 数据闭环的“接口清单”（episode、label、replay、safety）。

## Classic Scan 记录（20-40m）

- 1 句话讲清 DAgger：
- 它解决的核心 failure mode（covariate shift）：
- 算法骨架（只写步骤，不抄公式）：
  1.
  2.
  3.
- 关键假设 / 代价：
- 实验/结果最值得看的 1 点：

## 今日 Takeaway（必填）

- takeaway：
- 对未来 mini-stack 的接口要求（data loop / eval / replay）：

## 后续动作（可选）

- 需要精读的段落（指到 section）：
- 需要补的背景（no-regret / online learning）：
