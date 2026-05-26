# Architecture v0

## 一句话

`Embodied AI mini-stack` 是一个从任务配置到评测回放的机器人 AI 软件闭环，用来验证具身智能算法产品化、数据闭环、runtime 和鲁棒性。

## 系统闭环

```text
Task Config
  -> Simulation / Robot Interface
  -> Observation
  -> State / Perception
  -> Controller or Policy
  -> Action
  -> Robot / Simulator Step
  -> Episode Logger
  -> Dataset / Metadata
  -> Training
  -> Policy Runtime
  -> Evaluation
  -> Replay / Failure Analysis
```

## 模块边界

| 模块 | 负责什么 | 2026 最小实现 |
|---|---|---|
| `sim` | MuJoCo scene、reset、step、task config | MuJoCo hello-world + reach/push task |
| `robot_interface` | observation/action 统一接口 | state/action schema v0 |
| `perception` | camera / OpenCV / sensor fusion 入口 | camera frame + qpos/qvel 同步记录 |
| `data` | episode logging、trajectory、metadata | episode logger + trajectory schema |
| `train` | BC dataset、training、checkpoint | LeRobot / simple BC pipeline |
| `runtime` | policy runner、latency、fallback | policy_runtime v0 |
| `eval` | batch run、success metrics、failure categories | eval harness v0 |
| `replay` | trajectory replay、video export、failure case | replay_tool v0 |
| `deploy` | ONNX / TensorRT / quantization notes | ONNX export + latency measurement |

## 当前架构原则

- 先仿真，再真机。
- 先 state-based policy，再视觉输入。
- 先 reach / push，再 pick-place。
- 先 logging / replay / eval，再追更复杂模型。
- 任何 demo 都必须能回答：输入是什么、输出是什么、成功标准是什么、失败样本怎么复现。

## 面试讲法

这个项目不是证明“我会训练一个 policy”，而是证明：

- 我知道机器人软件里 `感知-决策-执行` 怎么拆。
- 我知道 robot learning 需要什么数据和 eval。
- 我知道 policy 上线前需要 runtime、latency、fallback。
- 我能把 DB / 存储 / 系统工程经验迁移到机器人数据闭环。
