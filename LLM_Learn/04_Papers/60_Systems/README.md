# Systems Papers

## 定位

这里收纳经典存储系统、分布式系统、分布式计算和 AI Infra systems 论文。

读法不是完整转向分布式系统，而是服务：

```text
AI Infra / LLM serving / distributed training
+ Robot Runtime / logging / replay / data loop
```

## 阅读原则

每篇只回答四个问题：

1. 它解决了什么系统问题？
2. 它提出了什么稳定抽象？
3. 它的失败边界和 trade-off 是什么？
4. 它如何迁移到 AI Infra / Robot Runtime？

## 初始候选

### Storage / Distributed Systems

- Martin Kleppmann, `How to do distributed locking`
- GFS
- Bigtable
- Dynamo
- Spanner
- Raft
- ZooKeeper

### Distributed Computing

- MapReduce
- Spark
- FlumeJava
- Naiad
- Ray

### Cluster / Serving / Scheduling

- Borg
- Omega
- Kubernetes design notes
- TensorFlow / Parameter Server systems papers
- vLLM / PagedAttention

## 当前边界

- 不作为 `start-my-day` 默认 paper slot，除非当天主题和 AI Infra / Robot Runtime 强相关。
- 不替代 `20_Robot_Learning/`、`30_VLA_and_Foundation_Policies/`。
- 不放内部业务材料；只放可长期复用的公开论文或整理后的抽象笔记。
