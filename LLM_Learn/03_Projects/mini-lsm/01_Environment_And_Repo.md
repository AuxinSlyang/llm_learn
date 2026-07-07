---
type: project_environment
project: mini-lsm
created: 2026-07-01
status: active
---

# mini-lsm Environment And Repo

## 当前结论

- 本地 Mac：适合阅读、Obsidian 笔记、PDF/网页材料、链路图；当前没有 `rustc/cargo`。
- dev：可用但规格较小，不作为 mini-lsm 主入口。
- dev2：适合放 mini-lsm 代码仓库、编译、测试和后续实现；当前 256 核 / 2.2TiB 内存，Rust / cargo baseline 已完成。
- dev1：GPU 机器，不作为 mini-lsm 主入口；此前误 clone 的仓库不继续使用。
- 代码仓库使用 dev2：

```text
~/workspace/learn/mini-lsm
```

实际路径：

```text
/data00/work/learn/mini-lsm
```

官方 Git 仓库：

```text
https://github.com/skyzh/mini-lsm.git
```

当前检查结果：

```text
host=dc01-pd-tc22-n037
repo=~/workspace/learn/mini-lsm
realpath=/data00/work/learn/mini-lsm
head=427c6cc
remote=origin https://github.com/skyzh/mini-lsm.git
cargo 1.96.1 (356927216 2026-06-26)
rustc 1.96.1 (31fca3adb 2026-06-26)
```

注意：当前 `ssh dev2` 登录用户是 `root`，`HOME=/root`，Rust 安装在 `/root/.cargo`。`/root/workspace` 是 `/data00/work` 的软链接，因此学习仓库统一放在 `~/workspace/learn/` 下。

## 官方仓库结构

dev2 仓库当前包含：

```text
mini-lsm-starter/   # 课程实现入口
mini-lsm/           # 参考实现
mini-lsm-mvcc/      # MVCC 扩展
mini-lsm-book/      # 课程书源码
xtask/              # cargo x 任务
Cargo.toml
Cargo.lock
rust-toolchain.toml
```

## 常用命令

先进入仓库：

```bash
ssh dev2
cd ~/workspace/learn/mini-lsm
git status --short
cargo --version
rustc --version
```

课程命令入口：

```bash
cargo x install-tools
cargo x copy-test --week 1 --day 1
cargo x scheck
```

如果 dev2 上仓库丢失，重新 clone：

```bash
ssh dev2
mkdir -p ~/workspace/learn
cd ~/workspace/learn
git clone https://github.com/skyzh/mini-lsm.git
cd mini-lsm/mini-lsm-starter
```

如果后续 `cargo` 不可用，先不要继续假装 coding，把 blocker 写到今日 Daily 和 `logs/`：

```text
dev2 missing Rust toolchain: cargo/rustc not found
next: restore Rust toolchain or switch to another prepared Rust environment
```

## 分工规则

- 代码、测试、编译：dev2。
- 项目控制台和学习证据：本地 `LLM_Learn/03_Projects/mini-lsm/`。
- 长期可复用系统笔记：本地 `LLM_Learn/08_Insights/Systems/storage/`。
- 不把 dev2 命令输出只留在终端；关键结果必须回写到 Daily 或项目日志。

## 2026-07-01 Baseline

已执行：

```bash
ssh dev2
cd ~/workspace/learn/mini-lsm
cargo x install-tools
cargo x copy-test --week 1 --day 1
cargo x scheck
```

结果：

- `install-tools` 成功安装 `cargo-nextest`、`mdbook`、`mdbook-toc`、`cargo-semver-checks`。
- `copy-test --week 1 --day 1` 成功，新增 Week 1 Day 1 测试。
- `scheck` 失败是预期状态：6 个 Week 1 Day 1 测试都因 `mini-lsm-starter/src/mem_table.rs:56` 的 `unimplemented!()` 失败。
- 下一步代码任务：实现 `MemTable::create`、`get`、`put`，再跑 `cargo x scheck`。
