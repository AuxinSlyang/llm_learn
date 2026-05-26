# LLM_Learn × OpenClaw 重构说明

这份目录用于把 `LLM_Learn/` 里原先偏 `Codex + script` 的工作流，整理成更适合 OpenClaw 长期复用的知识与 skill 结构。

## 当前目标

把下面几类能力从“仓库内工作流/脚本”重构成更可复用的 OpenClaw 协作能力：

1. `start-my-day`
2. `end-of-this-week`
3. LLM 学习环境 / 开发机上下文（`dev1`）

## 当前已重构出的 skill

- `skills/start-my-day/`
- `skills/end-of-this-week/`
- `skills/llm-learn-devbox/`

## 原始知识来源

主要来自：
- `LLM_Learn/AGENTS.md`
- `LLM_Learn/10_Workflows/start-my-day_command_spec.md`
- `LLM_Learn/10_Workflows/Workspace_Layout.md`
- `LLM_Learn/10_Workflows/skills/start-my-day/SKILL.md`
- `LLM_Learn/10_Workflows/scripts/start_my_day.py`
- `ssh dev1` 探查到的远端开发环境

## dev1 当前已确认信息

- 登录入口：`ssh dev1`
- 主机名：`n37-194-122`
- 用户：`yangshunlei`
- Home：`/home/yangshunlei -> /data00/home/yangshunlei`
- 当前已观察到的学习仓库根目录：`~/llm_learn`

### `~/llm_learn` 下目前可见项目
- `~/llm_learn/micrograd`
- `~/llm_learn/makemore`
- `~/llm_learn/nanogpt`
- `~/llm_learn/nano-vllm`

## 这批 skill 的定位

### 1. `start-my-day`
面向“今天做什么”的日启动流程：
- 读 Daily / Weekly / Monthly / Annual
- 抽取昨天承接与本周主线
- 输出最低完成线、建议顺序、Top 3、时间切片
- 优先回写当天 Daily Note

### 2. `end-of-this-week`
面向每周收口：
- 回顾本周完成情况
- 提炼产出和卡点
- 更新周计划
- 给下一周写承接点

### 3. `llm-learn-devbox`
面向 LLM 学习型工作区的远端实验环境：
- 了解 `dev1` 的环境与目录
- 知道本地笔记仓库与远端实验仓库如何配合
- 帮助后续做推理/Serving学习、环境盘点、实验推进

## 建议工作流

1. 日常启动时优先用 `start-my-day`
2. 周末或周末前收口时用 `end-of-this-week`
3. 涉及远端实验、环境排查、运行最小推理闭环时用 `llm-learn-devbox`

## 后续可以继续补的 skill

如果你后续继续扩，我建议还可以再做：
- `llm-inference-study-review`：面向 LLM 学习笔记回顾、抽取关键结论
- `llm-experiment-logbook`：面向实验记录规范化沉淀
- `llm-reading-queue`：面向论文/博客/代码阅读队列管理
