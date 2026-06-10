---
type: project_note
project: SO-ARM101 + LeRobot 首闭环
topic: data_schema
status: todo
---

# Data Schema

## 目标

把真实示教数据拆成可理解的字段：

```text
episode
-> observation.images
-> observation.state
-> action
-> task / instruction
-> metadata
```

## 首轮要回答

- `observation.images` 有几个视角？
- 每个图像的 shape、fps、相机位置是什么？
- `observation.state` 对应哪些关节？
- `action` 是绝对位置、相对位置，还是 action chunk？
- episode 起止条件是什么？
- replay 时哪些字段真正驱动机械臂？

## Mapping Table

| 字段 | 含义 | 来源 | shape / dim | 风险 |
|---|---|---|---|---|
| observation.images | 摄像头图像 | USB camera | | 视角不稳 |
| observation.state | 关节状态 | follower arm | | 校准误差 |
| action | 示教动作 | leader/follower | | 噪声 / 分布外 |
| task | 任务描述 | 人工输入 | | 描述不一致 |

## Camera Plan

- 第一阶段使用一个 `front` USB RGB 摄像头即可进入 `teleop -> record -> replay`。
- 教程支持两个摄像头：`front` 和 `side`。第二视角先作为可选项，不作为首闭环前置条件。
- 采集数据时主动臂不应出现在画面中；优先保证 follower、任务物体和操作区域可见。

## 和 LingBot-VLA 的连接

后续需要对齐：

- `configs/robot_configs/<data_name>.yaml`
- `data.joints`
- `data.cameras`
- `norm_stats_file`
- `scripts/open_loop_eval.py`
