---
type: paper_note
title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
category: 10_AI_Foundations
status: quick_read_done
read_mode: Structured Read
phase: 2026-06 / LLM phase 1 closure
source_url: https://arxiv.org/abs/2307.09288
arxiv: 2307.09288
submitted: 2023-07-18
last_revised: 2023-07-19
subjects:
  - cs.CL
  - cs.AI
doi: 10.48550/arXiv.2307.09288
pdf_url: https://arxiv.org/pdf/2307.09288
local_pdf: Llama_2_Open_Foundation_and_Fine_Tuned_Chat_Models.pdf
pages: 77
authors_short: Hugo Touvron et al.
metadata_source: https://arxiv.org/abs/2307.09288
pdf_refreshed: 2026-06-02
---

# Llama 2: Open Foundation and Fine-Tuned Chat Models

## 为什么现在读

- 它是 `Scaling Laws / Chinchilla / InstructGPT / CoT / FLAN` 之后，最适合用来收口现代 open LLM 工程全流程的论文。
- 目标不是深挖所有 benchmark，而是理解现代 LLM 如何组织：
  - pretraining data / tokenizer / model scale
  - supervised fine-tuning
  - reward modeling / RLHF
  - safety data and evaluation
  - release / responsible use
- 读完后应该能写出 `LLM phase 1 总结`：现代 LLM 从原始文本到可用 assistant 的训练与工程链路。

## 阅读问题

1. Llama 2 的 base model 和 chat model 分别是什么？
2. 它的 pretraining 数据、模型规模、context length、tokenizer 大致怎么组织？
3. 它的 fine-tuning pipeline 和 InstructGPT 有什么相同与不同？
4. 它如何处理 safety / helpfulness / human preference？
5. 它作为工程报告，对我们理解现代 LLM 训练流程有什么补全？

## 预期 Takeaway

- `Llama 2` 是一篇现代 open LLM 全流程工程报告：它把 base model 预训练、chat model 后训练、安全对齐、评估和发布串成了完整路线。
- 它适合用来把第一阶段 LLM 学习收口到：

```text
text/data -> tokenizer -> pretraining -> SFT/instruction tuning -> RLHF/preference -> safety/eval -> deployable chat model
```

## Pass 0: Metadata and Position

- 论文类型：foundation model / open LLM engineering report
- 所属阶段：LLM 第一阶段收口
- 推荐读法：Structured Read
- 本地 PDF：`Llama_2_Open_Foundation_and_Fine_Tuned_Chat_Models.pdf`
- 官方来源：arXiv `2307.09288`
- 本次优先级：
  1. Abstract + Introduction
  2. Model / pretraining setup
  3. Fine-tuning / RLHF pipeline
  4. Safety / evaluation
  5. 总结它和 InstructGPT / FLAN 的关系

## Abstract + Introduction Understanding

### 一句话定位

Llama 2 是一篇把现代 open LLM 从 `base model pretraining` 到 `chat model post-training`、再到 safety/evaluation/release 串起来的工程报告；它不是提出一个新 Transformer 架构，而是把“可用 assistant model”背后的训练流程公开化。

### Abstract 在说什么

- 他们发布了一组 pretrained 和 fine-tuned LLM，规模从 7B 到 70B。
- fine-tuned 版本叫 `Llama 2-Chat`，目标是 dialogue / assistant 场景。
- 论文声称：在他们测试的大多数 benchmark 上，Llama 2-Chat 优于开源 chat model；在人类 helpfulness / safety 评测中，可能接近部分闭源模型。
- 论文重点不是只报分数，而是公开 fine-tuning 与 safety improvement 的流程，方便社区复现和继续做 alignment。

### Introduction 主线

1. **问题背景**：LLM 已经能作为 AI assistant 处理 reasoning、programming、creative writing 等任务，并通过 chat interface 被广泛使用。
2. **关键矛盾**：基础训练方法看起来简单：auto-regressive Transformer 先在大规模 self-supervised data 上 pretrain，再用 RLHF 等方法对齐人类偏好；但真正做出“产品级 chat model”需要大量算力、标注和不透明的 post-training 工程。
3. **已有缺口**：BLOOM、LLaMA-1、Falcon 等开源 pretrained model 可以接近 GPT-3 / Chinchilla 这类 base model，但还不能直接替代 ChatGPT / Bard / Claude 这类产品级 assistant，因为后者 heavily fine-tuned，更可用也更安全。
4. **Llama 2 的贡献**：
   - 发布 `Llama 2` base models：7B / 13B / 70B。
   - 发布 `Llama 2-Chat`：针对 dialogue use cases 的 fine-tuned models。
   - 描述 pretraining、SFT、RLHF、safety tuning、red-teaming、evaluation 和 responsible release。
   - 分享一些开发过程观察，例如 tool use emergence、知识时间组织、RLHF 对生成分布的影响。
5. **第一张流程图的意义**：Llama 2-Chat 的训练过程是：

```text
public online data
-> pretraining base Llama 2
-> supervised fine-tuning
-> iterative RLHF
   -> rejection sampling
   -> PPO
   -> reward model data 随模型迭代持续更新
-> helpful/safe chat model
```

### 读这一节要抓住的概念

- `base model`：只做大规模 next-token pretraining，核心能力来自数据、规模和 Transformer。
- `chat model`：在 base model 上经过 SFT / RLHF / safety tuning，行为更像 assistant。
- `open-source pretrained model` 不等于 `product chat model`；差距主要在 post-training、evaluation、safety 和 release discipline。
- Llama 2 适合接在 `InstructGPT / FLAN` 后读：InstructGPT 解释 RLHF assistant 范式，FLAN 解释 instruction tuning scaling，Llama 2 把这些放进一个现代 open LLM 工程系统里。

## Section Map

第一轮只需要把正文分成 6 块：

| Section | 第一遍要看什么 | 第一遍可跳过什么 |
|---|---|---|
| Introduction | 论文定位、base vs chat、整体训练流程图 | 具体评测数字 |
| Pretraining | data/tokenizer/context/GQA/model scale | carbon footprint 细节 |
| Fine-tuning | SFT、reward model、RLHF、rejection sampling、PPO、GAtt | 每个 ablation 的细节 |
| Safety | safety SFT、safety RLHF、context distillation、red-teaming | 大量 safety benchmark 表 |
| Results / Discussion | helpfulness/safety 人评、tool use、RLHF observations | 所有榜单逐项比较 |
| Related Work / Appendix | 用作索引 | 第一遍基本跳过 |

## Method / Training Pipeline

### Pretraining：base model 是怎么训练出来的

Llama 2 的 pretraining 可以理解为：

```text
public online data
-> cleaned / remixed corpus
-> SentencePiece BPE tokenizer
-> autoregressive Transformer
-> next-token prediction on 2T tokens
-> base Llama 2
```

它不是从零发明一套架构，而是在 LLaMA-1 的配方上做了几个工程升级。

#### 1. 数据：公开来源 + 更强清洗 + 2T tokens

- 训练语料来自 publicly available online sources，不包含 Meta 产品/服务数据。
- 做了更严格的数据清洗，也移除了一些高个人信息风险站点。
- 训练 token 数提升到 `2T`，比 LLaMA-1 更多；作者认为这是性能和成本之间的较好折中。
- 对 factual sources 做 up-sampling，目标是增加知识密度并降低 hallucination。

直觉：base model 的能力主要来自大规模 next-token prediction；这里最重要的是数据质量、数据量和数据配比。

#### 2. 模型：还是 autoregressive Transformer

主体仍是 decoder-only autoregressive Transformer，沿用 LLaMA 系列常见组件：

- pre-normalization + `RMSNorm`
- `SwiGLU` activation
- `RoPE` rotary positional embeddings
- causal next-token prediction

所以这里和 nanoGPT 的连接很直接：

```text
tokens -> embedding -> Transformer blocks -> logits -> next-token loss
```

Llama 2 只是工业规模版本，核心训练目标仍然是 next-token prediction。

#### 3. Tokenizer：SentencePiece BPE，32k vocab

- 沿用 LLaMA-1 tokenizer。
- 使用 SentencePiece 实现的 BPE。
- vocabulary size 是 `32k`。
- 数字会拆成单个 digit；未知 UTF-8 字符会按 byte 分解。

这正好接到今晚的 tokenizer 学习：

```text
raw text -> BPE tokens -> token ids -> batch -> next-token training
```

#### 4. Context length：2k -> 4k

Llama 2 把 context window 从 LLaMA-1 的 `2048` 扩到 `4096`。

目的不是炫长上下文，而是为了：

- 支持更长 chat history。
- 支持 summarization / long document tasks。
- 不明显损害通用任务表现。

Appendix 里做了 ablation：4k context 在长上下文任务上更好，通用任务基本不退化。

#### 5. GQA：为大模型推理扩展做的 attention 改动

34B / 70B 使用 `Grouped-Query Attention (GQA)`。

原因是 autoregressive decoding 会缓存历史 token 的 K/V；context 变长、batch 变大后，KV cache 会成为显存瓶颈。GQA 通过让多个 query heads 共享较少的 K/V heads，在性能接近 MHA 的同时降低 KV cache 压力，推理扩展更容易。

对我们现在的理解：

```text
GQA 不是训练目标变化，而是服务大模型 inference scalability 的架构工程改动。
```

#### 6. 训练超参：标准稳定配方

- optimizer：`AdamW`
- `beta1 = 0.9`
- `beta2 = 0.95`
- `eps = 1e-5`
- cosine learning rate schedule
- warmup：`2000` steps
- final LR decay 到 peak LR 的 `10%`
- weight decay：`0.1`
- gradient clipping：`1.0`
- global batch size：`4M tokens`

这部分说明它没有靠奇怪的 trick，而是用稳定成熟的大规模训练设置。

#### 7. 训练后怎么判断 base model 好不好

Pretraining 结束后，他们评估的是 `base model`，不是 chat model。

评估覆盖：

- code：HumanEval / MBPP
- commonsense reasoning
- world knowledge
- reading comprehension
- math：GSM8K / MATH
- aggregated benchmark：MMLU / BBH / AGI Eval

论文主张：Llama 2 base models 整体优于 LLaMA-1，同规模下也强于许多开源 base model；70B 接近 GPT-3.5 的部分指标，但和 GPT-4 / PaLM-2-L 仍有明显差距，尤其 coding。

### 这一节的一句话 takeaway

Llama 2 的 base model 是用公开语料做 2T-token next-token pretraining 得到的 decoder-only Transformer；真正的升级点是更干净的数据、更长 4k context、对大模型推理更友好的 GQA，以及稳定的大规模训练配方。

### Fine-tuning：base model 怎么变成 Llama 2-Chat

Fine-tuning 这一章回答：

```text
一个只会 next-token prediction 的 base model，怎样被塑造成会对话、会遵循指令、相对安全的 assistant？
```

总链路是：

```text
base Llama 2
-> Supervised Fine-Tuning (SFT)
-> human preference data
-> reward models: Helpfulness RM + Safety RM
-> iterative RLHF
   -> rejection sampling fine-tuning
   -> PPO
-> Ghost Attention for multi-turn consistency
-> Llama 2-Chat
```

#### 1. SFT：先教模型“怎么像 assistant 回答”

SFT 阶段使用 prompt-answer 样本，训练模型在给定用户 prompt 后生成高质量 answer。

关键点：

- 先用公开 instruction tuning 数据 bootstrapping。
- 后来发现大量第三方 SFT 数据质量和多样性不够，尤其不适合 dialogue-style assistant。
- 因此重点收集少量但高质量的 vendor annotation。
- 最终 SFT annotation 约 `27,540` 条，不包含 Meta user data。
- 他们的结论很接近 `LIMA`：SFT 数据不是越多越好，质量非常关键。

训练细节：

- 每个样本是 `prompt + answer`。
- 使用 autoregressive objective。
- 对 user prompt token 的 loss 置零，只在 answer tokens 上反传。
- sequence length 是 `4096`。
- fine-tune `2 epochs`。

直觉：

```text
pretraining 学会“语言和知识”
SFT 学会“面对用户请求时应该怎么回答”
```

#### 2. Human Preference Data：收集“两个回答哪个更好”

SFT 后模型已经像 assistant，但还不够符合人类偏好。

他们让标注者：

```text
写一个 prompt
-> 看两个不同模型/温度采样出的 response
-> 选择更好的一个
-> 标注 preference 强度
```

偏好数据分两条线：

- `helpfulness`：是否满足用户请求、信息是否有用。
- `safety`：是否避免 unsafe response。

这里的关键是 weekly iterative collection：模型每进化一轮，输出分布会变；reward model 如果一直只看旧模型数据，就会 out-of-distribution。因此需要持续收集最新模型上的偏好数据。

#### 3. Reward Modeling：把人类偏好训练成可自动打分的模型

Reward model 输入：

```text
prompt + response (+ multi-turn context)
```

输出：

```text
scalar reward score
```

他们训练两个 reward model：

- `Helpfulness RM`
- `Safety RM`

原因：helpfulness 和 safety 有时会冲突。一个回答可能很有帮助但不安全，也可能很安全但没用。拆成两个 RM，任务更清楚。

Reward model 训练目标是 ranking loss：

```text
chosen response 的 reward > rejected response 的 reward
```

论文还用了 margin：如果标注者认为两个回答差距很大，就要求 reward 差距也更大。

#### 4. RLHF：用 reward model 继续优化 assistant 行为

RLHF 阶段核心是：

```text
让模型生成回答
-> reward model 打分
-> 用高分信号更新模型
```

Llama 2 使用两类方法。

##### Rejection Sampling Fine-Tuning

对同一个 prompt 采样 `K` 个回答：

```text
prompt -> response_1 ... response_K
-> reward model 评分
-> 选最高分 response
-> 把它当新的 gold answer 做 fine-tuning
```

特点：

- breadth：一次探索多个候选回答。
- 更像“用 reward model 自动筛一批更好的 SFT 数据”。
- Llama 2 只用 70B 做 rejection sampling；小模型用 70B 筛出来的数据进行蒸馏式 fine-tuning。

##### PPO

PPO 直接把语言模型当 policy：

```text
prompt = state/context
generation = action trajectory
reward model score = reward
```

优化目标是提升 reward，同时加 KL penalty，防止模型偏离原始策略太远。

这点很重要：没有 KL 约束，模型可能 reward hacking：reward model 分数高，但人类看起来反而差。

Llama 2 前期主要用 rejection sampling，到 RLHF-V4 后再结合 PPO。

#### 5. Ghost Attention (GAtt)：让多轮对话记住系统指令

问题：早期 RLHF model 在多轮对话中会忘记第一轮 system instruction，例如“始终简短回答”或“扮演某个角色”。

GAtt 的做法是构造特殊 fine-tuning 数据：

- 把要长期遵守的 instruction 合成进多轮对话。
- 训练时让模型在后续回合仍然遵守最初 instruction。
- 对前面历史 token 的 loss 置零，重点训练最后响应。

直觉：

```text
GAtt 是为了让 assistant 在长对话里持续关注 system message。
```

#### 这一节的一句话 takeaway

Llama 2 的 fine-tuning 是一个多阶段 alignment pipeline：先用高质量 SFT 教会模型按指令回答，再用人类偏好训练 helpfulness/safety reward models，最后通过 rejection sampling 和 PPO 迭代优化模型行为，并用 GAtt 改善多轮系统指令一致性。

### Safety：安全不是只加拒答，而是一套独立闭环

Safety 这一章回答：

```text
Llama 2 如何识别、缓解、评估和迭代修复模型的安全风险？
```

它的主链路是：

```text
pretraining data / base model risk analysis
-> safety SFT
-> safety RLHF + safety reward model
-> safety context distillation
-> red teaming
-> human / automatic safety evaluation
```

#### 1. Safety in Pretraining：先承认 base model 本身有风险

作者先分析 pretraining data：

- demographic representation：性别、身份、地域/宗教等词分布可能有偏。
- toxicity：训练语料里有少量 toxic data。
- language distribution：语料主要是 English，因此其他语言能力和安全性都不能默认等价。

一个关键选择是：他们没有对预训练数据做过度 aggressive filtering。

原因：

- 过度清洗可能删除某些群体/语境，造成 demographic erasure。
- 保留部分不良/敏感内容可能让 base model 更适合下游任务，例如 hate speech detection。
- 但这也意味着 base model 不能直接部署，必须经过后续 safety tuning。

#### 2. Safety Fine-Tuning：三种安全训练手段

安全 fine-tuning 包括三层。

##### Supervised Safety Fine-Tuning

收集 adversarial prompts 和 safe demonstrations，加入 SFT。

目标：

```text
在 RLHF 之前，先教模型遇到危险请求时应该怎样安全回应。
```

##### Safety RLHF

安全也进入 RLHF pipeline：

- 标注者写可能诱导 unsafe behavior 的 prompt。
- 比较多个 model response，选择更安全的回答。
- 训练 Safety RM。
- 在 rejection sampling / PPO 中使用安全 reward。

重点：Safety RLHF 不是只让模型拒答，而是让它在危险场景里更稳地遵守安全边界。

##### Safety Context Distillation

这是和 GAtt 类似的数据构造技巧。

做法：

```text
adversarial prompt
+ safety preprompt（例如 safe/responsible assistant）
-> 生成更安全的回答
-> 去掉 safety preprompt
-> 用这个安全回答继续 fine-tune
```

直觉：

```text
把“你是安全负责的助手”这种上下文提示蒸馏进模型参数里。
```

但它不能乱用。对正常 helpful prompts 使用 context distillation 可能导致 false refusal 或回答变空泛。因此他们用 Safety RM 选择：只有 context-distilled answer 比原 answer 分数更高时才保留。

#### 3. Safety Categories：安全问题按风险和攻击方式拆开

风险类别包括：

- illicit / criminal activities
- hateful / harmful activities
- unqualified advice，例如医疗、金融、法律建议

攻击方式包括：

- psychological manipulation
- false premises
- misspelling / syntax manipulation
- metaphor / semantic manipulation
- role playing
- non-English prompts
- multi-turn dialogue

这说明 safety 不是一个单点分类器，而是一组长尾边界条件。

#### 4. Red Teaming：主动找长尾漏洞

他们组织 350+ 人做 red teaming，包括网络安全、选举欺诈、法律、政策、公民权利、伦理、机器学习、创意写作等领域人员。

red teaming 的目标：

```text
不是证明模型安全，而是主动找出定量 benchmark 覆盖不到的长尾失败模式。
```

发现的问题包括：

- 早期模型会先说内容不合适，然后继续给出 unsafe details。
- 创意写作/诗歌/故事请求会绕过拒答。
- 把危险请求包装成积极、正向、进步语境，可以诱导模型输出问题内容。

这些 red team 数据会回流到 fine-tuning / feedback training / safety model training。

#### 5. Safety Evaluation：安全也需要人评 + 自动评估

他们做了：

- 约 2,000 adversarial prompts 的 human evaluation。
- 单轮和多轮分开看。
- 使用 5 分 Likert scale，1/2 视为 safety violation。
- 自动评估包括 TruthfulQA、ToxiGen、BOLD 等。

重要观察：

- multi-turn conversations 更容易诱导 unsafe responses。
- fine-tuned Llama 2 在 toxicity 上比 pretrained model 大幅改善。
- 但 safety 结果要谨慎解释，因为 prompt set、guidelines、raters 都会带来偏差。
- 过多 safety data 可能增加 false refusal，尤其在 borderline prompts 上。

#### 这一节的一句话 takeaway

Llama 2 的 Safety 章把安全做成一个闭环：先分析 pretraining/base model 风险，再用 safety SFT、Safety RM/RLHF、context distillation 做对齐，用 red teaming 找长尾漏洞，最后用人评和自动 benchmark 验证；核心不是“简单拒答”，而是在 helpfulness 和 safety 之间做可迭代的边界管理。

## Experiments / Evaluation

- base model evaluation：Llama 2 base models 在 code、commonsense、world knowledge、reading comprehension、math、MMLU、BBH、AGI Eval 等 benchmark 上整体强于 LLaMA-1 和许多开源 base model；70B 部分指标接近 GPT-3.5，但和 GPT-4 / PaLM-2-L 仍有明显差距。
- chat model evaluation：Llama 2-Chat 在约 4k helpfulness prompts 上明显优于多数开源 chat models；70B 与 ChatGPT 接近但不完全等价。
- safety evaluation：fine-tuned Llama 2 在 toxicity / truthfulness / human safety evaluation 上相较 base model 明显改善，多轮对话仍更容易诱发 unsafe response。
- 评估局限：human evaluation 噪声很大，prompt set 覆盖有限，不含足够 coding/reasoning 场景；reward model 也可能偏向自家模型，因此论文用 GPT-4 judge 和人评交叉验证。

## Takeaway

### 一句话 takeaway

Llama 2 是一篇现代 open LLM 工程报告：它把 `public data -> base model pretraining -> SFT -> reward model/RLHF -> safety/red-teaming/evaluation -> responsible release` 做成一条可复述的完整路线。

### 3-5 个核心想法

1. `base model` 和 `chat model` 是两个阶段：pretraining 负责语言/知识底座，fine-tuning/RLHF/safety 负责 assistant 行为。
2. SFT 数据质量比数量更关键；Llama 2 只用了约 27k 高质量 SFT annotation，就足以建立初始 assistant 行为。
3. RLHF 的价值在于让人类只需比较回答好坏，不必亲自写出最优答案；reward model 可以逐步压低差回答分布。
4. Safety 是独立闭环：safety SFT、Safety RM/RLHF、context distillation、red teaming、evaluation 都要一起做。
5. 工程报告比单点算法更重要：数据、tokenizer、context、GQA、annotation、evaluation、release policy 一起决定最终模型质量。

### 其他值得带走的观察

- RLHF 可能让模型在 factual prompts 上更稳定，在 creative prompts 上仍保留多样性；作者称之为 in-context temperature rescaling。
- 少量 SFT 数据能让模型学到某些时间组织能力，说明 post-training 数据格式会强烈塑造模型行为。
- 论文观察到 tool use emergence，但这不是系统化 tool training；后续要用 Toolformer / ReAct 等论文补全。
- Llama 2 仍有局限：知识停止在 pretraining cutoff，非英语能力较弱，可能 hallucinate，可能 false refusal，也可能被 misuse。

## Robot Learning / Runtime Connection

- Llama 2 本身不是机器人论文，但它帮助我们理解未来 VLA / robot agent 中的语言智能底座如何训练、对齐、评估与部署。

## Open Questions

- Llama 2 的 safety/RLHF pipeline 和 InstructGPT 的核心差异是什么？
- Llama 2 是否已经足够代表现代 LLM 训练范式，哪些部分需要用 DPO / DeepSeek-R1 / vLLM 等后续论文补齐？

## 阅读记录

| 日期 | 阅读模式 | 进度 | 产出 |
|---|---|---|---|
| 2026-06-02 | Structured Read | done | 形成现代 open LLM `base model -> chat model -> safety/eval/release` 端到端视角 |
