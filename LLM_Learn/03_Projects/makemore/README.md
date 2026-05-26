# makemore

## 项目定位

这是 `llm-learner` 当前学习主线中的另一个核心专题，用于补齐：

- 最小语言模型主流程
- `token -> embedding -> logits -> next-token prediction`
- 训练与生成的最小闭环
- 从统计 bigram 到神经网络 bigram 的理解
- 为后续 inference / serving 主线建立直觉与表达基础

## 当前恢复说明

原先 `03_Projects/` 在一次目录收敛中被误删；当前已先恢复项目骨架，并根据仍保留的 Daily / Weekly 记录重建入口说明。

## 已知学习轨迹（可追溯）

### Daily Notes
- `01_DailyNotes/2026/2026-03/2026-03-12.md`
- `01_DailyNotes/2026/2026-03/2026-03-13.md`
- `01_DailyNotes/2026/2026-03/2026-03-16.md`
- `01_DailyNotes/2026/2026-03/2026-03-17.md`
- `01_DailyNotes/2026/2026-03/2026-03-18.md`
- `01_DailyNotes/2026/2026-03/2026-03-22.md`
- `01_DailyNotes/2026/2026-03/2026-03-23.md`
- `01_DailyNotes/2026/2026-03/2026-03-26.md`
- `01_DailyNotes/2026/2026-03/2026-03-30.md`

### Weekly / Long-range Notes
- `02_WeeklyNotes/2026/2026-04/2026-W14.md`
- 历史 12 个月路线图（JD1 框架，已归档）：`_archived/jd1-legacy/2026-W12_to_2027-W13_JD1转岗12个月路线图.md`
- 当前 active 年度计划：`00_Roadmap/03_Annual_Plan_2026.md`

## 当前已明确的阶段性收获

- 已建立 `makemore` 第一阶段的基础主线
- 已理解统计 bigram 与神经网络 bigram 的对应关系
- 已收口 `xenc @ W -> logits -> probs -> loss / generate` 的最小训练与生成闭环
- 当前后续重点已进入：在 `micrograd` 地基之上继续推进 `makemore` 第二阶段理解

## 学习总结的阶段划分（当前采用六阶段）

后续 `makemore` 的学习总结，按下面六个阶段组织：

1. 阶段一：`Bigram`
2. 阶段二：`MLP`
3. 阶段三：`CNN / WaveNet`
4. 阶段四：`RNN`
5. 阶段五：`LSTM / GRU`
6. 阶段六：`Transformer`

当前已新增：

- `makemore-六阶段学习地图.md`
- `makemore-阶段一-Bigram.md`
- `makemore-阶段二-MLP.md`

## 当前推荐的项目内沉淀方向

后续与 `makemore` 相关的高价值内容，建议优先沉淀为：

1. `makemore-六阶段学习地图.md`
2. `makemore-最小主线总结.md`
3. `makemore-阶段一-Bigram.md`
4. `makemore-阶段二-MLP.md`
5. 其余阶段按六阶段主线逐步补齐

## 当前状态

- 项目骨架已恢复
- 历史详细项目笔记未完全恢复
- 后续可根据 Daily / Weekly 记录逐步重建最核心的专题总结
