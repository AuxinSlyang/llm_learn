---
type: systems_note
title: How to do distributed locking
author: Martin Kleppmann
published: 2016-02-08
url: https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
track: Systems Thinking / Distributed Locking / Correctness / Robot Runtime
read_mode: Structured Systems Read
status: queued_today
created: 2026-06-22
---

# How to do distributed locking

## 今日定位

这篇不是泛泛的 Redis / Redlock 争论，而是一个非常适合放进 Systems Thinking 支撑线的判断框架：

```text
distributed lock
-> lease / timing assumption / fencing token
-> correctness vs efficiency
-> AI Infra / Robot Runtime 的资源保护和任务调度
```

## 今天只回答 5 个问题

1. 一个 lock 是为了 efficiency，还是为了 correctness？
2. lease 过期、GC pause、网络延迟、时钟跳变分别会造成什么安全问题？
3. fencing token 解决的到底是哪类 stale client 问题？
4. Redlock 的核心争议是 Redis，还是 timing assumption / monotonic fencing token？
5. 这个模型如何迁移到 AI Infra / Robot Runtime？

## 结构化阅读路径

- `What are you using that lock for?`
  - 先区分 efficiency lock 和 correctness lock。
- `Protecting a resource with a lock`
  - 看懂 lease 过期后 stale client 仍写入资源的问题。
- `Making the lock safe with fencing`
  - 抓住 fencing token：每次获取锁都拿到单调递增 token，下游资源拒绝旧 token。
- `Using time to solve consensus`
  - 抓住时间假设：网络延迟、进程 pause、时钟误差都不能作为 safety 前提。
- `Conclusion`
  - 整理：best-effort lock 可以简单；correctness lock 需要 consensus / transaction / fencing。

## AI / Robot 迁移问题

### AI Infra

- GPU job scheduler 中的资源租约：如果 scheduler 认为 lease 过期，旧 worker 是否还能写 checkpoint？
- Distributed training checkpoint：多个 trainer / retry worker 写同一个 checkpoint path 时，是否有 fencing token 或 version guard？
- Serving leader election：如果旧 leader 被 pause 后恢复，是否还能接受请求或写路由状态？

### Robot Runtime

- Robot task ownership：一个 robot / controller 的任务 lease 过期后，旧 controller 是否还能继续下发 action？
- Safety watchdog：timeout 只是 failure detector，不等于旧 actor 一定停止。
- Episode / replay log：多个 recorder 写同一 episode / metadata 时，是否有 monotonic run id / fencing token？
- Fleet coordination：多机器人任务分配不能只靠本地时钟判断 ownership。

## 待读后输出

- 一句话 takeaway：
- 系统问题：
- 关键抽象：
- 失败模式：
- AI / Robot 迁移：
- 仍需验证：

## 后续沉淀位置

读完后将可迁移 insight 精炼到：

`/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/08_Insights/Systems/runtime/`
