---
type: experiment_log
project: SO-ARM101 + LeRobot 首闭环
status: active
---

# Experiment Log

## 记录原则

每次实验只记录真实事实，不写泛泛心得。

必须保留：

- 日期
- 环境
- 命令
- 输入数据
- 观察
- 失败现象
- 下一步

## E001 Hardware Bring-Up

- 日期：`2026-06-10` 到货启动；`2026-06-08` 已下单
- 目标：让 SO-ARM101 被 LeRobot 识别，并完成 teleoperation。
- 环境：Mac 本地 + LeRobot（待安装 / 待验证）
- 硬件：SO-ARM101 Pro leader/follower 套件；已收到两盒：
  - `SO-ARM101 Low-Cost AI Arm 3D Printed Parts`（3D printed parts only）
  - `SO-ARM101 Low-Cost AI Arm Servo Motor Kit Pro`（motor kit only, without 3D printed parts）
- 端口：
- 命令：
- 观察：
  - `2026-06-08` 已完成采购，预计 `2026-06-10` 到货。
  - `2026-06-10` 已收到 3D 打印件盒和 Pro 舵机套件盒；尚未开箱清点，尚未通电。
  - `2026-06-10` 初步开箱：3D 打印件有两包，标签分别为 `3D Printed Follower 12 pcs / PLA+ White / Infill Density 15%` 和 `3D Printed Leader 12 pcs / PLA+ Black / Infill Density 15%`。
  - `2026-06-10` 初步开箱：看到 4 个黑橙色桌面固定夹 / fixing clips，待和 BOM 数量核对。
  - `2026-06-10` 舵机数量核对完成，符合预期：
    - `C001 / 7.4V / 1:345` x1
    - `C044 / 7.4V / 1:191` x2
    - `C046 / 7.4V / 1:147` x3
    - `C047 / 12V / 1:345` x6
  - `2026-06-10` 暂未在已开箱物料中看到 USB 摄像头；当前两大包小件主要像 leader/follower 的供电线、固定件、控制板和线材。需回看购买 SKU 是否包含摄像头；若只是 Pro motor kit + 3D printed parts，摄像头大概率为另购项。
  - `2026-06-10` 当前暂不开始安装：缺合适螺丝刀，且仍有部分物料/配件需要继续核对。不要为了赶进度强行装配，避免滑丝、接错电源或 leader/follower 零件混放。
  - `2026-06-10` 已补充采购 USB 摄像头、多功能螺丝刀、万用表。当前判断：第一阶段暂不继续买其他大件，等这些工具到位后再按子豪兄 LeRobot / SO-ARM101 教程进入装配。
- 失败：
  - 当前阻塞：安装工具不足；部分物料是否齐全仍待核对。
- 下一步：
  - 开箱拍照，按 BOM 清点 3D 打印件、舵机、控制板、线材、电源线、螺丝和固定夹。
  - 按子豪兄 `开箱清点` 提醒，先清理 3D 打印件残留支撑，重点检查孔、洞、槽、网格。
  - 先分拣并标记 leader / follower 舵机，不通电装配。
  - 核对 7.4V / 12V 舵机和供电线，避免电源接错。
  - 补齐合适螺丝刀和必要小工具后再开始机械装配。
  - 优先细读 `09_Primary_Tutorial_Zihao_AI.md` 中的 `开箱清点`、`准备舵机`、`舵机中位校准并编号`、`Mac电脑` 相关章节。
  - 安装 LeRobot，执行端口识别和单个舵机 ID 配置后再进入完整组装。

## E002 Dataset Recording

- 日期：
- 目标：录制首批示教数据。
- 任务：
- episode 数：
- 摄像头视角：
- 命令：
- 数据路径：
- 观察：
- 失败：
- 下一步：

## E003 Replay

- 日期：
- 目标：验证示教数据是否可 replay。
- episode：
- 命令：
- replay 结果：
- 失败：
- 下一步：

## E004 ACT Train V0

- 日期：
- 目标：训练第一版小策略。
- dataset：
- policy：
- 训练环境：
- 命令：
- 训练时长：
- loss / checkpoint：
- 观察：
- 失败：
- 下一步：

## E005 Real Eval V0

- 日期：
- 目标：真机评估第一版 policy。
- policy：
- eval 次数：
- 成功次数：
- 成功率：
- 失败类型：
- 观察：
- 下一步补数据策略：

## Eval Table Template

| Trial | 起始状态 | 是否成功 | 失败类型 | 备注 |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
