---
type: roadmap
project: SO-ARM101 + LeRobot 首闭环
time_window: 2_to_4_weeks
status: draft
---

# 2-4 Week Roadmap

## 总节奏

目标不是每天都学新知识，而是每周形成一个真实证据：

```text
Week 1: 环境 + 硬件 + teleoperation
Week 2: 数据 + replay + 第一版训练
Week 3: 真机 eval + failure analysis + 补数据
Week 4: 报告 + LingBot-VLA schema mapping
```

如果只有半个月：

```text
Week 1: 组装 / 校准 / teleoperate / record / replay
Week 2: train / eval / report
```

## 2026-06 执行映射

2026-06-08 修订后，本项目作为 6 月 Robot Learning 主线，不再只是后续备选项目：

| 周 | 日期 | 本周定位 | 最低证据 |
|---|---|---|---|
| W24 | 2026-06-08 ~ 2026-06-14 | 实物项目启动：BOM、采购决策、LeRobot/LingBot-VLA walkthrough、bring-up checklist | `BOM final` + `bring-up checklist` + schema first scan |
| W25 | 2026-06-15 ~ 2026-06-21 | 硬件 bring-up：assemble、ports、motor ID、calibration、teleop、record/replay | `E001_hardware_bringup` + 至少 1 条可 replay episode |
| W26 | 2026-06-22 ~ 2026-06-28 | 数据与第一版 policy：30-50 条 episode、ACT/BC v0、10 次 eval | dataset 说明 + train log + eval table + failure taxonomy |
| W27 | 2026-06-29 ~ 2026-07-05 | 报告与 7 月承接：补数据/阻塞报告、LingBot-VLA schema mapping、Modern Robotics 入口 | `first_loop_report_v0` 或 `hardware_blocker_report` |

执行原则：

- 有实物就优先推进真实硬件。
- 硬件未到或卡住时，不空等；用 LeRobot walkthrough、mock dataset、Gymnasium/MuJoCo smoke test 兜底。
- `LingBot-VLA` 第一月只做 schema/runtime mapping 或 open-loop 可行性，不做 4B full post-training。
- 算力平台按 `Mac/dev1 -> Jetson Orin -> Jetson AGX Thor` 演进：首闭环先用 dev 环境，Orin 用于后续本体侧 runtime，Thor 用于更复杂的 VLA / VLM / LLM 上机器人。

## Week 0：采购和准备

目标：下单前把风险降到最低。

- [ ] 确认购买清单和预算。
- [ ] 确认电脑和远端 GPU 使用方式。
- [ ] 看一遍同济子豪兄 `LeRobot + LingBot-VLA` 视频，只抓流程。
- [ ] 读 LeRobot SO-101 assemble 文档。
- [ ] 建立本项目实验记录。

输出：

- [ ] `02_Budget_And_BOM.md` 更新为最终采购版本。
- [ ] `99_Resources.md` 补齐链接。

## Week 1：硬件闭环

目标：机械臂能动起来。

- [ ] 组装 leader/follower。
- [ ] 安装 LeRobot。
- [ ] 找端口。
- [ ] 配置电机 ID。
- [ ] 校准。
- [ ] 完成一次 teleoperation。
- [ ] 录制 3-5 条短 episode。
- [ ] replay 1 条 episode。

最低完成线：

- 机械臂能被 LeRobot 识别。
- follower 能跟随 leader。
- 有一条可 replay 的数据。

输出：

- [ ] `05_Experiment_Log.md` 新增 `E001_hardware_bringup`。
- [ ] 记录端口、校准目录、失败现象。

## Week 2：数据和第一版 policy

目标：从示教数据进入训练。

- [ ] 固定一个最简单任务。
- [ ] 录制 30-50 条 episode。
- [ ] 可视化或检查 dataset。
- [ ] replay 3 条 episode，确认动作质量。
- [ ] 训练 ACT 第一版。
- [ ] 保存训练命令、checkpoint、loss 曲线。

最低完成线：

- 有一个 LeRobot dataset。
- 能解释数据字段。
- 至少完成一次训练尝试。

输出：

- [ ] `notes/data_schema.md`
- [ ] `experiments/E002_dataset_recording.md`
- [ ] `experiments/E003_act_train_v0.md`

## Week 3：评估和失败分析

目标：让模型真实执行，哪怕成功率很低。

- [ ] 用训练好的 policy 跑 10 次真机 eval。
- [ ] 记录每次是否成功。
- [ ] 按失败类型归类：抓不到、偏移、动作过慢、视角不稳、示教分布外。
- [ ] 根据失败类型补 10-20 条示教。
- [ ] 训练 v1。
- [ ] 对比 v0/v1。

最低完成线：

- 有 10 次 eval 表。
- 有失败分类。
- 能说清下一轮补数据策略。

输出：

- [ ] `experiments/E004_real_eval_v0.md`
- [ ] `reports/first_loop_report_v0.md`

## Week 4：初窥门径

目标：把首闭环迁移到更大的 VLA / robot runtime 视角。

- [ ] 读 LingBot-VLA 技术报告第一遍。
- [ ] 拆 `LingBot-VLA` repo：训练入口、open-loop eval、deploy、robot config。
- [ ] 对比 LeRobot dataset 与 LingBot-VLA data config。
- [ ] 写 `LingBot-VLA upgrade path`。
- [ ] 决定下一个项目：更难任务 / SmolVLA / LingBot-VLA open-loop / 仿真 baseline。

输出：

- [ ] `06_LingBot_VLA_Upgrade_Path.md` 更新为可执行版本。
- [ ] `reports/first_phase_review.md`

## 每日执行方式

工作日：

- 20-40m：看文档或做小修补。
- 60-90m：只推进一个动作，如校准、录数据、训练、评估。

周末：

- 2-4h：做需要连续时间的实验，如组装、录 50 条数据、训练/评估。

## 判断是否推进下一阶段

只有满足下面任一条件，才进入更复杂模型：

- ACT 已能在简单任务上稳定成功。
- 已经清楚失败主要来自模型而不是硬件/数据。
- 数据 schema 和 eval loop 已经能复述。

否则继续补：

- 示教质量
- 任务约束
- 摄像头固定
- 失败分类

## 判断是否采购 Orin / Thor

- `Orin` 的购买条件：首闭环已经能跑，且我们要把轻量 policy、相机和 ROS 2/TensorRT 放到机器人旁边长期开发。
- `Thor` 的购买条件：已经进入本体侧 VLA / VLM / LLM，真实需求变成多模态大模型推理、action chunk、低延迟和多传感器融合。
- 在这两个条件出现前，继续用 Mac / dev1 / 云单卡推进训练、eval 和 blocker report。
