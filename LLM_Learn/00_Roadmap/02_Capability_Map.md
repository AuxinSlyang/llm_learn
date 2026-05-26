# Capability Map

> 这份文件回答的问题：**通用机器人需要哪些能力？我当前 Level 是什么？**
> 这是一份 **living document**，每季度复盘时更新 Level。
> 版本：v0 / 写于 2026-05-17。

## 三大 Pillar 总览

| Pillar | 当前总体 Level | 2026 年底目标 | 主关注 |
|---|---|---|---|
| 1. Classical Robotics | L0- | L1+ | MR + MuJoCo |
| 2. AI Fundamentals | L1- | L2 | LLM 收口 + CV |
| 3. Robot Learning | L0 | L1 | RL/IL 概念 + 第一次动手 |
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
| URDF / MJCF | L0 | L1 | MuJoCo 文档 | Phase B-D |
| **MuJoCo** | L0 | **L2** | MuJoCo Python tutorial | **Phase B-F 主载体** |
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
| OpenCV 基础 | L0 | L1 | OpenCV-Python tutorial | Phase B |
| 检测（YOLO 等） | L0 | L1 | Ultralytics YOLOv8 | Phase D-E |
| 跟踪 | L0 | L1 | OpenCV trackers | Phase E |
| 位姿估计（ArUco/PnP） | L0 | L1 | OpenCV docs | Phase E |
| 分割 | L0 | L0 | 2027 | 后续 |
| 多视角 / 立体视觉 | L0 | L0 | 2027 | 远期 |

### NLP / LLM

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| **Transformer** | L1 | **L2** | nanoGPT ✅ 进行中 | Phase A |
| Tokenizer | L0 | L1 | Karpathy tokenizer | Phase A |
| Inference (KV cache / TTFT) | L0 | L1 | nano-vllm | Phase F |
| Serving (vLLM) | L0 | L0 | 2027 | 2027 |

### 多模态 / VLM / VLA

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| VLM 基础 (CLIP / LLaVA) | L0 | L0 | 2027 | awareness |
| VLA (RT-1/RT-2/OpenVLA/PI-0) | L0 | L0 | paper reading | **Phase F awareness** |

### 推理工程

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| vLLM / SGLang | L0 | L0 | 2027 | 2027 |
| 量化 / 部署 | L0 | L0 | 2027+ | 远期 |

---

## Pillar 3: Robot Learning

### RL 基础

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| MDP / value / policy | L0 | L1 | Sutton & Barto Ch.3-6 | Phase C |
| Q-learning / DQN | L0 | L1 | Spinning Up | Phase C |
| Policy Gradient / PPO / SAC | L0 | L1 | Spinning Up | Phase C |

### Imitation Learning（今年主推）

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| **Behavior Cloning (BC)** | L0 | **L2** | LeRobot tutorial | **Phase D-E 第一次动手** |
| DAgger | L0 | L1 | paper | Phase E |
| 数据采集 / teleop | L0 | L1 | LeRobot | Phase E |

### 现代 Policy 范式

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| ACT | L0 | L1 | paper + LeRobot 实现 | Phase D paper read |
| Diffusion Policy | L0 | L1 | paper + code | Phase D paper read |

### VLA / Foundation Models

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| RT-1 / RT-2 | L0 | L0 | paper | Phase F awareness |
| OpenVLA | L0 | L0 | paper + GitHub | Phase F awareness |
| PI-0 / RDT | L0 | L0 | paper | Phase F awareness |

### Sim-to-real

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| Domain randomization | L0 | L0 | 2027 | 实物期 |
| System identification | L0 | L0 | 2027 | 实物期 |

### Manipulation / Locomotion Learning

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| **Pick-place learning** | L0 | **L2** | LeRobot + MuJoCo | **Phase E** |
| Walking policies | L0 | L0 | 2027+ | 远期 |

### 工具链

| 子方向 | 当前 | 目标 | 资料 | 备注 |
|---|---|---|---|---|
| **LeRobot** | L0 | L1 | HF 官方 | Phase D-E 主框架 |
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
| 机器人足球（11v11） | P1 + P3 + 多智能体 | 长期主 anchor |
| Manipulation (pick-place) | P1 + P2 + P3 | **2026 H2 第一个 demo anchor** |
| Mobile navigation | P1 + P2 | 2027 |
| Multi-robot coordination | P1 + P3 + 通信 | 2027+ |

---

## 当前能力快照（2026-05-17）

- Pillar 1: **L0-**（MR 未启动，已恢复入口）
- Pillar 2: **L1-**（nanoGPT 收口中，CV 未启动）
- Pillar 3: **L0**（未启动，Phase C 起）
- 横切: **L2**（已有，持续用）

## 季度更新规则

- **Q2 末（2026-06-30）**：Phase A 结束，更新一次
- **Q3 末（2026-09-30）**：Phase B-D 结束，更新一次
- **Q4 末（2026-12-31）**：年终复盘，更新到 v1（带年度复盘 + 2027 方向）

每次更新只动 Level 列 + 备注列，不动结构。结构动了 = 文件版本号 +1（v0 → v1）。
