---
type: paper_note
title: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware
short_name: ACT / ALOHA
arxiv_id: "2304.13705"
url: https://arxiv.org/abs/2304.13705
pdf_url: https://arxiv.org/pdf/2304.13705
local_pdf: ./ACT_Learning_Fine_Grained_Bimanual_Manipulation_with_Low_Cost_Hardware.pdf
track: robot learning / imitation learning
read_mode: Project Must Read
status: first_pass_done
created: 2026-06-09
---

# ACT（ALOHA）QUICK_READ

- Paper：Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA / ACT)
- arXiv：2304.13705
- 输出标准：一句 takeaway + 一个和 mini-stack 的连接（接口/数据/评估）

## 2026-W24 Position

ACT 是本周和 SO-ARM101 最贴近的 robot learning 论文之一：低成本双臂硬件、teleoperation 数据、action chunking、模仿学习。它比 VLA 更接近第一阶段能动手的闭环。

本周只问：

```text
observation 是什么？
action chunk 怎么表示？
teleop 数据怎么采？
eval / failure 怎么记录？
```

## 3 句话总结（读完再写）

1. ALOHA 提供低成本 leader/follower teleoperation 系统，用 joint-space mapping 采集高质量 fine manipulation demonstration。
2. ACT 把普通 BC 的单步动作预测改成 `image/state -> future action chunk`，用 action chunking 降低长时序任务里的 compounding error。
3. Temporal ensembling 让重叠 action chunk 平滑融合，CVAE latent `z` 建模人类示教的多种合理动作风格，Transformer encoder-decoder 融合多摄图像、关节状态和 `z` 并输出动作序列。

## 我关心的 8 问（只填关键短句）

- 任务是什么：
- 任务是什么：双臂精细操作 imitation learning，例如开杯盖、插电池、处理胶带、穿扎带等 contact-rich / precise manipulation。
- observation：4 路 RGB camera + follower 当前关节状态；对应 LeRobot 里可类比为 `observation.images.*` + `observation.state`。
- action（重点：action chunk 怎么定义）：action 是目标关节位置；ALOHA 双臂 `action_dim=14`，ACT 输出未来 `k` 步，所以 shape 是 `k x 14`。SO-ARM101 单臂后续可类比成 `k x 6/7`。
- 数据怎么采：人拖动 leader arm，follower arm 执行；记录 leader joint positions 作为 action，记录 follower joint positions 和 camera images 作为 observation。
- policy 输出什么：给当前 observation，输出未来一段 target joint position sequence，即 action chunk。
- eval 怎么做：在真实任务上看分阶段和最终成功率，并和 BC-ConvMLP、BeT、RT-1、VINN 等 imitation learning baseline 比较。
- failure mode：compounding error、chunk 边界抖动、视觉遮挡/低对比度、精细接触误差、人类示教多模态导致平均动作失败。
- 工程化需要什么支撑（数据版本/runner/latency/replay）：dataset version、camera/state/action 时间同步、policy runner 支持 action chunk 和 replanning frequency、temporal ensemble buffer、latency logging、replay/eval、failure taxonomy。

## Takeaway（至少 1 条）

- ACT / ALOHA 最值得带到 SO-ARM101 + LeRobot 的不是双臂硬件本身，而是工作流：`teleop -> image/state/action dataset -> action chunk policy -> smooth runtime inference -> eval/failure -> 补数据`。
- `joint space` 是第一阶段最现实的控制语言：先把机器人理解成一组可观测/可控制的关节变量，再逐步补 `task space / IK / motion planning`。
- CVAE 的 `z` 不是简单噪声增强，而是把同一 observation 下多种合理 human demonstration mode 变成可学习的 latent style；推理时固定 `z=0` 走典型动作模式。

## 和 embodied-ai mini-stack 的连接（至少 1 条）

- `trajectory schema` 必须表达 `observation.images`、`observation.state`、`action`、`episode/task metadata`，并能支持 action chunk 训练样本。
- `policy_runner` 要支持：camera/state 输入、chunked action 输出、每步重新 query policy、temporal ensemble 平滑、action 下发和延迟日志。
- `failure log` 不能只记“成功/失败”，要能区分视觉问题、关节/校准问题、action chunk 边界问题、latency 问题和 demonstration 数据质量问题。

## 2026-06-11 阅读记录

- 已读：Abstract、Introduction、Related Work、Section 3 ALOHA、Section 4 ACT 主结构。
- 已理解：open-loop vs closed-loop、joint space vs task space、FK/IK、action chunking、temporal ensemble、CVAE `z`、ACT 的 Transformer encoder-decoder 架构。
- 下次继续：用 toy example 走一遍 ACT training/inference；再看实验和 ablation，确认 action chunk、temporal ensemble、CVAE 各自贡献。

## 2026-06-23 状态校准

用户确认 `ACT / ALOHA` 已经看完第一轮。当前状态改为 `first_pass_done`。

后续不再把它作为“待读主论文”重复排队；只有在 SO-ARM101 / LeRobot 有真实 E002/E003 数据、准备训练 ACT/BC v0 时，再回看：

- training / inference toy example
- experiments and ablations
- action chunk size / temporal ensemble / CVAE latent `z`
- 和 LeRobot dataset / runner / eval 的真实字段映射
