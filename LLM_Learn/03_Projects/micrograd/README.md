# micrograd

## 项目定位

这是 `llm-learner` 当前学习主线中的一个核心专题，用于补齐：

- `backward`
- `gradient accumulation`
- `parameter update`
- `Neuron / Layer / MLP`
- 从最小 autograd 到最小训练闭环的理解

它服务于后续：

- 理解训练与推理的边界
- 理解计算图与反向传播
- 为继续进入 `makemore`、推理系统和更完整 LLM 主流程打地基

## 当前恢复说明

原先 `03_Projects/` 在一次目录收敛中被误删；当前已先恢复项目骨架，并根据仍保留的 Daily / Weekly 记录重建入口说明。

## 已知学习轨迹（可追溯）

### Daily Notes
- `01_DailyNotes/2026/2026-03/2026-03-24.md`
- `01_DailyNotes/2026/2026-03/2026-03-25.md`
- `01_DailyNotes/2026/2026-03/2026-03-26.md`
- `01_DailyNotes/2026/2026-03/2026-03-30.md`

### Weekly Notes
- `02_WeeklyNotes/2026/2026-04/2026-W14.md`

## 当前已明确的阶段性收获

- 已建立 `backward` 的最小直觉
- 已从概念层进入到 `micrograd` 代码主线理解
- 已收口 `engine.py -> nn.py -> loss.backward()` 这条主线
- 当前重点不再是“看过代码”，而是“能不能不用笔记讲顺主线”

## 当前推荐的项目内沉淀方向

后续与 `micrograd` 相关的高价值内容，建议优先沉淀为：

1. `micrograd-主线总结.md`
2. `micrograd-5到8句可复述版.md`
3. `micrograd-关键概念与卡点.md`

## 当前状态

- 项目骨架已恢复
- 历史详细项目笔记未完全恢复
- 后续可根据 Daily / Weekly 记录逐步重建最核心的专题总结
