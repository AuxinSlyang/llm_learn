# Paper Overrides

这里用于指定某一天 `start-my-day` 必须优先安排的论文。

默认论文来自 `04_Papers/01_Reading_Index.md`。如果这里存在目标日期文件：

```text
04_Papers/99_Overrides/YYYY-MM-DD.md
```

当天的 `start-my-day` 会优先使用这个 override，而不是默认队列。

## 使用场景

晚上学习时突然对某篇论文感兴趣，可以让 Codex 写入明天 override：

```text
明天论文指定：arXiv:2303.04137，帮我从 arXiv 抓一下，明天 paper slot 读它。
```

或者：

```text
明天读 Diffusion Policy，不读默认队列。
```

## 文件格式

```markdown
---
type: paper_override
date: 2026-05-21
status: active
---

# Paper Override: 2026-05-21

- title:
- arxiv:
- source_url:
- read_mode: Scan
- reason:
- output_path:
```

## 规则

- override 只影响指定日期的 paper slot。
- override 不改变晚上主线学习计划。
- 如果有 arXiv URL / ID，优先抓取 arXiv 官方元信息和 PDF 链接。
- 如果网络不可用，先保留 URL / ID，第二天计划仍会引用这篇论文。

