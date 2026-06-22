---
type: reading_map
track: reinforcement learning / robot learning
status: queued
created: 2026-06-18
---

# RL for Robot Learning Reading Map

## Position

RL 不是当前阶段的新主线，而是 `robot policy / data loop / eval / recovery` 的支撑线。

它回答的问题是：

```text
policy 如何通过环境反馈改进？
reward / preference / success signal 如何进入训练？
offline logs / demonstrations / failed rollouts 如何变成更强 policy？
```

和当前 VLA 主线的关系：

```text
OpenVLA: supervised VLA fine-tuning + serving
pi0 / pi0-FAST: action distribution / flow / action tokenization
DAgger: imitation learning 的 closed-loop 数据聚合
RL: reward-driven improvement, offline data reuse, sim/real trial-and-error
```

边界：这条线服务具身智能系统，不切成泛 RL 全科；短期只补足能理解机器人策略学习和 LLM post-training 类比的部分。

## Why Robotics Feels Cross-Disciplinary

机器人把几乎所有 AI 子领域都压到同一个系统接口里：

```text
camera / sensors -> perception
language / goal -> task understanding
state history -> memory / world model
policy -> action
reward / success / human feedback -> learning signal
runtime -> latency / reliability / safety
data loop -> continual improvement
```

所以 CV、VLM、LLM、diffusion、RL、control、systems、serving、data infra 都会自然汇入机器人。机器人不是“又一个模型方向”，更像是一个会检验模型、数据、控制和工程系统是否真正闭环的综合场景。

## First Pass Reading Order

| 顺序 | 论文 / 材料 | 读法 | 为什么读 |
|---|---|---|---|
| 0 | Sutton & Barto RL 概念章节 / MDP, Bellman, policy, value | Concept Scan | 建立 reward、return、value、policy、exploration 的词表 |
| 1 | DQN / Human-level control through deep reinforcement learning | Quick Read | 理解 deep value learning、replay buffer、target network |
| 2 | Policy Gradient Methods for Reinforcement Learning with Function Approximation | Scan | 理解为什么可以直接优化 stochastic policy |
| 3 | TRPO / PPO | Quick Read | PPO 是 RLHF 和很多 sim RL baseline 的共同语言；TRPO 理解 trust region 来源 |
| 4 | DDPG / TD3 / SAC | Structured Read | 连续动作控制核心线；SAC 的 entropy regularization 对机器人控制很重要 |
| 5 | Hindsight Experience Replay (HER) | Quick Read | goal-conditioned manipulation / sparse reward 的经典技巧 |
| 6 | GAIL + DAgger | Structured Read | imitation learning 和 RL 的桥：expert demos、occupancy matching、covariate shift |
| 7 | CQL / IQL / AWAC / RLPD | Structured Read | offline RL / logged robot data reuse；理解为什么只靠离线数据会有 OOD action 风险 |
| 8 | QT-Opt | Quick Read | 大规模真实机器人抓取 RL，连接 vision-based manipulation 和 real robot data |
| 9 | World Models / DreamerV3 | Structured Read | model-based RL、latent dynamics、imagination；已在 `50_World_Models` 维护 |
| 10 | InstructGPT / DPO / DeepSeek-R1 | Cross-Link Scan | LLM post-training 的 RL / preference / verifiable reward 线，类比 high-level reasoning，不等同于低层控制 |

## Recommended Minimal Route

近期不要一次展开全部 RL。最小有效路线：

```text
DAgger
-> PPO / SAC 概念对照
-> HER
-> Offline RL: CQL or IQL
-> QT-Opt
-> DreamerV3
```

这条路线足够支撑：

- 看懂 robot policy 为什么会有 closed-loop distribution shift。
- 看懂 continuous action control 为什么常用 SAC / TD3 / PPO 作为 baseline。
- 看懂 robot logs / demonstrations 为什么不能直接当普通监督数据无限用。
- 看懂 world model / planning 为什么会重新回到机器人系统里。

## Connection to Current Papers

| 当前材料 | RL 线提供什么背景 |
|---|---|
| OpenVLA | 主要是 supervised VLA，不是典型 RL；RL 用来理解后续 failure-driven fine-tuning 和 eval loop |
| pi0 | flow matching action expert 不是传统 RL，但 policy 仍要通过成功率、任务完成度、数据闭环评估 |
| pi0-FAST | action tokenization 解决 representation，不解决 reward-driven improvement |
| DAgger | 最直接连接：BC 在 learner-induced states 下失败，必须把数据采到 policy 自己会到达的状态上 |
| Diffusion Policy | 从 action distribution 角度建模 policy；可和 RL 的 exploration / multimodality 对照 |
| LeRobot / SO-ARM101 | record / replay / train / eval 以后，RL 线才会变成真实工程问题 |

## When to Read

短期触发条件：

- OpenVLA / pi0 / pi0-FAST 第一轮读完。
- LeRobot 有 record/replay 或 ACT 训练/eval 证据。
- 观察到 policy drift、failure recovery、sparse success signal、sim-to-real gap。

在触发前，RL 只保留为 P2 支撑线；本周不抢 OpenVLA / pi0 / SO-ARM101 主线时间。

## Note Output Standard

每篇 RL 论文笔记都必须回答：

- observation / state 是什么？
- action space 是离散还是连续？
- reward / feedback signal 是什么？
- policy / value / model 学了什么？
- 数据来自 online rollout、offline logs、expert demos 还是 sim？
- evaluation 是否能说明真实机器人闭环能力？
- 对 VLA / robot data loop / runtime 有什么可迁移点？
