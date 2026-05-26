---
name: start-my-day
description: Analyze the current workspace's daily, weekly, monthly, and annual notes to produce a concrete "start my day" plan, then optionally write it back into today's Daily Note. Use when the user asks what to do today, wants to start the day, wants a daily plan generated from notes, asks to align today's work with this week or current learning goals, or explicitly mentions start-my-day.
---

# Start My Day

## Overview

Read the note system first, then synthesize today's minimum viable plan. Prefer the existing Daily Note and Weekly Note structure over inventing a new format.

This file is a historical / workflow-local copy. The maintained workspace skill lives at `skills/start-my-day/SKILL.md`.

For this workspace, Codex-driven synthesis is the primary implementation of `start-my-day`. The local script is only a deterministic fallback utility and should not replace note-aware analysis.

## Read Order

When the user mentions "today", "this week", "start my day", or similar relative timing, inspect notes in this order:

1. Today's Daily Note: `01_DailyNotes/YYYY/YYYY-MM/YYYY-MM-DD.md`
2. Yesterday's Daily Note when it exists
3. This week's Weekly Note in `02_WeeklyNotes/`
4. Relevant monthly plan in `07_MonthlyPlans/`
5. Paper override for today: `04_Papers/99_Overrides/YYYY-MM-DD.md`
6. Classic paper queue in `04_Papers/01_Reading_Index.md`
7. Relevant annual or roadmap files in `00_Roadmap/`

If the needed Daily or Weekly note is missing, create it by extending the matching template in `99_Templates/` instead of inventing a new shape.

## Extract

Collect only the facts that should influence today's execution:

- Yesterday's carry-over: unfinished items, blockers, and any `明天唯一主线`
- This week's main line, minimum completion line, and explicit deliverables
- Today's paper override if present; otherwise this week's or current phase's paper queue, only enough to select one paper slot
- Monthly or annual constraints only if they materially change today
- The user's current spoken goal if it conflicts with existing notes

Do not spend tokens on a broad summary of all notes. Pull only the facts that determine today's plan.

## Decide

Construct the day around execution, not around reading more notes.

Always produce these in priority order:

1. Minimum completion line
2. Recommended execution order
3. Today's Top 3
4. Today's paper slot
5. Time slices matched to the available time budget
6. Concrete commands, files, or note edits when they help

Apply these rules:

- Preserve the user's current spoken goal over stale notes, then write that resolution back into notes if needed
- Prefer one main line plus at most two supporting tasks
- If time is tight, aggressively cut scope instead of making a crowded plan
- Prefer output tasks over more planning tasks
- For this workspace, stay aligned with the current monthly and weekly main line. `LLM / AI Infra` is a support line for the broader robotics and embodied AI goal, not the only default track.
- On Monday to Thursday, include one `paper slot` from `04_Papers/01_Reading_Index.md`: 20-40 minutes, one takeaway, one mini-stack connection. On Friday, prefer paper catch-up and takeaway consolidation. On weekends, paper reading is optional unless it is the week's main line.
- If `04_Papers/99_Overrides/YYYY-MM-DD.md` exists, it takes priority over the default queue. Preserve the specified paper, arXiv ID/URL, reason, and output path in `今日论文槽位`.
- Do not let the paper slot consume the evening main study block. Default weekday rhythm is daytime paper slot plus 90 minutes evening execution.

## Paper Override Requests

When the user says they want to read a specific paper tomorrow or on a specific date:

1. Parse the target date; default to tomorrow when unspecified.
2. If they provide an arXiv URL, ID, or title, fetch arXiv metadata from official arXiv sources when possible.
3. Create or update `04_Papers/99_Overrides/YYYY-MM-DD.md`.
4. If the paper is identified, create or update the corresponding paper note under `04_Papers/`.
5. Do not change the evening main study plan unless the user explicitly asks.

## Output Shape

Unless the user requests a different format, answer in Chinese and keep it practical.

Default response structure:

- `最低完成线`
- `建议顺序`
- `今日 Top 3`
- `今日论文槽位`
- `时间切片`
- `对应文件或命令`

Do not bury execution advice below long explanations.

## Write-Back Rules

When asked to update notes, prefer editing today's existing Daily Note. Do not create duplicate daily or weekly files.

When writing back:

- Reuse the current Daily template sections if they already exist
- Update only the sections that the workflow owns, such as `今日锚点`, `今日 Top 3`, `今日论文槽位`, `今日时间切片`, `今日输入`, `今日代码 / 实验任务`, and `今日总结`
- Keep existing experiment records or personal notes unless they directly conflict
- If the spoken goal and the notes conflict, preserve the spoken goal and reflect that into the Daily or Weekly note

## Fallback

If the note structure is incomplete or inconsistent:

1. Use the best matching existing files
2. State the assumption briefly
3. Still produce a concrete day plan instead of blocking

The local script entry `./start-my-day` or `zsh 10_Workflows/bin/start-my-day` is only for deterministic fallback, dry-run checks, or batch backfill. Prefer Codex-driven synthesis over the script's fixed rule assembly.
