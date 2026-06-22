---
name: start-my-day
description: Build today's plan for the LLM_Learn workspace by reading today's Daily Note, at least the previous seven days of Daily Notes, this week's Weekly Note, the current Monthly Plan, annual/roadmap notes, and local paper-reading context, then produce a concrete execution plan, arrange the next 2-3 days at a lightweight level, and update today's Daily Note if needed. Use when the user asks what to do today, wants to start the day, wants today's learning plan, asks to align today with this week or current embodied AI, robotics, AI Infra, or LLM learning goals, or explicitly mentions start-my-day.
---

# Start My Day

Use this skill for the `LLM_Learn/` note workspace.

## Read order

Read in this order:
1. `LLM_Learn/01_DailyNotes/YYYY/YYYY-MM/YYYY-MM-DD.md`
2. At least the previous 7 calendar days of Daily Notes if they exist. Do not stop at yesterday; scan the full recent week for completed work, repeated carry-over, blockers, and changes in direction.
3. This week's note under `LLM_Learn/02_WeeklyNotes/`
4. Current monthly plan under `LLM_Learn/07_MonthlyPlans/`
5. Relevant annual or roadmap notes under `LLM_Learn/00_Roadmap/`
6. Local paper-reading context, at minimum:
   - `LLM_Learn/04_Papers/00_Paper_Session_Context.md`
   - `LLM_Learn/04_Papers/00_Reading_Workflow.md`
   - `LLM_Learn/04_Papers/01_Reading_Index.md`
   - `LLM_Learn/04_Papers/02_TOREAD_LLM_Papers.md`
   - latest `LLM_Learn/04_Papers/*Read_Status*` review when present
   - current phase reading pack, such as `LLM_Learn/04_Papers/Core_Path_Reading_Pack_YYYY-Www.md` when present
   - current VLA / robot-learning maps when relevant: `LLM_Learn/04_Papers/30_VLA_and_Foundation_Policies/VLA_First_Stage_Reading_Plan.md` and `VLA_VLM_Foundation_Map.md`
7. Today's paper override: `LLM_Learn/04_Papers/99_Overrides/YYYY-MM-DD.md` when present
8. `LLM_Learn/AGENTS.md` if you need workspace-wide context

If needed, also read:
- `references/workspace-layout.md`
- `references/start-my-day-spec.md`

## Extract only what matters

Pull only facts that affect today:
- Completed work, carry-over, blockers, and direction changes from the previous 7 Daily Notes
- `明天唯一主线`
- This week's唯一主线 / 最低完成线 / 明确产出
- Monthly or annual constraints only if they change today's priorities
- The user's current spoken goal if it conflicts with notes
- Whether tasks already marked as "today's plan" have actually been completed in yesterday/recent notes; if so, remove them from today's Top 3 and turn them into the next executable output
- Current local paper queues and reading context: already-read papers, queued papers, current phase reading pack, VLA/robot-learning reading plan, and today's override if any
- Whether a paper is a hard daily task, a lightweight paper slot, a follow-up queue item, or only a reference/radar item

Do not summarize the whole notebook system.

## Decide

Always produce, in priority order:
1. 方向锚点
2. 本周 / 今日目标
3. 最低完成线
4. 建议顺序
5. 今日 Top 3
6. 今日论文槽位
7. 时间切片
8. 后续 2-3 天递进安排
9. 对应文件或命令

Rules:
- Keep the user's spoken goal above stale notes, then write that resolution back into today's note if needed
- Prefer one main line plus at most two supporting tasks
- If time is tight, cut scope aggressively
- For this workspace, stay aligned with the current monthly and weekly main line. `LLM / AI Infra` is a support line for the broader robotics and embodied AI goal, not the only default track.
- Prefer execution over planning
- Build today's plan from the recent 7-day arc, not only yesterday. The day should feel like the next step in a layered progression, not a standalone task list.
- Include a compact `后续 2-3 天递进安排` block. It should name the next 2-3 calendar days or sessions, each with one main line and one expected evidence/output. Keep it lightweight; do not turn it into a new weekly plan.
- Before choosing or suggesting papers, check local paper context first. Do not add a new paper slot just because a paper was mentioned; classify it as `today`, `follow-up`, `reference`, or `radar`.
- Paper reading must not crowd out the weekly hard output. If the week is hardware/project-heavy, paper work should usually be triage, catch-up, or a 20-40m support slot.
- The recurring goal block must stay compact: only show `本周目标`, `今日目标`, and `今日证据`. Do not repeat North Star, annual roadmap, or long-term career framing in the daily output unless the user explicitly asks.
- Keep `方向锚点` focused on this week and today; avoid monthly/annual/long-term framing unless it changes today's priority.

## Write-back

When asked to update notes, prefer editing today's existing Daily Note.
Update only workflow-owned sections such as:
- `本周 / 今日目标`
- `今日锚点`
- `今日 Top 3`
- `今日时间切片`
- `后续 2-3 天递进安排`
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
