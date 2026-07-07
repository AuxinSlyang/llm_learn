---
name: start-my-day
description: Analyze the current workspace's Daily Notes for today and at least the previous seven days, plus weekly, monthly, roadmap, recent carry-over notes, and local paper-reading context, to produce a concrete "start my day" plan with a lightweight 2-3 day progression, then optionally write it back into today's Daily Note. Use when the user asks what to do today, wants to start the day, wants a daily plan generated from notes, asks to align today's work with this week/month/year or current learning goals, or explicitly mentions start-my-day.
---

# Start My Day

## Overview

Read the note system first, then synthesize today's minimum viable plan. Prefer the existing Daily Note and Weekly Note structure over inventing a new format.

The workflow must preserve direction sense. Before planning tasks, build a compact `方向锚点` from yesterday, this week, this month, and the active roadmap. Do not plan a day that feels detached from the user's current phase.

This file is a historical / workflow-local copy. The maintained workspace skill lives at `skills/start-my-day/SKILL.md`.

For this workspace, Codex-driven synthesis is the primary implementation of `start-my-day`. The local script is only a deterministic fallback utility and should not replace note-aware analysis.

## Read Order

When the user mentions "today", "this week", "start my day", or similar relative timing, inspect notes in this order:

1. Today's Daily Note: `01_DailyNotes/YYYY/YYYY-MM/YYYY-MM-DD.md`
2. At least the previous 7 calendar days of Daily Notes when they exist. Do not stop at yesterday; scan the full recent week for completed work, repeated carry-over, blockers, and direction changes.
3. This week's Weekly Note in `02_WeeklyNotes/`
4. Relevant monthly plan in `07_MonthlyPlans/`
5. Annual plan and active roadmap files in `00_Roadmap/`; for this workspace, include `03_Annual_Plan_2026.md`, `09_One_Year_Robot_Learning_Full_Stack_Roadmap.md`, and keep `08_One_Year_Roadmap_LLM_Inference_to_Robot_Runtime.md` as the runtime support line
6. Local paper-reading context, at minimum:
   - `04_Papers/00_Paper_Session_Context.md`
   - `04_Papers/00_Reading_Workflow.md`
   - `04_Papers/01_Reading_Index.md`
   - `04_Papers/02_TOREAD_LLM_Papers.md`
   - latest `04_Papers/*Read_Status*` review when present
   - current phase reading pack, such as `04_Papers/Core_Path_Reading_Pack_YYYY-Www.md` when present
   - current VLA / robot-learning maps when relevant: `04_Papers/30_VLA_and_Foundation_Policies/VLA_First_Stage_Reading_Plan.md` and `VLA_VLM_Foundation_Map.md`
7. Automation memory when available: `$CODEX_HOME/automations/daily-start-my-day/memory.md`
8. Paper override for today: `04_Papers/99_Overrides/YYYY-MM-DD.md`

If the needed Daily or Weekly note is missing, create it by extending the matching template in `99_Templates/` instead of inventing a new shape.

## Extract

Collect facts in two layers.

### Direction Layer

- Current North Star and active role target
- Current 12-month route and this month's phase
- This week's single main line and minimum completion line
- Completed work, carry-over, blockers, and any `明天唯一主线` from the previous 7 Daily Notes
- Recent spoken correction from the user if it overrides stale notes

### Execution Layer

- Today's paper override if present; otherwise this week's or current phase's paper queue, only enough to select one paper slot
- Concrete files, commands, experiments, or note outputs that can move the day forward
- Recently planned tasks that are already complete; remove them from today's Top 3 and convert them into the next executable project output
- Current local paper queues and reading context: already-read papers, queued papers, current phase reading pack, VLA/robot-learning reading plan, and today's override if any
- Whether a paper is a hard daily task, a lightweight paper slot, a follow-up queue item, or only a reference/radar item

Do not paste a broad recap of all notes. Produce a short `方向锚点` first, then a concrete day plan.

## Decide

Construct the day around execution, not around reading more notes.

Always produce these in priority order:

1. Direction anchor
2. Minimum completion line
3. Recommended execution order
4. Today's Top 3
5. Today's paper slot
6. Time slices matched to the available time budget
7. A lightweight 2-3 day progression plan
8. Concrete commands, files, or note edits when they help
9. Session/thread title

Apply these rules:

- Preserve the user's current spoken goal over stale notes, then write that resolution back into notes if needed
- Prefer one main line plus at most two supporting tasks
- If time is tight, aggressively cut scope instead of making a crowded plan
- Prefer output tasks over more planning tasks
- Build today's plan from the recent 7-day arc, this week's tasks, and this month's tasks, not only from yesterday. The day should feel like the next step in a layered learning progression.
- Include a compact `后续 2-3 天递进安排` block. It should name the next 2-3 calendar days or sessions, each with one main line and one expected evidence/output. Keep it lightweight and do not turn it into a parallel weekly plan.
- Before choosing or suggesting papers, check local paper context first. Do not add a new paper slot just because a paper was mentioned; classify it as `today`, `follow-up`, `reference`, or `radar`.
- Paper reading must not crowd out the weekly hard output. If the week is hardware/project-heavy, paper work should usually be triage, catch-up, or a 20-40m support slot.
- For this workspace, stay aligned with `Robot Learning Full-Stack` as the active upper route. `LLM / AI Infra` is a support line for VLA / policy runtime / edge inference, not the only default track.
- If today is Friday, Sunday, or the last day of a month, reserve a small review slice or explicitly suggest `end-my-day` / `end-of-this-week` / `end-of-this-month` at close.
- If the previous calendar days include an unclosed week or month because no session was active on a rest day, run a missed-boundary check before today's plan: close the previous week/month first, or explicitly add a catch-up review slice.
- On Monday to Thursday, include one `paper slot` from `04_Papers/01_Reading_Index.md`: 20-40 minutes, one takeaway, one mini-stack connection. On Friday, prefer paper catch-up and takeaway consolidation. On weekends, paper reading is optional unless it is the week's main line.
- If `04_Papers/99_Overrides/YYYY-MM-DD.md` exists, it takes priority over the default queue. Preserve the specified paper, arXiv ID/URL, reason, and output path in `今日论文槽位`.
- Do not let the paper slot consume the evening main study block. Default weekday rhythm is daytime paper slot plus 90 minutes evening execution.

## Session / Thread Title

After deciding today's main line and writing the Daily Note, compute a concise thread title:

```text
<today mainline> YYYY-MM-DD
```

Examples:

- `Rust Ch3-Ch6 + DDIA 2026-07-03`
- `MiniLSM W1 Coding 2026-07-05`
- `TabletServer Read/Write Path 2026-07-06`

Rules:

- Prefer 25-55 characters; keep the task first and the date last.
- Use the strongest execution line, not the automation name. Avoid leaving recurring runs titled `Daily Start My Day`.
- If a Codex thread-title tool is available, rename the current/active automation thread after write-back. If the tool requires a thread id, list recent threads and rename only the unique active thread in the same workspace/current request; if ambiguous, do not rename and include the suggested title in the final output.
- If no thread-title tool is available, include `建议 session 标题：...` in the final output.

## Paper Override Requests

When the user says they want to read a specific paper tomorrow or on a specific date:

1. Parse the target date; default to tomorrow when unspecified.
2. If they provide an arXiv URL, ID, or title, fetch arXiv metadata from official arXiv sources when possible.
3. Create or update `04_Papers/99_Overrides/YYYY-MM-DD.md`.
4. If the paper is identified, create or update the corresponding paper note under `04_Papers/`.
5. Do not change the evening main study plan unless the user explicitly asks.

## Missed Boundary Catch-Up

Rest days can skip Daily Notes and close-out sessions. Therefore `start-my-day` must detect missed weekly/monthly close-outs on the next active day.

Check:

- If today is Monday and the previous week has no `本周复盘` / weekly close result, run or schedule `end-of-this-week` for the previous week before planning new work.
- If today is the first active day of a new month and the previous month has no `月末复盘` / monthly close result, run or schedule `end-of-this-month` for the previous month before planning new work.
- If multiple rest days were skipped, do not create fake Daily Notes for each rest day unless the user asks. Instead create one compact catch-up block in today's Daily Note.

Output a compact `补复盘提醒` section when a missed close-out is detected:

- `需补周复盘：YYYY-Www`
- `需补月复盘：YYYY-MM`
- `今天先做：补复盘 / 正常启动 / 两者都做`

## Output Shape

Unless the user requests a different format, answer in Chinese and keep it practical.

Default response structure:

- `方向锚点`
- `最低完成线`
- `建议顺序`
- `今日 Top 3`
- `今日论文槽位`
- `时间切片`
- `后续 2-3 天递进安排`
- `对应文件或命令`

Do not bury execution advice below long explanations.

## Write-Back Rules

When asked to update notes, prefer editing today's existing Daily Note. Do not create duplicate daily or weekly files.

When writing back:

- Reuse the current Daily template sections if they already exist
- Update only the sections that the workflow owns, such as `今日锚点`, `今日 Top 3`, `今日论文槽位`, `今日时间切片`, `后续 2-3 天递进安排`, `今日输入`, `今日代码 / 实验任务`, and `今日总结`
- Prefer adding or updating `方向锚点`, `昨日承接`, and `明日唯一主线` when those sections exist or the Daily Note is otherwise context-poor
- Keep existing experiment records or personal notes unless they directly conflict
- If the spoken goal and the notes conflict, preserve the spoken goal and reflect that into the Daily or Weekly note

## Fallback

If the note structure is incomplete or inconsistent:

1. Use the best matching existing files
2. State the assumption briefly
3. Still produce a concrete day plan instead of blocking

The local script entry `./start-my-day` or `zsh 10_Workflows/bin/start-my-day` is only for deterministic fallback, dry-run checks, or batch backfill. Prefer Codex-driven synthesis over the script's fixed rule assembly.
