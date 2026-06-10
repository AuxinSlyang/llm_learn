---
type: reading_plan
track: VLA / robot learning / SO-ARM101
status: active
created: 2026-06-10
linked_project: [[so-arm101-lerobot-first-loop]]
---

# VLA First Stage Reading Plan

## 判断

当前清单作为 VLA 第一阶段已经足够，不需要再盲目扩论文数量。

真正的问题不是论文不够，而是要把论文分层：

```text
P0: 直接服务 SO-ARM101 首闭环
P1: 解释 VLA 主流范式
P2: 前沿雷达和后续扩展
Reference: 大清单，只用于查漏补缺
```

## P0：本周必须围绕实物闭环读

| 材料 | 作用 | 读法 |
|---|---|---|
| LeRobot docs | 先跑通 SO-ARM101 的 teleop / record / replay / ACT | 跟做，不精读 |
| ACT | 第一阶段最现实的 imitation learning policy | 精读 method + 跟 LeRobot 训练链路对应 |
| XLeRobot | 双臂 / 移动底盘 / SO101 社区工程参考 | 先扫硬件和 bring-up 流程 |
| LingBot-VLA | 看 LeRobot dataset/config/eval/deploy 如何接 VLA | 项目 walkthrough，暂不训练 4B |
| SmolVLA | affordable robotics / 小 VLA / LeRobot 生态 | 重点看 runtime、数据、异步推理 |

## P1：VLA 主线必读

| 材料 | 为什么必须读 | 当前状态 |
|---|---|---|
| RT-1 | language-conditioned robot policy 的早期系统化路线 | 待读 |
| RT-2 | action-as-token，把 VLM 变成 VLA | 已完成第一轮 |
| Open X-Embodiment / RT-X | 多机器人数据规模化和 embodiment gap | 待读 |
| OpenVLA | 开源 VLA，理解 7B VLA、Open X 数据、fine-tune/deploy | 已下载，待结构化读 |
| π0 | flow matching action expert，理解连续动作 VLA | 已下载，待结构化读 |
| π0-FAST | action tokenizer，从离散 token 化走向更高效动作序列 | 待读 |
| π0.5 | open-world generalization，异构数据 co-training | 待读 |

## P2：补充但不抢主线

| 材料 | 作用 | 触发条件 |
|---|---|---|
| PaLM-E | embodied multimodal LM，理解视觉/语言/机器人状态统一输入 | VLM->VLA 谱系补全 |
| Octo | open generalist robot policy | OpenVLA 后 |
| Diffusion Policy | 连续动作生成和 action distribution 基础 | ACT 跑通后 |
| DAgger | BC 分布偏移和 dataset aggregation | 发现 policy drift 后 |
| Mobile ALOHA | 双臂移动操作系统参考 | 进入双臂/移动底盘阶段 |

## Reference：大清单的定位

Epoch robotic manipulation compute CSV 是雷达库，不是阅读队列。

使用方式：

- 每月 review 一次，看是否有新的关键范式。
- 只把能解释当前项目问题的论文提升到 P0/P1。
- 不用为了“读得多”去扫 400+ 条模型表。

## 2026-06-11 用户补充资源分层

这些材料都值得保留，但不能同一天全部精读。按和 `SO-ARM101 + LeRobot` 首闭环的距离分层：

| 层级 | 材料 | 链接 | 当前读法 |
|---|---|---|---|
| P0 | XLeRobot | https://github.com/Vector-Wangel/XLeRobot | 社区工程参考：先看硬件、bring-up、teleop/sim/VR/VLA tutorial，不作为本月新硬件项目 |
| P0 | SmolVLA | https://huggingface.co/blog/smolvla | 贴近 LeRobot / affordable robotics：重点看数据格式、action chunk、async inference 和 consumer hardware |
| P0/P1 | LingBot-VLA | https://arxiv.org/abs/2601.18692 | LeRobot-style VLA 工程栈：dataset/config/eval/deploy，对齐 SO-ARM101 数据闭环 |
| P1 | OpenVLA | https://arxiv.org/abs/2406.09246 / https://github.com/openvla/openvla | 开放 VLA 模型：理解 Open X 数据、7B VLA、fine-tune/deploy；SO-ARM101 record/replay 前不训练 |
| P2 | pi0 / openpi | https://github.com/Physical-Intelligence/openpi | 前沿模型与工程实现：只看 action interface、LeRobot dataset conversion、policy server / remote inference |
| P2 | pi0-FAST | https://huggingface.co/blog/pi0 | FAST action tokenizer / autoregressive VLA，作为 action representation 对照 |
| P2 | pi0.5 | https://www.pi.website/blog/pi05 | open-world generalization / 异构数据 co-training，后续 awareness |
| Reference | Robotics Models CSV | https://github.com/epoch-research/robotic-manipulation-compute/blob/main/data/Robotics%20Models.csv | 雷达库：每月 review，不变成逐篇阅读队列 |
| Reference | ACT repo | https://github.com/Shaka-Labs/ACT | 只在训练 ACT v0 时查实现，不再作为今天阅读任务 |

## 第一阶段阅读顺序

```text
1. ACT
2. LeRobot ACT training / dataset flow
3. LingBot-VLA project walkthrough
4. SmolVLA
5. OpenVLA
6. π0
7. π0-FAST
8. π0.5
```

这条顺序和 SO-ARM101 的工程进度对齐：

```text
assemble/calibrate
-> teleop
-> record/replay
-> train ACT
-> understand small VLA
-> understand OpenVLA / π family
```

## 现阶段不要做的事

- 不要把 VLA 论文阅读变成纯 survey。
- 不要在 SO-ARM101 没有 record/replay 前训练大 VLA。
- 不要跳到 Thor/Orin runtime，除非本地数据闭环已经跑通。
- 不要把 World Model、Dexterous Hand、Humanoid、Navigation 全部同时打开。

## 当前缺口

| 缺口 | 补法 |
|---|---|
| 数据闭环经验不足 | 先用 LeRobot record/replay 和 ACT 补 |
| action representation 还不稳定 | 对比 ACT action chunk / RT-2 token / π0 flow matching / π0-FAST tokenizer |
| VLA 工程部署经验不足 | LingBot-VLA / SmolVLA / OpenPI 只看 deployment path |
| CV 基础较薄 | 在 SO-ARM101 首闭环后补 ResNet / ViT / CLIP / DINO/SAM/Vision Banana |
