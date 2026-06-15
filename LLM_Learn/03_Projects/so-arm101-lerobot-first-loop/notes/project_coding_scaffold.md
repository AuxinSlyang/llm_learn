---
type: project_note
project: SO-ARM101 + LeRobot 首闭环
topic: project coding scaffold
status: draft
created: 2026-06-15
linked_week: [[2026-W25]]
---

# Project Coding Scaffold

## 本周定位

这份文件只服务 `2026-W25` 的 LeRobot 首闭环主路径，不做完整 LeRobot framework 设计。

目标是把本周所有命令、数据路径、episode、失败和 eval 记录固化下来：

```text
hardware validation
-> teleop
-> record
-> replay
-> eval stub
-> failure note
```

## Scope

### P0：必须

- 记录 LeRobot 命令顺序和每步前置条件。
- 记录 dataset path 和 episode 命名约定。
- 记录每次运行的命令、结果、失败和下一步。
- 建立最小 eval stub：人工记录 replay / teleop / episode 是否成功。

### P1：顺利时

- 准备 ACT/BC v0 的数据入口：dataset repo/path、fps、camera、task。
- 整理 `observation.images / observation.state / action / task` schema。

### P2：本周不做

- 不训练 VLA。
- 不进入 SmolVLA / OpenVLA / pi0 源码。
- 不做复杂自动化脚本；先以可复查命令和日志为准。

## Command Path

| 阶段 | 命令 | 前置条件 | 输出证据 | 状态 |
|---|---|---|---|---|
| Find port | `lerobot-find-port` | USB 线、控制板、Mac 端口可见 | 端口名 / 失败日志 | todo |
| Setup motors | `lerobot-setup-motors` | 舵机和电源线核对；不混淆 7.4V / 12V | motor ID / config 记录 | todo |
| Calibrate | `lerobot-calibrate` | 机械臂安全装配，桌面固定 | calibration 文件 / 观察 | todo |
| Teleoperate | `lerobot-teleoperate` | leader/follower 都能连接和校准 | follower 跟随 leader 观察 | todo |
| Record | `lerobot-record` | teleop 可用，camera 可用，任务区域固定 | dataset path + episode 数 | todo |
| Replay | `lerobot-replay` | dataset 至少 1 条 episode | replay 成功/失败记录 | todo |
| Eval stub | 手工表格 | replay 或 policy rollout 结果 | success/failure/manual notes | todo |

## Dataset Path

第一版先用本地路径，不急着推 Hugging Face Hub。

```text
datasets/
  so_arm101_push_to_zone_v0/
    data/
    videos/
    meta/
    run_log.md
    failure_log.md
```

待实际命令确认后，把真实路径写回这里：

- dataset root:
- repo id:
- fps:
- robot type:
- cameras:
- task:

## Episode Log Template

| Date | Episode | Task | Camera | Duration | Record command | Replay result | Notes |
|---|---|---|---|---:|---|---|---|
| 2026-06-__ | 000 | push-to-zone | front | | | | |

## Run Log Template

| Date | Stage | Command | Result | Observation | Next step |
|---|---|---|---|---|---|
| 2026-06-15 | tool gate | manual check | | | |

## Failure Log Template

| Date | Stage | Failure | Likely cause | Evidence | Next action |
|---|---|---|---|---|---|
| 2026-06-__ |  |  |  |  |  |

## Eval Stub

第一版 eval 不追 policy 成功率，只记录 episode / replay / manual task outcome。

| Trial | Input | Success | Failure type | Manual note |
|---:|---|---|---|---|
| 1 | episode_000 | | | |
| 2 | episode_001 | | | |
| 3 | episode_002 | | | |

## First Task: Push To Zone

优先任务：

```text
push-to-zone:
  object: small block / bottle cap
  start: table center
  target: marked zone A
  success: object crosses target boundary and stays for 2s
```

选择原因：

- 比 pick-and-place 更少依赖夹爪稳定性。
- 更容易用单摄像头观察。
- 失败类型更容易拆：camera、teleop、calibration、surface friction、action noise。

## 本周验收

- 绿色：真实 SO-ARM101 完成 teleop、record、replay，且 E001/E002/E003 有记录。
- 黄色：硬件阻塞，但 command walkthrough、mock dataset/replay path、blocker report 和 scaffold 都完成。
- 红色：只读材料，没有命令、路径、episode、失败或 blocker 证据。
