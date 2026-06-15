---
type: paper_note
title: YOLO Family - Real-Time Object Detection
short_name: YOLO family
track: CV foundations / robot perception / object detection
read_mode: Family Scan
status: downloaded
created: 2026-06-11
---

# YOLO Family - QUICK READ

## Position

YOLO 是 real-time object detection 的代表路线。它不是 VLA 的替代品，而是机器人系统里很常用的 perception module：

```text
camera image -> detector -> boxes / classes / confidence
```

第一版 SO-ARM101 + LeRobot / ACT 不强制使用 YOLO；先跑通 raw image/state 到 action 的 imitation learning 闭环。后续做 object-centric task、自动标注、失败检测、安全监控或给 VLA 提供 object hints 时，YOLO-style detector 会很实用。

## Downloaded Papers

| Order | Paper | arXiv | Local PDF | Why |
|---|---|---|---|---|
| 1 | You Only Look Once: Unified, Real-Time Object Detection | `1506.02640` | `./YOLOv1_You_Only_Look_Once_Unified_Real_Time_Object_Detection.pdf` | 原始 YOLO：把 detection 从 proposal/classifier pipeline 改成 single-shot regression。 |
| 2 | YOLO9000: Better, Faster, Stronger | `1612.08242` | `./YOLO9000_Better_Faster_Stronger.pdf` | YOLOv2 / YOLO9000：改进速度/精度，并连接 detection 与 classification 数据。 |
| 3 | YOLOv3: An Incremental Improvement | `1804.02767` | `./YOLOv3_An_Incremental_Improvement.pdf` | 多尺度预测、Darknet-53 等工程化改进，是常见 YOLO 直觉来源。 |
| 4 | YOLOv4: Optimal Speed and Accuracy of Object Detection | `2004.10934` | `./YOLOv4_Optimal_Speed_and_Accuracy_of_Object_Detection.pdf` | 汇总大量 bag-of-freebies / bag-of-specials，体现 detector 工程配方。 |
| 5 | YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors | `2207.02696` | `./YOLOv7_Trainable_Bag_of_Freebies.pdf` | 现代实时 detector 代表，适合后续看 speed/accuracy tradeoff。 |

## Official Links

- YOLOv1: https://arxiv.org/abs/1506.02640
- YOLO9000 / YOLOv2: https://arxiv.org/abs/1612.08242
- YOLOv3: https://arxiv.org/abs/1804.02767
- YOLOv4: https://arxiv.org/abs/2004.10934
- YOLOv7: https://arxiv.org/abs/2207.02696

## Core Question

如果机器人任务需要知道“物体在哪里、类别是什么、置信度多高”，是否一定要让 VLA 从原始 image 里自己学出来？

YOLO 的回答是：不一定。很多系统里可以显式抽一个 detection module，把 object boxes / labels / confidence 作为中间信号，用于控制、评估、日志或安全。

## YOLO vs VLA

```text
端到端 policy:
image + robot state -> ACT / VLA -> action

模块化 perception:
image -> YOLO -> boxes / labels / confidence
boxes / labels + state -> planner / policy -> action

混合系统:
image + state -> ACT / VLA -> action
YOLO -> eval / logging / safety / failure analysis / optional object hints
```

## Robot Learning Connection

- `push-to-zone`: 可以用 detector 判断目标物体是否进入区域，辅助 eval。
- `pick specific object`: 可以用 detector 给出目标框，减少策略需要自己从零学 object localization。
- `failure analysis`: 抓取失败时记录目标框、遮挡、离手距离、误检/漏检。
- `dataset tooling`: 可用 detector 给 episode 自动打标签，辅助筛选数据。
- `VLA context`: 后续可以把 detector output 作为 tool/context 给 VLA 或 planner。

## Reading Plan

- 第一轮只读 YOLOv1：理解 single-shot object detection 的基本 formulation。
- 第二轮读 YOLOv2 / YOLOv3：理解 anchor、multi-scale、speed/accuracy tradeoff。
- YOLOv4 / YOLOv7 暂时只扫：它们更偏工程配方和实时 detector benchmark。

## Current Status

- [x] PDFs downloaded
- [ ] YOLOv1 quick read
- [ ] YOLOv2 / YOLOv3 family scan
- [ ] Robot perception connection note
