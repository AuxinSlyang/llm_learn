---
name: start-my-day
description: Build today's plan for the LLM_Learn workspace by reading today's Daily Note, yesterday's carry-over, this week's Weekly Note, the current Monthly Plan, and annual/roadmap notes, then produce a concrete execution plan and update today's Daily Note if needed. Use when the user asks what to do today, wants to start the day, wants today's learning plan, asks to align today with this week or current embodied AI, robotics, AI Infra, or LLM learning goals, or explicitly mentions start-my-day.
---

# Start My Day

Use this skill for the `LLM_Learn/` note workspace.

## Read order

Read in this order:
1. `LLM_Learn/01_DailyNotes/YYYY/YYYY-MM/YYYY-MM-DD.md`
2. Yesterday's Daily Note if it exists
3. This week's note under `LLM_Learn/02_WeeklyNotes/`
4. Current monthly plan under `LLM_Learn/07_MonthlyPlans/`
5. Relevant annual or roadmap notes under `LLM_Learn/00_Roadmap/`
6. `LLM_Learn/AGENTS.md` if you need workspace-wide context

If needed, also read:
- `references/workspace-layout.md`
- `references/start-my-day-spec.md`

## Extract only what matters

Pull only facts that affect today:
- Yesterday's carry-over and blockers
- `明天唯一主线`
- This week's唯一主线 / 最低完成线 / 明确产出
- Monthly or annual constraints only if they change today's priorities
- The user's current spoken goal if it conflicts with notes

Do not summarize the whole notebook system.

## Decide

Always produce, in priority order:
1. 最低完成线
2. 建议顺序
3. 今日 Top 3
4. 时间切片
5. 对应文件或命令

Rules:
- Keep the user's spoken goal above stale notes, then write that resolution back into today's note if needed
- Prefer one main line plus at most two supporting tasks
- If time is tight, cut scope aggressively
- For this workspace, stay aligned with the current monthly and weekly main line. `LLM / AI Infra` is a support line for the broader robotics and embodied AI goal, not the only default track.
- Prefer execution over planning

## Write-back

When asked to update notes, prefer editing today's existing Daily Note.
Update only workflow-owned sections such as:
- `今日锚点`
- `今日 Top 3`
- `今日时间切片`
- `今日输入`
- `今日代码 / 实验任务`
- `今日总结`

Linking rules for new or updated Daily Notes:
- Always link to the real target filename, not a guessed display title.
- Use Obsidian alias style when you want readable text: `[[real_file_name|readable title]]`.
- Weekly note links must be computed from the day being processed (its actual ISO week), then matched to the real weekly file name for that week. Do not hardcode examples like `W14`.
- Monthly plan links must be computed from the day being processed (its actual `YYYY-MM`), then matched to the real monthly plan filename for that month. Do not hardcode examples like `2026-04`.
- For frontmatter fields like `linked_week`, use the real weekly filename target for that date.
- If unsure about a target note name, inspect the actual file path first instead of inventing a wiki-link title.
- Preferred pattern:
  - Weekly: resolve that date's weekly file, then write `[[actual_week_file_name|readable weekly title]]`
  - Monthly: resolve that date's monthly file, then write `[[actual_month_file_name|readable monthly title]]`

Do not create duplicate Daily or Weekly files.

## Fallback

The older script idea is useful as a deterministic fallback, but the main implementation should remain agent-driven synthesis.
