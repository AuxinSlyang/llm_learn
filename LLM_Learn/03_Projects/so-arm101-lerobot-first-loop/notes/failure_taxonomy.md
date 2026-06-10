---
type: project_note
project: SO-ARM101 + LeRobot 首闭环
topic: failure_taxonomy
status: todo
---

# Failure Taxonomy

## 为什么要做

第一版 policy 成功率低是正常的。关键不是立刻调模型，而是判断失败来自哪里：

```text
hardware / calibration / camera / data / policy / task design / runtime
```

## 失败类型

| 类型 | 表现 | 优先处理 |
|---|---|---|
| 硬件固定问题 | 底座移动、线材拉扯 | 加固桌面和线材 |
| 校准问题 | 关节位置偏、replay 不一致 | 重做校准 |
| 视觉问题 | 物体出画、反光、遮挡 | 固定相机和光照 |
| 示教问题 | 人示教不一致、轨迹抖 | 重新录制高质量 episode |
| 分布外问题 | 换位置后失败 | 补不同起点数据 |
| policy 问题 | 动作迟滞、预测发散 | 降任务难度或调训练 |
| runtime 问题 | 延迟、动作频率不稳 | 记录 latency 和 action horizon |

## Eval 记录

每次 eval 后只写事实：

- 成功 / 失败
- 初始位置
- 第一个错误动作
- 失败类型
- 下一轮补什么数据

