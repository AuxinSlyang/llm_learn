---
name: end-of-this-month
description: Close the current learning month by scanning monthly plan, weekly notes, daily notes, roadmap, papers, projects, and produce a monthly summary, progress adjustment, and next-month plan. Use when the user asks for monthly review, end-of-month summary, month close, 月度总结, 月末复盘, or when end-my-day is run on the last practical day of a month.
---

# End Of This Month

## Overview

Use this for month-end review. The output should compare actual work against the monthly plan and adjust next month, not merely summarize diary entries.

## Read Order

1. Current Monthly Plan: `07_MonthlyPlans/YYYY/YYYY-MM_月计划.md`
2. All Weekly Notes in the month: `02_WeeklyNotes/YYYY/YYYY-MM/`
3. Daily Notes in the month: `01_DailyNotes/YYYY/YYYY-MM/`
4. Active roadmap: `00_Roadmap/09_One_Year_Robot_Learning_Full_Stack_Roadmap.md`
5. Annual plan: `00_Roadmap/03_Annual_Plan_2026.md`
6. Paper index and paper notes touched this month
7. Project notes touched this month
8. Next month's Monthly Plan if it exists

## Extract

- Monthly planned minimum completion line
- Actual completed outputs
- Slipped items and reasons
- Direction changes or route corrections
- Repeated blockers
- Paper takeaways worth retaining
- Projects or experiments that produced evidence
- Next month constraints and realistic focus

## Decide

Produce:

1. `本月实际完成`
2. `计划对照`
3. `未完成与原因`
4. `路线调整`
5. `本月学习证据`
6. `下月最低完成线`
7. `下月 Top 3`
8. `需要回写的位置`

## Write-Back Rules

Prefer editing the current Monthly Plan and next month's Monthly Plan.

Current month workflow-owned sections:

- `月末复盘`
- `实际完成`
- `未完成与原因`
- `路线调整`
- `下月入口`

Next month workflow-owned sections:

- `本月定位`
- `本月最低完成线`
- `本月关键产出`
- `对应周计划`
- `月末自检`

Do not rewrite historical notes unless the user asks. If the roadmap changed during the month, record the change explicitly and keep old plans as history.

## Retroactive Close

If this skill is invoked after the target month already ended, determine the target month before writing:

- Use the month explicitly requested by the user if present.
- Otherwise, if invoked by `start-my-day` missed-boundary catch-up on the first active day of a new month, target the previous completed month.
- Write the close-out into that target month's Monthly Plan, not the new current month's main planning area.
- Use the target month in the commit message: `monthly: YYYY-MM`.

## Git Maintenance

If the workspace is a Git repository and the user has not explicitly disabled commits, commit workflow-owned month-close changes after write-back.

Rules:

- Always inspect `git status --short` before staging.
- Stage only the current Monthly Plan, next month's Monthly Plan, directly related Weekly summaries, roadmap adjustment notes, and month summary outputs created by this run.
- Do not stage unrelated working-tree changes.
- If unrelated changes already exist, leave them unstaged and mention them briefly.
- If there are no staged changes, do not create an empty commit.

Commit message:

- `monthly: YYYY-MM`

Example:

- `monthly: 2026-06`

## Fallback

If the month has sparse notes, still produce a practical summary from weekly notes, daily notes, and conversation memory. Mark assumptions briefly.
