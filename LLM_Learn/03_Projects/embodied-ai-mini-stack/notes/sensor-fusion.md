# Sensor Fusion Notes

## 今年边界

2026 年只建立多传感器融合的软件系统视角，不展开完整 SLAM / EKF / factor graph。

## 必须理解的问题

- time synchronization
- coordinate frames
- calibration
- sensor noise
- missing data
- confidence / uncertainty
- fusion output as state estimate

## 最小实践

- 同步记录 camera frame 和 qpos / qvel。
- 在 replay 中同时展示视觉帧和 robot state。
- 记录 timestamp drift / dropped frame。
- 解释 observation 如何变成 policy 可用的 state。

## 和 JD 的关系

这个模块对齐：

- 相机、IMU、激光雷达等传感器的物理特性与常见失效模式。
- 多传感器融合的应用经验。
- 通过问题表现和日志定位软硬件耦合问题。
