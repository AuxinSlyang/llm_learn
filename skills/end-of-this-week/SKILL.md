---
name: end-of-this-week
description: Close the current week for the LLM_Learn workspace by reading this week's Weekly Note, recent Daily Notes, and the current monthly plan, then summarize what was done, what is blocked, what should carry forward, and update the Weekly Note or next-week handoff if needed. Use when the user asks to close the week, summarize this week, prepare next week, do a weekly review, or mentions end-of-this-week.
---

# End Of This Week

Use this skill for weekly close-out in `LLM_Learn/`.

## Read order
1. Current week's Weekly Note in `LLM_Learn/02_WeeklyNotes/`
2. Recent Daily Notes from this week
3. Current monthly plan in `LLM_Learn/07_MonthlyPlans/`
4. Relevant annual/roadmap files in `LLM_Learn/00_Roadmap/` only if needed

## Extract
Focus on:
- What was actually completed
- What remains unfinished
- Blockers and repeated failure patterns
- This week's outputs, experiments, and notes worth retaining
- What should become next week's carry-over

## Produce
Default structure:
- 本周完成
- 本周未完成
- 本周阻塞 / 风险
- 下周承接
- 是否需要调整月计划

## Write-back
Prefer updating the existing Weekly Note instead of creating a duplicate review file.
If the user wants a separate summary, write one and keep it linked back to the Weekly Note.
