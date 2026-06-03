---
type: paper_note
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
authors:
  - Shunyu Yao
  - Jeffrey Zhao
  - Dian Yu
  - Nan Du
  - Izhak Shafran
  - Karthik Narasimhan
  - Yuan Cao
arxiv: "2210.03629"
source_url: "https://arxiv.org/abs/2210.03629"
pdf_url: "https://arxiv.org/pdf/2210.03629"
project_url: "https://react-lm.github.io/"
local_pdf: "/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models/ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models.pdf"
published: "2022-10-06"
updated: "2023-03-10"
venue: ICLR 2023
categories:
  - cs.CL
  - cs.AI
  - cs.LG
status: quick_read_done
read_mode: Quick Scan
---

# ReAct: Synergizing Reasoning and Acting in Language Models

## Metadata

- 论文：ReAct: Synergizing Reasoning and Acting in Language Models
- 作者：Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- arXiv：2210.03629
- 官方来源：https://arxiv.org/abs/2210.03629
- PDF：https://arxiv.org/pdf/2210.03629
- 项目页：https://react-lm.github.io/
- 本地 PDF：`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/04_Papers/10_AI_Foundations/ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models/ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models.pdf`

## Why Now

今天已经读完 DPO 和 Self-Consistency：

- DPO：训练阶段，如何用 preference pairs 替代显式 reward model + PPO。
- Self-Consistency：推理阶段，如何用多条 CoT 路径和 final answer voting 提高推理稳定性。
- ReAct：继续往 agent/runtime 方向走，把 `reasoning` 和 `acting` 交替起来，让模型能通过 action 接触外部知识库或环境，再用 observation 更新推理。

## Reading Questions

1. ReAct 和普通 Chain-of-Thought 的区别是什么？
2. `Thought -> Action -> Observation` 这条循环具体解决了什么问题？
3. 为什么只 reasoning 容易 hallucination / error propagation，只 acting 又缺少可解释计划？
4. 它在 HotpotQA / FEVER / ALFWorld / WebShop 上分别证明了什么？
5. 它如何连接到未来 robot runtime / tool use / environment feedback？

## Reading Prep

- 推荐读法：Quick Scan（20-30m），只抓 `Abstract / Introduction / ReAct prompting format / main results`。
- 今日重点：理解 `reasoning traces` 和 `task-specific actions` 为什么要 interleave。
- 不展开方向：不细挖所有 benchmark，也不进入 agent framework 工程实现。

## Section Map

| Section | 读什么 | 第一遍是否必读 |
|---|---|---|
| Abstract + Introduction | 为什么 reasoning 和 acting 过去被分开研究，ReAct 想把它们结合 | 必读 |
| Method / Prompting | `Thought -> Action -> Observation` 轨迹格式 | 必读 |
| Knowledge-intensive QA | HotpotQA / FEVER：通过 Wikipedia API 减少 hallucination 和 error propagation | 扫读 |
| Interactive Decision Making | ALFWorld / WebShop：模型在环境中行动并根据 observation 调整计划 | 扫读 |
| Analysis / Examples | 看 1-2 个 trajectory，理解可解释性和错误恢复 | 必读一个例子 |
| Appendix | 细节和更多轨迹 | 可跳 |

## Abstract + Introduction Understanding

### 问题

LLM 的 reasoning 能力和 acting 能力过去常被分开研究：CoT 强调生成推理轨迹，但不和外部环境交互；action generation 能让模型执行动作，但缺少显式 reasoning trace，遇到异常时不容易解释和修正。

### 核心想法

ReAct 让模型交替生成 reasoning traces 和 task-specific actions：

```text
Thought -> Action -> Observation -> Thought -> Action -> Observation -> ...
```

reasoning 用来规划、跟踪状态、处理异常；action 用来查询外部信息或在环境中执行动作；observation 再反馈给下一步 reasoning。

### 一句话直觉

ReAct 不是只让模型“想”，也不是只让模型“做”，而是让模型边想、边做、边看反馈，再继续调整。

## Method

待读时重点确认：

```text
prompt with ReAct examples
  -> model emits Thought
  -> model emits Action
  -> environment/tool returns Observation
  -> model continues Thought/Action
  -> final answer or task completion
```

关键点：

- 它是 prompting / inference-time agent pattern，不是新模型架构。
- 它把 CoT 的 reasoning trace 和 tool/environment action 放在同一条 trajectory 中。
- 对 QA 任务，action 往往是查 Wikipedia API；对 ALFWorld/WebShop，action 是环境动作。

## Experiments

官方摘要中报告：

- HotpotQA / FEVER：ReAct 通过和 Wikipedia API 交互，缓解纯 CoT 的 hallucination 和 error propagation。
- ALFWorld / WebShop：ReAct 在交互式决策任务上优于若干 imitation / reinforcement learning baselines，并且只需要少量 in-context examples。

后续阅读重点：

- ReAct 相比 CoT / Act-only / CoT-SC 的差别；
- 哪些任务收益来自 external observation，哪些收益来自 reasoning trace；
- ReAct 是否依赖 prompt example 质量；
- 轨迹是否真的可解释，错误时是否能恢复。

## Takeaway

ReAct 是把 CoT 推理变成可交互 agent trajectory 的最小范式：`Thought` 负责计划、状态跟踪和纠错，`Action` 负责调用工具或环境，`Observation` 由外部 runtime 返回并注入下一轮上下文。

## Quick Read Summary

- 核心问题：纯 CoT 只能在模型内部推理，容易 hallucination / error propagation；纯 action generation 缺少显式计划和状态跟踪。
- 核心方法：用 few-shot ReAct trajectories 引导模型交替生成 `Thought -> Action -> Observation`，其中 Observation 不是模型生成，而是外部工具/环境返回。
- 工程结构：ReAct 本质是 `prompt protocol + runtime loop`；runtime 负责解析 action、调用工具、截断模型生成的伪 observation、写入真实 observation。
- 成功机制：Thought 维护子目标和状态，Action 接入外部事实或环境，Observation 让下一步 Thought 能修正计划。
- 典型失败：search result 无效、Thought 状态跟踪错误、Action 无效后无法恢复、长 horizon 下重复循环。
- 机器人映射：ReAct 只能作为高层 planner / skill dispatcher 的启发；连续感知、运动规划、低层控制和安全闭环必须由 robot stack 承担。

## Robot Learning / Runtime Connection

ReAct 对当前路线的价值很直接：它提供了一个高层 agent/runtime 模式，能把语言推理、工具调用、环境观察和行动闭环连接起来。未来机器人系统中的 `planner / policy runtime / tool use / simulator check / failure recovery` 都可以参考这种 `Thought -> Action -> Observation` 结构。

## Open Questions

- 如果 action 是机器人动作而不是 API query，observation 如何结构化给 LLM？
- ReAct 的 reasoning trace 是真正提升任务表现，还是主要提升可解释性？
- 在长 horizon 任务里，ReAct 是否会累积错误或产生无效 action？
- ReAct 与 Self-Consistency 能否结合：多条 ReAct trajectories + environment/verifier selection？
