---
type: paper_session_context
status: active
updated: 2026-06-14
scope: paper_reading_bootstrap / daily_routine_context / current_learning_state
---

# Paper Session Context

新开论文阅读或学习 session 时，先读这个文件。它保存当前学习主线、已读论文、待读队列、daily routine 和近期执行状态，避免不同 ChatGPT / Codex session 之间丢上下文。

这个文件不是每篇论文的完整笔记，也不是替代 Daily / Weekly / Monthly；它是“启动总览”。具体细节仍回到对应 Daily、Weekly、paper note 和 project note。

## 启动读序

新 session 默认按这个顺序读：

1. `04_Papers/00_Paper_Session_Context.md`
2. `04_Papers/01_Reading_Index.md`
3. 当前 sprint / map：
   - `04_Papers/15_CV_Foundations/CV_Foundation_Sprint_2026-W24.md`
   - `04_Papers/Core_Path_Reading_Pack_2026-W24.md`
   - `04_Papers/30_VLA_and_Foundation_Policies/VLA_First_Stage_Reading_Plan.md`
   - `04_Papers/30_VLA_and_Foundation_Policies/VLA_VLM_Foundation_Map.md`
4. 当前论文 `QUICK_READ.md`
5. 如果是 daily planning，再读：
   - 今日 Daily
   - 前 7 天 Daily
   - 本周 Weekly
   - 本月 Monthly
   - `00_Roadmap/09_One_Year_Robot_Learning_Full_Stack_Roadmap.md`
   - `00_Roadmap/08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime.md`

## 权威事实来源

本文件最近一次汇总时扫描过：

- Daily：`01_DailyNotes/2026/2026-06/2026-06-08.md` 到 `2026-06-14.md`
- Weekly：`02_WeeklyNotes/2026/2026-06/2026-W24.md`、`2026-W25.md`
- Monthly：`07_MonthlyPlans/2026/2026-06_月计划.md`
- Roadmap：
  - `00_Roadmap/09_One_Year_Robot_Learning_Full_Stack_Roadmap.md`
  - `00_Roadmap/08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime.md`
- Paper workflow / queues：
  - `04_Papers/00_Reading_Workflow.md`
  - `04_Papers/01_Reading_Index.md`
  - `04_Papers/02_TOREAD_LLM_Papers.md`
  - `04_Papers/03_Read_Status_Review_2026-06-07.md`
  - `04_Papers/Core_Path_Reading_Pack_2026-W24.md`
  - `04_Papers/15_CV_Foundations/CV_Foundation_Sprint_2026-W24.md`
  - `04_Papers/30_VLA_and_Foundation_Policies/VLA_First_Stage_Reading_Plan.md`
  - `04_Papers/30_VLA_and_Foundation_Policies/VLA_VLM_Foundation_Map.md`
  - `04_Papers/35_Multimodal_Foundations/Multimodal_Model_Map.md`
- Project：
  - `03_Projects/so-arm101-lerobot-first-loop/README.md`
  - `03_Projects/so-arm101-lerobot-first-loop/notes/lerobot_code_map.md`
- Routines：
  - `skills/start-my-day/SKILL.md`
  - `10_Workflows/skills/end-my-day/SKILL.md`
  - `skills/end-of-this-week/SKILL.md`
  - `10_Workflows/skills/end-of-this-month/SKILL.md`
  - `$CODEX_HOME/automations/daily-start-my-day/memory.md`

## 上位目标

当前工作区角色：

```text
具身智能 / 机器人系统 / 语言智能 / AI Infra 学习规划与知识沉淀助手
```

短期职业目标：

```text
Embodied AI Software Engineer
/ Robot Learning Infra
/ Policy Runtime
/ 机器人全栈工程入口
```

长期能力目标：

```text
roboticist:
机器人本体 + 感知 + 控制 + 学习 + runtime + 数据闭环 + 语言智能
```

当前上位主线：

```text
Robot Learning Full-Stack
-> SO-ARM101 + LeRobot 首个真实硬件闭环
-> observation/state/action/dataset/replay/train/eval/failure loop
```

LLM / AI Infra 的定位：

```text
支撑 VLA / policy runtime / edge inference / 多机器人语言协作
不是当前唯一主线
```

## 当前阶段状态

当前日期：`2026-06-14`。

当前月：`2026-06`。

月主题：

```text
LLM phase 1 收口
+ tokenizer / nanoGPT / GPT-2 主链路
+ SO-ARM101 / LeRobot 首个真实机器人闭环
```

W24：`2026-06-08 ~ 2026-06-14`

- 主题：`SO-ARM101 + LeRobot 实物首闭环启动周`
- 已完成：
  - SO-ARM101 已采购并到货初检。
  - BOM / 项目目录 / LeRobot 数据链路 / ACT/ALOHA 第一轮理解已建立。
  - CV foundation 在硬件工具等待期启动。
  - LeRobot 官方源码 code map 已建立，当前 commit `8515d456be1dbef8c133f07188c785e683eca899`。
- 阻塞：
  - 摄像头 / 螺丝刀 / 万用表 / 桌面固定等工具状态仍是硬件 gate。
  - 未进入真实装配、通电、端口识别、motor ID、calibration、teleop。
  - tokenizer / nanoGPT 一页收口仍未完成。

W25：`2026-06-15 ~ 2026-06-21`

- 主题：`SO-ARM101 coding first loop`
- 硬产出：
  - `E001_hardware_bringup`
  - `E002_dataset_recording`
  - `E003_replay`
  - `project coding scaffold`
- 最低完成线：
  - 硬件识别 / 端口 / 电机 ID / calibration 记录。
  - 完成一次 teleoperation。
  - 录制 3-5 条短 episode。
  - replay 至少 1 条 episode。
  - 建立命令记录、dataset path、episode log、eval stub。
  - 如果硬件继续阻塞，做 LeRobot 命令 walkthrough / mock dataset / Gymnasium smoke test，并写 blocker report。

## Daily / Weekly / Monthly Routine

### start-my-day

触发：今天做什么、start my day、今日计划、对齐本周 / 本月 / roadmap。

读序：

```text
今日 Daily
-> 前 7 天 Daily
-> 本周 Weekly
-> 本月 Monthly
-> Roadmap
-> paper context / reading index / current pack / VLA maps
-> automation memory
-> 今日 paper override
```

输出：

- 方向锚点
- 本周 / 今日目标
- 最低完成线
- 建议顺序
- 今日 Top 3
- 今日论文槽位
- 时间切片
- 后续 2-3 天递进安排
- 对应文件或命令

规则：

- 用户口头校准优先于旧笔记。
- 工作日默认白天 paper slot 20-40m，晚上主线 90m。
- paper slot 不抢当前周硬产出。
- 周末 paper reading 可选；硬件 / 项目证据优先。
- 如果 `04_Papers/99_Overrides/YYYY-MM-DD.md` 存在，paper slot 必须优先使用 override。

### end-my-day

触发：今天到这里、收工、复盘今天、end my day。

读序：

```text
今日 Daily
-> 本周 Weekly
-> 本月 Monthly
-> Robot Learning roadmap
-> runtime support roadmap
-> 今天触碰的 paper notes
-> automation memory
```

输出：

- 今日实际完成
- 未完成与原因
- 今日学习证据
- 明天唯一主线
- 明天最低完成线
- 明天承接点

如果是周五 / 周日 / 本周最后学习日，会触发 weekly close logic。

### end-of-this-week

触发：周复盘、close this week、end-of-this-week。

读序：

```text
本周 Weekly
-> 本周 Daily
-> 本月 Monthly
-> Roadmap
```

输出：

- 本周完成
- 本周未完成
- 本周阻塞 / 风险
- 下周承接
- 是否需要调整月计划

### end-of-this-month

触发：月末复盘、monthly review、end-of-this-month。

读序：

```text
当前 Monthly
-> 本月 Weekly
-> 本月 Daily
-> Robot Learning roadmap
-> Annual plan
-> paper index / touched paper notes
-> project notes
-> next month plan
```

输出：

- 本月实际完成
- 计划对照
- 未完成与原因
- 路线调整
- 本月学习证据
- 下月最低完成线
- 下月 Top 3

当前待补：`2026-05` 月末复盘仍是历史待补事项，但不打断 W24/W25 的 SO-ARM101 主线。

## 近期 7 天学习轨迹

### 2026-06-08

- SO-ARM101 已下单，预计 2026-06-10 到货。
- 完成 PagedAttention / vLLM quick scan：KV cache paging / block table / COW / latency-throughput。
- 建立 `CLIP -> BLIP-2 / LLaVA -> RT-2 -> LingBot-VLA` 粗扫链路。
- tokenizer 一页总结未完成。

### 2026-06-09

- 今日目标切到 RT-2 action representation + LingBot-VLA engineering walkthrough + SO-ARM101 到货前 checklist。
- 明确不扩完整 CV/VLM 专项，只沿 `vision encoder -> connector/LLM -> action/runtime -> LeRobot data schema` 推进。

### 2026-06-10

- SO-ARM101 到货优先。
- paper slot 选 LeRobot paper/docs。
- 今日方向：真实硬件 bring-up；如果硬件未到，补 LeRobot 命令链路和 checklist。

### 2026-06-11

- 完成 LeRobot real-robot imitation learning 主链路理解：

```text
teleop -> record -> visualize -> replay -> train -> inference/eval -> failure log
```

- 理解 LeRobotDataset v3.0：

```text
parquet: state/action/timestamp
mp4: videos
metadata: schema / episode / task / features
```

- 完成 ACT/ALOHA 第一轮结构化阅读：
  - leader/follower teleop
  - action chunking
  - temporal ensemble
  - CVAE z
  - real eval

### 2026-06-12

- 轻量收口日。
- 继续 LeNet-5 Section 3/4/5/7：
  - CNN local-to-global feature hierarchy。
  - GTN：graph-in/graph-out 的 trainable multi-module system，不是现代 Transformer。
  - segmentation graph / recognition transformer / Viterbi path / discriminative Viterbi training / Forward scoring。
- hardware tools 仍是阻塞，不做装配、通电、端口或校准。

### 2026-06-13

- 周六不新开 VLA / world model / detection / robotics 大主题。
- 计划：LLM phase 1 closure + LeNet/AlexNet/ResNet bridge + 周日硬件 gate。
- ResNet 原本被安排为今日 slot，但实际后续被 VGG / ResNet 顺序校准覆盖。

### 2026-06-14

- 早期目标曾校准为 `ViT + LeRobot code analysis`。
- 已完成 LeRobot 官方源码整体 code map：

```text
robot / teleoperator abstraction
-> teleop
-> record
-> replay
-> train
-> eval / rollout
```

- 最后 paper slot 改为 VGG structured quick read，已收尾：
  - VGG 核心：`depth matters`。
  - `3x3 conv` stack 扩大 effective receptive field、增加 non-linearity、参数可控。
  - VGG 自然引出 ResNet 的 degradation / optimization problem。
- 已新增本文件作为跨 session paper context。

## 当前项目上下文：SO-ARM101 + LeRobot

项目定位：

```text
SO-ARM101 leader/follower
-> assemble / calibrate
-> teleop
-> record demonstrations
-> replay
-> train ACT / small policy
-> real eval
-> failure note
```

第一阶段不做：

- 不训练 LingBot-VLA 4B。
- 不买 Jetson / Orin / Thor / RealSense / 3D 打印机作为首闭环依赖。
- 不追复杂任务和机械改造。
- 不提前追 VLA frontier 训练。

当前 LeRobot code map 已知入口：

- `lerobot-find-port`
- `lerobot-setup-motors`
- `lerobot-calibrate`
- `lerobot-teleoperate`
- `lerobot-record`
- `lerobot-replay`
- `lerobot-train`
- `lerobot-eval`
- `lerobot-rollout`

核心抽象：

- `Robot`
  - `get_observation()`
  - `send_action(action)`
  - `observation_features`
  - `action_features`
- `Teleoperator`
  - `get_action()`
  - `action_features`
- `LeRobotDataset`
- `Policy`

SO101 数据接口直觉：

```text
leader Present_Position
-> action: shoulder_pan.pos / shoulder_lift.pos / elbow_flex.pos / wrist_flex.pos / wrist_roll.pos / gripper.pos
-> follower Goal_Position
```

Record flow：

```text
robot.get_observation()
-> build observation frame
teleop.get_action()
-> processor
-> robot.send_action()
-> build action frame
-> dataset.add_frame()
-> dataset.save_episode()
```

W25 先追真实命令与实验记录，不追策略效果。

## Paper Reading 规则

默认读法：

- 先做 `Structured Quick Read`。
- 只有当前项目强相关时再 Deep Read。
- 每篇至少留下：
  - one-sentence takeaway
  - core concept
  - historical position
  - 和 Robot Learning / VLA / runtime 的连接
  - open questions

当前 paper slot 原则：

- 论文服务项目，不替代项目。
- W25 paper slot 降级为 project explainer，只解释 SO-ARM101 / LeRobot 当前问题。
- 如果硬件可推进，优先硬件和数据闭环。
- 如果硬件阻塞，才补 CV / VLA / LLM 支撑线。

## 已读 / 已建立直觉：AI Foundations

### Transformer 前传和 GPT 主线

- `Finding Structure in Time`：skimmed。RNN 用内部状态处理时间，但串行且长依赖困难。
- `Long Short-Term Memory`：skimmed。LSTM 用 gates / cell state 缓解长程记忆问题。
- `Sequence to Sequence Learning with Neural Networks`：done。encoder-decoder seq2seq。
- `Neural Machine Translation by Jointly Learning to Align and Translate`：done。Bahdanau attention 动态读取 source states。
- `Attention Is All You Need`：structured read done。Transformer 用 attention 作为主计算机制；GPT/nanoGPT 继承 decoder-only causal self-attention。
- `GPT-1`：done。pretrain -> supervised fine-tune。
- `GPT-2`：done。更大 LM 出现 zero-shot task framing。
- `GPT-3`：done。in-context examples -> few-shot behavior。

### Scaling / Post-training / Reasoning

- `Scaling Laws`：done。参数量 / 数据量 / compute 与 loss 存在稳定规律。
- `Chinchilla`：done。固定 compute 下参数与 tokens 要配平。
- `InstructGPT / RLHF`：done。base LM -> SFT -> RM -> PPO/RLHF。
- `Chain-of-Thought`：done。中间推理 token 释放复杂任务能力，但不保证 faithful。
- `FLAN`：done。多任务 instruction tuning 提升 unseen-task generalization。
- `Llama 2`：done。现代 open LLM 的 pretraining / SFT / RLHF / safety / eval / release 工程报告。
- `DPO`：done。用 reference-constrained preference loss 简化 RLHF。
- `Self-Consistency`：done。test-time 多路径 CoT + answer voting。
- `ReAct`：done。`Thought -> Action -> Observation` 是高层 agent/runtime loop。
- `Toolformer`：done。模型学习何时调用工具、传什么参数、如何利用结果。
- `RAG`：done。外部检索记忆接入生成模型。

### Position / Context / Runtime 支撑线

- `RoPE / RoFormer`：done。对 q/k 按位置旋转，使 attention 内积携带相对距离。
- `ALiBi`：done。attention logits 上加 head-specific 距离惩罚。
- `PagedAttention / vLLM`：in progress / quick scan done。核心是 KV cache memory paging，不是新 attention 数学。
- `Transformers are Inherently Succinct`：queued。后续理论支撑线，不抢项目。

LLM 未完成收口：

- `tokenizer / BPE` 一页总结未完成。
- `nanoGPT 主链路总结 v0` 未完成。
- `LLM phase 1 总结` 未完成。

## 已读 / 当前：CV Foundations

当前 CV 只服务：

```text
camera image
-> visual backbone / visual tokens
-> multimodal connector
-> LLM / VLA / policy
```

不扩成完整 CV 全科。

### 已建立

- `CNN Primer`：active。已建立 convolution / locality / weight sharing / feature map / pooling / CNN inductive bias。
- `LeNet-5`：downloaded but actually read beyond first pass。已理解 early CNN、subsampling、GTN、segmentation graph、Viterbi / Forward training。
- `AlexNet`：background scan done。核心是 `ImageNet + deep CNN + GPU + ReLU + augmentation/dropout + end-to-end training`。
- `VGG`：structured quick read done。核心是 `depth matters`，`3x3 conv` stack 让深度增加参数可控并形成强 visual backbone。

### 当前

当前下一篇：`ResNet - Deep Residual Learning for Image Recognition`

ResNet 本轮只回答：

- 什么是 degradation problem？
- 为什么 plain deep network 不是简单“更深就更好”？
- `y = F(x) + x` 为什么让深层网络更容易优化？
- ResNet 和后续 ViT / CLIP / VLA visual encoder 的关系是什么？

已读 ResNet Abstract / Introduction 的第一性理解：

```text
VGG 证明 depth matters。
ResNet 问：继续堆层是否就够？
答案：不是。plain deeper network 会出现 training error 反而更高的 degradation problem。
Residual learning 让新增层只学习 F(x)=H(x)-x，并通过 identity shortcut 保留 x。
```

### 下一步

建议顺序：

```text
ResNet
-> ViT
-> Vision Transformers Need Registers
-> CLIP / BLIP-2 / LLaVA 回看或补桥
```

口头校准：

- 原 sprint 中 `GoogLeNet / Inception` 排在 ResNet 前。
- 但当前先读 ResNet，再读 ViT。
- `GoogLeNet / Inception` 作为 compute-aware architecture 支线后补，不阻塞 ResNet / ViT。

### CV 后续 / 支线

- `GoogLeNet / Inception`：downloaded。多尺度 feature + compute-aware architecture，后补。
- `ViT`：queued after ResNet。image patches as tokens。
- `Vision Transformers Need Registers`：queued。ViT attention / feature artifact / interpretability。
- `YOLO family`：downloaded。后续 robot perception / labeling / failure analysis 支线，不抢当前。
- `Diffusion Models for Generative Vision`：queued awareness。只为理解生成式视觉和 Diffusion Policy 的桥。

CV 历史链条：

```text
LeNet
-> AlexNet
-> VGG
-> ResNet
-> ViT
-> CLIP
-> BLIP-2 / LLaVA
-> VLA / robot policy
```

一句话版本：

- LeNet：CNN + backprop 的早期范式。
- AlexNet：CNN + GPU + ImageNet，证明大规模端到端视觉训练可行。
- VGG：证明 depth 对视觉表征很重要。
- ResNet：解决 plain deep CNN 继续加深后的 optimization / degradation problem。
- ViT：把图像 patch 转成 token sequence，进入 Transformer vision 范式。
- CLIP：image-text contrastive alignment，进入 open-vocabulary vision。
- BLIP-2 / LLaVA：frozen vision encoder 接 LLM，进入 VLM。

## Multimodal / VLM / VLA 队列

### VLM bridge

- `CLIP`：downloaded / prior pass。图文 contrastive alignment，open-vocabulary visual representation。
- `BLIP-2`：downloaded / prior pass。frozen vision encoder + Q-Former + frozen LLM。
- `LLaVA`：downloaded / prior pass。vision encoder + projector + LLM + visual instruction tuning。
- `PaLM-E`：downloaded。embodied multimodal LM awareness。

VLM mental model：

```text
vision encoder output
-> connector / Q-Former / projector
-> LLM-compatible token embeddings
-> generation / instruction following
```

### VLA / Foundation Robot Policy

- `RT-1`：downloaded。language-conditioned robot policy at scale，待读。
- `RT-2`：downloaded / first pass。VLM -> VLA，action-as-token。
- `LingBot-VLA`：downloaded。LeRobot-style VLA engineering stack，项目 walkthrough。
- `SmolVLA`：downloaded。affordable / efficient VLA，LeRobot community data，async inference。
- `OpenVLA`：downloaded。open VLA，Open X 数据，fine-tune/deploy awareness。
- `pi0`：downloaded。flow matching action expert，continuous action VLA frontier。
- `Octo`：downloaded。open generalist robot policy。

第一阶段 VLA 阅读顺序：

```text
ACT
-> LeRobot ACT training / dataset flow
-> LingBot-VLA project walkthrough
-> SmolVLA
-> OpenVLA
-> pi0
-> pi0-FAST
-> pi0.5
```

但当前 W25 不按这个顺序硬读论文；W25 优先硬件 / teleop / record / replay。

## Robot Learning / Data / Eval / World Models

### Robot Learning

- `LeRobot paper/docs`：downloaded / project must read。直接对应 SO-ARM101 数据、训练、评估。
- `ACT / ALOHA`：downloaded / first structured pass。当前最贴近 LeRobot 首闭环的 imitation learning policy。
- `DAgger`：planned quick scan。BC covariate shift / dataset aggregation，发现 policy drift 后读。
- `Diffusion Policy`：downloaded。ACT 跑通后再读，用来理解 action sequence denoising。

### Data / Eval

- `Open X-Embodiment`：PDF downloaded / later。cross-robot data and RT-X style generalization。
- `LeRobot`：当前实操软件栈入口。

### World Models

- `World Models`：downloaded。
- `DreamerV3`：downloaded。
- 当前不读。等 SO-ARM101 有 trajectory / simulation loop 后再进入：

```text
state + action -> future state
```

## 还有哪些想看但没看

### 近期可能看

- ResNet：当前。
- ViT：ResNet 后。
- Vision Transformers Need Registers：ViT 后的解释性支线。
- CLIP / BLIP-2 / LLaVA：如果 ViT 后需要桥到 VLM，可回看并补齐。
- LingBot-VLA / SmolVLA：硬件数据闭环跑通后做 engineering walkthrough。
- ACT：teleop/record/replay 之后，进入训练 ACT/BC v0 时回看 method。

### 支撑线，暂不抢主线

- GoogLeNet / Inception：compute-aware architecture。
- YOLO family：object detection / labeling / failure analysis。
- Diffusion Policy：action generation as denoising。
- DAgger：policy drift / dataset aggregation。
- LoRA / QLoRA：低显存微调。
- FlashAttention / FlashAttention-2：attention IO optimization。
- Position Interpolation / YaRN / LongRoPE / RULER：long context。
- Distributed Training / Parallelism：data/model/tensor/pipeline parallelism、ZeRO/FSDP、Megatron/GPipe 等。
- Transformers are Inherently Succinct：Transformer expressivity / theory。

### 雷达，不进入当前阶段

- OpenVLA full fine-tuning。
- pi0 / pi0-FAST / pi0.5 深读。
- Open X full data system。
- World Models / DreamerV3。
- DETR / SAM / DINO / MAE / Swin。
- Vision Banana / Image Generators are Generalist Vision Learners。

## 当前不要做什么

- 不把 CV foundation 扩成完整 CV 全科。
- 不同时完整刷 CS231n、Modern Robotics、CS285。
- 不让 LLM inference / AI Infra 抢走 SO-ARM101 主线。
- 不在 record/replay 之前训练大 VLA。
- 不追 LingBot-VLA 4B full post-training。
- 不买 Jetson/Orin/Thor/RealSense/3D 打印机作为首轮依赖。
- 不让 paper slot 消耗 W25 的硬件 / 数据闭环时间。

## 当前最重要的 open loops

- `SO-ARM101`：工具 gate -> hardware validation -> ports / motor ID / calibration -> teleop。
- `LeRobot`：从 code map 进入真实命令记录和 project coding scaffold。
- `Dataset`：录制 3-5 条 episode，replay 1 条。
- `LLM closure`：tokenizer / BPE 一页总结；nanoGPT 主链路总结。
- `CV`：ResNet structured read；再进入 ViT。
- `VLA`：等 LeRobot record/replay 有证据后，回到 ACT / LingBot / SmolVLA。

## 当前下一步

如果下一个 session 是论文阅读：

```text
读 ResNet Section 3: Deep Residual Learning
重点看 F(x)+x, shortcut connection, dimension matching, plain vs residual comparison
```

如果下一个 session 是项目执行：

```text
打开 SO-ARM101 experiment log
确认工具 / USB / 电源 / 摄像头 / 桌面固定
推进 E001 hardware bring-up 或写 blocker
```

如果下一个 session 是 daily planning：

```text
运行 start-my-day
但保持 W25 唯一主线：hardware validation -> teleop -> record -> replay -> coding scaffold
```

