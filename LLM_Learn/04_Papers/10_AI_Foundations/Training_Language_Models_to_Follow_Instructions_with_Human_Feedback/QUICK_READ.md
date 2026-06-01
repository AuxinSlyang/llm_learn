---
type: paper_note
title: Training language models to follow instructions with human feedback
category: 10_AI_Foundations
status: queue
read_mode: Quick Read
phase: 2026-05 / post-GPT lineage
source_url: https://arxiv.org/abs/2203.02155
arxiv: 2203.02155
pdf_url: https://arxiv.org/pdf/2203.02155
local_pdf: Training_Language_Models_to_Follow_Instructions_with_Human_Feedback.pdf
submitted: 2022-03-04
subjects:
  - cs.CL
  - cs.AI
  - cs.LG
---

# Training language models to follow instructions with human feedback (InstructGPT / RLHF)

## 为什么现在读

- 回答 GPT-3 之后另一个问题：为什么“会续写”的模型后来变得更会听指令、更像助手。
- 区分 base LM capability 和 instruction-following / alignment。

## 接读定位（2026-05-31）

- GPT-1/2/3 与 nanoGPT：解释 **base LM / pretraining**，即通过 next-token prediction 学语言与世界知识的概率规律。
- Scaling Laws / Chinchilla：解释 base LM 预训练如何 scale，以及固定 compute 下 `N/D/C` 怎么配。
- InstructGPT：进入 **post-training / alignment**，解释一个会续写的 base GPT-3 如何变成更会听指令、对用户更有用的模型。
- 注意：InstructGPT 不是“只有 RL”。它的主链路是 `base GPT-3 -> SFT -> reward model -> PPO/RLHF`。

## 训练阶段关系

- **Pretraining（预训练）**：在大规模文本上做 next-token prediction，目标是学 `P(next token | prefix)`；对应 GPT-1/2/3、nanoGPT、Scaling Laws、Chinchilla 这条线。
- **Post-training（后训练）**：在 base LM 之后，把能力转成更符合人类任务和交互习惯的行为；通常包括 SFT、偏好学习、RLHF/DPO、安全/风格调优等。
- **SFT（supervised fine-tuning）**：用人工示范的 prompt-response 数据继续监督训练，让模型学“应该如何回答指令”。
- **Reward model（RM）**：收集人类对多个模型输出的排序，用排序数据训练一个奖励模型，近似“人类更偏好哪个回答”。
- **RLHF / PPO**：用 reward model 给生成结果打分，再用强化学习方式继续优化 SFT 模型，使输出更符合人类偏好。
- 因此，InstructGPT 的贡献是一个 post-training / alignment pipeline，而不是单独一个 RL 算法。

## SFT 是怎么做的

- 数据形态：`prompt -> labeler-written demonstration`。prompt 来自 OpenAI API/Playground 用户请求和一部分标注员写的 prompts；demonstration 是标注员写出的理想回答。
- 训练目标：仍然是语言模型的 next-token cross-entropy / NLL，不是新损失。区别是训练文本变成了指令格式：
  - 输入上下文：`<prompt>`
  - 目标输出：`<human demonstration answer>`
- 实现直觉：把 `prompt + answer` 拼成一段序列，让模型在 answer token 上最大化 `P(answer | prompt)`。很多实现会 mask 掉 prompt 部分的 loss，只对 response 部分算 CE。
- 和预训练的区别：
  - 预训练：从互联网/书籍/代码等文本里学习通用 `P(next token | prefix)`。
  - SFT：从高质量指令示范里学习 `P(good answer | instruction)`。
- 和 behavior cloning 的关系：SFT 可以理解成 imitation learning / behavior cloning。人类示范“遇到这个指令应该怎么答”，模型用监督学习模仿这个行为。
- 它解决的问题：让 base LM 从“会续写”变成“看到指令就给出符合格式/意图的回答”。它不能充分表达“哪个回答更好”的细粒度偏好，所以后面还需要 reward model + RLHF。

## InstructGPT 三步法

1. **SFT**：用人类示范回答监督微调 GPT-3，得到一个初始 instruction-following model。
2. **Reward Model**：对同一个 prompt 采样多个模型回答，让标注员排序；训练奖励模型预测人类更偏好的回答。
3. **PPO/RLHF**：以 SFT 模型为初始化，用 reward model 作为奖励函数，通过 PPO 继续优化模型；论文还引入 pretraining mix（PPO-ptx）来减轻部分公开 NLP 任务退化。

## 官方来源记录（2026-05-31）

- arXiv abs: https://arxiv.org/abs/2203.02155
- arXiv PDF: https://arxiv.org/pdf/2203.02155
- 提交时间：2022-03-04
- 分类：`cs.CL`（Computation and Language），`cs.AI`（Artificial Intelligence），`cs.LG`（Machine Learning）
- 作者：Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe
- 本地 PDF：[Training_Language_Models_to_Follow_Instructions_with_Human_Feedback.pdf](/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/Training_Language_Models_to_Follow_Instructions_with_Human_Feedback/Training_Language_Models_to_Follow_Instructions_with_Human_Feedback.pdf)

## 本轮学习入口（2026-05-31）

- 先读 Abstract：抓住“模型变大不等于更会跟随用户意图”，以及 InstructGPT 用人类反馈对齐 GPT-3 的核心动机。
- 再读 Introduction + Figure 2：确认三步流程 `SFT -> RM -> PPO/RLHF`，不要把 InstructGPT 简化成“只有 RL”。
- 第一轮只解决三个问题：
  - SFT 数据怎么构造，loss 和预训练有什么不同？
  - Reward model 如何从排序数据学到人类偏好？
  - PPO/RLHF 为什么接在 SFT 后面，而不是直接从 base GPT-3 开始？

## Abstract & Introduction 理解（2026-05-31）

- 论文的出发点：**模型变大不自动等于更会遵循用户意图**。GPT-3 这类 base LM 会续写文本，但仍可能不真实、有毒、无帮助，论文把这称为没有和用户意图对齐。
- 对齐目标不是抽象的“全人类价值”，而是更具体的用户任务行为：helpful、honest、harmless。论文明确说它对齐的是标注员/研究者表达出来的偏好，而不是完整的人类价值体系。
- 核心方法：用人类反馈 fine-tune GPT-3。先收集人类示范回答做 SFT，再收集人类对多个模型回答的排序训练 reward model，最后用 reward model 作为奖励通过 PPO 做 RLHF。
- SFT 的作用：给 base GPT-3 一个可模仿的 instruction-following 起点。它让模型知道“指令输入后应该直接给答案”，而不是继续做开放式续写。
- RM 的作用：把人类“哪个回答更好”的排序信号变成一个可优化的标量奖励。它解决 SFT 只能模仿单个示范、难以表达多个回答质量差异的问题。
- PPO/RLHF 的作用：在 SFT 模型基础上进一步优化，让模型输出更符合 reward model 代表的人类偏好。
- 主要结果：在人类评估的 API prompt 分布上，`1.3B` InstructGPT 输出甚至比 `175B` GPT-3 更受偏好，说明“好用/听话/对齐”不是单靠参数规模获得的。
- 一个重要副作用：RLHF 可能造成某些公开 NLP benchmark 退化，论文称为 alignment tax；他们用 PPO-ptx（混入预训练分布的更新）来缓解这类退化。
- 第一轮读法：这篇不是先学 PPO 算法，而是先记住 post-training pipeline：`base LM capability -> SFT behavior cloning -> RM preference modeling -> RLHF preference optimization`。

## 明日导读问题

1. SFT、reward model、RLHF 三步分别做什么？
2. 为什么 1.3B InstructGPT 可以在人类偏好上超过 175B GPT-3？
3. 它解决的是能力问题、对齐问题，还是产品可用性问题？

## 明日最低产出

- 写清 `base GPT-3 -> SFT -> RM -> PPO/RLHF -> instruction-following model` 主链路。
- 写清“能力强”和“好用/听话”不是同一件事。

## 完整论文理解（2026-05-31）

- **论文问题**：GPT-3 这类 base LM 已经有很强能力，但能力不等于遵循用户意图。模型可能不 helpful、不 honest、不 harmless；InstructGPT 研究如何用人类示范和偏好把 GPT-3 对齐到用户任务行为。
- **数据来源**：prompt 主要来自 OpenAI API Playground 的用户请求，以及一部分 labeler-written prompts。训练/验证/测试按 user ID 切分，训练集过滤 PII。
- **数据集分三类**：
  - SFT dataset：约 13k prompts，配 labeler-written demonstrations，用来监督微调。
  - RM dataset：约 33k prompts，配人类对多个模型输出的排序，用来训练 reward model。
  - PPO dataset：约 31k prompts，无人工标签，只作为 RLHF 里让模型生成回答的输入。
- **Step 1 / SFT**：从 GPT-3 pretrained model 出发，用人类示范回答做 supervised fine-tuning。本质仍是 next-token CE/NLL，让模型学 `P(good answer | instruction)`。论文训练 SFT 16 epochs，并用 reward model validation score 选最终 SFT checkpoint；虽然 validation loss 1 epoch 后过拟合，但更多 epoch 对 RM score 和人类偏好更好。
- **Step 2 / RM**：从 SFT 模型去掉 final unembedding layer 开始，训练一个输入 `(prompt, response)` 输出标量 reward 的模型。标注员对同一 prompt 下 `K=4~9` 个回答排序，排序被转成 pairwise comparisons；reward loss 是让 preferred answer 的 reward 高于 rejected answer：`-log sigmoid(r(x,y_w)-r(x,y_l))`。
- **Step 3 / PPO/RLHF**：把 SFT 模型作为初始 policy，让模型对 prompt 生成回答，用 RM 打分，再用 PPO 优化。目标里包含 reward，同时加 KL penalty 约束 RL policy 不要偏离 SFT policy 太远。PPO-ptx 还混入 pretraining log-likelihood 更新，用来减轻公开 NLP benchmark 上的退化。
- **评估定义**：论文把 alignment 操作化为 helpful / honest / harmless。主评估是 API prompt distribution 上的人类偏好；辅助评估包括 TruthfulQA、RealToxicityPrompts、CrowS-Pairs 和传统 NLP benchmark。
- **主要结果 1**：InstructGPT 在 API prompt 上显著优于 GPT-3。`1.3B` InstructGPT 可在人类偏好上超过 `175B` GPT-3，说明 instruction-following / alignment 不是单纯参数规模问题。
- **主要结果 2**：SFT 已经带来明显改进，PPO/RLHF 在 SFT 上继续提高偏好分数。效果阶梯大致是：GPT-3 < GPT-3 prompted < SFT < PPO/RLHF。
- **主要结果 3**：truthfulness 有改善，尤其在 TruthfulQA 和闭域任务 hallucination 上，InstructGPT 比 GPT-3 更少编造。
- **主要结果 4**：toxicity 有条件改善。加入 respectful instruction 时 InstructGPT 更少 toxic；但如果明确要求 toxic 输出，它仍可能遵循指令生成有害内容。
- **主要结果 5**：RLHF 会带来 alignment tax，在部分公开 NLP benchmark 上退化；PPO-ptx 通过混入预训练梯度缓解但没有完全消除。
- **限制**：它对齐的是一组标注员/研究者/API 用户分布表达出来的偏好，不代表全人类价值；模型仍会犯简单错误、过度 hedging、接受 false premise、在多约束任务中失败，也并不彻底安全。
- **核心 takeaway**：pretraining 给模型能力；SFT 让模型学会指令回答格式；RM 把人类偏好变成可优化信号；RLHF/PPO 用这个信号进一步塑造行为。

## 按论文结构完整分析（2026-05-31）

### 0. Abstract：一句话问题设定

- 摘要第一句的关键判断是：**making language models bigger does not inherently make them better at following user intent**。
- 这句话直接接上 Scaling Laws / Chinchilla：前两篇解释“如何把 base LM 训练得更强”，这篇指出“更强的 base LM 不等于更符合用户意图”。
- Abstract 给出的解决路线是：用人类反馈 fine-tune。具体不是一步，而是：
  - 先用 labeler demonstrations 做 supervised fine-tuning；
  - 再用 labeler rankings 训练 reward model；
  - 最后用 RLHF 继续 fine-tune supervised model。
- 摘要最重要的证据是：`1.3B` InstructGPT 在人类偏好上能超过 `175B` GPT-3。这说明 post-training 对“好用/听话”的收益可以超过单纯增加参数。

### 1. Introduction：定义 alignment 和研究边界

- Introduction 把目标定义成让模型按照用户意图行动，并借用 helpful / honest / harmless 框架。
- Helpful：不仅要跟随显式指令，还要从 prompt 格式、few-shot 示例、隐式续写意图中推断用户想做什么。
- Honest：论文承认“honesty”难以严格测，因为无法直接知道模型 belief；因此用 truthfulness / hallucination proxy 来评估。
- Harmless：论文也承认 harms 依赖部署上下文，所以用 toxicity、bias、inappropriate for customer assistant 等 proxy。
- 这章需要注意的边界：论文不是声称“对齐全人类价值”，而是对齐到 labelers / researchers / API prompt distribution 中表达出来的偏好。

### 2. Related Work：它站在哪条线之上

- 这篇不是凭空发明 RLHF，而是接在 Christiano et al. 2017、Ziegler et al. 2019、Stiennon et al. 2020 等 human feedback work 后面。
- 区别在于：之前常在 summarization / stylistic continuation 这类较窄任务上做；InstructGPT 扩展到更宽泛的 API instruction distribution。
- 对我们来说，Related Work 只需要记住：它把 RLHF 从专项任务推到通用指令跟随场景。

### 3. Methods：全文最重要的一章

- 输入条件：
  - 一个 pretrained GPT-3；
  - 一个真实 prompt distribution；
  - 一组训练过的 human labelers。
- Step 1 / SFT：
  - labelers 对 prompts 写理想回答；
  - 用这些 `prompt -> demonstration` 做监督微调；
  - 本质还是 next-token CE，只是训练目标从“续写任意文本”变成“按指令给出理想回答”。
- Step 2 / RM：
  - 对同一 prompt 采样多个模型回答；
  - labelers 排序；
  - 排序转成 pairwise comparisons；
  - RM 学习让 preferred completion 的 scalar reward 高于 rejected completion。
- Step 3 / PPO/RLHF：
  - 以 SFT model 作为初始 policy；
  - policy 对 prompt 生成回答；
  - RM 给回答打 reward；
  - PPO 优化 policy；
  - KL penalty 约束新 policy 不要偏离 SFT 太远。
- PPO-ptx：
  - 在 PPO 更新中混入 pretraining distribution 的 log-likelihood 更新；
  - 目的不是提高偏好分数本身，而是降低 alignment tax，避免公开 NLP benchmark 退化太多。

### 4. Dataset / Human Data Collection：数据决定对齐对象

- prompt 来源主要是 OpenAI API Playground，另有 labeler-written prompts 用于 bootstrapping。
- 数据分三类：
  - SFT dataset：demonstration 数据；
  - RM dataset：comparison / ranking 数据；
  - PPO dataset：无标签 prompt，用于 RL 采样。
- 论文按 user ID 切分 train/val/test，减少用户泄漏；训练 split 过滤 PII。
- labelers 约 40 人，有筛选、onboarding、详细标注说明和沟通渠道。
- 关键理解：模型最终不是“直接对齐用户真实意图”，而是通过 labelers 对 prompt 的解释和排序来近似用户意图。

### 5. Models：SFT / RM / PPO 的具体差异

- SFT models：
  - 从 GPT-3 初始化；
  - 在 demonstrations 上训练；
  - 论文观察到 validation loss 早早过拟合，但更多 epoch 反而改善 RM score 和人类偏好。
- RM：
  - 从 SFT 模型去掉 final unembedding layer；
  - 输入 prompt + completion，输出 scalar reward；
  - 使用 pairwise ranking loss：`-log sigmoid(r_w - r_l)`。
- PPO / PPO-ptx：
  - PPO 是只用 RM reward + KL penalty；
  - PPO-ptx 是 PPO 再加 pretraining mix；
  - 论文默认 InstructGPT 指 PPO-ptx models。

### 6. Evaluation：这篇怎么证明“更对齐”

- 主评估不是传统 NLP benchmark，而是 API prompt distribution 上的人类偏好。
- 评估还包括：
  - overall quality Likert score；
  - 是否 follow correct instruction；
  - 是否 hallucinate；
  - 是否 inappropriate for customer assistant；
  - TruthfulQA；
  - RealToxicityPrompts；
  - CrowS-Pairs；
  - 传统 NLP datasets。
- 这很关键：论文在论证“真实用户 prompt 分布上的偏好”，所以公开 benchmark 只是辅助，不是主指标。

### 7. Results：主要证据链

- Preference：
  - GPT-3 最差；
  - GPT-3 prompted 有改善；
  - SFT 明显提升；
  - PPO/RLHF 继续提升；
  - 1.3B InstructGPT 可超过 175B GPT-3。
- Metadata：
  - InstructGPT 更适合作为 customer assistant；
  - 更能遵守显式约束；
  - 更少完全跑错任务；
  - closed-domain tasks 上 hallucination 更少。
- Truthfulness：
  - TruthfulQA 上比 GPT-3 更 truthful/informative；
  - 在不确定时更倾向于保守回答。
- Toxicity / bias：
  - respectful prompt 下 toxicity 降低；
  - no prompt 下优势不明显；
  - 明确要求 toxic 时仍可能照做；
  - bias 没有稳定改善。
- Alignment tax：
  - PPO 会导致某些公开 NLP tasks 退化；
  - PPO-ptx 混入预训练更新可以缓解，但不能完全消除。

### 8. Discussion / Limitations：读这篇必须保留的谨慎点

- 对齐对象有限：labelers、researchers、API customers 都不是全体人类。
- 标注任务包含价值判断；labeler 背景、说明书、研究者反馈都会影响最终模型行为。
- 模型仍不安全：仍会 hallucinate、toxic、biased，也会跟随有害指令。
- 模型有行为副作用：
  - 过度 hedging；
  - 接受 false premise；
  - 多约束任务失败；
  - 对少见类型的指令泛化不稳定。
- 论文的意义不是“解决 alignment”，而是证明 human feedback fine-tuning 可以显著改善当前 LM 的可用性，并提供一个可迭代工程反馈闭环。

### 9. 对后续 roadmap 的位置

- GPT-1/2/3：解释 base LM 能力从哪里来。
- Scaling Laws / Chinchilla：解释 base LM 如何更合理地 scale。
- InstructGPT：解释 base LM 如何通过 post-training 变成 instruction-following assistant。
- 下一篇 CoT：解释不改参数时，如何通过 prompt elicitation 释放推理能力。
- 下一篇 FLAN：解释 instruction tuning 如何从单一 API prompt distribution 扩展到多任务泛化。

## 通读 Takeaway

- InstructGPT 是现代 post-training / alignment pipeline 的代表论文，不是“单独一篇 RL 论文”。
- 它把 `base GPT-3` 转成 instruction-following assistant 的关键链路是 `SFT -> RM -> PPO/RLHF`。
- SFT 本质还是 CE 训练，只是数据从普通文本变成高质量 `prompt -> answer` 示范。
- RM/RLHF 解决的是“单个示范不够表达偏好”的问题：同一 prompt 可以有多个合理回答，排序数据更适合表达人类对质量的细粒度判断。
- 论文最重要的认知转变：能力、听话、好用、安全不是同一件事；更大模型不自动更对齐。
