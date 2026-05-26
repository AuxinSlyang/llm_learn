---
name: llm-reading-queue
description: Manage reading choices, reading order, and reading extraction for the LLM_Learn workspace. Use when the user wants help choosing what to read next, trimming a reading queue, comparing papers/blogs/code for study value, turning reading materials into actionable note-taking priorities, or deciding whether to read paper, code, or blog first.
---

# LLM Reading Queue

Use this skill when the task is about selecting, ordering, or extracting value from reading materials.

## Typical sources
- `LLM_Learn/04_Reference/Papers/`
- `LLM_Learn/04_Reference/Links/`
- related project notes in `03_Projects/`
- current Daily / Weekly goals

## Primary goals
- choose the next best reading item
- connect reading to the current learning line
- avoid overloading the queue
- turn “interesting material” into an execution decision

## Output shape
Default structure:
- 当前最值得读的 1-3 项
- 每项为什么值得现在读
- 每项应该读到什么程度
- 不建议现在读什么
- 读完后应该沉淀到哪里

## Decision rules
- Prefer materials that directly support the current weekly main line
- Prefer code or implementation-facing material when the current stage is execution-heavy
- Prefer paper/blog abstraction when the current stage is concept-building
- If the queue is too large, cut aggressively instead of ranking ten items
- Reading should serve execution, not replace execution

## Write-back
When asked to update notes, prefer adding a short “推荐阅读 / 当前阅读顺序” section to:
- today's Daily Note
- this week's Weekly Note
- or a project note tied to the topic
