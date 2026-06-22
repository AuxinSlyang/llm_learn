# Systems Insights

## 定位

这里放可长期复用的系统思考，重点是经典存储系统、分布式系统和分布式计算系统中能迁移到 AI Infra / Robot Runtime 的抽象。

默认不是业务日志，也不是完整课程笔记。

## 收录标准

一条内容适合放进来，需要至少满足一个条件：

- 能解释 AI training / serving / checkpoint / scheduling 的系统问题。
- 能解释 robot runtime / logging / replay / watchdog / failure handling。
- 能解释 robot learning data loop 中的数据版本、可复现、可观测性或容错。
- 能从具体系统机制中抽象出可迁移原则。

## 推荐模板

```markdown
# 主题

## 系统问题

## 关键抽象

## 失败模式

## AI / Robot 迁移

## 仍需验证
```

## 边界

- 不放 TokaDB 主业务任务。
- 不放平台治理执行记录。
- 不放未整理的排障流水账。
- 不把这里变成和 Robot Learning Full-Stack 平行竞争的新主线。

## 初始分类

- `storage/`：WAL、LSM、checkpoint、snapshot、replication、consistency。
- `distributed-compute/`：MapReduce、Spark、Ray、scheduler、straggler、lineage。
- `runtime/`：backpressure、tail latency、timeout、fallback、watchdog、observability。
