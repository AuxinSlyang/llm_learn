---
type: reading_plan
track: CV foundations for VLM/VLA/robot observation
status: active
created: 2026-06-11
---

# CV Foundation Sprint 2026-W24

## 目标

利用 SO-ARM101 硬件工具未到的等待期，补一条最短但完整的 CV foundation 线，服务后续 VLM / VLA / robot observation。

这不是转向传统 CV 全科；只回答一个主问题：

```text
camera image
-> visual backbone / visual tokens
-> multimodal connector
-> LLM / VLA / policy
```

## 读法约束

- 每篇都做 `Structured Quick Read`，不是逐公式 deep read。
- 每篇必须留下 3 个输出：
  - 一句话 takeaway。
  - 解决的核心概念。
  - 和 `VLM / VLA / robot observation` 的连接。
- 不进入完整 detection / segmentation / self-supervised vision 专题；只在 foundation sprint 之后按项目需要补。
- 周末如果摄像头和螺丝刀到位，硬件 bring-up 优先；CV sprint 顺延，不抢 SO-ARM101。

## P0 主线：必须完整读一轮

| Order | Paper | 核心概念 | 读完要能回答 |
|---|---|---|---|
| 0 | CNN Primer | convolution / locality / weight sharing / feature map | CNN 为什么适合图像？为什么能成为 visual backbone？ |
| 1 | LeNet-5 | early CNN / convolution + subsampling / end-to-end learning | CNN 的基本结构怎样从 raw pixels 学出层级视觉特征？ |
| 2 | AlexNet | ImageNet / deep CNN / data + GPU + ReLU | 为什么 2012 后 deep CNN 成为视觉 backbone 起点？ |
| 3 | VGG | depth / small conv / simple backbone | 为什么加深网络有价值？小卷积堆叠带来什么？ |
| 4 | GoogLeNet / Inception | multi-scale feature / compute efficiency | 为什么同一层要看不同尺度？为什么不能只盲目加宽加深？ |
| 5 | ResNet | residual connection / degradation problem | 为什么 `F(x) + x` 让很深的视觉网络可训练？ |
| 6 | ViT | image patch as token / Transformer vision | 图像如何变成 token sequence？ViT 少了哪些 CNN inductive bias？ |
| 7 | Vision Transformers Need Registers | artifact token / register token / interpretability | 为什么 attention map 不能直接等价为解释？ |

## P1 桥接：从 CV 到 VLM/VLA

| Order | Paper | 核心概念 | 读完要能回答 |
|---|---|---|---|
| 8 | CLIP | contrastive image-text pretraining / open vocabulary | 图像表征如何和语言表征对齐？ |
| 9 | BLIP-2 | frozen image encoder / Q-Former / frozen LLM | visual features 如何接到 LLM？ |
| 10 | LLaVA | visual instruction tuning | VLM 如何从 image-text model 变成对话式视觉助手？ |

## P1.5 机器人感知模块：按任务需要补

| Paper / 方向 | 核心概念 | 什么时候用 |
|---|---|---|
| YOLO family | real-time object detection / bounding boxes / class confidence | 当任务需要明确物体框、目标位置、数据标注、失败检测或模块化 perception -> policy 接口时使用；本地入口见 `YOLO_Family_Real_Time_Object_Detection/QUICK_READ.md`。 |

YOLO 和 VLA 不是二选一：

```text
端到端路线：
camera image + robot state -> ACT / VLA -> action

模块化路线：
camera image -> YOLO / detector -> object boxes / labels
-> planner / policy / VLA tool context -> action

混合路线：
camera image + state -> ACT / VLA -> action
YOLO / detector -> logging / eval / safety / failure analysis / optional object hints
```

第一版 SO-ARM101 + LeRobot 不强制用 YOLO；先跑通 `teleop -> dataset -> policy -> eval`。后续如果任务变成 `find cup / push object to zone / pick specific object`，YOLO-style detector 很可能成为实用工具。

已下载 YOLO family 代表论文：

- `YOLOv1`: You Only Look Once: Unified, Real-Time Object Detection
- `YOLO9000 / YOLOv2`: Better, Faster, Stronger
- `YOLOv3`: An Incremental Improvement
- `YOLOv4`: Optimal Speed and Accuracy of Object Detection
- `YOLOv7`: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors

## P1.7 生成式视觉 / Diffusion awareness：简单了解

| Paper / 方向 | 核心概念 | 什么时候看 |
|---|---|---|
| DDPM / DDIM / Score SDE / Latent Diffusion | noising -> denoising / score / latent-space generation | CNN/ViT/CLIP 主线跑完后，用 30-60m 建立生成式视觉直觉。 |
| Diffusion Policy | action sequence denoising / multimodal action distribution | ACT / LeRobot 第一闭环后，再和 robot action generation 对照。 |

本地入口：`Diffusion_Models_for_Generative_Vision/QUICK_READ.md`

Diffusion 这条线先回答两个问题：

```text
视觉生成：random noise -> repeated denoising -> image
机器人策略：noisy action sequence + observation -> denoising -> action sequence
```

当前不训练 diffusion，不复现 Stable Diffusion，不让它抢 `CNN -> ViT -> CLIP` 的基础线。

## P2 后续雷达：先不进入本周

| Paper / 方向 | 为什么暂缓 |
|---|---|
| DETR | detection 很重要，但不是当前 VLM/VLA visual token 主线的第一层缺口。 |
| MAE / DINO / DINOv2 | self-supervised visual representation 后续重要；先读完 supervised CNN -> ViT -> CLIP。 |
| SAM | segmentation foundation model 很重要，但会把当前线带向 dense prediction。 |
| Swin Transformer | hierarchical vision transformer 重要，但先用 ViT 建立最小概念。 |
| Vision Banana / Image Generators are Generalist Vision Learners | 生成式视觉统一范式，放在 SO-ARM101 首闭环后。 |

## 2026-W24 建议节奏

| 日期 | 主线 | 证据 / 产出 |
|---|---|---|
| 2026-06-11 周四 | CNN Primer + LeNet-5 + AlexNet 背景 | CNN 5 个概念 + LeNet-5 一句话 + AlexNet 一句话背景 |
| 2026-06-12 周五 | VGG / Inception 背景 + ViT structured quick read | `CNN backbone -> visual token` 对照表 |
| 2026-06-13 周六 | Vision Transformers Need Registers 或 CLIP | 解释性 takeaway 或 image-text alignment takeaway |
| 2026-06-14 周日 | 工具到位则硬件；否则继续 CLIP / BLIP-2 | hardware evidence 或 VLM bridge note |

## 每篇输出模板

```text
## One-sentence takeaway

## Core concept

## Why it mattered historically

## What to skip on first pass

## VLM / VLA / robot observation connection

## Open questions
```
