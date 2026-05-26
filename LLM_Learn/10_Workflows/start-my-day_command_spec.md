---
type: workflow_doc
topic: start_my_day
status: active
---

# `start-my-day` Command Spec

## 当前可用入口

当前脚本已经实现，但 `/start-my-day` 这种 slash 形式并没有在宿主聊天界面里真正注册。

因此目前可用入口只有这两种：

```text
./start-my-day
./start-my-day 1h
zsh LLM_Learn/10_Workflows/bin/start-my-day
zsh LLM_Learn/10_Workflows/bin/start-my-day 4h
```

如果当前目录已经在 `LLM_Learn/` 内，也可以使用：

```text
zsh 10_Workflows/bin/start-my-day
zsh 10_Workflows/bin/start-my-day 4h
```

如果在聊天框里直接输入 `/start-my-day`，宿主会先报：

```text
Unrecognized command '/start-my-day'
```

这不是脚本故障，而是 slash command 没有注册到宿主。

## 仓库内的语义约定

在本工作区语义上，`/start-my-day` 仍然表示“执行今日启动流程”，等价于：

```bash
./start-my-day
```

带参数时等价于：

```bash
./start-my-day 4h
```

- 若未提供参数，默认 `time_budget = 2h`
- `--dry-run` 和 `--date YYYY-MM-DD` 走确定性脚本路径，适合补写和测试

## 目标

每天启动后，只调用一次 `/start-my-day`，系统完成：

- 读取昨天、本周、本月、本年上下文
- 生成今天的学习与实验 / 阅读安排
- 给出今天建议阅读的材料，以及一个轻量 classic paper slot
- 回写今日 Daily Note

## 输入上下文

默认读取：

- 昨天的 Daily Note
- 今天的 Daily Note（如果已存在）
- 本周 Weekly Note
- 本月 Monthly Plan
- 年度 / 路线图：`00_Roadmap/`
- 今日论文指定：`04_Papers/99_Overrides/YYYY-MM-DD.md`
- 经典论文队列：`04_Papers/01_Reading_Index.md`
- 最近未完成事项

可选输入：

- 今天预计可用学习时间
- 今天是否加班/活动日
- 今天是否要安排运动
- 今天是否优先阅读 / 优先代码 / 优先实验

## 输出内容

- 今日主题
- 今日 Top 3
- 今日论文槽位
- 今日时间切片
- 今日最低完成线
- 今日建议阅读
- 今日不要做什么
- 明天承接点

## 回写范围

默认只回写：

- 今天的 Daily Note

可选附加回写：

- 本周 Weekly Note 中的 `今日承接点` 或 `本周推进情况`

不默认修改：

- Monthly Plan
- Annual Plan
- 长期 roadmap

## 建议的内部步骤

1. 定位今天日期
2. 定位昨天的 Daily Note
3. 定位本周 Weekly Note
4. 定位本月 Monthly Plan
5. 定位年度 / 路线图
6. 抽取：
   - 未完成项
- 当前主线
- 当前阻塞
- 当前可用时间
7. 生成：
- 今日计划
- 今日论文槽位
- 时间切片
- 阅读建议
- 实验 / 阅读 / 笔记安排
8. 回写今日 Daily Note

## 阅读材料策略

建议不要默认自动下载 PDF。

推荐策略：

1. 先产出 `1-3` 个候选材料
2. 记录标题、链接、摘要、推荐原因
3. 只有确认“今天要读”时，再抓 PDF / 元信息

## Classic Paper Slot 策略

默认每周一到周四安排一篇 classic AI / Robotics paper 的轻量阅读：

- 时间：白天碎片 `20-40m`
- 目标：一句 takeaway + 一个和 `embodied-ai-mini-stack` 的连接
- 来源：`04_Papers/01_Reading_Index.md`
- 回写位置：Daily Note 的 `今日论文槽位` 和 `今日总结`

周五默认做 catch-up / takeaway 汇总；周末只有当前主线需要时才升级为精读。

paper slot 不能挤占晚上主学习时间。工作日默认节奏是：

```text
白天：paper slot 20-40m
晚上：主线学习 / 实验 / 笔记 90m
```

### Paper Override

如果存在：

```text
04_Papers/99_Overrides/YYYY-MM-DD.md
```

当天 `start-my-day` 必须优先使用该文件指定的论文，而不是默认队列。

常见触发方式：

```text
明天论文指定：arXiv:xxxx.xxxxx
明天读 <paper title>，帮我从 arXiv 抓一下
下周一 paper slot 读 OpenVLA
```

override 不改变晚上主线，只改变 `今日论文槽位`。

## 需要后续回答的问题

- 如何定位今天的 Daily Note 路径
- 如何自动创建缺失的 Daily / Weekly / Monthly 文件
- 如何接入 arXiv / blog / PDF 拉取
- 如何让命令幂等，避免重复回写
- 如何处理“今天时间很少”的降级策略

## v1 实现状态

- 已实现脚本：`10_Workflows/scripts/start_my_day.py`
- 已实现命令包装：`10_Workflows/bin/start-my-day`
- 已实现仓库根入口：`./start-my-day`
- 当前支持：
  - `time_budget` 参数，默认 `2h`
  - `--date YYYY-MM-DD`（仅用于补写/测试）
  - `--dry-run`
- 当前读取：
  - 年度 / 路线图：`00_Roadmap/`
  - 月计划
  - 周计划
  - 昨天 Daily Note
  - 今天 Daily Note
- 当前回写：
  - `今日锚点`
  - `今日 Top 3`
  - `今日论文槽位`
  - `今日时间切片`
  - `今日输入`
  - `今日代码 / 实验任务`
  - `今日总结`
