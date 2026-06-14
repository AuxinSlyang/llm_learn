---
type: code_reading_note
project: SO-ARM101 + LeRobot 首闭环
topic: LeRobot code map
status: draft
source_repo: https://github.com/huggingface/lerobot
source_commit: 8515d456be1dbef8c133f07188c785e683eca899
created: 2026-06-14
---

# LeRobot Code Map

## 今日定位

今天不做 LeRobot 逐行源码精读，先建立一张可执行代码地图：

```text
robot / teleoperator abstraction
-> teleop
-> record dataset
-> replay dataset
-> train policy
-> eval / rollout
```

当前本地知识库没有 LeRobot 源码 checkout；本次只读官方 GitHub 仓库临时 clone，不把第三方源码复制进知识库。

## Source Snapshot

- Repository: `https://github.com/huggingface/lerobot`
- Commit: `8515d456be1dbef8c133f07188c785e683eca899`
- Package version in `pyproject.toml`: `0.5.2`
- Python requirement: `>=3.12`
- Local scratch checkout: `/tmp/lerobot-code-map-8515`

## Top-Level Mental Model

| 模块 | 目录 | 今天只问 |
|---|---|---|
| CLI / scripts | `src/lerobot/scripts/` | 用户命令如何进入 Python 主函数 |
| Robot abstraction | `src/lerobot/robots/` | follower robot 如何暴露 observation/action |
| Teleoperator abstraction | `src/lerobot/teleoperators/` | leader arm / keyboard / phone 如何产生 action |
| Dataset | `src/lerobot/datasets/` | observation/action/task/episode 如何落到 parquet / mp4 / metadata |
| Policy | `src/lerobot/policies/` | ACT / SmolVLA / pi0 等如何统一为 policy |
| Processor | `src/lerobot/processor/` | raw obs/action 和 policy/robot 接口之间如何转换 |
| Train / eval / rollout | `src/lerobot/scripts/lerobot_train.py`, `lerobot_eval.py`, `lerobot_rollout.py` | 训练和部署入口如何接 dataset / policy / env / robot |

## Console Scripts

来自 `pyproject.toml` 的核心命令：

| CLI | Python entry | 首闭环意义 |
|---|---|---|
| `lerobot-find-port` | `lerobot.scripts.lerobot_find_port:main` | 找串口 |
| `lerobot-setup-motors` | `lerobot.scripts.lerobot_setup_motors:main` | 配置电机 ID |
| `lerobot-calibrate` | `lerobot.scripts.lerobot_calibrate:main` | 标定机械臂 |
| `lerobot-teleoperate` | `lerobot.scripts.lerobot_teleoperate:main` | leader 控 follower，不写数据 |
| `lerobot-record` | `lerobot.scripts.lerobot_record:main` | teleop 同时写 dataset |
| `lerobot-replay` | `lerobot.scripts.lerobot_replay:main` | 从 dataset 读取 action 回放到 robot |
| `lerobot-train` | `lerobot.scripts.lerobot_train:main` | 用 LeRobotDataset 训练 policy |
| `lerobot-eval` | `lerobot.scripts.lerobot_eval:main` | 仿真或评估入口 |
| `lerobot-rollout` | `lerobot.scripts.lerobot_rollout:main` | policy-driven deployment / rollout |

第一阶段优先级：

```text
find-port
-> setup-motors
-> calibrate
-> teleoperate
-> record
-> replay
-> train ACT
-> rollout / eval
```

## Core Abstractions

### Robot

入口：`src/lerobot/robots/robot.py`

`Robot` 是所有 follower / robot 设备的抽象基类，关键接口：

- `observation_features`：robot 能输出哪些 observation 字段。
- `action_features`：robot 能接收哪些 action 字段。
- `connect(calibrate=True)`：连接设备，必要时校准。
- `get_observation()`：读取当前 state / images。
- `send_action(action)`：发送 action 到电机或执行器，并返回实际发送的 action。
- `calibrate()` / `configure()` / `disconnect()`：设备生命周期。

### Teleoperator

入口：`src/lerobot/teleoperators/teleoperator.py`

`Teleoperator` 是 leader arm / keyboard / phone 等控制设备抽象，关键接口：

- `action_features`：teleop 能产生哪些 action 字段。
- `get_action()`：读取用户示教动作。
- `send_feedback(feedback)`：可选，把 robot feedback 发回 teleop。
- `connect()` / `calibrate()` / `configure()` / `disconnect()`：设备生命周期。

## SO-ARM / SO101 相关代码

### Follower

入口：

- `src/lerobot/robots/so_follower/config_so_follower.py`
- `src/lerobot/robots/so_follower/so_follower.py`

配置字段：

- `port`
- `disable_torque_on_disconnect`
- `max_relative_target`
- `cameras`
- `use_degrees`

注册名：

- `so100_follower`
- `so101_follower`

核心实现：

- 使用 `FeetechMotorsBus`
- 6 个 STS3215 电机：
  - `shoulder_pan`
  - `shoulder_lift`
  - `elbow_flex`
  - `wrist_flex`
  - `wrist_roll`
  - `gripper`
- observation features:
  - `{motor}.pos`
  - camera image keys from config
- action features:
  - `{motor}.pos`
- `get_observation()`：
  - `sync_read("Present_Position")`
  - 追加 camera `read_latest()`
- `send_action()`：
  - 从 `{motor}.pos` 去掉 `.pos`
  - 可选 `max_relative_target` 做相对目标限幅
  - `sync_write("Goal_Position", goal_pos)`

### Leader

入口：

- `src/lerobot/teleoperators/so_leader/config_so_leader.py`
- `src/lerobot/teleoperators/so_leader/so_leader.py`

注册名：

- `so100_leader`
- `so101_leader`

核心实现：

- 也是 `FeetechMotorsBus`
- 6 个同名电机
- `get_action()` 读取 leader arm 的 `Present_Position`
- 输出 action 字段同样是 `{motor}.pos`

因此 SO-ARM leader/follower 的最小数据接口非常直接：

```text
leader Present_Position
-> action: shoulder_pan.pos / ... / gripper.pos
-> follower Goal_Position
```

## Teleoperation Flow

入口：`src/lerobot/scripts/lerobot_teleoperate.py`

核心流程：

```text
make_teleoperator_from_config(cfg.teleop)
make_robot_from_config(cfg.robot)
make_default_processors()
teleop.connect()
robot.connect()

loop:
  obs = robot.get_observation()
  raw_action = teleop.get_action()
  teleop_action = teleop_action_processor((raw_action, obs))
  robot_action_to_send = robot_action_processor((teleop_action, obs))
  robot.send_action(robot_action_to_send)
```

注意：

- teleop 本身不写 dataset。
- `display_data=true` 时会把 observation / action 送到 Rerun。
- processor pipeline 是后续理解 policy / action conversion 的关键层。

## Record Flow

入口：`src/lerobot/scripts/lerobot_record.py`

`record` 是首闭环最重要的代码路径：

```text
robot.get_observation()
-> robot_observation_processor
-> build_dataset_frame(..., prefix="observation")

teleop.get_action()
-> teleop_action_processor
-> robot_action_processor
-> robot.send_action()

build_dataset_frame(..., prefix="action")
frame = {observation..., action..., "task": single_task}
dataset.add_frame(frame)
dataset.save_episode()
dataset.finalize()
```

数据集创建：

```text
dataset_features =
  action features from robot.action_features
  + observation features from robot.observation_features

LeRobotDataset.create(
  repo_id,
  fps,
  robot_type=robot.name,
  features=dataset_features,
  use_videos=cfg.dataset.video,
  ...
)
```

当前必须理解的点：

- dataset action 当前来自 teleop processed action，而不是 policy。
- dataset observation 来自 follower robot 当前 state + cameras。
- `single_task` 被写入每一帧的 `task` 字段。
- `streaming_encoding=true` 会影响视频写入性能，不改变 schema 概念。

## Dataset Layout

入口：`src/lerobot/datasets/lerobot_dataset.py`

LeRobotDataset v3.0 的核心结构：

```text
dataset_root/
  data/
    chunk-xxx/file-xxx.parquet
  meta/
    info.json
    stats.json
    tasks.parquet
    episodes/.../*.parquet
  videos/
    observation.images.<camera_name>/chunk-xxx/file-xxx.mp4
```

和本项目 `notes/data_schema.md` 的对应关系：

| 项目字段 | LeRobot 代码中的落点 |
|---|---|
| `observation.images.<camera>` | robot camera features + videos 路径 |
| `observation.state` | SO follower motor `{motor}.pos`，实际 key 可能是 `observation.state` 或展开后的 per-motor feature，取决于 feature builder / dataset version |
| `action` | robot action features，即 `{motor}.pos` |
| `task` | `DatasetRecordConfig.single_task` |
| episode | `dataset.save_episode()` 后写入 meta episode |

后续需要细读：

- `src/lerobot/datasets/feature_utils.py`
- `src/lerobot/datasets/dataset_writer.py`
- `src/lerobot/utils/feature_utils.py`

## Replay Flow

入口：`src/lerobot/scripts/lerobot_replay.py`

核心流程：

```text
robot = make_robot_from_config(cfg.robot)
dataset = LeRobotDataset(repo_id, episodes=[episode])
actions = dataset.select_columns("action")

for idx in range(dataset.num_frames):
  action_array = actions[idx]["action"]
  action = {dataset.features["action"]["names"][i]: action_array[i]}
  robot_obs = robot.get_observation()
  processed_action = robot_action_processor((action, robot_obs))
  robot.send_action(processed_action)
  sleep to match dataset.fps
```

含义：

- replay 不看 teleop。
- replay 的实际驱动只有 dataset 里的 action。
- 这正好验证 record 数据能否驱动 follower 重现动作。

## Train Flow

入口：

- `src/lerobot/scripts/lerobot_train.py`
- `src/lerobot/policies/factory.py`
- `src/lerobot/policies/pretrained.py`

核心流程：

```text
cfg.validate()
dataset = make_dataset(cfg)
policy = make_policy(...)
optimizer / scheduler = make_optimizer_and_scheduler(...)

loop:
  batch = next(dataloader)
  loss, output_dict = policy.forward(batch)
  accelerator.backward(loss)
  optimizer.step()
  policy.update() if implemented
  checkpoint / eval / logging
```

policy 统一接口：

- `PreTrainedPolicy` 继承 `torch.nn.Module`
- 每个 policy 必须定义 `config_class` 和 `name`
- `factory.get_policy_class(name)` 支持：
  - `act`
  - `diffusion`
  - `smolvla`
  - `pi0`
  - `pi0_fast`
  - `pi05`
  - `vqbet`
  - `tdmpc`
  - `groot`
  - `wall_x`
  - `xvla`
  - 等

SO-ARM 首闭环不要从 SmolVLA/pi0 开始。第一优先细读：

- `src/lerobot/policies/act/configuration_act.py`
- `src/lerobot/policies/act/modeling_act.py`
- `src/lerobot/policies/act/processor_act.py`

## 今日代码阅读结论

LeRobot 不是单一训练脚本，而是一个 robot learning 工具链：

```text
hardware abstraction
-> teleop control loop
-> dataset writer
-> policy training
-> replay / rollout / eval
```

对 `SO-ARM101 + LeRobot` 首闭环而言，最重要的不是先读完所有 policy，而是先打通这条具体路径：

```text
so101_leader.get_action()
-> so101_follower.send_action()
-> so101_follower.get_observation()
-> LeRobotDataset.add_frame()
-> LeRobotDataset.save_episode()
-> lerobot-replay
-> ACT train v0
```

## 下一次细读顺序

1. `src/lerobot/scripts/lerobot_find_port.py`
2. `src/lerobot/scripts/lerobot_setup_motors.py`
3. `src/lerobot/scripts/lerobot_calibrate.py`
4. `src/lerobot/scripts/lerobot_teleoperate.py`
5. `src/lerobot/scripts/lerobot_record.py`
6. `src/lerobot/datasets/lerobot_dataset.py`
7. `src/lerobot/policies/act/*`

今天不要继续进入：

- `smolvla`
- `pi0 / pi0_fast / pi05`
- `async_inference`
- RL / SAC / HIL
- annotation / reward models

这些等 `record -> replay -> ACT` 跑通后再读。
