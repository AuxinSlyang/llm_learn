---
name: end-my-day
description: Close the current learning day by reading today's Daily Note, recent conversation/carry-over, weekly/monthly/roadmap context, then write a concise daily review and tomorrow handoff. Use when the user says "OK，今天就到这里吧", "今天到这里", "收工", "结束今天", "复盘今天", "end my day", "wrap up today", or asks to close the day.
---

# End My Day

## Overview

Use this when the user wants to stop for the day. The goal is not a long diary; it is a clean handoff so tomorrow's `start-my-day` has context.

## Read Order

1. Today's Daily Note: `01_DailyNotes/YYYY/YYYY-MM/YYYY-MM-DD.md`
2. This week's Weekly Note: `02_WeeklyNotes/`
3. This month's Monthly Plan: `07_MonthlyPlans/`
4. Active roadmap: `00_Roadmap/09_One_Year_Robot_Learning_Full_Stack_Roadmap.md`
5. Runtime support route when relevant: `00_Roadmap/08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime.md`
6. Paper notes touched today, if today's Daily Note or conversation mentions them
7. Automation memory when available: `$CODEX_HOME/automations/daily-start-my-day/memory.md`

## Extract

- What was actually finished today
- What was planned but not finished
- What changed in direction or priority
- Paper takeaways and where they were written
- Files, commands, experiments, or notes touched today
- Blockers and next concrete action

## Decide

Always produce:

1. `今日实际完成`
2. `未完成与原因`
3. `今日学习证据`
4. `明天唯一主线`
5. `明天最低完成线`
6. `需要回写的位置`

Keep the tomorrow handoff small: one main line plus at most two support items.

## Write-Back Rules

Prefer updating today's Daily Note. Reuse existing sections when possible.

Workflow-owned sections:

- `今日总结`
- `实际完成`
- `未完成与原因`
- `今日论文 takeaway`
- `学习证据`
- `明天唯一主线`
- `明天最低完成线`
- `明天承接点`

Do not rewrite unrelated personal notes or experiment details. If there is a conflict between stale notes and the user's current spoken direction, preserve the spoken direction and write it as the next handoff.

## Week / Month Boundary

If today is Friday, Sunday, the last learning day of the week, or the user says this week is done:

- Also run the weekly-close logic from `end-of-this-week`
- Update this week's Weekly Note with actual completion, slips, blockers, and next-week entry
- If a previous week was skipped because there was no active session on the weekend, close that previous completed week first; do not pretend the skipped rest day had a Daily Note

If today is the last calendar day of the month, the last practical learning day of the month, or the user asks for month close:

- Also run the month-close logic from `end-of-this-month`
- Compare actual work against the monthly plan and draft next-month adjustments
- If a previous month was skipped because month-end fell on a rest day, close that previous completed month first, then continue today's close-out

## Git Maintenance

If the workspace is a Git repository and the user has not explicitly disabled commits, commit workflow-owned note changes after write-back.

Rules:

- Always inspect `git status --short` before staging.
- Before staging, read the target Daily Note's `今日学习证据`, `今日输入`, `今日对应文件或命令`, and close-out sections to identify all learning materials that belong to that date.
- A normal daily commit must include the target Daily Note and all same-day learning artifacts evidenced by that Daily Note: project notes, experiment logs, paper `QUICK_READ.md` files, reading indexes, local workflow notes, and directly related PDFs/images when they are part of the learning record.
- Do not commit only the Daily Note when same-day learning materials are still unstaged. Either stage the related materials with the daily commit, or explicitly record why a file is excluded.
- If uncommitted materials span multiple days, split them by Daily Note evidence and attach each group to the corresponding `daily: YYYY-MM-DD` commit. For an existing local daily commit, prefer a fixup/autosquash or amend workflow so the final history has the materials merged into the right daily commit.
- Stage only files created or modified by this close-out run, plus directly related Daily / project / paper / workflow notes and same-day learning artifacts. Do not stage unrelated working-tree changes.
- If unrelated changes already exist, leave them unstaged and mention them briefly.
- If there are no staged changes, do not create an empty commit.

Commit order:

1. Normal day close: commit daily changes and all same-day learning artifacts with `daily: YYYY-MM-DD`.
2. If weekly close also ran, then commit weekly/monthly-plan handoff changes separately with `weekly: YYYY-Www`.
3. If monthly close also ran, then commit month-close changes separately with `monthly: YYYY-MM`.

Daily material split checklist:

- `Daily Note`: target date only, unless intentionally backfilling a missed day.
- `Project artifacts`: experiment logs, BOM/checklists, code maps, dataset/schema/failure notes, reports, and command scaffolds evidenced by the target Daily Note.
- `Paper artifacts`: paper notes, reading plans, reading indexes, downloaded PDFs, figures, and paper-session context created or advanced for that date.
- `Workflow artifacts`: skill/template/workflow notes changed to support that day's learning workflow.
- `Exclude`: `.obsidian/workspace.json`, `.DS_Store`, unrelated old Daily Notes, and broad historical cleanup unless the Daily Note explicitly says they are part of today's work.

Examples:

- `daily: 2026-06-01`
- `weekly: 2026-W23`
- `monthly: 2026-06`

## Fallback

If today's Daily Note is missing, create it from `99_Templates/Daily_Templates.md` or write a compact close note using the existing Daily structure. Do not block the close-out.
