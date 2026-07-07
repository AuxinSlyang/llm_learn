---
type: chapter_notes
project: mini-lsm
chapter: 02_environment_setup
title: Environment Setup
source_pages: p9-p10
status: done
---

# Environment Setup Notes

## Summary

- 本章是环境准备章节，目标是确认 starter code、Rust toolchain、课程工具和测试命令。
- 官方流程：clone `skyzh/mini-lsm`，进入 `mini-lsm-starter`，执行 `cargo x install-tools`，再按章节 copy test 并运行 `cargo x scheck`。
- dev2 当前已完成基础环境：repo 位于 `~/workspace/learn/mini-lsm/mini-lsm-starter`，Rust/Cargo 可用，Week 1 Day 1 测试已复制。
- 本地 Mac 负责阅读和笔记；dev2 负责编译、测试和代码实现。

## Key Concepts

- `mini-lsm-starter`: 学习实现入口，包含未完成 starter code。
- `cargo x install-tools`: 安装课程辅助工具。
- `cargo x copy-test --week 1 --day 1`: 复制指定章节测试。
- `cargo x scheck`: 运行课程检查。
- 测试不等于完整正确性；后续章节可能暴露前面实现的问题。

## MiniLSM Code Mapping

- 当前 dev2 状态：
  - repo: `~/workspace/learn/mini-lsm/mini-lsm-starter`
  - head: `427c6cc`
  - `cargo 1.96.1`
  - `rustc 1.96.1`
  - Week 1 Day 1 tests copied: `src/tests/week1_day1.rs`
- 目前应阅读 starter/tests，不直接跳到完整 solution。

## RocksDB / Real System Mapping

- 本章没有 RocksDB 机制内容，只建立工程入口。
- 后续每个 MiniLSM 章节都要补一条 RocksDB 对应对象或链路映射。
