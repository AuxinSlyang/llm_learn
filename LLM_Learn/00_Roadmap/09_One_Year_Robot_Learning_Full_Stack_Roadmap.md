---
type: one_year_roadmap
time_window: 2026-06-01_to_2027-05-31
target_role: Embodied AI Systems Builder / Robot Full-Stack Engineer -> Roboticist
current_role: DB / Storage Kernel Engineer
updated: 2026-06-01
linked_files:
  - "[[00_North_Star]]"
  - "[[02_Capability_Map]]"
  - "[[03_Annual_Plan_2026]]"
  - "[[06_Embodied_AI_Software_Engineer_Learning_Curve]]"
  - "[[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]"
  - "[[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]"
---

# One-Year Roadmap: Robot Learning Full-Stack

> 这份文件回答的问题：**如果 Unitree 具身智能软件 / Robot Learning 是目标，一年内应该怎样系统学习并形成可展示闭环？**

## 一句话定位

目标分层：

- 短期职业目标：具身智能系统构建者 / 机器人全栈工程入口，现实落点是 `具身智能软件工程师 / Robot Learning Infra / Policy Runtime`。
- 长期能力目标：机器人全栈工程师 / roboticist，能打通机器人本体、感知、控制、学习、runtime、数据闭环与语言智能。

未来一年主线调整为：

```text
课程主线 + 每周仿真闭环 + 论文解释器 + runtime/data loop 工程化
```

最终目标不是“只会读 robot learning 论文”，而是能把一个 policy/model 接入机器人系统：

```text
sim/task -> observation/action -> train policy -> eval -> log/replay -> runtime -> failure analysis -> data loop
```

## 岗位入口判断

| 岗位层级 | 定位 | 当前最合适程度 |
|---|---|---|
| JD1：具身智能软件工程师 | 算法产品化、模型部署、低延迟链路、数据闭环、鲁棒性 | 最适合作为第一跳 |
| Robot Learning Infra / Policy Runtime | policy 训练、评测、部署、日志、回放和 runtime 工具链 | 强匹配，应该重点准备 |
| 深度强化学习算法工程师 | 多自由度机器人 RL、仿真训练、sim2real、真机验证 | 长期最终目标，需要项目证据后再冲 |

## 学习原则

- 每个阶段只有一门主课，不同时完整刷多门课。
- 论文只作为当前阶段的解释器，不随机追热点。
- 每个阶段必须有一个可展示产出：笔记、代码、曲线、报告、mapping。
- LLM / AI Infra 不丢弃，但降级为机器人 policy runtime / VLA runtime 的支撑能力。

## 12 个月总表

| 时间 | 主模块 | 主公开课 / 主资源 | 论文穿插 | 硬件 / 系统补充 | 阶段产出 | 对 JD1 的帮助 |
|---|---|---|---|---|---|---|
| M1 | 最小 RL 闭环 | Gymnasium + Stable-Baselines3 官方教程 | PPO、DAgger 轻读 | Linux headless、conda/docker、训练曲线 | `MuJoCo PPO report v0` | 证明能跑通 policy 训练-评估 |
| M2-M3 | 机器人本体 | Modern Robotics | locomotion / robot control 综述 | URDF、joint、motor、encoder、control frequency | `MR notes + FK/IK/Jacobian demo` | 看懂机器人身体、状态和动作空间 |
| M4 | 控制 / 动力学 | MIT Underactuated Robotics 精选 | LQR、MPC、legged control | 实时控制、latency、jitter、稳定性 | `control baseline note` | 支撑低延迟执行和鲁棒性分析 |
| M5-M6 | 视觉感知 | Stanford CS231n 精选 | ResNet、ViT、CLIP、视觉表征 | camera/depth、calibration、数据格式 | `robot perception map` | 对齐感知-决策-执行链路 |
| M7-M8 | Robot Learning | Berkeley CS285 精选 | BC、DAgger、PPO、SAC、Diffusion Policy、RMA | logging/eval、domain randomization、dataset schema | `BC/PPO/SAC experiment report` | 从部署模型升级到理解 policy |
| M9 | ROS2 / Runtime | ROS2 官方教程 | policy deployment / runtime 相关论文 | ROS2、tf2、rosbag、nodes/topics/actions | `policy runtime mini-stack` | JD1 主命中：部署、日志、数据闭环 |
| M10 | 高保真仿真 | Isaac Lab 官方入门 | sim2real、domain randomization | RTX/cloud、Isaac、传感器仿真 | `Isaac Lab feasibility report` | 对齐工业机器人训练平台 |
| M11 | VLA / 具身智能 | MIT Robotic Manipulation 精选 | RT-1、RT-2、OpenVLA、ACT、Octo、π0 | 多模态输入、动作接口、推理延迟 | `VLA -> policy runtime mapping` | 对齐具身智能长期方向 |
| M12 | 作品化 / JD 对齐 | 项目驱动 | 只补缺口论文 | README、benchmark、复现脚本、失败案例 | `portfolio + JD mapping` | 形成可投递证据 |

## 课程选择原则

- **Modern Robotics**：机器人数学和本体语言，不追求一遍推完所有证明，先建立 `frame / pose / twist / Jacobian / dynamics` 的工作直觉。
- **CS231n**：只取机器人视觉需要的部分：CNN、detection、segmentation、ViT、representation。
- **CS285**：只取 robot learning 的方法主线：BC、DAgger、policy gradient、PPO、SAC、offline RL。
- **MIT Underactuated**：作为控制和动力学加深课，只精选和 locomotion/control 相关章节。
- **ROS2 官方教程**：作为系统落地入口，目标是会组织 nodes、topics、tf2、rosbag 和 runtime 边界。

## 论文穿插规则

每篇论文只回答三层问题：

1. **问题层**：解决什么任务，为什么旧方法不够。
2. **方法层**：observation、action、model/policy、data、loss/reward、eval 各是什么。
3. **工程层**：如果产品化，需要什么 runtime、数据闭环、评测和 failure handling。

论文队列按阶段进入：

- M1-M2：PPO、DAgger、Gymnasium/MuJoCo 基础论文或文档。
- M5-M6：ResNet、ViT、CLIP、DINO/representation。
- M7-M8：BC、DAgger、SAC、RMA、Diffusion Policy。
- M9-M11：ACT、RT-1、RT-2、OpenVLA、Octo、π0、system/runtime 论文。

## 硬件 / 系统补充线

| 层级 | 必须理解的问题 |
|---|---|
| 机器人硬件 | joint、motor、encoder、IMU、camera/depth、LiDAR、控制频率、动作限幅 |
| 计算硬件 | CPU/GPU、CUDA、显存、batch、profiling、V100 与 RTX/Jetson/Orin 的差异 |
| 机器人软件 | ROS2、URDF、tf2、rosbag、message passing、launch、time sync |
| Runtime | policy latency、timeout、fallback、watchdog、logging、failure replay |
| 数据闭环 | trajectory schema、episode metadata、dataset version、eval harness、再训练入口 |

## 30 天第一闭环

目标：先跑通最小 robot learning 闭环，不等待所有理论学完。

| 周 | 内容 | 产出 |
|---|---|---|
| W1 | Gymnasium/MuJoCo + Stable-Baselines3 PPO 跑 `Pendulum` / `InvertedPendulum` | 训练脚本 + reward 曲线 |
| W2 | 换到 `HalfCheetah` / `Hopper`，跑固定 seed eval | `eval.py` + success/reward 表 |
| W3 | 加 noise / reward 改动 / domain randomization 小实验 | 对比图 + 失败样例 |
| W4 | 写实验报告并映射 JD1 | `MuJoCo PPO report v0` |

## 阶段结束标准

每月结束至少留下一个证据：

- 一页结构化笔记。
- 一个可运行脚本或 notebook。
- 一个指标图或实验表。
- 一个失败案例和原因分析。
- 一个对 JD1 / Robot Learning 的连接说明。

## 不做事项

- 不在第一月直接上 Isaac Lab 作为主入口；现有 V100 不适合现代 Isaac Sim/Lab 主力运行。
- 不同时完整刷 CS231n、Modern Robotics、CS285。
- 不把论文阅读变成主线；论文必须服务课程和实验。
- 不把 LLM inference 彻底丢掉；它作为 VLA/policy runtime 的系统能力保留。

## 一句话回锚

> 第一跳靠 `具身智能软件 / policy runtime / robot learning infra / 机器人全栈工程入口` 进入机器人团队；长期目标是成长为能跨本体、感知、控制、学习与系统工程的机器人全栈工程师 / roboticist。
