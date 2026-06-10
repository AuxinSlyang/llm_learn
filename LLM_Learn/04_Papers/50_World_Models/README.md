---
type: reading_index
track: world models / dynamics / planning
status: queued
created: 2026-06-09
---

# 50 World Models

World model 是后续路线，不进入 W24 主线。

## Position

VLA/policy 关注：

```text
observation + instruction -> action
```

World model 进一步关注：

```text
state + action -> future state / future observation
```

它服务 planning、simulation、imagination、data efficiency 和安全评估。

## Queue

| Paper | Status | Why |
|---|---|---|
| World Models | downloaded | world model 经典入口 |
| DreamerV3 | downloaded | learning dynamics + policy in latent imagination |

## Not This Week

本周先完成 SO-ARM101 bring-up 和 LeRobot 数据闭环。world model 等有真实 trajectory / sim loop 后再展开。

