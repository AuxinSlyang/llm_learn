---
type: reading_map
track: VLA / VLM / robot runtime
status: draft
created: 2026-06-08
linked_project: [[so-arm101-lerobot-first-loop]]
---

# VLA / VLM Foundation Map

## 今日目标

今天不精读整条 VLA/VLM 历史，只建立第一版谱系：

```text
vision-language representation
-> embodied multimodal reasoning
-> vision-language-action policy
-> robot runtime / deployment
```

## 今日读法

今天用 `VLM bridge mini-scan -> RT-2 VLA entry` 的方式读：

```text
CLIP
-> BLIP-2 / LLaVA
-> RT-2
-> LingBot-VLA project walkthrough
```

目标不是把每篇都精读，而是理解两个跃迁：

1. `LLM -> VLM`：图像如何进入语言模型。
2. `VLM -> VLA`：动作如何进入模型输出空间。

## 下一步阅读顺序

2026-06-08 只进入第 1-2 步：

1. `CLIP`：mini-scan，图文对齐和 zero-shot transfer。
2. `BLIP-2 / LLaVA`：mini-scan，vision encoder / connector / LLM / instruction tuning。
3. `RT-2`：主读，回答 VLM 如何变成 VLA，以及 action 如何被模型预测。
4. `PaLM-E`：2026-06-09 或后续补，理解 embodied multimodal language model 如何接收图像、语言和机器人状态。
5. `OpenVLA`：后续补，理解开放 VLA 模型、数据和 deployment awareness。
6. `LingBot-VLA`：项目 walkthrough，映射到 LeRobot / SO-ARM101 的 observation/action/schema/runtime。

2026-06-10 预计 SO-ARM101 到货，阅读必须让位给开箱清点、组装和 bring-up。

2026-06-10 更新：VLA 第一阶段不再继续无差别扩论文数量，改为围绕 SO-ARM101 首闭环组织：

```text
ACT / LeRobot
-> LingBot-VLA / SmolVLA
-> OpenVLA
-> PI0 / PI0-FAST / PI0.5
```

详细执行队列见：[[VLA_First_Stage_Reading_Plan]]

## Paper Links

| Paper | Link | 今日问题 |
|---|---|---|
| CLIP: Learning Transferable Visual Models From Natural Language Supervision | https://arxiv.org/abs/2103.00020 | image/text 如何对齐？ |
| BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models | https://arxiv.org/abs/2301.12597 | frozen vision encoder 和 frozen LLM 之间如何桥接？ |
| LLaVA: Visual Instruction Tuning | https://arxiv.org/abs/2304.08485 | visual instruction tuning 如何让 VLM 能对话？ |
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | https://arxiv.org/abs/2307.15818 | robot action 如何 tokenized 并接入 VLM？ |
| LingBot-VLA: A Pragmatic VLA Foundation Model | https://arxiv.org/abs/2601.18692 | VLA 如何变成工程化数据/训练/eval/deploy 栈？ |

## Local Download / Notes

| Material | Local PDF | Quick note | 今晚状态 |
|---|---|---|---|
| CLIP | `CLIP_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision/CLIP_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision.pdf` | `CLIP_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision/QUICK_READ.md` | downloaded, mini-scan entry |
| BLIP-2 | `BLIP_2_Bootstrapping_Language_Image_Pretraining/BLIP_2_Bootstrapping_Language_Image_Pretraining.pdf` | `BLIP_2_Bootstrapping_Language_Image_Pretraining/QUICK_READ.md` | downloaded, mini-scan entry |
| LLaVA | `LLaVA_Visual_Instruction_Tuning/LLaVA_Visual_Instruction_Tuning.pdf` | `LLaVA_Visual_Instruction_Tuning/QUICK_READ.md` | downloaded, mini-scan entry |
| RT-2 | `RT_2/RT_2_Vision_Language_Action_Models_Transfer_Web_Knowledge_to_Robotic_Control.pdf` | `RT_2/QUICK_READ.md` | downloaded, tomorrow structured read |
| LingBot-VLA | `LingBot_VLA_A_Pragmatic_VLA_Foundation_Model/LingBot_VLA_A_Pragmatic_VLA_Foundation_Model.pdf` | `LingBot_VLA_A_Pragmatic_VLA_Foundation_Model/QUICK_READ.md` | downloaded, tomorrow project walkthrough |

## Supporting Maps

| Map | Purpose |
|---|---|
| `../35_Multimodal_Foundations/Multimodal_Model_Map.md` | 多模态模型从 CLIP 到 BLIP-2 / LLaVA / VLA 的路线图 |
| `../15_CV_Foundations/README.md` | ResNet / ViT 等视觉 backbone 补课入口 |

## 建索引

| 位置 | 代表材料 | 今天只问 |
|---|---|---|
| VLM 表征 | CLIP | 图像和语言如何对齐到同一语义空间？ |
| 多模态生成 / instruction VLM | BLIP-2 / LLaVA | 视觉 token 如何接入 LLM，如何做 instruction tuning？ |
| VLA policy | RT-1 / RT-2 | action 如何被模型预测，和普通文本 token 有什么关系？ |
| 开放 VLA | OpenVLA / LingBot-VLA | 模型、数据 schema、部署接口如何开放出来？ |
| Runtime | LeRobot / Jetson Orin / Thor | VLA 输出如何变成真实机器人 action loop？ |

## 今晚粗扫结论

这组材料先按一条线理解：

```text
CLIP: image/text contrastive alignment
-> BLIP-2: frozen vision encoder + Q-Former + frozen LLM
-> LLaVA: vision encoder + projector + LLM + visual instruction tuning
-> RT-2: image + instruction -> action-as-token VLA policy
-> LingBot-VLA: LeRobot-style data/config/eval/deploy engineering stack
```

今天不继续扩论文数量。明天重点放在 `RT-2` 的 action representation 和 `LingBot-VLA` 的工程流程；等 SO-ARM101 到货后，阅读必须回到 observation/action/data/eval 的实物闭环。

## 今日必须留下的 4 个问题

1. VLM 到 VLA 的关键跃迁是什么？
2. action 是连续控制量、离散 token，还是 action chunk？
3. 高层 VLA 与低层 policy/control 如何分层？
4. 为什么后续需要 Orin / Thor 这样的本体侧 runtime？

## 和 SO-ARM101 的连接

SO-ARM101 第一阶段不训练 VLA，但它提供后续 VLA 必需的真实接口：

```text
observation.images
+ observation.state
+ task/language
-> policy / VLA
-> action
-> replay / eval / failure log
```

首闭环的价值是先建立数据、动作、评估和失败分析。等这些接口清楚后，再把 RT-2 / OpenVLA / LingBot-VLA 放进同一条 runtime 链路里理解。
