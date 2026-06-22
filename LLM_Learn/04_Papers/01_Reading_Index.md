# Reading Index

## 当前 4 周论文队列

> `start-my-day` 默认从这里挑选 paper slot。完成后手动打勾或移动顺序。
> 如果 `04_Papers/99_Overrides/YYYY-MM-DD.md` 存在，指定日期优先读 override，不使用本队列。
> LLM 扩展论文的完整 TOREAD 清单位于：[[02_TOREAD_LLM_Papers]]
> 新 session 先读：[[00_Paper_Session_Context]]

### 2026-W23：LLM 经典论文收口队列（已读 / 收口中）

- [x] Scaling Laws for Neural Language Models: 参数量 / 数据量 / compute 和 loss 的可预测关系
- [x] Training Compute-Optimal Large Language Models (Chinchilla): 固定 compute 下参数和 token 如何配平
- [x] Training Language Models to Follow Instructions with Human Feedback (InstructGPT): SFT + RM + RLHF 的 assistant 对齐范式
- [x] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models: few-shot CoT 释放推理过程
- [x] Scaling Instruction-Finetuned Language Models (FLAN): 多任务 instruction tuning 与未见任务泛化
- [x] LLM 经典论文 takeaways 汇总：Scaling Laws / Chinchilla / InstructGPT / CoT / FLAN（见 [[03_Read_Status_Review_2026-06-07]]）

### LLM 端到端扩展队列（额外 10-15 篇，不计入已读核心 5 篇）

> 本队列服务 `tokenizer -> nanoGPT -> post-training -> reasoning/tool/context/runtime` 的端到端闭环。按兴趣和主线需要逐步读，不要求本周全部完成。
> 完整分组、链接和阅读顺序见：[[02_TOREAD_LLM_Papers]]

- [ ] Tokenizer / BPE：跟做 Karpathy tokenizer 视频与最小 BPE 实现
- [x] Llama 2：现代 open LLM 的 pretraining / SFT / RLHF / safety 工程报告
- [x] Direct Preference Optimization (DPO)：从 PPO/RLHF 到 preference optimization 的简化路线
- [x] Self-Consistency：CoT 多路径采样与答案投票
- [ ] DeepSeek-R1：reasoning RL / verifiable reward / distillation
- [x] ReAct：reasoning + acting，连接 tool use / agent / environment interaction
- [x] Toolformer：模型学习何时调用工具、传什么参数、如何使用结果
- [x] Retrieval-Augmented Generation (RAG)：外部知识检索和生成结合
- [x] RoPE / ALiBi：位置编码与长度外推直觉
- [ ] Transformer-XL：固定上下文限制与 recurrence memory
- [ ] Position Interpolation：RoPE 模型上下文扩展基础
- [ ] YaRN：高效 RoPE context window extension
- [ ] LongRoPE：更长上下文扩展路线
- [ ] LoRA / QLoRA：参数高效微调和量化微调
- [ ] Distributed Training / Parallelism：data/model/tensor/pipeline parallelism + ZeRO/FSDP，AI Infra 支撑线，见 [[Distributed_Training_Parallelism_Reading_Map]]
- [ ] MoE / Sparse Expert Routing：Sparsely-Gated MoE、Switch Transformer、GShard、Mixtral；理解 sparse compute / routing / expert parallelism，不抢 SO-ARM101 主线
- [ ] FlashAttention / FlashAttention-2：attention IO 优化与训练/推理效率
- [ ] PagedAttention / vLLM：KV cache serving 优化
- [ ] RULER / Needle-in-a-Haystack：长上下文“能放进去”和“能用起来”的评估差异
- [ ] Transformers are Inherently Succinct：Transformer succinctness / expressivity 理论支撑线；后续 30-60m scan，不抢 SO-ARM101 主线
- [ ] Transformer Is Inherently a Causal Learner：autoregressive Transformer / time-series causal discovery / gradient attribution；2026-06-22 作为 causal learner 支撑槽位保存并 structured scan

### CV / Multimodal bridge 队列（服务 VLM/VLA，不切换主线）

- 当前执行计划：[[CV_Foundation_Sprint_2026-W24]]
- 读法校准：硬件工具未到的等待期可以完整读一轮代表性 CV foundation 论文，但只服务 `robot observation -> visual backbone / visual tokens -> VLM/VLA`，不扩成完整 CV 全科。
- 2026-06-14 口头校准：VGG 已收尾，下一篇优先读 ResNet；GoogLeNet / Inception 作为 compute-aware architecture 支线后补，不阻塞 ResNet / ViT。

- [ ] CNN Primer：convolution / locality / weight sharing / feature map / pooling，AlexNet 前置概念
- [ ] LeNet-5：Gradient-Based Learning Applied to Document Recognition；PDF 已下载，早期 CNN 完整形态
- [x] AlexNet：ImageNet / deep CNN / data + GPU + ReLU，理解现代 CV 起点；background scan done
- [x] VGG：depth / small conv / simple backbone，理解深度和结构简洁性；structured quick read done
- [x] ResNet：residual connection 和 CNN backbone 基础；2026-06-15 guided structured read done，后续只需补代码/shape 精读
- [ ] GoogLeNet / Inception：multi-scale feature / compute efficiency，理解多尺度和算力约束；defer after ResNet if needed
- [ ] ViT：image patches as tokens，理解 visual tokens
- [ ] Vision Transformers Need Registers：ViT attention / feature map artifact，可解释性边界；后续 30-45m 支撑线阅读，不抢 SO-ARM101 主线
- [ ] CLIP：contrastive image-text pretraining / open vocabulary visual representation
- [ ] DINOv2：self-supervised robust visual features；服务 OpenVLA 的 spatial / dense visual feature 直觉
- [ ] SigLIP：sigmoid loss for image-text pretraining；服务 OpenVLA 的 language-aligned semantic feature 直觉
- [ ] BLIP-2：frozen image encoder + Q-Former + frozen LLM
- [ ] LLaVA：visual instruction tuning
- [ ] YOLO family：real-time object detection；PDF 已下载，作为后续 robot perception / data labeling / failure analysis / object-centric task 的实用模块，不替代 VLA。
- [ ] Diffusion Models for Generative Vision：DDPM / DDIM / Score SDE / Latent Diffusion；只做 awareness scan，理解 image generation 和 Diffusion Policy 的桥。
- [ ] RT-2：VLM 输出 action-as-token
- [ ] LingBot-VLA：LeRobot-style VLA 工程流程
- [ ] SmolVLA：LeRobot community data、小模型、异步推理和 affordable robotics
- [ ] LeRobot：SO-ARM101 项目软件栈入口
- [ ] Vision Banana / Image Generators are Generalist Vision Learners：生成式视觉统一范式，SO-ARM101 首闭环后作为 CV foundation 专题阅读

### VLA 第一阶段核心队列（SO-ARM101 对齐）

> 详细分层见：[[VLA_First_Stage_Reading_Plan]]

- [ ] ACT：第一阶段最现实的 imitation learning policy，优先和 LeRobot 训练链路对应
- [ ] XLeRobot：SO101 双臂 / 移动底盘 / 社区工程参考，先扫 bring-up 和硬件流程
- [ ] LingBot-VLA：LeRobot-style VLA 工程流程，重点看 dataset/config/eval/deploy
- [ ] SmolVLA：小模型、consumer hardware、异步推理和 affordable robotics
- [ ] OpenVLA：开源 7B VLA、Open X 数据、fine-tune/deploy 路线
- [ ] PI0：flow matching action expert 和连续动作 VLA
- [ ] PI0-FAST：FAST action tokenizer，理解 autoregressive VLA 动作表示
- [ ] PI0.5：异构数据 co-training 与 open-world generalization

### Diffusion / Flow / Action Generation Track

> 独立入口：[[25_Diffusion_Flow_and_Action_Generation/README]]

- [ ] DDPM / DDIM / Score SDE：理解 noising / denoising / score 视角
- [ ] Flow Matching / Rectified Flow：理解 pi0 action expert 背后的 flow 直觉
- [ ] Latent Diffusion：理解 latent-space generation 的工程动机
- [ ] Diffusion Policy：理解 `observation + noisy action sequence -> denoised action sequence`
- [ ] pi0 / pi0-FAST 对照：flow action expert vs action tokenizer

### 2026-W24 起：Robot Learning 队列

- [ ] RL for Robot Learning Reading Map: reward-driven improvement / continuous control / offline RL / world-model RL 支撑线；不抢 OpenVLA / pi0 主线
- [ ] DAgger: dataset aggregation and covariate shift
- [ ] ACT: action chunking for fine-grained manipulation
- [ ] Diffusion Policy: action generation as conditional denoising
- [ ] RT-1: scalable real-world robot learning with language-conditioned policies
- [ ] RT-2: VLM-to-VLA transfer from web knowledge to robot control
- [ ] Open X-Embodiment: cross-robot data and RT-X style generalization
- [ ] Octo: open generalist robot policy
- [ ] OpenVLA: open vision-language-action model
- [ ] PI0: flow-based general robot policy

## 分类

### 10 AI Foundations

| 材料 | 价值 | 状态 |
|---|---|---|
| The Bitter Lesson | 判断 AI 系统长期趋势，不迷信手工规则 | 已有 insight，可回看 |
| Finding Structure in Time | 理解简单 RNN / Elman network 如何表示时间和记忆 | skimmed / 前传直觉已建立 |
| Long Short-Term Memory | 理解 LSTM 如何缓解 RNN 长距离依赖问题 | skimmed / 前传直觉已建立 |
| Sequence to Sequence Learning with Neural Networks | 理解 Transformer 前的 encoder-decoder seq2seq 框架 | Quick Read done |
| Neural Machine Translation by Jointly Learning to Align and Translate | 理解 attention 如何解决 fixed-length vector 瓶颈 | Quick Read done |
| Attention Is All You Need | Transformer / attention 基础 | Structured Read done，可回看 nanoGPT 映射 |
| Transformers are Inherently Succinct | 从 succinctness 角度理解 Transformer 为什么能紧凑表达复杂模式 | queued / follow-up theory scan |
| GPT-1: Improving Language Understanding by Generative Pre-Training | 理解 decoder-only Transformer 如何变成通用预训练语言模型 | Quick Read done |
| GPT-2: Language Models are Unsupervised Multitask Learners | 理解规模化 LM 如何出现 zero-shot / 无监督多任务能力 | Quick Read done |
| GPT-3: Language Models are Few-Shot Learners | 理解 in-context learning / few-shot prompting 如何成为新范式 | Quick Read done |
| Scaling Laws for Neural Language Models | 理解参数量 / 数据量 / compute 和 loss 的可预测关系 | Quick Read done |
| Training Compute-Optimal Large Language Models (Chinchilla) | 理解固定 compute 下参数和 token 如何配平 | Quick Read done |
| InstructGPT / RLHF | 理解 base LM 如何通过 SFT + RM + RLHF 变得更会跟随指令 | Quick Read done |
| Chain-of-Thought Prompting | 理解中间推理步骤如何释放大模型复杂任务能力 | Quick Read done |
| Scaling Instruction-Finetuned Language Models (FLAN) | 理解多任务 instruction tuning 如何提升未见任务泛化 | Quick Read done |
| Distributed Training / Parallelism Reading Map | data/model/tensor/pipeline parallelism、ZeRO/FSDP，支撑 LLM/VLA training infra 直觉 | queued / AI Infra support |
| ResNet / ViT | CV 表征基础 | CS231n/CV 入口阶段选读 |
| Vision Transformers Need Registers | ViT attention / feature map artifact，可解释性边界 | queued / follow-up support |

### 15 CV Foundations

| 材料 | 价值 | 状态 |
|---|---|---|
| AlexNet | 现代深度 CNN / ImageNet 起点 | background scan done |
| VGG | 小卷积堆叠和 depth 直觉 | structured quick read done |
| GoogLeNet / Inception | 多尺度特征和计算效率 | downloaded / background scan |
| ResNet | residual connection 和深层 CNN backbone | guided read done; code/shape follow-up |
| ViT | image patches as tokens，视觉 Transformer | downloaded / structured read later |
| Vision Transformers Need Registers | register tokens 修复 ViT attention / feature map artifact，校准 attention visualization 的解释边界 | queued / follow-up support |
| DINOv2 | self-supervised robust visual features，解释 OpenVLA 为什么需要 spatial / dense visual representation | queued / OpenVLA support |
| SigLIP | image-text alignment 的 sigmoid loss 路线，解释 OpenVLA 为什么需要 language-aligned semantic visual features | queued / OpenVLA support |
| Vision Banana / Image Generators are Generalist Vision Learners | 生成式视觉模型作为 generalist vision learner，观察是否形成 CV 的 GPT-style 统一接口 | follow-up after SO-ARM101 first loop |

### 20 Robot Learning

| 论文 | 价值 | 建议时间 |
|---|---|---|
| RL for Robot Learning Reading Map | 把 DQN / PPO / SAC / HER / offline RL / QT-Opt / DreamerV3 接到 robot policy data loop | OpenVLA / pi0 第一轮后，作为 P2 支撑线 |
| DAgger | 理解 BC 的分布偏移问题 | 2026-08/09 |
| ACT / ALOHA | manipulation imitation learning 入口 | 2026-09 |
| Diffusion Policy | robot action generation 经典路线 | 2026-09/10 |

### 30 VLA And Foundation Policies

| 论文 | 价值 | 建议时间 |
|---|---|---|
| RT-1 | language-conditioned robot policy 早期系统化路线 | 2026-11 |
| RT-2 | VLM knowledge transfer to robotic action | 2026-11 |
| SmolVLA | affordable / efficient VLA, LeRobot community data | W24 awareness |
| Octo | open generalist robot policy | 2026-11/12 |
| OpenVLA | open VLA model and deployment awareness | 2026-11/12 |
| PI0 | general robot policy frontier awareness | 2026-11/12 |

### 40 Data And Eval

| 材料 | 价值 | 建议时间 |
|---|---|---|
| Open X-Embodiment | robot data scale, heterogeneity, embodiment gap | 2026-10/11 |
| LeRobot | practical dataset / policy / eval stack | W24 P0 |
| RoboMimic / robosuite materials | imitation learning dataset and benchmark awareness | 2026-09/10 |

### 50 World Models

| 材料 | 价值 | 建议时间 |
|---|---|---|
| World Models | latent dynamics / imagination 经典入口 | SO-ARM101 有数据闭环后 |
| DreamerV3 | model-based RL / latent world model | 后续 simulation / planning 阶段 |

## 读完后的沉淀标准

每篇论文目录至少保留：

- `QUICK_READ.md`：通读 / 核心思路 / takeaway
- `DEEP_READ.md`：精读 / 公式细节 / 训练推理 / 实验分析
- `README.md`：可选，仅用于目录或论文资源介绍，不作为默认阅读笔记
- `takeaways.md`：真正能迁移到项目里的 idea
- 可选 `links.md`：代码、项目主页、复现资料
