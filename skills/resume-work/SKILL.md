---
name: resume-work
description: Resume work in the llm-learner workspace across local/remote machines by syncing GitHub, inspecting git status, reading the latest Daily Notes/work diary, current Weekly/Monthly/Roadmap context, active Storage+Inference TODO queues, and then producing or executing the next focused continuation step. Use when the user says to resume work, continue from the last session, start from the work diary, sync two machines, inspect local TODOs, or continue llm-learner work after a GitHub pull.
---

# Resume Work

Use this skill for repository-level handoff in `llm-learner` when work may have happened on another machine.

## First Sync

Run these checks before reading notes deeply:

1. `git status --branch --short`
2. `git remote -v`
3. `git fetch --all --prune`
4. Compare local and upstream:
   - `git log --oneline --left-right --cherry-pick HEAD...@{u}` when upstream exists
   - `git diff --name-only` for local uncommitted files
   - `git diff --name-only HEAD..@{u}` for incoming files

If the branch can fast-forward without overlapping local modifications, run:

```bash
git pull --ff-only
```

If incoming files overlap with local dirty files, stop and report the conflict risk. Do not reset, rebase, stash, or discard user changes unless explicitly asked.

Treat GitHub as the cross-machine source of truth, but preserve local scratch files until the user decides.

## Read Handoff Context

After sync, read only enough context to resume work:

1. Workspace rules:
   - `AGENTS.md`
   - `MEMORY.md` if relevant
2. Git state:
   - latest 5-10 commits
   - current dirty/untracked files
3. Recent work diary:
   - today's Daily Note
   - yesterday's Daily Note
   - at least the previous 3-7 Daily Notes when the last active thread is unclear
4. Current planning layer:
   - current Weekly Note under `LLM_Learn/02_WeeklyNotes/`
   - current Monthly Plan under `LLM_Learn/07_MonthlyPlans/`
   - active execution map under `LLM_Learn/00_Roadmap/`
5. Active queue and TODO sources:
   - `LLM_Learn/00_Roadmap/12_Current_Execution_Map_DeepSeek_Storage_Inference_2026H2_2027Q1.md`
   - `LLM_Learn/07_MonthlyPlans/2026-07_to_2027-04_DeepSeek_Storage_Inference_月周计划.md`
   - `LLM_Learn/07_MonthlyPlans/2026-07_to_2027-04_DeepSeek_Storage_Inference_详细周任务.md`
   - `LLM_Learn/04_Papers/60_Systems/AI_Core_Storage_and_KVCache/TOREAD_Storage_Inference_2026H2_2027Q1.md`
   - relevant files under `LLM_Learn/08_Insights/Systems/storage/`

Use `rg` to find actionable carry-over:

```bash
rg -n "TODO|todo|待办|未完成|下一步|承接点|最低完成线|Top 3|gap|Gap|blocker|阻塞" LLM_Learn
```

Keep the scan bounded. Do not summarize the whole vault.

## Decide The Continuation

Always report:

1. Sync result: pulled commits, ahead/behind state, and local scratch files.
2. Last durable evidence: latest Daily/commit/note that proves completed work.
3. Current mainline: one sentence tied to the active roadmap.
4. Open TODOs: grouped as `today`, `this week`, and `backlog`.
5. Recommended next step: one primary task and one minimum completion line.
6. Files to open or edit next.

Prefer the newest user request over stale notes. If the user asks to continue work, execute the next step instead of only planning, while keeping edits scoped.

## Write-Back Rules

Write back only when the user asks to update notes, continue the workflow, or when a continuation action creates new durable evidence.

Preferred write-back targets:

- Today's Daily Note: add a compact `接力启动 / Resume` block or update `今日 Top 3`, `今日最低完成线`, `明天承接点`.
- Current Weekly Note: update only if the weekly mainline or blocker changed.
- Current Monthly Plan/Roadmap: update only for actual strategy changes, not routine progress.

Do not create duplicate Daily/Weekly/Monthly files. Resolve filenames from the actual directory first.

## Git Rules

When committing handoff work:

- Stage only files changed by this resume workflow.
- Keep `.obsidian/workspace.json` and root-level temporary screenshots unstaged unless the user explicitly asks.
- Use dated/topic commits, for example:
  - `workflow: add resume-work handoff skill`
  - `notes: YYYY-MM-DD resume handoff`
  - `papers: YYYY-MM-DD <topic>`
- Push after commit when the user asks for cross-machine sync.

Never use destructive commands such as `git reset --hard` or `git checkout --` unless explicitly requested.
