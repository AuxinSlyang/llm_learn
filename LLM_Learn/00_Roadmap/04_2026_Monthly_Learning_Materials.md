---
type: roadmap_material_index
date_range: 2026-06 ~ 2027-05
target_role: Robot Learning Full-Stack -> Robot Full-Stack Engineer / Roboticist
linked_roadmap: [[03_Annual_Plan_2026]]
active_roadmap: [[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]
updated: 2026-06-01
---

# 2026-2027 Monthly Learning Materials

> 这份文件回答的问题：**每个月具体学什么、看什么材料、产出什么？**
> 使用方式：月计划负责节奏；本文件负责把课程、文档、论文和项目内容展开成可执行学习清单。

## 总原则

- 当前主线是 `Robot Learning Full-Stack / Policy Runtime / Robot Learning Infra`。
- `LLM / AI Infra / Runtime` 是 VLA、policy runtime、edge inference、语言任务分解和多机器人协作的支撑线。
- 每个月只保一个主课程或主实验，不同时完整刷多门课。
- 每个月必须有一个可见产物：笔记、代码、曲线、实验报告、failure analysis、demo 或 JD mapping。
- 论文只作为当前阶段解释器，必须回答 task、obs/action、policy/data/loss/reward、eval/runtime。

## 月度材料优先级

| 月份      | 主模块                  | 主材料                                  | 论文 / 文档                                      | 阶段产出                                                      |
| ------- | -------------------- | ------------------------------------ | -------------------------------------------- | --------------------------------------------------------- |
| 2026-06 | M1：路线切换 + 最小 RL 闭环   | nanoGPT、Gymnasium、Stable-Baselines3  | PPO / DAgger 轻读                              | `nanoGPT 主链路总结 v0`、`MuJoCo PPO report v0`                 |
| 2026-07 | M2：机器人本体语言 I         | Modern Robotics Ch.1-3               | MR video / book notes                        | `frame/SO(3)/SE(3) notes`、`state-action schema v0`        |
| 2026-08 | M3：机器人本体语言 II        | Modern Robotics Ch.4-6               | kinematics / Jacobian examples               | `FK/IK/Jacobian demo`、`MR notes v0`                       |
| 2026-09 | M4：控制 / 动力学入口        | MIT Underactuated 精选、MuJoCo control  | LQR / MPC / legged control overview          | `control baseline note`、`latency/jitter/robustness note`  |
| 2026-10 | M5：视觉感知入口            | CS231n 精选、OpenCV                     | ResNet / ViT / detection / segmentation      | `robot perception map`、`vision data pipeline note`        |
| 2026-11 | M6：感知到 runtime 桥接    | CS231n 精选、policy runtime notes       | CLIP / representation / VLA runtime overview | `perception-to-policy runtime bridge`、`dataset schema v0` |
| 2026-12 | M7：Robot Learning 入口 | CS285 精选、BC/PPO/DAgger               | BC、DAgger、PPO、Diffusion Policy 轻读            | `BC/PPO experiment v0`、`policy runtime mini-stack draft`  |
| 2027-01 | M8：Robot Learning 深化 | CS285 精选、SAC / offline RL            | SAC / offline RL / RMA                       | `BC/PPO/SAC experiment report`                            |
| 2027-02 | M9：ROS2 / Runtime    | ROS2 官方教程、tf2、rosbag                 | policy deployment / runtime notes            | `policy runtime mini-stack v0`                            |
| 2027-03 | M10：高保真仿真可行性         | Isaac Lab 官方入门、RTX/cloud feasibility | sim2real / domain randomization              | `Isaac Lab feasibility report`                            |
| 2027-04 | M11：VLA / 具身智能       | MIT Robotic Manipulation 精选          | RT-1、RT-2、OpenVLA、ACT、Octo、π0                | `VLA -> policy runtime mapping`                           |
| 2027-05 | M12：作品化 / JD 对齐      | 项目 README、benchmark、复现脚本             | 只补缺口论文                                       | `portfolio + JD mapping`                                  |

## 2026-06：M1 / 路线切换 + 最小 RL 闭环

| 项 | 内容 |
|---|---|
| 月主题 | `nanoGPT 收口 + Robot Learning Full-Stack 路线 + Gymnasium/MuJoCo PPO 最小闭环` |
| 主材料 | nanoGPT 本地笔记；Gymnasium docs；Stable-Baselines3 PPO docs |
| 学习内容 | LLM 主链路、obs/action/reward/policy/eval、训练曲线、seed、eval |
| 实验内容 | `Pendulum` / `InvertedPendulum` PPO 训练；固定 seed eval；保存 reward 曲线 |
| 关键产出 | `nanoGPT 主链路总结 v0`；`Robot Learning Full-Stack 路线 v0`；`MuJoCo PPO report v0` |
| 月末自检 | 能讲清 LLM training/generate 主链路，也能讲清 robot learning 最小闭环 |

## 2026-07：M2 / Modern Robotics Ch.1-3

| 项    | 内容                                                                               |
| ---- | -------------------------------------------------------------------------------- |
| 月主题  | `机器人本体语言：frame / pose / SO(3) / SE(3) / configuration`                           |
| 主材料  | Modern Robotics Ch.1-3；Lynch videos                                              |
| 学习内容 | coordinate frame、rotation、rigid motion、homogeneous transform、configuration space |
| 实验内容 | 用 Python 写最小 SE(3) transform demo；记录 state/action schema                         |
| 关键产出 | `frame/SO(3)/SE(3) notes`；`state-action schema v0`                               |
| 月末自检 | 能看懂机器人状态和坐标系，不再把 action 当成抽象 label                                               |

## 2026-08：M3 / Modern Robotics Ch.4-6

| 项 | 内容 |
|---|---|
| 月主题 | `FK / IK / Jacobian` |
| 主材料 | Modern Robotics Ch.4-6；MR code examples |
| 学习内容 | product of exponentials、forward kinematics、Jacobian、inverse kinematics |
| 实验内容 | 做一个简化机械臂 FK/IK/Jacobian demo |
| 关键产出 | `FK/IK/Jacobian demo`；`MR notes v0` |
| 月末自检 | 能解释 policy 输出的动作如何作用到机器人关节/末端执行器 |

## 2026-09：M4 / 控制与动力学入口

| 项 | 内容 |
|---|---|
| 月主题 | `control baseline + runtime stability` |
| 主材料 | MIT Underactuated 精选；MuJoCo control docs |
| 学习内容 | PD、LQR、MPC awareness、stability、latency、jitter、action clipping |
| 实验内容 | MuJoCo 简单控制 baseline；记录 latency/jitter/failure case |
| 关键产出 | `control baseline note`；`latency/jitter/robustness note` |
| 月末自检 | 能解释为什么 policy runtime 不能只看 reward，还要看稳定性和故障处理 |

## 2026-10：M5 / 视觉感知入口

| 项 | 内容 |
|---|---|
| 月主题 | `robot perception map` |
| 主材料 | CS231n 精选；OpenCV；PyTorch vision examples |
| 学习内容 | CNN、detection、segmentation、ViT、camera/depth、calibration、数据格式 |
| 实验内容 | OpenCV 读图/视频；整理 vision observation 到 policy input 的数据结构 |
| 关键产出 | `robot perception map`；`vision data pipeline note` |
| 月末自检 | 能说明视觉模型输出如何进入机器人决策，而不是只会讲分类准确率 |

## 2026-11：M6 / 感知到 runtime 桥接

| 项 | 内容 |
|---|---|
| 月主题 | `perception-to-policy runtime bridge` |
| 主材料 | CS231n 精选；CLIP / representation materials；policy runtime notes |
| 学习内容 | representation、multi-modal input、preprocess、batch/latency、dataset schema |
| 实验内容 | 设计 observation schema；记录 episode metadata；写 eval harness 草稿 |
| 关键产出 | `perception-to-policy runtime bridge`；`dataset schema v0` |
| 月末自检 | 能把感知、数据格式、推理延迟和 policy runtime 连起来 |

## 2026-12：M7 / Robot Learning 入口 + 年终作品化

| 项 | 内容 |
|---|---|
| 月主题 | `BC/PPO experiment + policy runtime mini-stack draft` |
| 主材料 | CS285 精选；Stable-Baselines3；LeRobot / robot learning examples |
| 学习内容 | BC、DAgger、PPO、SAC 位置；eval harness；failure analysis |
| 实验内容 | 至少一个 BC/PPO 小实验；保存 eval 表、失败样例和 replay |
| 关键产出 | `BC/PPO experiment v0`；`policy runtime mini-stack draft`；`2027 plan` |
| 月末自检 | 能用作品证明自己理解 robot learning infra / policy runtime，而不只是读过论文 |

## 使用边界

- 不因为材料表存在就同时开所有课程；每月只执行当前月主线。
- 不把 CS336 / vLLM / TensorRT-LLM 完全删除；它们进入 `LLM / AI Infra / Runtime 支撑线`，在 VLA、edge inference、policy runtime 需要时调用。
- 不在第一月直接上 Isaac Lab；现有 V100 不适合作为现代 Isaac Sim/Lab 主力环境。
- 不追论文数量；论文必须服务当前课程或实验。
