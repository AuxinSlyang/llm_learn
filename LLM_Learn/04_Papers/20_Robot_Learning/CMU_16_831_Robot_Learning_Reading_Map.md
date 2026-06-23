---
type: reading_map
track: robot learning / CMU 16-831 / sim2real / safe robotics
status: active_long_term_queue
created: 2026-06-23
source_course: https://16-831-s24.github.io/
linked_project: [[so-arm101-lerobot-first-loop]]
---

# CMU 16-831 Robot Learning Reading Map

## 定位

CMU `16-831: Introduction to Robot Learning` 是后续系统补齐 Robot Learning 的课程级路线。它覆盖：

```text
imitation learning
-> model-free RL
-> model-based RL / world models
-> offline RL / inverse RL
-> exploration
-> sim2real / real2sim
-> safe robot learning
-> transferable / adaptive robot learning
-> foundation models in robotics
```

这条线是长期学习队列，不替代当前 `SO-ARM101 + LeRobot` 首闭环。当前执行规则：

- SO-ARM101 没有真实 record/replay 前，不把 16-831 变成晚间主线。
- 每次只从课程表里抽 1 个主题做 structured read。
- 每个主题都要回到 `observation -> action -> policy -> eval -> failure -> runtime/data loop`。

## 当前优先级

| 层级 | 内容 | 为什么 |
|---|---|---|
| P0 | `ACT / ALOHA`、LeRobot dataset flow | 已完成第一轮；训练 ACT/BC v0 时回看 |
| P1 | `Agile But Safe`、sim2real / real2sim | 用户明确提到；服务安全、部署、sim-real gap |
| P1 | `DAgger`、`Diffusion Policy` | 直接解释 BC 失败、action generation 和数据闭环 |
| P2 | 16-831 model-free / model-based / offline RL 全课程 | 后续慢慢补，不抢硬件首闭环 |
| P2 | foundation models in robotics | OpenVLA / pi0 / SayCan / CLIPort / RT-1 等已在 VLA 队列中逐步覆盖 |

## Added Explicit Queue - 2026-06-23

### Safe / Agile Locomotion

| 状态 | 材料 | 链接 | 读法 | 输出标准 |
|---|---|---|---|---|
| queued | Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion | https://arxiv.org/abs/2401.17583 | Structured Read | agile policy / recovery policy / reach-avoid value / exteroception / sim2real randomization |
| queued | Agile But Safe project page | https://agile-but-safe.github.io/ | Demo + system scan | 看真实部署、传感器、速度、安全切换 |
| queued | ABS code | https://github.com/LeCAR-Lab/ABS | Code triage later | 只查模块结构，不复现 |
| radar | Bridging Adaptivity and Safety | https://adaptive-safe-locomotion.github.io/ | Later scan | ABS 后续 adaptive safety |

### Sim2Real / Real2Sim

| 状态 | 材料 | 链接 | 读法 | 输出标准 |
|---|---|---|---|---|
| queued | Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World | https://arxiv.org/abs/1703.06907 | Classic Scan | sim2real 为什么要随机化视觉/物理参数 |
| queued | Real2Sim or Sim2Real: Robotics Visual Insertion using Deep Reinforcement Learning and Real2Sim Policy Adaptation | https://arxiv.org/abs/2206.02679 | Structured Scan | real2sim policy adaptation 和 sim2real 的差异 |
| queued | Champion-Level Drone Racing using Deep Reinforcement Learning | https://www.nature.com/articles/s41586-023-06419-4 | Case Study | 高速真实部署里的 sim2real / safety / latency |
| radar | Precision home robots learn with real-to-sim-to-real | https://news.mit.edu/2024/precision-home-robotics-real-sim-real-0731 | Later scan | scanned home env -> sim -> real deployment |

## CMU 16-831 Course Reading Queue

Source: `https://16-831-s24.github.io/lectures/`.

### Introduction / ML-DL Refresher

| Lecture | Reading | 状态 | 备注 |
|---|---|---|---|
| L1 | Building Machines That Learn and Think Like People | queued | cognitive / compositional motivation |
| L2 | Sutton & Barto RL Textbook Ch.1 | queued | RL problem framing |
| L3-L4 | Deep Learning Book Ch.5-10 | reference | ML/DL refresher，按缺口查 |

### Imitation Learning

| Lecture | Reading | 状态 | 备注 |
|---|---|---|---|
| L5 | ICML Imitation Learning Tutorial | queued | IL 总览 |
| L5 | An Invitation to Imitation | queued | IL 入门 survey |
| L6 | DAgger | queued | BC covariate shift / dataset aggregation |
| L6 | GAIL | queued | imitation as adversarial occupancy matching |
| L6 | Diffusion Policy | queued | action sequence denoising |
| L6 | Transporter Networks | queued | visual manipulation / pick-place representations |

### Model-Free RL

| Lecture | Reading | 状态 | 备注 |
|---|---|---|---|
| L7 | Sutton & Barto Ch.3-4 | queued | value / policy iteration |
| L7 | Spinning Up: Key Concepts in RL | reference | 概念查漏 |
| L7 | Spinning Up: Kinds of RL Algorithms | reference | algorithm taxonomy |
| L8 | Sutton & Barto Ch.5-7 | queued | TD / Q-learning basics |
| L8 | DQN | queued | deep Q-learning 经典入口 |
| L9 | Sutton & Barto Ch.13 | queued | policy gradients |
| L9 | Spinning Up: Intro to Policy Gradient | reference | REINFORCE / policy gradient |
| L10 | Sutton & Barto Ch.13 | queued | actor-critic |
| L11 | PPO | queued | practical policy optimization |
| L11 | TRPO | queued | trust-region policy optimization |
| L11 | DDPG | queued | deterministic actor-critic / continuous control |
| L11 | SAC | queued | entropy-regularized off-policy RL |

### Model-Based RL / World Models / Planning

| Lecture | Reading | 状态 | 备注 |
|---|---|---|---|
| L12 | Feedback Systems Textbook | reference | control basics |
| L13 | Murray's Notes | reference | optimal control |
| L13 | iLQR | queued | trajectory optimization |
| L13 | DDP | queued | differential dynamic programming |
| L13 | SCP | queued | sequential convex programming |
| L14 | PETS | queued | probabilistic ensembles + trajectory sampling |
| L14 | Neural-Control Family | reference | Guanya Shi related control/RL work |
| L14 | MPPI | queued | sampling-based model predictive control |
| L14 | PILCO | queued | data-efficient model-based policy search |
| L14 | MBPO | queued | model-based policy optimization |
| L15 | Dreamer | queued | latent world model + imagined rollout |
| L15 | TD-MPC | queued | task-oriented latent dynamics / MPC |

### Structured World Models / Physical Interactions

| Lecture | Reading | 状态 | 备注 |
|---|---|---|---|
| L16 | RoboCook | queued | deformable object / structured physical interaction |
| L16 | DynRes | queued | dynamics residual / structured dynamics |
| L16 | SparseDyn | queued | sparse dynamics |
| L16 | DPI-Net | queued | dynamic particle interaction networks |

### Offline RL / IRL / Preferences / Exploration

| Lecture | Reading | 状态 | 备注 |
|---|---|---|---|
| L17 | NeurIPS Offline RL Tutorial | queued | offline RL 总览 |
| L17 | IQL | queued | implicit Q-learning |
| L17 | Diffuser | queued | planning with diffusion |
| L18 | Maximum Entropy IRL | queued | IRL 经典入口 |
| L18 | LP-IRL | queued | inverse RL formulation |
| L19 | Sutton & Barto Ch.2 | queued | bandits |
| L19 | Dueling Bandits | queued | preference-based bandit |
| L20 | Curiosity | queued | intrinsic motivation |
| L20 | RND | queued | random network distillation exploration |

### Specialized Topics

| Lecture | Reading | 状态 | 备注 |
|---|---|---|---|
| L21 | Domain Randomization | queued | sim2real 经典入口 |
| L21 | Champion-Level Drone Racing | queued | high-speed sim2real deployment |
| L22 | Safe Robot Learning Survey | queued | safe RL / safe robot learning |
| L22 | Data-Driven Safety Filters | queued | runtime safety filters |
| L23 | Teacher-Student | queued | transferable / adaptive robot learning |
| L23 | RMA | queued | rapid motor adaptation |
| L23 | Neural-Fly | queued | adaptive control for flight |
| L24 | Foundation Models in Robotics Survey | queued | robotics foundation model survey |
| L24 | SayCan | queued | LLM high-level planning + affordance |
| L24 | CLIPort | queued | CLIP + Transporter for manipulation |
| L24 | RT-1 | queued | scalable language-conditioned robot policy |
| L24 | Code as Policies | queued | LLM-generated robot policy code |

## How To Read

### First 5-session path

1. `Agile But Safe`：safe agile locomotion system map。
2. `Domain Randomization` + `Real2Sim or Sim2Real`：sim2real / real2sim 对照。
3. `DAgger`：为什么 BC 在 learner-induced states 会崩。
4. `Diffusion Policy`：action sequence generation。
5. `Dreamer` 或 `TD-MPC`：world model / planning 入口。

### 每篇输出模板

```text
one_sentence:
robot problem:
observation:
action:
policy / model:
training:
eval:
sim2real / safety / runtime:
connection_to_SO_ARM101:
```

## Boundary

- 不因为 CMU16-831 清单很完整就暂停 SO-ARM101。
- 不一次性精读所有 RL 论文；按项目问题触发。
- legged locomotion / humanoid / drone 论文先作为系统思想和 sim2real/safety 案例，不切换当前硬件主线。
