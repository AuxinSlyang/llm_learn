---
type: reading_pack
week: 2026-W24
track: CV -> VLM -> VLA -> LeRobot
status: active
created: 2026-06-09
linked_project: [[so-arm101-lerobot-first-loop]]
---

# Core Path Reading Pack - 2026-W24

## 本周目标

本周不是把所有论文精读完，而是把第一阶段路径打通：

```text
最小 CV
-> CLIP / BLIP-2 / LLaVA
-> RT-2 / LingBot / SmolVLA
-> LeRobot / SO-ARM101 bring-up
```

理论阅读必须服务两个现实产出：

1. 把两个 SO-ARM101 装起来并完成基础 bring-up。
2. 形成第一版项目理解：`observation -> state -> action -> episode -> dataset -> policy/eval`。

## 本周必读

| Priority | Paper / Material | Why |
|---|---|---|
| P0 | LeRobot paper/docs | 直接对应 SO-ARM101 数据、训练、评估与项目组织 |
| P0 | ACT / ALOHA | 双臂低成本硬件和 action chunking，最贴近 SO-ARM101 首项目 |
| P0 | BLIP-2 / LLaVA | 理解视觉信息如何进入 LLM |
| P0 | RT-2 | 理解 VLM 如何变成 action policy |
| P1 | LingBot-VLA | 理解 LeRobot-style VLA 工程流程 |
| P1 | SmolVLA | 小模型、LeRobot community data、异步推理，最贴近低成本机器人 |

## 本周只做 awareness

| Material | Why not deep now |
|---|---|
| ResNet / ViT | 先补最小 backbone 直觉，不切换成 CV 专项 |
| Diffusion Policy | 重要，但要等 LeRobot 数据闭环清楚后再细读 |
| Open X-Embodiment | 数据规模化入口，本周先知道 schema 问题 |
| Octo / OpenVLA / pi0 | VLA frontier awareness，本周不追训练 |
| World Models / DreamerV3 | 后续 planning/dynamics 入口，本周不展开 |

## Complete Paper List

### CV Foundations

| Priority | Paper | Role |
|---|---|---|
| P2 | AlexNet: ImageNet Classification with Deep Convolutional Neural Networks | 现代深度 CNN / ImageNet 起点 |
| P2 | VGG: Very Deep Convolutional Networks for Large-Scale Image Recognition | 小卷积堆叠和 depth 直觉 |
| P2 | GoogLeNet: Going Deeper with Convolutions | Inception、多尺度特征、计算效率 |
| P1 | ResNet: Deep Residual Learning for Image Recognition | residual connection，CNN backbone 核心 |
| P1 | ViT: An Image is Worth 16x16 Words | image patches as tokens，视觉 Transformer |

本阶段只要求会解释：

```text
image -> visual features / visual tokens
```

### Multimodal / VLM

| Priority | Paper | Role |
|---|---|---|
| P0 | CLIP: Learning Transferable Visual Models From Natural Language Supervision | 图文语义对齐，open-vocabulary visual representation |
| P0 | BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and LLMs | frozen vision encoder + Q-Former + frozen LLM |
| P0 | LLaVA: Visual Instruction Tuning | vision encoder + projector + LLM + visual instruction tuning |
| P2 | PaLM-E: An Embodied Multimodal Language Model | embodied multimodal reasoning awareness |

本阶段只要求会解释：

```text
vision encoder -> connector / Q-Former / projector -> LLM
```

### Robot Learning

| Priority | Paper / Material | Role |
|---|---|---|
| P0 | LeRobot: An Open-Source Library for End-to-End Robot Learning | 本项目软件栈、dataset/teleop/record/replay/eval |
| P0 | ACT / ALOHA: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware | 双臂低成本硬件、action chunking、模仿学习 |
| P1 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | action sequence generation，后续 policy 方向 |
| P2 | DAgger | covariate shift / dataset aggregation 基础 |

本阶段只要求会解释：

```text
observation -> action -> episode -> dataset -> replay/eval
```

### VLA / Foundation Robot Policy

| Priority | Paper | Role |
|---|---|---|
| P1 | RT-1: Robotics Transformer for Real-World Control at Scale | language-conditioned robot policy at scale |
| P0 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | VLM -> VLA，action-as-token |
| P1 | LingBot-VLA: A Pragmatic VLA Foundation Model | LeRobot-style VLA engineering stack |
| P1 | SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | affordable / efficient VLA，LeRobot community data，async inference |
| P2 | Open X-Embodiment | cross-robot data / schema / evaluation |
| P2 | Octo: An Open-Source Generalist Robot Policy | open generalist robot policy |
| P2 | OpenVLA: An Open-Source Vision-Language-Action Model | open VLA model / fine-tuning / deployment |
| P2 | pi0: A Vision-Language-Action Flow Model for General Robot Control | VLA + flow/action expert frontier |

本阶段只要求会解释：

```text
image + language + robot state -> action token / action chunk / continuous action
```

### World Models / Planning

| Priority | Paper | Role |
|---|---|---|
| P3 | World Models | latent world model 经典入口 |
| P3 | DreamerV3: Mastering Diverse Domains through World Models | latent dynamics + imagined rollout + policy learning |

本阶段只排队，不读。等 SO-ARM101 有 trajectory / simulation loop 后再展开：

```text
state + action -> future state
```

## 推荐顺序

### 2026-06-09

- BLIP-2 abstract / intro / Q-Former 粗读。
- LLaVA abstract / intro / projector + instruction tuning 粗读。
- 建立 VLM mental model：`vision encoder -> connector -> LLM`。

### 2026-06-10

- SO-ARM101 到货优先：开箱、清点、拍照、确认电源/线材/结构件。
- 同步读 LeRobot paper/docs，只看 dataset / teleop / train / eval。
- 晚上只快速看 ACT：`observation / action chunk / dual-arm teleop / eval`。

### 2026-06-11

- 组装两个机械臂，记录 blocker。
- 完成端口识别、motor ID、calibration 入口确认。
- 若有时间：RT-2 abstract / method action-as-token。

### 2026-06-12

- 尝试 teleop / record / replay 最小闭环。
- LingBot / SmolVLA 只看数据格式、action format、open-loop eval、deployment。

### 2026-06-13 ~ 2026-06-14

- 整理项目理解文档：
  - `bring-up checklist`
  - `data_schema.md`
  - `lingbot_smolvla_mapping.md`
  - `first_failure_log.md`

## 本周不做

- 不训练 VLA。
- 不下载大模型权重。
- 不开多卡训练。
- 不把 world model 展开成新主线。
- 不在两个机械臂未装起来前继续堆论文。
