---
name: end-of-this-week
description: Scan this week's daily and weekly notes, synthesize what was completed, what slipped, what blockers matter, then produce a weekly summary, adjust the current weekly plan, and draft next week's plan. Use when the user asks for an end-of-week review, weekly wrap-up, weekly summary, weekly adjustment, or next-week planning.
---

# End Of This Week

## Overview

Read the note system for the current week, then produce a practical week-close result:

1. summarize this week
2. adjust the current week's outcome
3. plan next week

Prefer the existing Weekly Note structure over inventing a separate review format.

This file is a historical / workflow-local copy. The maintained workspace skill lives at `skills/end-of-this-week/SKILL.md`.

## Read Order

When the user asks for "end of this week", "weekly review", "wrap up this week", "plan next week", or similar:

1. This week's Weekly Note: `02_WeeklyNotes/YYYY/YYYY-MM/YYYY-Www.md`
2. All Daily Notes for this week in `01_DailyNotes/YYYY/YYYY-MM/`
3. Relevant monthly plan in `07_MonthlyPlans/`
4. Relevant annual or roadmap files in `00_Roadmap/`, especially the active route `09_One_Year_Robot_Learning_Full_Stack_Roadmap.md`
5. Next week's Weekly Note if it already exists

If this week's or next week's Weekly Note is missing, create it from `99_Templates/Weekly_Templates.md`.

## Extract

Collect only facts that matter for a week-close decision:

- what was actually finished
- what was planned but not finished
- carry-over items and blockers
- repeated themes across the week
- whether the current week drifted from the monthly or annual main line
- what should become next week's one main line and supporting tasks

Do not produce a long diary recap. Compress aggressively into execution-relevant facts.

## Decide

Always produce these in priority order:

1. This week's completion snapshot
2. This week's unfinished and why
3. Weekly-level summary and adjustment
4. Next week's minimum completion line
5. Next week's recommended order
6. Next week's Top 3
7. Concrete note updates when helpful

Apply these rules:

- Preserve the user's current spoken goal over stale notes
- Prefer one weekly main line plus at most two supporting lines
- Distinguish clearly between `本周计划` and `实际完成`
- If the week was overloaded, reduce scope for next week instead of rolling everything forward unchanged
- Keep alignment with `Robot Learning Full-Stack` as the active upper route; frame `LLM / AI Infra` work as runtime support for VLA / policy runtime rather than a detached track.
- If the week also closes the month, call out that `end-of-this-month` should be run or produce a compact month-close section.

## Retroactive Close

If this skill is invoked after the target week already ended, determine the target week before writing:

- Use the week explicitly requested by the user if present.
- Otherwise, if invoked by `start-my-day` missed-boundary catch-up on Monday or the first active day after a rest period, target the previous completed week.
- Write the close-out into that target week's Weekly Note, not the new current week's planning area.
- Use the target week in the commit message: `weekly: YYYY-Www`.

## Output Shape

Unless the user requests a different format, answer in Chinese and keep it practical.

Default response structure:

- `本周实际完成`
- `未完成与原因`
- `本周总结`
- `下周最低完成线`
- `下周建议顺序`
- `下周 Top 3`
- `对应文件或回写建议`

## Write-Back Rules

When asked to update notes:

- prefer editing this week's existing Weekly Note
- if needed, create or update next week's Weekly Note
- reuse current template sections if they already exist
- update only workflow-owned sections such as `本周复盘`, `风险与阻塞`, `本周学习笔记`, `下周唯一主线`, `下周最低完成线`, `时间预算`
- keep existing experiment records unless they directly conflict

If this week's notes and the user's current goal conflict, preserve the spoken goal and reflect that into the weekly notes.

When writing back to this week's Weekly Note, prefer these concrete edits:

- fill `本周复盘` with finished work, unfinished work, blockers, and one short weekly conclusion
- update `风险与阻塞` with the real constraint that affected execution
- append a short `下周入口` block if the template does not already contain one

When writing or creating next week's Weekly Note, prefer these concrete sections:

- `本周锚点`
- `时间预算`
- `本周任务清单`
- `风险与阻塞`
- `本周复盘`

If `下周入口` is missing from the current template, add a compact block near the end with:

- `下周最低完成线`
- `下周建议顺序`
- `下周 Top 3`

## Git Maintenance

If the workspace is a Git repository and the user has not explicitly disabled commits, commit workflow-owned weekly close changes after write-back.

Rules:

- Always inspect `git status --short` before staging.
- Stage only this week's Weekly Note, next week's Weekly Note, directly related Daily summaries, and monthly-plan handoff edits made by this run.
- Do not stage unrelated working-tree changes.
- If unrelated changes already exist, leave them unstaged and mention them briefly.
- If there are no staged changes, do not create an empty commit.

Commit message:

- `weekly: YYYY-Www`

Example:

- `weekly: 2026-W23`

## Fallback

If the note structure is incomplete:

1. use the best matching weekly and daily files
2. state the assumption briefly
3. still produce a concrete weekly close and next-week plan

The local command entry `./end-of-this-week` is only a convenience wrapper for invoking this skill. Prefer Codex-driven synthesis over deterministic scripts.
