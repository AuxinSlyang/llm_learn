---
name: llm-inference-study-review
description: Review, summarize, and structure learning progress for the LLM_Learn workspace. Use when the user wants to review what has been learned in robotics, embodied AI, Modern Robotics, MuJoCo, Robot Learning, LLM fundamentals, or AI Infra; turn scattered notes into a clearer understanding; prepare study summaries; compare notes across daily/weekly/project files; or extract key concepts, open questions, and next steps from current learning materials.
---

# Learning Study Review

Use this skill when the task is not “plan today” but “understand what has already been learned and turn it into a cleaner knowledge structure”.

## Primary goals

Help the user:
- review what was learned
- extract key concepts and mental models
- identify gaps, confusions, and next questions
- turn scattered notes into reusable summaries
- keep study effort aligned with the current Roadmap Phase

## Read order

Prefer this order:
1. Relevant project note under `LLM_Learn/03_Projects/`
2. Recent Daily Notes mentioning the topic
3. Recent Weekly Notes mentioning the topic
4. Relevant insight notes under `LLM_Learn/08_Insights/`
5. Annual / roadmap notes only if needed to reconnect the topic to the long line

Also read:
- `references/review-structure.md`

## Produce

Default output shape:
- 这次学习到底在解决什么问题
- 目前已经搞明白了什么
- 还没彻底搞明白什么
- 最关键的 3-5 个概念
- 推荐下一步
- 如果需要，建议写回哪个笔记文件

## Rules

- Prefer compression over repetition
- Do not rewrite all notes into a long summary
- Pull out the “why / how / tradeoff / unknowns” layer
- Tie the topic back to the current Pillar / Phase. Only tie back to inference / runtime when the topic is part of the language intelligence or AI Infra support line.
- If the user is still in an early learning phase, do not over-upgrade the output into fake certainty

## Write-back

When asked to write back, prefer one of:
- the relevant project note
- `08_Insights/`
- today's Daily Note
- this week's Weekly Note

Do not create duplicate summary files unless the user explicitly wants a standalone review note.
