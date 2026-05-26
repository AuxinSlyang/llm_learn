# Paper Request Workflow

## 目标

支持临时指定第二天的论文，并尽量从 arXiv 抓取基础信息。

这个流程用于回答：

- “明天读这篇论文”
- “我今天学到这里，明天想看某篇 arXiv”
- “帮我从 arXiv 上扒一下这篇论文，明天 paper slot 学”

## 入口语义

用户可以直接说：

```text
明天论文指定：arXiv:2303.04137
```

```text
明天读 Diffusion Policy，帮我从 arXiv 抓一下
```

```text
下周一 paper slot 读 OpenVLA
```

## Codex 应该做什么

1. 解析目标日期。未指定日期时，默认明天。
2. 如果有 arXiv URL / ID / title，优先查 arXiv 官方页面或 API。
3. 创建或更新：

```text
04_Papers/99_Overrides/YYYY-MM-DD.md
```

4. 如果能确认论文身份，创建对应论文目录：

```text
04_Papers/<category>/<paper_slug>/README.md
```

5. 在 override 中写入：

- title
- arxiv
- source_url
- read_mode
- reason
- output_path

## arXiv 抓取内容

优先抓：

- title
- authors
- abstract
- arXiv ID
- PDF URL
- published / updated date
- categories
- project page / code URL if obvious

不要默认全文复制论文内容。笔记中只保留摘要、链接、阅读问题和个人 takeaway。

## 与 start-my-day 的关系

第二天 `start-my-day` 会读取：

```text
04_Papers/99_Overrides/YYYY-MM-DD.md
```

如果存在 active override，则 `今日论文槽位` 优先使用指定论文；否则回到 `04_Papers/01_Reading_Index.md` 的默认队列。

