# Paper Reading Workflow

## 目标

论文阅读要服务两个目标：

1. 建立 AI / Robotics 的长期判断力。
2. 给 `Embodied AI mini-stack` 提供可迁移的系统设计 idea。

不追求每天完整精读一篇。默认先做 lightweight pass，抓核心问题、系统结构和 takeaway。

## 每日 Paper Slot

默认节奏：

| 时间 | 内容 | 产出 |
|---|---|---|
| 白天碎片 20-40m | 读 1 篇论文的 abstract / intro / method overview / figures / conclusion | 一句话 takeaway + 1 个项目连接 |
| 晚上 1.5h | 当前周主线学习 / 实验 / 笔记 | Weekly / Monthly 硬产出 |
| 周五 20-30m | 汇总本周 3-4 篇 paper slot | 本周 paper takeaways |
| 周末可选 | 精读当前 Phase 关键论文 | 结构化 paper note |

## 阅读深度分级

| Level | 适用场景 | 标准 |
|---|---|---|
| Scan | 非当前主线，但值得知道 | 能讲清论文解决什么问题和一个 takeaway |
| Structured Read | 当前阶段相关 | 完成 8 问模板，能连接到 mini-stack |
| Deep Read | 当前 Phase 核心论文 | 读方法细节、实验设置、失败模式，必要时看代码 |
| Reproduce | 项目强相关 | 复现最小代码或把 idea 放入 mini-stack |

## 文件命名约定

- `QUICK_READ.md`：通读笔记，记录核心问题、主线结构、takeaway、历史位置和后续连接。
- `DEEP_READ.md`：精读笔记，记录逐节细节、公式 / 算法推导、训练与推理过程、实验设置、疑问和代码映射。
- `README.md`：只用于目录或资源介绍；不要把逐步学习笔记默认写成 `README.md`。
- 对于刚进入视野的论文，先维护 `QUICK_READ.md`；只有进入当前主线精读时，再新增 `DEEP_READ.md`。

## 每篇论文只先回答 8 个问题

- 任务是什么？
- observation 是什么？
- action 是什么？
- 数据怎么采？
- policy / model 输出什么？
- eval 怎么做？
- failure mode 是什么？
- 如果我要产品化，需要什么 software / data / runtime 支撑？

## Daily Note 回写格式

`start-my-day` 生成计划时，应在 Daily Note 写入：

```text
## 今日论文槽位

- 候选论文：
- 阅读模式：Scan / Structured Read / Deep Read
- 今日目标：一句 takeaway + 一个和 mini-stack 的连接
- 输出位置：
```

完成后，在 `今日总结` 或论文目录的 `QUICK_READ.md` / `DEEP_READ.md` 里补：

```text
- 今日论文 takeaway：
- 和 mini-stack 的连接：
- 后续 idea：
```

## 指定明天论文

如果当天晚上突然想指定某篇论文，写入：

```text
04_Papers/99_Overrides/YYYY-MM-DD.md
```

第二天 `start-my-day` 会优先使用 override，不再从默认队列取第一篇。

推荐对话方式：

```text
明天论文指定：arXiv:xxxx.xxxxx，帮我从 arXiv 抓一下，明天 paper slot 读它。
```

如果只给标题，也可以先创建 override；能确认 arXiv 身份时再补 `arxiv` 和 `source_url`。

## 不做什么

- 不把 paper slot 变成当天主任务，除非它就是本周主线。
- 不默认下载和管理 PDF。
- 不为了覆盖数量牺牲理解质量。
- 不读完就结束，必须留下 takeaway 或项目连接。
