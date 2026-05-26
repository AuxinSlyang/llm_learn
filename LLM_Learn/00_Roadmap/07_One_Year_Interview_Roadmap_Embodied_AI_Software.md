---
type: one_year_interview_roadmap
time_window: 2026-05-18_to_2027-05-31
target_role: Embodied AI Software Engineer / Robot Learning Infra / Physical AI Systems
current_role: DB / Storage Kernel Engineer
updated: 2026-05-18
linked_files:
  - "[[03_Annual_Plan_2026]]"
  - "[[04_2026_Monthly_Learning_Materials]]"
  - "[[05_Career_Strategy_2026_2030]]"
  - "[[06_Embodied_AI_Software_Engineer_Learning_Curve]]"
---

# One-Year Interview Roadmap: Embodied AI Software

> 这份文件回答的问题：**从 2026-05-18 开始，用一年时间如何达到可以去和具身智能软件 / Robot Learning Infra 岗位认真聊机会的水平？**

## JD Anchor

目标岗位不是普通后端，也不是纯机器人算法，而是围绕这四件事：

| JD 模块 | 真实含义 | 一年内要做出的证据 |
|---|---|---|
| 算法产品化 | 把具身智能算法 / policy / model 接进机器人软件栈，变成稳定功能 | `policy_runner`、接口边界、config/version 管理 |
| 模型部署与优化 | 在 Jetson Orin/Thor、昇腾等端侧硬件上部署和优化模型，降低系统延迟 | ONNX/TensorRT/量化 awareness，小模型导出和 latency report |
| 数据闭环迭代 | 建设数据采集、存储、清洗、标注、回放、训练、评测链路 | trajectory schema、episode logger、dataset、eval harness、failure replay |
| 鲁棒性与可靠性 | 处理算法失效、传感器异常、动作异常，建立测试评价体系 | timeout、watchdog、action clipping、fault injection、long-run eval |

一年后的目标不是“成为成熟真机系统 owner”，而是达到：

> 能用一个完整项目证明：我理解机器人 AI 软件闭环，能把仿真、控制、policy、数据、评测、回放、runtime、鲁棒性和 failure analysis 串起来。

## 一年面试叙事

> 我本职是 DB / 存储内核工程师，擅长复杂系统、性能、可靠性和数据管理。过去一年我系统补了 Robotics / MuJoCo / Robot Learning，并做了一个 `Embodied AI mini-stack`：从仿真任务、控制循环、episode logging、trajectory schema、BC training、policy runtime、eval harness、latency report 到 failure replay 都跑通了一版。

## 核心项目：Embodied AI Mini-Stack

一年内所有学习都围绕这个项目收敛，不做分散玩具。

```text
embodied-ai-mini-stack/
├── sim/                # MuJoCo scene, task config, control loop
├── robot_interface/    # observation/action interface
├── perception/         # camera / OpenCV / sensor fusion entry
├── data/               # trajectory schema, episode logger, metadata
├── train/              # BC training, dataset loader, configs
├── runtime/            # policy runner, latency measurement, fallback
├── eval/               # eval harness, success metrics, batch runs
├── replay/             # replay tool, video export, failure cases
├── deploy/             # ONNX/TensorRT/quantization notes and small demos
├── docs/               # architecture notes, paper notes, design docs
└── reports/            # monthly reports, interview-ready summaries
```

最终要能演示：

`task config -> simulation -> perception/state -> control/policy -> data logging -> train -> policy runtime -> eval -> replay -> failure analysis`

## 一年总节奏

| Phase | 时间 | 主目标 | 主要证据 |
|---|---|---|---|
| **A** | 2026-05-18 ~ 2026-05-31 | LLM 收口 | nanoGPT 总结、GPT 到 runtime 桥接 |
| **B** | 2026-06 ~ 2026-07 | Modern Robotics 大部分内容 + AI fundamentals / perception 入口 | MR Ch.1-6、机器人系统图、MuJoCo step loop、CS231n/CV 入口 |
| **C** | 2026-08 | MR 动力学/控制 + RL 基本概念 | 控制闭环、trajectory schema、RL/IL 概念地图 |
| **D** | 2026-09 ~ 2026-10 | IL 概念 + MuJoCo 仿真 + Robot Learning 第一次动手 | classic-control demo、BC dataset、train/eval、eval harness |
| **E** | 2026-11 | 算法产品化 + runtime / TensorRT / 量化 awareness | policy runtime、latency report、ONNX/TensorRT 小验证 |
| **F** | 2026-12 | 鲁棒性、多传感器融合入口、作品化 | fault tests、sensor fusion note、mini-stack README |
| **G** | 2027-01 ~ 2027-02 | ROS2 / real robot / edge deployment 入口 | ROS2 map、bag/replay demo、edge inference demo |
| **H** | 2027-03 ~ 2027-04 | 面试作品强化 + Robot Learning 论文线 | 技术文章、demo video、JD mapping、外部 review |
| **I** | 2027-05 | 市场测试和面试聊天 | portfolio、mock interview、岗位差距清单 |

## Phase A：LLM 收口（2026-05-18 ~ 2026-05-31）

### 目标

5 月底前结束 LLM phase 1，不再拖成长期主线。

### 学习内容

- Karpathy `nn-zero-to-hero`：nanoGPT / tokenizer / GPT-2 收口。
- GPT 最小链路：`tokenizer -> embedding -> attention -> block -> logits -> loss/generate`。
- CS336 只做结构对照：tokenization、Transformer、training loop、eval、deployment 在语言模型系统中的位置。

### 产出

- `nanoGPT 第一轮总结`
- `tokenizer / nanoGPT / GPT-2 主线映射`
- `makemore -> nanoGPT -> inference_runtime 映射`
- `后续 LLM / AI Infra 只保留支撑线` 说明

### 面试可讲点

- 为什么 LLM inference / runtime 对机器人语言智能有意义。
- 为什么 5 月之后不继续深挖通用 LLM Infra，而是把它作为具身智能软件支撑能力。

## Phase B：Robotics + AI Fundamentals 入口（2026-06 ~ 2026-07）

### 目标

用两个月建立机器人系统底层语言，并补感知 / AI fundamentals 入口。这个阶段是后续所有 Robot Learning 和具身智能软件的地基。

### 学习内容

- Modern Robotics Ch.1-6：
  - configuration space
  - rigid-body motion
  - SO(3) / SE(3)
  - forward kinematics
  - Jacobian
  - inverse kinematics
- MuJoCo Python：
  - model / data / step
  - qpos / qvel / ctrl / actuator
  - simulation loop
- CS231n / CV 精选：
  - 图像分类 / 检测 / segmentation 的问题形态
  - CNN / ViT 基本直觉
  - OpenCV 读图、相机、简单检测
- CS336 精选：
  - deployment / inference / runtime 概念位置
  - 不做完整 assignment，不做 distributed training project

### 项目任务

- 画 `sensor -> state -> perception -> decision -> action -> robot -> log -> dataset -> train -> eval` 系统图。
- 跑通 `mujoco_hello_world`。
- 写 `sim_loop.py`：reset、step、read state、apply action。
- 写 `episode_logger v0`：保存 timestamp、state、action、config。
- 写 `state/action schema v0`。

### 面试可讲点

- observation、state、action、control command 的区别。
- 为什么机器人数据必须按 episode 组织。
- `感知-决策-执行` 链路中每层负责什么。
- 为什么 CS231n 和 CS336 都不是主线课程，而是分别服务 perception 和 runtime。

## Phase C：动力学/控制 + RL 基本概念（2026-08）

### 目标

把 MR 运动学接到控制闭环，并建立 RL/IL 的概念地图。

### 学习内容

- MR 动力学 / 轨迹 / 控制入口：
  - 第一遍不追完整推导，先建立控制边界。
  - 重点理解运动学、动力学、控制、policy 的接口。
- MuJoCo 控制：
  - joint PD control
  - end-effector target
  - optional simple IK
- RL 概念：
  - MDP
  - policy
  - reward
  - value
  - Q-learning / PPO 的位置
- IL 概念预热：
  - BC
  - DAgger
  - covariate shift

### 项目任务

- 实现一个关节 PD 控制实验。
- 可选实现一个简单 IK / 末端目标控制。
- 定义 `trajectory schema v1`：
  - `episode_id`
  - `task_id`
  - `seed`
  - `observation`
  - `qpos/qvel`
  - `action`
  - `reward/success`
  - `failure_reason`
- 实现 `metrics v0`：success rate、episode length、control error、latency placeholder。

### 面试可讲点

- classic control 和 Robot Learning 的关系。
- 机器人数据 schema 为什么需要保留 task config、seed、failure reason。
- 为什么训练 loss 不等于真实机器人任务成功率。

## Phase D：IL + MuJoCo 仿真闭环（2026-09 ~ 2026-10）

### 目标

用 MuJoCo 做出一个可复现任务，再用 Behavior Cloning 跑通第一次 Robot Learning。

### 学习内容

- task definition、success criteria、failure mode。
- Imitation Learning：
  - Behavior Cloning
  - DAgger 概念
  - data distribution
  - policy input/output contract
- LeRobot：
  - dataset
  - policy
  - training
  - eval
- Robot Learning 论文：
  - ACT / ALOHA
  - Diffusion Policy
  - 只先看 observation、action、数据采集、eval 和系统结构。

### 项目任务

- 选择 `reach` / `push` / `pick-place` 三选一，默认从 `reach` 或 `push` 起步。
- 用 classic control 跑通 N 个 episode。
- 输出 eval report：
  - success rate
  - mean steps
  - failure categories
  - sample videos
- 用 scripted policy 或 teleop 采集 `BC dataset v0`。
- 训练一个简单 BC policy。
- 写 `policy_runner v0`，把 policy 接回 sim loop。
- 用同一套 eval harness 对比 classic-control baseline 和 BC policy。

### 面试可讲点

- BC 为什么会失败。
- 数据分布如何影响 policy。
- eval harness 比单次 demo 为什么更重要。
- 从 failure case 如何反推下一轮数据采集和训练需求。

## Phase E：算法产品化 + Runtime / TensorRT / 量化入口（2026-11）

### 目标

把 policy demo 从“训练实验”推进成“具身智能软件组件”。

### 学习内容

- AI runtime 概念：
  - prefill / decode
  - KV cache
  - TTFT / TPOT
  - throughput / latency
  - control loop latency budget
- 模型部署：
  - ONNX export
  - TensorRT 基础概念
  - quantization awareness
  - FP16 / INT8 概念
  - model compile vs runtime inference
- 机器人 runtime：
  - policy timeout
  - action clipping
  - fallback
  - watchdog

### 项目任务

- 写 `policy_runtime v0`。
- 记录：
  - policy inference latency
  - simulation step latency
  - end-to-end loop latency
  - jitter
- 做一个最小 `ONNX export + latency measurement`。
- 如果环境允许，尝试 TensorRT 或等价推理优化；如果环境不允许，写清楚理论路径和缺口。
- 实现三类异常处理：
  - observation missing
  - policy timeout
  - action out-of-bound

### 面试可讲点

- 机器人为什么不能只看模型 accuracy。
- latency、jitter、fallback 在机器人里为什么重要。
- TensorRT / 量化解决什么问题，不解决什么问题。
- 高层 VLA 推理和低层控制频率为什么需要分层。

## Phase F：鲁棒性 + 多传感器融合入口 + 作品化（2026-12）

### 目标

把 mini-stack 包装成作品，同时补多传感器融合的第一层理解。

### 多传感器融合怎么做

今年不追完整 SLAM / EKF / factor graph，只建立软件系统视角：

- 传感器来源：
  - RGB camera
  - depth
  - IMU
  - joint states
  - force / torque
  - robot base pose
- 核心问题：
  - time synchronization
  - coordinate frames
  - calibration
  - noise / missing data
  - sensor confidence
  - fusion output as state estimate
- 最小实践：
  - camera frame + qpos/qvel 同步记录
  - 用 timestamp 对齐 observation
  - 在 replay 中同时显示视觉帧和 robot state
  - 写 `sensor_fusion_note v0`

### 项目任务

- 写 `fault_injection_tests v0`。
- 写 `sensor_fusion_note v0`。
- 整理 `Embodied AI mini-stack README`。
- 补架构图和 demo video。
- 写 `目标岗位差距分析`。
- 更新 `Capability Map v1`。

### 年底最低标准

- 有一个完整可运行项目。
- 能展示数据闭环和 eval report。
- 能讲清 Robot Learning 的基本问题。
- 能讲清多传感器融合为什么是 state estimation 的入口。
- 能讲清具身智能软件工程师 JD 和自己项目的对应关系。

## Phase G：ROS2 / 真机 / Edge Deployment 入口（2027-01 ~ 2027-02）

### 目标

进入真实机器人软件边界，不再只停留在 MuJoCo。

### 学习内容

- ROS2：
  - nodes
  - topics
  - services
  - bags
  - launch
- real robot data:
  - camera calibration
  - sensor timestamp
  - data synchronization
  - robot state/action interface
- edge deployment：
  - Jetson 基础
  - ONNX Runtime
  - TensorRT demo
  - Docker / deployment / monitoring

### 项目任务

- 写 `ROS2 robot software map`。
- 做一个最小 ROS2 logging / replay demo。
- 把一个小模型导出 ONNX，并做本地或远端推理 latency 测试。
- 如果条件成熟，评估 SO-100 / SO-101 或其他低成本平台，并开始实物平台数据采集。

### 面试可讲点

- ROS2 bag 和 robot data logging 的关系。
- edge inference 和云端 inference 的差异。
- 真机数据为什么比仿真数据更难管理。

## Phase H：面试作品强化（2027-03 ~ 2027-04）

### 目标

把学习项目升级成面试作品。

### 项目任务

- 项目结构整理成可以展示的版本。
- 写三篇技术文章：
  - `Robot data lifecycle`
  - `Simulation eval harness`
  - `Policy runtime and failure handling`
- 加入一个真实或半真实扩展：
  - ROS2 bag 数据回放
  - 真实摄像头输入
  - 低成本机械臂数据采集
  - 或者更完整的 MuJoCo batch eval
- 做一次外部 review：找同学、机器人方向朋友或社区工程师看项目。

### 面试可讲点

- 如何设计一个 robot learning software stack。
- 如何 debug policy failure。
- 如何把 DB / 存储经验迁移到机器人数据闭环。

## Phase I：市场测试（2027-05）

### 目标

正式开始面试聊天和机会判断。

### 准备材料

- 项目 README。
- 3-5 分钟 demo video。
- 架构图。
- 技术文章 2-3 篇。
- JD mapping 文档：
  - 算法产品化
  - 模型部署优化
  - 低延迟链路
  - 数据闭环
  - 鲁棒性
  - 真机测试评价
- 面试 Q&A 文档。

### 目标交流对象

- 宇树 / 云深处 / 海康机器人 / 蓝芯机器人中的软件系统、数据闭环、AI Infra 岗位。
- 做机器人数据平台、仿真评测、Robot Learning Infra 的工程师。
- 学术实验室中做 robot learning / locomotion / manipulation 的 PhD 或工程师。

### 到 2027-05 的合格线

- 能讲清一个端到端项目。
- 能把项目映射到 JD。
- 能回答 Robot Learning 基本问题。
- 能解释机器人数据闭环。
- 能解释 runtime latency、TensorRT/量化 awareness 和 fallback。
- 能讲清多传感器融合的基本问题：时间同步、坐标系、标定、噪声、缺失数据。
- 能承认短板：真机经验不足、复杂控制不足、VLA 只到 awareness。

## Robot Learning 学习线

### 必须理解

- Behavior Cloning
- DAgger 概念
- covariate shift
- observation / action representation
- success rate vs training loss
- teleop / scripted policy / dataset quality
- eval and failure analysis

### 论文阅读顺序

集中索引见：`04_Papers/01_Reading_Index.md`。每日轻量阅读按 `04_Papers/00_Reading_Workflow.md` 执行；只有进入当前 Phase 的论文才升级为精读。

第一层：能动手的 Imitation Learning

- ACT / ALOHA
- Diffusion Policy
- 3D Diffusion Policy 选读

第二层：generalist robot policy

- RT-1 / RT-2
- Octo
- OpenVLA
- PI-0

第三层：数据和系统

- Open X-Embodiment
- LeRobot
- robot data curation / eval 相关材料

### 论文阅读模板

模板见：`99_Templates/Paper_Templates.md`。每篇论文第一遍只回答 8 个问题：

- 任务是什么？
- observation 是什么？
- action 是什么？
- 数据怎么采？
- policy 输出什么？
- eval 怎么做？
- failure mode 是什么？
- 如果我要产品化，需要什么 software / data / runtime 支撑？

## 面试能力矩阵

| 能力 | 2026-11 市场测试 | 2027-05 正式聊天 |
|---|---|---|
| Robotics 基础 | 能讲 FK/IK/Jacobian/控制边界 | 能结合项目讲 state/action/control |
| MuJoCo | 跑通并记录 episode | 能做 batch eval / replay / failure analysis |
| Robot Learning | 理解 BC/IL，跑通 train/eval | 能讲数据分布、policy failure、eval |
| Perception / CV | OpenCV / CS231n 入口 | 能讲视觉 observation 如何进入 policy |
| Multi-sensor fusion | awareness | 能讲 time sync / frame / calibration / missing data |
| Data loop | trajectory schema / logger | dataset、metadata、replay、failure index |
| Runtime | latency 概念 | policy runtime、timeout、fallback |
| AI Infra | nanoGPT / inference awareness | ONNX/TensorRT/量化 awareness + profiling |
| ROS2 / real robot | awareness | 至少有 ROS2 logging/replay demo |
| 职业叙事 | 兴趣和方向清晰 | 作品能对齐 JD |

## 不做事项

- 不在一年内追求完整 VLA 训练。
- 不把 CS231n / CS336 / MR 全部当成必须完整刷完的课程。
- 不把多传感器融合扩展成完整 SLAM 主线。
- 不把项目做成普通后端数据平台。
- 不只做论文阅读，不落到可运行系统。
- 不为了面试过度包装自己已经能做真机系统 owner。

## 一句话回锚

> 一年路线的核心不是“学完机器人”，而是做出一个可解释、可运行、可评测的具身智能软件 mini-stack，并用它去和真实岗位认真对话。
