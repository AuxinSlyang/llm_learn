#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import List, Optional


ROOT = Path(__file__).resolve().parents[2]


@dataclass
class Context:
    today: date
    time_budget: str
    daily_path: Path
    yesterday_path: Optional[Path]
    weekly_path: Optional[Path]
    monthly_path: Optional[Path]
    paper_index_path: Optional[Path]
    paper_override_path: Optional[Path]
    roadmap_path: Optional[Path]
    annual_path: Optional[Path]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate today's plan from annual/monthly/weekly/daily notes.")
    parser.add_argument("time_budget", nargs="?", default="2h", help="Today's learning time budget, default 2h")
    parser.add_argument("--date", dest="date_str", help="Override date in YYYY-MM-DD format")
    parser.add_argument("--dry-run", action="store_true", help="Print generated content without writing file")
    return parser.parse_args()


def parse_date(value: Optional[str]) -> date:
    if value:
        return datetime.strptime(value, "%Y-%m-%d").date()
    return date.today()


def today_daily_path(day: date) -> Path:
    return ROOT / "01_DailyNotes" / day.strftime("%Y") / day.strftime("%Y-%m") / f"{day:%Y-%m-%d}.md"


def weekly_candidates(day: date) -> List[Path]:
    iso_year, iso_week, _ = day.isocalendar()
    monday = day - timedelta(days=day.weekday())
    return [
        ROOT / "02_WeeklyNotes" / f"{iso_year}" / monday.strftime("%Y-%m") / f"{iso_year}-W{iso_week:02d}.md",
        ROOT / "02_WeeklyNotes" / f"{iso_year}" / f"{iso_year}-W{iso_week:02d}.md",
    ]


def monthly_candidates(day: date) -> List[Path]:
    return [
        ROOT / "07_MonthlyPlans" / day.strftime("%Y") / f"{day:%Y-%m}_月计划.md",
        ROOT / "07_MonthlyPlans" / f"{day:%Y-%m}_月计划.md",
    ]


def first_existing(paths: List[Path]) -> Optional[Path]:
    for path in paths:
        if path.exists():
            return path
    return None


def build_context(day: date, time_budget: str) -> Context:
    # JD1 12-month roadmap was archived 2026-05-17; keep glob for backward-compat read only.
    roadmap_matches: List[Path] = []
    roadmap_dir = ROOT / "00_Roadmap"
    annual_matches = list(roadmap_dir.glob("03_Annual_Plan_*.md"))
    yday = day - timedelta(days=1)
    return Context(
        today=day,
        time_budget=time_budget,
        daily_path=today_daily_path(day),
        yesterday_path=today_daily_path(yday) if today_daily_path(yday).exists() else None,
        weekly_path=first_existing(weekly_candidates(day)),
        monthly_path=first_existing(monthly_candidates(day)),
        paper_index_path=ROOT / "04_Papers" / "01_Reading_Index.md",
        paper_override_path=ROOT / "04_Papers" / "99_Overrides" / f"{day:%Y-%m-%d}.md",
        roadmap_path=roadmap_matches[0] if roadmap_matches else None,
        annual_path=annual_matches[0] if annual_matches else None,
    )


def read(path: Optional[Path]) -> str:
    if not path or not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def extract_section(text: str, heading: str) -> str:
    if not text:
        return ""
    pattern = re.compile(rf"(^## {re.escape(heading)}\n)(.*?)(?=^## |\Z)", re.S | re.M)
    match = pattern.search(text)
    return match.group(2).strip() if match else ""


def extract_first_unchecked_bullets(text: str, max_items: int = 5) -> List[str]:
    items = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [ ] ") or stripped.startswith("* [ ] "):
            items.append(stripped[6:].strip())
        elif stripped.startswith("- ") and "`" in stripped:
            items.append(stripped[2:].strip())
        if len(items) >= max_items:
            break
    return items


def extract_first_checked_or_plain_bullets(text: str, max_items: int = 5) -> List[str]:
    items = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [ ] "):
            items.append(stripped[6:].strip())
        elif stripped.startswith("- [x] "):
            items.append(stripped[6:].strip())
        elif stripped.startswith("- "):
            items.append(stripped[2:].strip())
        if len(items) >= max_items:
            break
    return items


def extract_tomorrow_line(yesterday_text: str) -> str:
    match = re.search(r"明天唯一主线：`?(.+?)`?$", yesterday_text, re.M)
    return match.group(1).strip() if match else ""


def normalize_time_budget(value: str) -> str:
    v = value.strip().lower()
    if not v:
        return "2h"
    if v.endswith("h"):
        return v
    if v.isdigit():
        return f"{v}h"
    return value


def time_hours(value: str) -> float:
    match = re.match(r"(\d+(?:\.\d+)?)h", normalize_time_budget(value))
    if not match:
        return 2.0
    return float(match.group(1))


def phase_from_budget(hours: float) -> str:
    if hours <= 1.5:
        return "light"
    if hours <= 2.5:
        return "standard"
    return "full"


def make_theme(ctx: Context, y_tomorrow: str, weekly_mainline: List[str], monthly_targets: List[str]) -> str:
    if y_tomorrow:
        return clip_code(y_tomorrow)
    if weekly_mainline:
        return clip_code(weekly_mainline[0])
    if monthly_targets:
        return clip_code(monthly_targets[0])
    return clip_code("沿当前主线推进，不偏离本周与本月目标")


def clip_code(text: str) -> str:
    text = re.sub(r"^[\-\*\s\[\]xX]+", "", text)
    text = re.sub(r"`", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def build_top3(weekly_tasks: List[str], monthly_tasks: List[str], theme: str) -> List[str]:
    pool = weekly_tasks + monthly_tasks
    cleaned = []
    seen = set()
    for item in [theme] + pool:
        c = clip_code(item)
        if not c or c in seen:
            continue
        seen.add(c)
        cleaned.append(c)
        if len(cleaned) >= 3:
            break
    while len(cleaned) < 3:
        cleaned.append("围绕今天唯一主线补齐最小输出")
    return cleaned[:3]


def build_sessions(hours: float, top3: List[str]) -> List[str]:
    mode = phase_from_budget(hours)
    if mode == "light":
        return [
            "Paper Slot（20-40m，白天碎片）：只抓一句 takeaway 和一个 mini-stack 连接",
            f"Evening Session 1（45-60m）：先推进 `{top3[0]}`，只保最低完成线",
            f"Evening Session 2（20-30m）：收口 `{top3[1]}`，补一条今日总结和明天承接点",
        ]
    if mode == "standard":
        return [
            "Paper Slot（20-40m，白天碎片）：只抓一句 takeaway 和一个 mini-stack 连接",
            f"Evening Session 1（45-60m）：主攻 `{top3[0]}`",
            f"Evening Session 2（30-45m）：推进 `{top3[1]}`",
            f"Wrap-up（15-20m）：收口 `{top3[2]}`，补最小笔记和明天承接点",
        ]
    return [
        "Paper Slot（20-40m，白天碎片）：只抓一句 takeaway 和一个 mini-stack 连接",
        f"Evening Session 1（45-60m）：主攻 `{top3[0]}`",
        f"Evening Session 2（45-60m）：推进 `{top3[1]}`",
        f"Session 3（45-60m）：推进 `{top3[2]}`",
        "Session 4（20-30m）：统一收口，补笔记、阻塞和明天承接点",
    ]


def extract_paper_queue(text: str, max_items: int = 8) -> List[str]:
    section = extract_section(text, "当前 4 周论文队列")
    if not section:
        section = text
    items = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [ ] "):
            items.append(stripped[6:].strip())
        if len(items) >= max_items:
            break
    return items


def paper_output_path(paper: str) -> str:
    mappings = [
        ("DAgger", "04_Papers/20_Robot_Learning/DAgger/README.md"),
        ("ACT", "04_Papers/20_Robot_Learning/ACT/README.md"),
        ("Diffusion Policy", "04_Papers/20_Robot_Learning/Diffusion_Policy/README.md"),
        ("RT-1", "04_Papers/30_VLA_and_Foundation_Policies/RT_1/README.md"),
        ("RT-2", "04_Papers/30_VLA_and_Foundation_Policies/RT_2/README.md"),
        ("Open X-Embodiment", "04_Papers/40_Data_and_Eval/Open_X_Embodiment/README.md"),
        ("Octo", "04_Papers/30_VLA_and_Foundation_Policies/Octo/README.md"),
        ("OpenVLA", "04_Papers/30_VLA_and_Foundation_Policies/OpenVLA/README.md"),
        ("PI0", "04_Papers/30_VLA_and_Foundation_Policies/PI0/README.md"),
    ]
    for key, path in mappings:
        if key in paper:
            return path
    return "04_Papers/01_Reading_Index.md"


def extract_override_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    if not text:
        return fields
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped in {"---"}:
            continue
        match = re.match(r"-?\s*([A-Za-z_]+|[\u4e00-\u9fff_]+)\s*[:：]\s*(.*)", stripped)
        if not match:
            continue
        key = match.group(1).strip().lower()
        value = match.group(2).strip().strip("`")
        if value:
            fields[key] = value
    return fields


def slugify_paper_title(title: str) -> str:
    cleaned = re.sub(r"https?://\S+", "", title)
    cleaned = re.sub(r"arxiv[:：]?\s*\d{4}\.\d{4,5}(v\d+)?", "", cleaned, flags=re.I)
    cleaned = re.sub(r"[^A-Za-z0-9\u4e00-\u9fff]+", "_", cleaned).strip("_")
    return cleaned[:80] or "specified_paper"


def build_override_paper_slot(ctx: Context, override_text: str) -> tuple[str, str] | None:
    fields = extract_override_fields(override_text)
    if not fields:
        return None
    title = (
        fields.get("title")
        or fields.get("论文")
        or fields.get("paper")
        or fields.get("name")
        or "指定论文"
    )
    arxiv_id = fields.get("arxiv") or fields.get("arxiv_id") or fields.get("arxivid")
    source_url = fields.get("source_url") or fields.get("url") or fields.get("link")
    read_mode = fields.get("read_mode") or fields.get("mode") or fields.get("阅读模式") or "Scan"
    reason = fields.get("reason") or fields.get("why") or fields.get("原因") or "昨晚指定，优先于默认论文队列"
    output = fields.get("output_path") or fields.get("输出位置")
    if not output:
        output = f"04_Papers/99_Overrides/{ctx.today:%Y-%m-%d}_{slugify_paper_title(title)}/README.md"
    display = title
    if arxiv_id:
        display = f"{display} (arXiv:{arxiv_id})"
    elif source_url:
        display = f"{display} ({source_url})"
    body_lines = [
        f"- 候选论文：`{display}`",
        f"- 阅读模式：`{read_mode}`",
        "- 来源：`paper override`，优先于默认论文队列",
        f"- 指定原因：{reason}",
        "- 今日目标：20-40m，抓一句 takeaway + 一个和 mini-stack 的连接",
        f"- 输出位置：`{output}`",
    ]
    if arxiv_id:
        body_lines.append(f"- arXiv：`{arxiv_id}`")
    if source_url:
        body_lines.append(f"- URL：{source_url}")
    return display, "\n".join(body_lines)


def build_paper_slot(ctx: Context, paper_text: str, override_text: str) -> tuple[str, str]:
    override_slot = build_override_paper_slot(ctx, override_text)
    if override_slot:
        return override_slot
    queue = extract_paper_queue(paper_text)
    weekday = ctx.today.weekday()
    if weekday <= 3 and queue:
        paper = queue[0]
        mode = "Scan"
        output = paper_output_path(paper)
        body = "\n".join(
            [
                f"- 候选论文：`{paper}`",
                f"- 阅读模式：`{mode}`",
                "- 今日目标：20-40m，抓一句 takeaway + 一个和 mini-stack 的连接",
                f"- 输出位置：`{output}`",
            ]
        )
        return paper, body
    if weekday == 4:
        paper = "本周 classic paper takeaways 汇总"
        body = "\n".join(
            [
                f"- 候选论文：`{paper}`",
                "- 阅读模式：Review",
                "- 今日目标：汇总本周 3-4 个 takeaway，选 1 个进入项目 backlog",
                "- 输出位置：`04_Papers/01_Reading_Index.md` 或今日 Daily Note",
            ]
        )
        return paper, body
    paper = "周末不强制新论文，主线完成后再补精读"
    body = "\n".join(
        [
            f"- 候选论文：`{paper}`",
            "- 阅读模式：Optional",
            "- 今日目标：不挤占主实验 / 主编码时间",
            "- 输出位置：`04_Papers/01_Reading_Index.md`",
        ]
    )
    return paper, body


def build_inputs(weekly_inputs: List[str], monthly_focus: List[str], theme: str) -> List[str]:
    items = []
    seen = set()
    for source in weekly_inputs + monthly_focus + [theme]:
        c = clip_code(source)
        if not c or c in seen:
            continue
        seen.add(c)
        items.append(c)
        if len(items) >= 3:
            break
    while len(items) < 3:
        items.append("不新开材料，只回接当前主线相关笔记")
    return items[:3]


def classify_inputs(items: List[str]) -> List[str]:
    doc = ""
    src = ""
    video = ""
    for item in items:
        c = clip_code(item)
        if not doc and any(k in c for k in ["论文", "文章", "文档", "paper", "arxiv"]):
            doc = c
        elif not src and any(k in c for k in ["源码", "PR", "代码", "repo"]):
            src = c
        elif not video and any(k in c for k in ["视频", "blog", "B站", "YouTube", "lecture"]):
            video = c
    leftovers = [clip_code(x) for x in items if clip_code(x) not in {doc, src, video}]
    if not doc and leftovers:
        doc = leftovers.pop(0)
    if not video and leftovers:
        video = leftovers.pop(0)
    if not doc:
        doc = "不新开材料，只回接当前主线相关笔记"
    if not src:
        src = "只在卡住时回看相关源码或已有笔记"
    if not video:
        video = "不额外加新视频，优先完成今天主线"
    return [doc, src, video]


def build_exec_tasks(top3: List[str]) -> List[str]:
    return [
        "不切新主题，先完成今天主线",
        f"优先收口：`{top3[0]}`",
        f"输出沉淀：`{top3[1]}`",
        f"最后补齐：`{top3[2]}`",
    ]


def build_summary_next(theme: str, top3: List[str]) -> str:
    return clip_code(top3[1] if top3 else theme)


def replace_section(text: str, heading: str, body: str) -> str:
    body = body.strip() + "\n"
    pattern = re.compile(rf"(^## {re.escape(heading)}\n)(.*?)(?=^## |\Z)", re.S | re.M)
    if pattern.search(text):
        return pattern.sub(rf"\1{body}\n", text, count=1)
    return text.rstrip() + f"\n\n## {heading}\n\n{body}"


def ensure_daily_exists(ctx: Context) -> None:
    if ctx.daily_path.exists():
        return
    template = (ROOT / "99_Templates" / "Daily_Templates.md").read_text(encoding="utf-8")
    iso_year, iso_week, _ = ctx.today.isocalendar()
    rendered = (
        template.replace("{{date:gggg-[W]ww}}", f"{iso_year}-W{iso_week:02d}")
        .replace("{{date:YYYY-MM-DD}}", f"{ctx.today:%Y-%m-%d}")
        .replace("{{date}}", f"{ctx.today:%Y-%m-%d}")
    )
    ctx.daily_path.parent.mkdir(parents=True, exist_ok=True)
    ctx.daily_path.write_text(rendered, encoding="utf-8")


def build_daily_content(ctx: Context) -> str:
    ensure_daily_exists(ctx)
    text = read(ctx.daily_path)
    yesterday_text = read(ctx.yesterday_path)
    weekly_text = read(ctx.weekly_path)
    monthly_text = read(ctx.monthly_path)
    paper_text = read(ctx.paper_index_path)
    paper_override_text = read(ctx.paper_override_path)

    y_tomorrow = extract_tomorrow_line(yesterday_text)
    weekly_mainline = extract_first_unchecked_bullets(extract_section(weekly_text, "本周唯一主线"), 3)
    weekly_tasks = extract_first_unchecked_bullets(extract_section(weekly_text, "本周最低完成线（先保底）"), 6)
    if not weekly_tasks:
        weekly_tasks = extract_first_unchecked_bullets(extract_section(weekly_text, "本周最低完成线"), 6)
    weekly_inputs = extract_first_checked_or_plain_bullets(extract_section(weekly_text, "本周输入材料"), 5)
    monthly_targets = extract_first_unchecked_bullets(extract_section(monthly_text, "本月最低完成线"), 5)
    monthly_focus = extract_first_checked_or_plain_bullets(extract_section(monthly_text, "本月关键产出"), 5)

    hours = time_hours(ctx.time_budget)
    theme = make_theme(ctx, y_tomorrow, weekly_mainline, monthly_targets)
    top3 = build_top3(weekly_tasks, monthly_targets, theme)
    sessions = build_sessions(hours, top3)
    inputs = build_inputs(weekly_inputs, monthly_focus, theme)
    input_slots = classify_inputs(inputs)
    paper_candidate, paper_body = build_paper_slot(ctx, paper_text, paper_override_text)
    if paper_candidate and "不强制新论文" not in paper_candidate:
        input_slots[0] = paper_candidate
    exec_tasks = build_exec_tasks(top3)
    next_line = build_summary_next(theme, top3)

    iso_year, iso_week, _ = ctx.today.isocalendar()
    anchor_body = "\n".join(
        [
            f"- 今天属于哪一周：`{iso_year}-W{iso_week:02d} / {ctx.today:%Y-%m}`",
            f"- 今日主题：`{theme}`",
            f"- 今日硬产出：`{clip_code(top3[0])}` + `{clip_code(top3[1])}`",
            f"- 今日时间预算：`白天 paper slot 20-40m + 晚上主线 {normalize_time_budget(ctx.time_budget)}`",
        ]
    )
    top3_body = "\n".join([f"- [ ] {item}" for item in top3])
    session_body = "\n".join([f"- [ ] {item}" for item in sessions])
    input_body = "\n".join(
        [
            f"- 文档 / 论文：`{input_slots[0]}`",
            f"- 源码 / PR：`{input_slots[1]}`",
            f"- 视频 / blog：`{input_slots[2]}`",
        ]
    )
    exec_body = "\n".join([f"- [ ] {item}" for item in exec_tasks])

    today_section = extract_section(text, "今日总结")
    current_gain = re.search(r"今天最重要的收获：(.*)", today_section)
    current_paper = re.search(r"今日论文 takeaway：(.*)", today_section)
    current_block = re.search(r"今天最大的阻塞：(.*)", today_section)
    gain = current_gain.group(1).strip() if current_gain else ""
    paper_takeaway = current_paper.group(1).strip() if current_paper else ""
    block = current_block.group(1).strip() if current_block else ""
    summary_body = "\n".join(
        [
            f"- 今天最重要的收获：{gain}",
            f"- 今日论文 takeaway：{paper_takeaway}",
            f"- 今天最大的阻塞：{block}",
            f"- 明天唯一主线：`{next_line}`",
        ]
    )

    text = re.sub(
        r"time_budget:.*",
        f"time_budget: {normalize_time_budget(ctx.time_budget)}",
        text,
        count=1,
    )
    text = re.sub(r"date:\s*.*", f"date: {ctx.today:%Y-%m-%d}", text, count=1)
    text = re.sub(r"^# .* Daily Note$", f"# {ctx.today:%Y-%m-%d} Daily Note", text, count=1, flags=re.M)
    text = replace_section(text, "今日锚点", anchor_body)
    text = replace_section(text, "今日 Top 3", top3_body)
    text = replace_section(text, "今日论文槽位", paper_body)
    text = replace_section(text, "今日时间切片", session_body)
    text = replace_section(text, "今日输入", input_body)
    text = replace_section(text, "今日代码 / 实验任务", exec_body)
    text = replace_section(text, "今日总结", summary_body)
    return text


def terminal_summary(ctx: Context, content: str) -> str:
    sections = {
        "今日锚点": extract_section(content, "今日锚点"),
        "今日 Top 3": extract_section(content, "今日 Top 3"),
        "今日论文槽位": extract_section(content, "今日论文槽位"),
        "今日时间切片": extract_section(content, "今日时间切片"),
        "今日输入": extract_section(content, "今日输入"),
    }
    parts = [
        f"date: {ctx.today:%Y-%m-%d}",
        f"daily_note: {ctx.daily_path.relative_to(ROOT)}",
        "",
        "## 今日锚点",
        sections["今日锚点"],
        "",
        "## 今日 Top 3",
        sections["今日 Top 3"],
        "",
        "## 今日论文槽位",
        sections["今日论文槽位"],
        "",
        "## 今日时间切片",
        sections["今日时间切片"],
        "",
        "## 今日输入",
        sections["今日输入"],
    ]
    return "\n".join(parts)


def main() -> int:
    args = parse_args()
    ctx = build_context(parse_date(args.date_str), normalize_time_budget(args.time_budget))
    content = build_daily_content(ctx)
    if not args.dry_run:
        ctx.daily_path.write_text(content, encoding="utf-8")
    print(terminal_summary(ctx, content))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
