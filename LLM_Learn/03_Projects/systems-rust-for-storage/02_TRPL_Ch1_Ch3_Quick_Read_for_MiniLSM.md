---
type: quick_read
project: [[systems-rust-for-storage]]
track: Rust / MiniLSM
status: active
created: 2026-07-01
source: materials/The Rust Programming Language.pdf
---

# TRPL Ch1-Ch3 Quick Read for MiniLSM

## 范围

本地 PDF：

```text
/Users/bytedance/.openclaw/workspaces/llm-learner/LLM_Learn/03_Projects/systems-rust-for-storage/materials/The Rust Programming Language.pdf
```

PDF 页码：

- Ch1 Getting Started：第 8 页开始。
- Ch2 Programming a Guessing Game：第 22 页开始。
- Ch3 Common Programming Concepts：第 43 页开始。
- Ch4 Understanding Ownership：第 77 页开始。

今天只快速看 Ch1-Ch3，Ch4 ownership 晚上按 MiniLSM 代码需求补。

## Ch1: Getting Started

只抓这些：

- `rustc` 可以单文件编译，但真实项目基本用 `cargo`。
- `cargo new` 创建项目。
- `Cargo.toml` 描述 package、edition、dependencies。
- `src/main.rs` 是默认二进制入口。
- `cargo build` 编译，`cargo run` 编译并运行，`cargo check` 快速检查。

和 MiniLSM 的关系：

- MiniLSM 不是单文件 Rust，而是 Cargo workspace / crate 项目。
- 今天在 dev2 上主要用 `cargo x scheck`，本质是封装了 `fmt/check/test/clippy`。

## Ch2: Programming a Guessing Game

旧笔记已经学过，今天只复习：

- `let mut guess = String::new()`：默认不可变，需要 `mut` 才能修改。
- `read_line(&mut guess)`：把可变引用传给函数，让函数写入这个变量。
- `Result`：可能成功，也可能失败。
- `match`：按不同返回值做分支。
- `loop` / `continue` / `break`：测试/CLI/服务循环都会见到。
- shadowing：同名变量可以重新绑定不同类型。

和 MiniLSM 的关系：

- `Result<()>` 出现在 `MemTable::put`，后续 WAL 写入可能失败。
- `match` / `if let` 会用于处理 `Option` / `Result`。
- `mut` 和引用是理解 `&self` / `&mut self` 的前置。

## Ch3: Common Programming Concepts

只抓这些：

### Variables and Mutability

- Rust 变量默认不可变。
- `let mut x` 才能修改。
- shadowing 是重新绑定，不等于修改原变量。

MiniLSM 对应：

- `let estimated_size = key.len() + value.len();`
- `let mut snapshot = guard.as_ref().clone();`

### Data Types

- Rust 静态类型，编译期要知道类型。
- 整数类型如 `usize` 常用于长度、下标、大小。
- tuple / array 了解即可。

MiniLSM 对应：

- `id: usize`
- `approximate_size: Arc<AtomicUsize>`
- `key: &[u8]`
- `value: &[u8]`

### Functions

- `fn name(args) -> ReturnType`
- 最后一行没有分号可以作为返回值。
- 有分号通常表示语句，不返回该表达式的值。

MiniLSM 对应：

```rust
pub fn create(id: usize) -> Self
pub fn get(&self, key: &[u8]) -> Option<Bytes>
pub fn put(&self, key: &[u8], value: &[u8]) -> Result<()>
```

### Control Flow

- `if` 是表达式。
- `loop`、`while`、`for` 都会用到。
- 今天只需要能读懂测试里的顺序控制。

MiniLSM 对应：

- `if let Some(ref wal) = self.wal { ... }`
- `for memtable in snapshot.imm_memtables.iter() { ... }`

## 今天暂时不深挖

- macro 细节。
- `const` / `static` 细节。
- tuple / array 全语法。
- Unicode / char 细节。
- Ch4 ownership 全章细节。
- 高级 trait / lifetime / async / unsafe。

## 读完 Ch1-Ch3 后马上进入 MiniLSM

今天要把这些概念落到：

```rust
pub struct MemTable {
    map: Arc<SkipMap<Bytes, Bytes>>,
    wal: Option<Wal>,
    id: usize,
    approximate_size: Arc<AtomicUsize>,
}
```

先能解释字段，再读 tests，再写 `create/get/put`。
