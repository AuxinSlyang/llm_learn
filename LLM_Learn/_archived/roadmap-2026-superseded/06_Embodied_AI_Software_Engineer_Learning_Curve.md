---
type: role_learning_curve
target_role: Embodied AI Software Engineer / Physical AI Systems Engineer
time_window: 2026-2028
updated: 2026-06-01
linked_files:
  - "[[03_Annual_Plan_2026]]"
  - "[[04_2026_Monthly_Learning_Materials]]"
  - "[[05_Career_Strategy_2026_2030]]"
  - "[[07_One_Year_Interview_Roadmap_Embodied_AI_Software]]"
  - "[[08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime]]"
---

# Embodied AI Software Engineer Learning Curve

> 这份文件回答的问题：**如果目标岗位是“具身智能软件工程师”，学习曲线应该怎么设计？**

## 2026-06-01 修订说明

未来一年执行主线已重新调整为 `Robot Learning Full-Stack / Policy Runtime / Robot Learning Infra`，本文件重新成为当前机器人全栈学习曲线的关键参考。

新的执行顺序是：

```text
DB / Storage Kernel
-> Robot Learning Full-Stack / Simulation / Evaluation
-> Policy Runtime / Robot Data Loop / Embodied AI Software
-> Robot Full-Stack Engineer / Roboticist
```

因此，下方 Robotics-first 学习比例和 2026 H2 机器人 demo 节奏重新进入当前执行依据；LLM / AI Infra 只作为 VLA、policy runtime 和 edge inference 的支撑线。

## 目标岗位画像

这个目标比单纯 `Robot Infra` 更接近当前兴趣：

> 把具身智能算法、模型和 policy 接入真实机器人系统，使其在端侧设备上低延迟、可观测、可评测、可回滚、可持续迭代。

它不是纯算法岗，也不是普通后端 / 数据平台岗，而是以下几层的交叉：

- 机器人系统软件
- AI 模型部署 / runtime
- Robot Learning pipeline
- 数据闭环
- 真机可靠性 / 安全兜底
- 仿真、评测和回放工具

## 岗位能力拆解

| 岗位要求 | 实际含义 | 对应学习模块 |
|---|---|---|
| 算法产品化 | 把 research code / policy / model 接入机器人软件栈，变成稳定功能 | Robot software integration, API boundary, config, versioning |
| 模型部署优化 | 模型在 Jetson / Thor / 昇腾等端侧硬件上跑得动、跑得稳、延迟可控 | ONNX, TensorRT, quantization, profiling, CUDA awareness |
| 低延迟链路 | `sensor -> perception -> decision -> action` 高频稳定响应 | control loop, async pipeline, latency budget, jitter handling |
| 数据闭环 | 真机数据能采集、存储、清洗、标注、回放、训练、评测 | trajectory schema, dataset, metadata, replay, eval |
| 鲁棒性与可靠性 | 模型失效、传感器异常、通信超时、动作异常时系统能降级或停机 | fault handling, safety guard, watchdog, fallback |
| 真机测试评价 | 用长时间运行和场景测试发现系统问题 | test harness, metrics, scenario suite, failure analysis |

## 总学习策略

### 一句话

> Robotics-first, software-stack-shaped.

先补机器人系统语言和仿真基础，再把每个 demo 都做成“软件系统闭环”，而不是只做一个算法实验。

### 学习比例

2026 H2 建议比例：

- `35%` Robotics / MuJoCo / control loop
- `25%` Robot Learning / policy / LeRobot
- `20%` AI runtime / data loop / eval infra
- `10%` perception / multi-sensor fusion awareness
- `10%` paper reading / VLA awareness

2027 建议比例：

- `35%` real robot / ROS2 / edge deployment
- `30%` Robot Learning software stack
- `25%` data / eval / observability / reliability
- `10%` VLA / foundation model tracking

## 2026：从学习 demo 到 Embodied AI mini-stack

### 2026-05：LLM 收口

目标：

- 在 5 月底前收口 nanoGPT，理解模型 forward / decode / runtime 的基本链路。
- 明确后续 LLM / AI Infra 只是具身智能软件的支撑线。

学习内容：

- `tokenizer -> transformer -> logits -> decode`
- `inference / runtime / KV cache` 概念入口
- CS336 只做结构对照，不做完整作业

产出：

- `nanoGPT 第一轮总结`
- `makemore -> nanoGPT -> inference_runtime 映射`
- `具身智能软件工程师岗位能力图`

### 2026-06 ~ 2026-07：Robotics + AI Fundamentals 入口

目标：

- 用两个月建立机器人系统底层语言。
- 同时补 perception / AI fundamentals / runtime awareness 的入口。
- 画出 `sensor -> state -> perception -> decision -> action -> robot -> log -> dataset -> train -> eval` 系统图。

学习内容：

- Modern Robotics Ch.1-6
- configuration space
- SO(3) / SE(3) / frame
- FK / Jacobian / IK
- MuJoCo model / data / step
- CS231n / OpenCV 视觉入口
- CS336 deployment / inference / runtime awareness

产出：

- `机器人系统总图 v0`
- `MR Ch.1-6 第一轮笔记`
- `mujoco_hello_world`
- `episode_logger v0`
- `state/action schema v0`

### 2026-07：MuJoCo + 机器人软件最小循环

目标：

- 跑通 MuJoCo step loop。
- 能读取 state，发送 action，记录 episode。
- 第一次建立 `sim loop` 的软件边界。

学习内容：

- MuJoCo model / data / step
- qpos / qvel / ctrl / actuator
- FK / Jacobian / IK 基础
- Python 项目结构、config、logging

产出：

- `mujoco_hello_world`
- `sim_loop.py`
- `episode_logger v0`
- `state/action schema v0`

最低标准：

- 能解释每一步 simulation 中 observation、action、state 分别是什么。
- 能保存一条 trajectory，并能离线 replay。

### 2026-08：控制闭环 + 数据记录

目标：

- 在 MuJoCo 中完成简单关节 PD 控制或末端控制。
- 每次实验都有 metrics、config、trajectory 和失败记录。

学习内容：

- PD control
- FK / IK / controller / simulation loop
- MDP / policy / reward / success
- 数据记录格式：`episode_id, task_id, seed, observation, action, reward, success, failure_reason`

产出：

- `MuJoCo 单臂控制最小实验`
- `trajectory format v1`
- `eval metrics v0`
- `failure mode taxonomy v0`

最低标准：

- demo 不只会动，还能统计成功率、失败原因、episode 长度、控制误差。

### 2026-09：Classic-control demo + eval harness

目标：

- 做一个 reach / push / pick-place 的 classic-control demo。
- 建立评测脚本和回放工具。

学习内容：

- task definition
- success criteria
- scenario config
- replay / video export
- ACT / Diffusion Policy 论文精读一篇，只看系统结构和数据定义

产出：

- `classic-control manipulation demo`
- `eval_harness v0`
- `replay_tool v0`
- `demo 系统拆解与失败模式记录`

最低标准：

- 能一键跑 N 个 episode，输出 metrics 和若干失败样例。

### 2026-10：Behavior Cloning + policy integration

目标：

- 用 scripted policy 或 teleop 采数据。
- 训练一个 BC policy。
- 把 policy 接回 simulation control loop 做 eval。

学习内容：

- LeRobot dataset / policy / training / eval
- BC / DAgger 概念
- policy input/output contract
- model checkpoint / config / versioning

产出：

- `BC dataset v0`
- `BC train/eval pipeline`
- `policy_runner v0`
- `model registry v0`

最低标准：

- 能从 dataset 训练一个 policy，并用同一套 eval harness 评估 classic-control baseline 和 BC policy。

### 2026-11：Runtime / latency / robustness

目标：

- 把 10 月的 policy pipeline 包装成更接近真实机器人软件的 runtime。
- 关注延迟、超时、异常输入、TensorRT / 量化入口和 fallback。

学习内容：

- prefill / decode / inference latency 概念
- TTFT / TPOT / throughput / latency budget
- ONNX / TensorRT / quantization awareness：FP16 / INT8 / model compile / runtime inference
- watchdog / timeout / safety guard / fallback
- VLA / OpenVLA / RT-2 / PI-0 概念阅读

产出：

- `policy_runtime v0`
- `latency_report v0`
- `fault_injection_tests v0`
- `ONNX / TensorRT / quantization awareness note`
- `VLA 概念笔记`

最低标准：

- 能说清 control frequency、policy inference latency、simulation step rate 之间的关系。
- 能处理至少三类异常：observation missing、policy timeout、action out-of-bound。

### 2026-12：作品化和年终决策

目标：

- 把全年 demo 整理成一个 `Embodied AI software mini-stack`。
- 用岗位画像检查能力缺口。
- 补多传感器融合的第一层系统视角。

产出：

- `Embodied AI mini-stack README`
- `2026 deliverable index`
- `Capability Map v1`
- `sensor_fusion_note v0`
- `2027 real-robot / edge-deployment plan`
- `目标岗位差距分析`

最低标准：

- 可以向别人演示一个完整闭环：
  `task config -> simulation -> policy/control -> data logging -> replay -> eval report -> failure analysis`
- 能讲清多传感器融合的基本问题：time sync、coordinate frame、calibration、noise、missing data。

## 2027：从仿真闭环到真实机器人 / 端侧部署

### 2027-H1：Real robot readiness

目标：

- 进入 ROS2 / real robot / Jetson / camera / actuator 的真实系统边界。
- 如果条件成熟，使用 SO-100 / SO-101 或其他低成本平台。

学习内容：

- ROS2 nodes / topics / services / bags
- camera calibration
- robot state and action interface
- Jetson basics
- ONNX export / TensorRT inference
- Docker / deployment / monitoring

产出：

- `ROS2 robot software map`
- `real robot data collection v0`
- `edge inference demo v0`
- `sensor-action logging pipeline`

### 2027-H2：职业证据型项目

目标：

- 做出一个可展示的 `robot-learning-software-stack` 项目。
- 项目要证明你不是只会玩 demo，而是能 owner 一条机器人 AI 闭环。

项目建议：

```text
robot-learning-software-stack/
├── sim/
├── robot_interface/
├── data/
├── train/
├── runtime/
├── eval/
├── replay/
├── docs/
└── reports/
```

必须包含：

- trajectory schema
- episode logger
- replay viewer
- eval harness
- policy runner
- latency profiler
- failure case index
- model / config versioning
- real or simulated robot task

年底标准：

- 外部机器人 / AI Infra 工程师看到项目后，能判断你理解机器人系统闭环。

## 2028：岗位匹配和硬决策

目标：

- 根据作品和行业机会，判断是否从当前 DB / 存储岗位切到 AI Infra / Embodied AI Software / Robot Infra。

目标岗位关键词：

- 具身智能软件工程师
- Physical AI Systems Engineer
- Robot Learning Infra Engineer
- Robot Runtime Engineer
- Robot Data / Evaluation Engineer
- AI Infra for Robotics Engineer
- Robotics Systems Software Engineer

硬决策条件：

- 有一个能讲清楚的端到端项目。
- 能解释从 sensor 到 action 的实时链路。
- 能解释机器人数据如何形成训练和评测闭环。
- 能解释模型部署、延迟、fallback 和可靠性问题。
- 对真实机器人调试的慢反馈仍然有兴趣。
- 有至少 3-5 次行业交流或面试反馈。

## 能力 Level 目标

| 能力 | 2026 年底 | 2027 年底 | 2028 决策前 |
|---|---|---|---|
| Robotics foundations | L1 | L2- | L2 |
| MuJoCo / simulation | L2- | L2 | L2 |
| Robot Learning / BC | L1+ | L2 | L2 |
| Data loop / eval | L2- | L2+ | L3- |
| AI runtime / deployment | L1 | L2 | L2+ |
| ROS2 / real robot | L0 | L1+ | L2- |
| Reliability / observability | L1 | L2 | L2+ |
| System owner thinking | L2 | L2+ | L3- |

## 不做事项

- 不把目标降级成普通后端 / 数据清洗。
- 不一开始就追求完整 VLA 训练。
- 不把 AI Infra 学成脱离机器人系统的新主线。
- 不在没有仿真和数据闭环前做复杂真机。
- 不只做“模型跑通”，必须有 eval、replay、failure analysis。

## 一句话回锚

> 目标不是成为只会写机器人业务软件的人，而是成为能把具身智能模型接入机器人、跑在端侧、采回数据、持续评测和迭代的系统 owner。
