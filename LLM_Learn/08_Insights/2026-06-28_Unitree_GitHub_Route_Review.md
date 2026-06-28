---
type: insight
date: 2026-06-28
topic: Unitree GitHub route review
status: active
linked_roadmap: [[09_One_Year_Robot_Learning_Full_Stack_Roadmap]]
---

# Unitree GitHub Route Review

## One-line conclusion

整体学习路径不需要推倒重来，但需要从“通用 Robot Learning Full-Stack”轻微收紧为：

```text
Unitree-style robot software stack
-> SDK / DDS / ROS2 / MuJoCo / IsaacLab
-> teleop + data + LeRobot conversion/training/eval
-> policy runtime / sim2real / VLA runtime
```

当前 `SO-ARM101 + LeRobot` 仍适合作为低成本 first loop；但它应该被明确定位为 `Unitree-style data/runtime first loop` 的替代训练场，而不是最终目标本身。

## Unitree repo map

| 层级 | Unitree repo | 说明 | 学习定位 |
|---|---|---|---|
| Official access layer | `unitree_sdk2`, `unitree_sdk2_python` | SDK2 / Python SDK / DDS communication / high-level and low-level control examples | 必须早读，理解 Unitree 的通信和控制边界 |
| ROS2 bridge | `unitree_ros2` | Unitree SDK2 基于 CycloneDDS；ROS2 可直接使用消息通信和控制 | 7-8 月开始做 awareness，不等到 2027 |
| Lightweight sim | `unitree_mujoco`, `unitree_rl_mjlab` | MuJoCo simulator / low-level message / Train -> Play -> Sim2Real | 7-9 月应提前进入 smoke test |
| Isaac stack | `unitree_sim_isaaclab`, `unitree_rl_lab` | Isaac Lab tasks, DDS topics aligned with real robot, RL train/play/deploy | 先做 repo walkthrough，等 GPU/环境条件成熟后再实跑 |
| Teleop / data collection | `xr_teleoperate`, `UniArmL1` | XR / keyboard / leader teleop, standard data collection, connects to `unitree_lerobot` | 对齐我们当前 LeRobot first loop 的核心证据 |
| IL / data loop | `unitree_lerobot` | Unitree data conversion, bad episode editor, replay, LeRobot training, real robot eval | 当前最应该进入结构化 walkthrough |
| VLA / WMA | `unifolm-vla`, `unifolm-world-model-action` | VLA / world model action training, dataset conversion, server-client real eval | 先读架构和 schema，不作为 7 月主线 |

## What this changes

### Keep

- `Robot Learning Full-Stack` 仍是上位路线。
- `LLM / AI Infra` 仍只是 VLA / policy runtime 支撑线。
- `SO-ARM101 + LeRobot` 仍作为 first loop，但验收必须更像 Unitree 官方栈：dataset schema、replay、eval、failure log、runtime boundary。
- `Modern Robotics` 仍是 7-8 月基础课，不取消。

### Adjust

- 7 月不能只学 `Modern Robotics Ch.1-3`。每周都要把 frame / pose / transform / joint / action 映射到一个 Unitree repo 或 SO-ARM101 项目文件。
- `MuJoCo` 不能等到 9 月才进入视野；7 月先做 `unitree_mujoco` repo walkthrough + local feasibility note，9 月再正式做 control baseline。
- `ROS2 / DDS` 不能等到 2027 才第一次接触；7 月先读 `unitree_sdk2_python` 和 `unitree_ros2` 的通信边界，理解 topic / msg / network interface / CycloneDDS。
- VLA / WMA 不能抢 7 月主线；只读 `unifolm-vla` 和 `unifolm-world-model-action` 的 dataset schema、server-client eval、action horizon、control frequency。

## Revised 7-9 month emphasis

| 月份 | 原主线 | Unitree 对齐后 |
|---|---|---|
| 2026-07 | Modern Robotics Ch.1-3 | MR Ch.1-3 + Unitree SDK2/DDS/ROS2 awareness + `unitree_mujoco`/`unitree_lerobot` repo map |
| 2026-08 | Modern Robotics Ch.4-6 | FK/IK/Jacobian + robot model / URDF / MJCF / Unitree model mapping |
| 2026-09 | Control / dynamics + MuJoCo baseline | MuJoCo control baseline should prefer Unitree-style simulator / message boundary when possible |

## Near-term action

For `2026-W27`, do not open a large VLA project. The correct scope is:

- Finish or downgrade `SO-ARM101 E001` into a durable blocker/report.
- Add one `Unitree repo map` note: SDK2 / ROS2 / MuJoCo / LeRobot / VLA / WMA.
- Add one `Unitree communication boundary` note: DDS, ROS2, network interface, topics, low-level vs high-level control.
- Keep MR study tied to `state/action schema v0`.

## Sources checked

- GitHub org: `https://github.com/unitreerobotics`
- `unitree_lerobot`: `https://github.com/unitreerobotics/unitree_lerobot`
- `UniArmL1`: `https://github.com/unitreerobotics/UniArmL1`
- `unitree_sdk2`: `https://github.com/unitreerobotics/unitree_sdk2`
- `unitree_sdk2_python`: `https://github.com/unitreerobotics/unitree_sdk2_python`
- `unitree_ros2`: `https://github.com/unitreerobotics/unitree_ros2`
- `unitree_mujoco`: `https://github.com/unitreerobotics/unitree_mujoco`
- `unitree_rl_mjlab`: `https://github.com/unitreerobotics/unitree_rl_mjlab`
- `unitree_sim_isaaclab`: `https://github.com/unitreerobotics/unitree_sim_isaaclab`
- `unitree_rl_lab`: `https://github.com/unitreerobotics/unitree_rl_lab`
- `xr_teleoperate`: `https://github.com/unitreerobotics/xr_teleoperate`
- `unifolm-vla`: `https://github.com/unitreerobotics/unifolm-vla`
- `unifolm-world-model-action`: `https://github.com/unitreerobotics/unifolm-world-model-action`

