---
name: llm-experiment-logbook
description: Record, clean up, and structure LLM learning experiments across the LLM_Learn notes workspace and the dev1 remote machine. Use when the user wants to log an experiment, turn shell output or trial-and-error into a proper note, summarize what was tried, record environment facts, capture benchmark results, or make experiment notes reproducible.
---

# LLM Experiment Logbook

Use this skill when the task is about turning ad-hoc experimentation into a reusable record.

## Typical inputs
- shell commands that were run
- environment facts from `dev1`
- benchmark output
- model loading / CUDA / torch / vLLM / nano-vllm observations
- “I tried X and got Y” style notes

## Primary goals
- capture what was attempted
- capture environment and assumptions
- capture result and interpretation
- capture what to do next
- reduce loss of experiment context

## Preferred read sources
1. Today's Daily Note
2. Relevant project note in `03_Projects/` or `06_AI/`
3. Existing experiment-related note if one already exists
4. `references/log-template.md`
5. If needed, inspect `dev1` for repo paths / environment facts

## Default output structure
- 实验目标
- 环境信息
- 操作步骤
- 结果
- 结论
- 当前阻塞
- 下一步

## Rules
- Prefer exact commands over vague descriptions when commands matter
- Distinguish observation from interpretation
- Keep reproducibility in mind: someone should know how to rerun the experiment
- If the result is inconclusive, say so explicitly
- Tie the experiment back to the current learning line

## Write-back

Prefer writing into:
- today's Daily Note if the experiment is small
- a project note if the experiment belongs to a project/theme
- a dedicated note only if the experiment is large enough to deserve one
