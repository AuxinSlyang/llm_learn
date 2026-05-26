# Data Schema Notes

## 目标

记录机器人 episode 数据的最小结构，为后续 MuJoCo / LeRobot / 真机数据闭环服务。

## Episode v0

```text
episode_id
task_id
seed
start_time
end_time
config
observations
states
actions
rewards
success
failure_reason
latency
artifacts
```

## Step v0

```text
timestamp
observation
qpos
qvel
action
policy_output
controller_state
reward
done
info
```

## 需要保留的原因

- `task_id / config / seed`：保证实验可复现。
- `qpos / qvel / action`：回答机器人做了什么。
- `policy_output / controller_state`：区分 policy 问题和控制器问题。
- `success / failure_reason`：支撑 eval 和 failure analysis。
- `latency`：支撑模型部署与 runtime 优化。
- `artifacts`：视频、轨迹、日志和报告的索引。
