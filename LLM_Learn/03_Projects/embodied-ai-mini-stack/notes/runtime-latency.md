# Runtime Latency Notes

## 目标

建立 `感知 -> 决策 -> 执行` 链路的 latency budget 视角。

## 最小链路

```text
sensor capture
-> preprocessing
-> model / policy inference
-> postprocess
-> action validation
-> command send
-> robot / simulator step
```

## 指标

- sensor frame interval
- preprocessing latency
- policy inference latency
- postprocess latency
- command latency
- end-to-end loop latency
- jitter
- timeout count

## 和 JD 的关系

这个模块对齐：

- 模型部署与优化
- 降低系统延迟
- 确保感知-决策-执行链路高频、稳定响应
- 异常处理和 fallback
