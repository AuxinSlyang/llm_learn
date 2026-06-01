# Capability Map

> 这份文件回答的问题：**通用机器人需要哪些能力？我当前 Level 是什么？**
> 这是一份 **living document**，每季度复盘时更新 Level。
> 版本：v0.2 / 写于 2026-05-17；2026-06-01 修订一年主线为 Robot Learning Full-Stack。

## 能力 Pillar 总览

| Pillar | 当前总体 Level | 2026 年底目标 | 主关注 |
|---|---|---|---|
| 1. Classical Robotics | L0- | L1+ | Modern Robotics / kinematics / control |
| 2. AI Fundamentals | L1- | L1+ | nanoGPT 收口 + robot perception support |
| 3. Robot Learning | L0 | L1 | Gymnasium/MuJoCo / PPO / BC / eval harness |
| 4. LLM / AI Infra / Runtime | L0 | L1 | VLA / policy runtime / edge inference 支撑线 |
| 0. 横切（工程底座） | L2 | L2+（保持） | Python / Linux / Git |

---

## Pillar 1: Classical Robotics

### 数学基础

| 子方向 | 当前 | 目标(2026) | 主要资料 | 备注 |
|---|---|---|---|---|
| 线性代数 | L2 | L2 | 已有 | 学过 |
| 微积分 | L2 | L2 | 已有 | 学过 |
| 概率论 | L1 | L2 | Bishop / MIT 6.041 选读 | 后续补 |
| 优化基础 | L0 | L1 | MR Appendix | Phase B 顺便补 |
| **李群 / 李代数 (SE(3))** | L0 | **L2** | MR Ch.3 | **机器人核心数学** |

### 运动学

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| 刚体表示 | L0 | L2 | MR Ch.3 + Lynch C1 | Phase A-B |
| Forward Kinematics | L0 | L2 | MR Ch.4 + Lynch C2 | Phase B |
| Inverse Kinematics | L0 | L2 | MR Ch.6 + Lynch C2 | Phase B |
| Jacobian | L0 | L2 | MR Ch.5 + Lynch C2 | Phase B |

### 动力学

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| Lagrangian / Newton-Euler | L0 | L1 | MR Ch.8 + Lynch C3 | Phase C |

### 控制

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| PID（经典控制） | L1 | L2 | 通用 + 嵌入式经验 | 已有底子 |
| LQR / MPC | L0 | L1 | MR Ch.11 / 2027 | 2027 |
| 阻抗 / 力控 | L0 | L1 | 2027 | 2027 |

### 规划

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| 路径规划 (A* / RRT) | L0 | L1 | 2027 | 2027 |
| 运动规划 | L0 | L1 | MR Ch.10 / 2027 | 2027 |
| 任务规划 (TAMP) | L0 | L0 | 2027+ | 远期 |

### 状态估计 / SLAM

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| 卡尔曼滤波 | L0 | L1 | 2027 | 2027 |
| SLAM | L0 | L0 | 2027+ | 远期 |

### 软件栈 / 仿真

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| URDF / MJCF | L0 | L1 | MuJoCo 文档 | 后续机器人回接 |
| **MuJoCo** | L0 | **L2** | MuJoCo Python tutorial | 后续机器人回接主载体 |
| ROS2 | L0 | L0 | 2027 | 2027 主推 |
| Isaac Sim | L0 | L0 | 2027+ | 看 MuJoCo 是否够用 |

---

## Pillar 2: AI Fundamentals

### DL 基础

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| autograd / backward | L2 | L2 | micrograd ✅ | 已收口 |
| 优化器 | L1 | L2 | makemore / nanoGPT | 进行中 |
| 训练 loop | L1 | L2 | nanoGPT | Phase A 收口 |

### CV

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| OpenCV 基础 | L0 | L1 | OpenCV-Python tutorial | 后续机器人回接 |
| 检测（YOLO 等） | L0 | L1 | Ultralytics YOLOv8 | 后续机器人回接 |
| 跟踪 | L0 | L1 | OpenCV trackers | 后续机器人回接 |
| 位姿估计（ArUco/PnP） | L0 | L1 | OpenCV docs | 后续机器人回接 |
| 分割 | L0 | L0 | 2027 | 后续 |
| 多视角 / 立体视觉 | L0 | L0 | 2027 | 远期 |

### NLP / LLM

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| **Transformer** | L1 | **L2** | nanoGPT ✅ 进行中 | Phase A |
| Tokenizer | L0 | L1 | Karpathy tokenizer | Phase A |
| Inference (KV cache / TTFT) | L0 | L1 | nanoGPT / vLLM 精选 | VLA / policy runtime 支撑线 |
| Serving (vLLM) | L0 | L1 | vLLM / SGLang 精选 | 支撑线，不作为上位主线 |

### 多模态 / VLM / VLA

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| VLM 基础 (CLIP / LLaVA) | L0 | L0 | 2027 | awareness |
| VLA (RT-1/RT-2/OpenVLA/PI-0) | L0 | L0+ | paper reading | 2027 回接入口 |

### 推理工程

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| vLLM / SGLang | L0 | L1 | vLLM docs / SGLang docs | VLA / edge inference 支撑线 |
| TensorRT-LLM | L0 | L1 | NVIDIA docs / examples | awareness |
| 量化 / 部署 | L0 | L1 | ONNX / TensorRT / quantization notes | policy runtime 支撑 |

---

## Pillar 4: LLM / AI Infra / Runtime 支撑线

> 2026-06-01 修订：LLM / AI Infra / Runtime 作为 VLA、policy runtime、edge inference 的支撑线保留，不再作为当前上位主线。

### 推理链路

| 子方向 | 当前 | 目标(2026) | 主要资料 | 备注 |
|---|---|---|---|---|
| Transformer inference path | L0+ | L2 | nanoGPT / CS336 精选 | `training -> inference` 桥接 |
| Prefill / decode | L0 | L2 | vLLM / serving notes | 推理系统核心语言 |
| KV cache | L0 | L2 | vLLM / PagedAttention | 显存管理核心 |
| Sampling / streaming | L0 | L1 | HF / vLLM | 服务输出路径 |

### Serving / 调度

| 子方向 | 当前 | 目标(2026) | 主要资料 | 备注 |
|---|---|---|---|---|
| vLLM | L0 | L1 | vLLM docs / code reading | 支撑线 |
| SGLang | L0 | L1 | SGLang docs | 对比学习 |
| Continuous batching | L0 | L2 | vLLM / serving papers | scheduler 核心 |
| Request scheduler | L0 | L1+ | 自建 mini-stack | 项目证据 |
| Load test / benchmark | L0 | L2 | 自建 harness | TTFT / TPOT / throughput |

### GPU / 优化

| 子方向 | 当前 | 目标(2026) | 主要资料 | 备注 |
|---|---|---|---|---|
| GPU memory / HBM awareness | L0+ | L1+ | CUDA / profiling notes | 系统背景可迁移 |
| PyTorch profiler / nsys | L0 | L1 | official docs | 先会用工具定位 |
| TensorRT-LLM | L0 | L1 | NVIDIA docs | awareness + 小验证 |
| Quantization | L0 | L1 | FP16 / INT8 / AWQ / GPTQ | 不追完整算法 |
| CUDA kernel awareness | L0 | L0+ | CUDA basics | 先懂边界，不硬写 kernel |

### 分布式训练 Awareness

| 子方向 | 当前 | 目标(2026) | 主要资料 | 备注 |
|---|---|---|---|---|
| DP / TP / PP | L0 | L1 | Megatron-LM overview | 面试级概念 |
| ZeRO / optimizer state | L0 | L1 | DeepSpeed overview | 不做主项目 |
| Megatron-LM | L0 | L0+ | docs / blogs | 保留入口 |

---

## Pillar 3: Robot Learning

### RL 基础

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| MDP / value / policy | L0 | L1 | Sutton & Barto Ch.3-6 | Phase C |
| Q-learning / DQN | L0 | L1 | Spinning Up | Phase C |
| Policy Gradient / PPO / SAC | L0 | L1 | Spinning Up | Phase C |

### Imitation Learning（后续机器人阶段主推）

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| **Behavior Cloning (BC)** | L0 | **L2** | LeRobot tutorial | 后续机器人阶段第一次动手 |
| DAgger | L0 | L1 | paper | 后续机器人回接 |
| 数据采集 / teleop | L0 | L1 | LeRobot | 后续机器人回接 |

### 现代 Policy 范式

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| ACT | L0 | L1 | paper + LeRobot 实现 | 后续机器人回接 |
| Diffusion Policy | L0 | L1 | paper + code | 后续机器人回接 |

### VLA / Foundation Models

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| RT-1 / RT-2 | L0 | L0 | paper | 2027 回接 |
| OpenVLA | L0 | L0 | paper + GitHub | 2027 回接 |
| PI-0 / RDT | L0 | L0 | paper | 2027 回接 |

### Sim-to-real

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| Domain randomization | L0 | L0 | 2027 | 实物期 |
| System identification | L0 | L0 | 2027 | 实物期 |

### Manipulation / Locomotion Learning

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| **Pick-place learning** | L0 | **L2** | LeRobot + MuJoCo | 后续机器人阶段 |
| Walking policies | L0 | L0 | 2027+ | 远期 |

### 工具链

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| **LeRobot** | L0 | L1 | HF 官方 | 后续机器人阶段主框架 |
| Stable Baselines 3 | L0 | L0 | 2027 | 2027 |

---

## Pillar 0: 横切能力（工程底座）

| 能力 | 当前 | 备注 |
|---|---|---|
| 嵌入式 / 硬件抽象 | L2 ✅ | 差异化资产 |
| CS / 系统工程 | L2 ✅ | 差异化资产 |
| Python / NumPy / PyTorch | L2 | 持续用 |
| Linux / SSH / venv | L2 | 持续用 |
| Git / 项目管理 | L2 | 持续用 |
| Docker / 部署 | L1 | 按需补 |

---

## Anchor 场景清单

| Anchor | Pillar 覆盖 | 时间窗 |
|---|---|---|
| Manipulation (pick-place) | P1 + P2 + P3 | 2027+ 机器人回接 anchor |
| Mobile navigation | P1 + P2 | 2027 |
| Multi-robot coordination | P1 + P3 + 通信 | 2027+ |
| LLM / VLA runtime for robots | P2 + P4 + P3 | **2026 H2 -> 2027 回接桥** |

---

## 当前能力快照（2026-06-01）

- Pillar 1: **L0-**（2026 H2 开始进入 Modern Robotics / kinematics / control）
- Pillar 2: **L1-**（nanoGPT 收口中，后续服务 perception / VLA / language intelligence）
- Pillar 3: **L0**（2026-06 开始用 Gymnasium/MuJoCo + PPO 建最小闭环）
- Pillar 4: **L0**（作为 VLA / policy runtime / edge inference 支撑线保留）
- 横切: **L2**（已有，持续用）

## 季度更新规则

- **Q2 末（2026-06-30）**：更新 nanoGPT 收口、Robot Learning Full-Stack 路线、Gymnasium/MuJoCo PPO 最小闭环进度
- **Q3 末（2026-09-30）**：更新 Modern Robotics、控制 / 动力学入口、policy runtime awareness 进度
- **Q4 末（2026-12-31）**：年终复盘，更新到 v1（带 robot learning / policy runtime mini-stack 复盘 + 2027 H1 方向）

每次更新只动 Level 列 + 备注列，不动结构。结构动了 = 文件版本号 +1（v0 → v1）。
