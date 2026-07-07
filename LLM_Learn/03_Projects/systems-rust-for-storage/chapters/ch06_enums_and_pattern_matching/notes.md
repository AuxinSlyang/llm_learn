---
type: chapter_notes
project: [[systems-rust-for-storage]]
status: todo
---

# Ch6 Enums and Pattern Matching Notes

## Takeaways

- `enum` 表达一个值的互斥状态：同一时刻只能是其中一个 variant。
- Rust enum 的关键能力不是只有“枚举名”，而是每个 variant 都可以携带自己的 payload，并且 payload 可以有不同类型、不同数量、不同结构。
- `Option<T>` 是 Rust 用 enum 替代 null 的核心类型：`Some(T)` 表示有值，`None` 表示无值；`Option<T>` 和 `T` 是不同类型，必须显式处理空值后才能使用内部的 `T`。
- `match` 是处理 enum 的核心控制流：它根据 pattern 选择分支，并且能在匹配 variant 的同时解构/绑定 payload。
- `match` 是 expression，会产生一个值；每个 arm 的返回类型要统一。arm 可以是单个表达式，也可以是 block，block 的最后一个表达式作为该 arm 的值。
- `match` 必须 exhaustive：所有可能情况都要覆盖。可以显式列出所有 variant，也可以用 catch-all binding 或 `_` 兜底。
- `other` 不是 Rust 关键字，只是普通绑定变量；`_` 才是特殊通配 pattern。`other` 会绑定值并遵循 ownership 规则，`_` 不绑定值。
- Pattern matching 不是普通 `==`。enum variant 匹配主要检查 tag/discriminant，struct/tuple pattern 按结构递归解构，literal/range pattern 会生成比较逻辑。
- `if let` 是“只关心一个 pattern”的简写；`let...else` 是“必须匹配，否则提前退出，并把 payload 留在后续主路径里用”的写法。

## Code / System Mapping

- MiniLSM lookup 可以先用 `Option<Bytes>` 表达：

```rust
fn get(key: &[u8]) -> Option<Bytes> {
    // Some(value): found
    // None: not found
}
```

- 如果需要区分 tombstone 和 not found，`Option<Bytes>` 不够，应使用业务 enum：

```rust
enum GetResult {
    Found(Bytes),
    Deleted,
    NotFound,
}
```

- 后台任务/状态机适合用 enum 表达统一类型下的多种互斥任务：

```rust
enum BackgroundTask {
    Flush { memtable_id: u64 },
    Compact { level: usize, sst_ids: Vec<u64> },
    Stop,
}
```

- 消费任务时用 `match task`，payload 默认可能被 move；只观察任务时用 `match &task` 借用 payload。

```rust
match &task {
    BackgroundTask::Flush { memtable_id } => {
        // memtable_id is borrowed from task
    }
    BackgroundTask::Compact { level, sst_ids } => {
        // level/sst_ids are borrowed
    }
    BackgroundTask::Stop => {}
}
```

## Detailed Summary

### 1. Enum Defines Mutually Exclusive Variants

`enum` 用一个统一类型表达多种互斥形态：

```rust
enum IpAddrKind {
    V4,
    V6,
}

let four = IpAddrKind::V4;
let six = IpAddrKind::V6;
```

`IpAddrKind::V4` 和 `IpAddrKind::V6` 都是 `IpAddrKind` 类型的值。`V4` / `V6` 只是这个类型的不同 variant。

### 2. Enum Variants Can Carry Payloads

传统写法会用 `kind + payload struct`：

```rust
enum IpAddrKind {
    V4,
    V6,
}

struct IpAddr {
    kind: IpAddrKind,
    address: String,
}
```

Rust enum 可以直接把 payload 放进 variant：

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));
```

更进一步，不同 variant 可以携带不同形状的数据：

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}
```

所以 Rust enum 更像编译器支持的 tagged union / sum type：统一类型、互斥 variant、variant 自带 payload，并且 tag 和 payload 始终匹配。

### 3. Common Variant Shapes

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

- `Quit`：不带 payload，unit-like variant。
- `Move { x, y }`：struct-like variant，带命名字段。
- `Write(String)`：tuple-like variant，带一个字段。
- `ChangeColor(i32, i32, i32)`：tuple-like variant，带多个字段。

多个 struct 也能表达类似数据，但会变成多个不同类型；enum 的好处是它们都属于同一个统一类型，方便统一传参、调度和 `match` 分发。

### 4. Option<T> Encodes Presence or Absence

`Option<T>` 概念上是：

```rust
enum Option<T> {
    None,
    Some(T),
}
```

`Some` 不是另一个 enum，而是 `Option<T>` 的一个 variant，同时也像构造函数：

```rust
Some(5) // Option<i32> in a suitable context
```

`T` 是泛型参数。`Option<i32>`、`Option<char>`、`Option<String>` 是不同的具体类型。

`None` 不带 payload，所以有时需要显式类型：

```rust
let absent_number: Option<i32> = None;
```

`Option<T>` 比 null 安全的核心原因是：`Option<T>` 和 `T` 是不同类型。不能直接把 `Option<i8>` 当成 `i8` 做加法：

```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);
// let sum = x + y; // compile error
```

必须先决定 `None` 怎么处理：

```rust
let sum = match y {
    Some(v) => Some(x + v),
    None => None,
};
```

或者用默认值：

```rust
let sum = x + y.unwrap_or(0);
```

### 5. match Selects by Pattern and Extracts Payload

`match` 可以匹配任意支持 pattern 的值，不只 enum。Ch6 重点用 enum 讲，因为 enum + pattern matching 是最核心组合。

```rust
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

`match` 是 expression，可以直接作为函数返回值。每个 arm 是 `pattern => expression`。

带 payload 时，pattern 可以绑定内部值：

```rust
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

match coin {
    Coin::Quarter(state) => {
        println!("State quarter from {state:?}");
        25
    }
    _ => 0,
}
```

`Coin::Quarter(state)` 是 pattern：匹配 `Quarter` variant，并把 payload 绑定到 `state`。

### 6. match with Option<T>

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}
```

语义：

- `Some(5)` -> `Some(6)`
- `None` -> `None`

这是 `Option::map` 的显式版本：

```rust
let y = x.map(|i| i + 1);
```

### 7. Exhaustive Matching and Catch-All Patterns

`match` 必须覆盖所有可能情况：

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
        // missing None => compile error
    }
}
```

可以用 catch-all 兜底：

```rust
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    other => move_player(other),
}
```

`other` 是普通变量名，不是关键字；它绑定所有剩余值。

如果不需要这个值，用 `_`：

```rust
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => (),
}
```

`()` 是 unit value，表示这个分支什么也不做。

### 8. Pattern Matching and Ownership

普通绑定默认遵守 Rust ownership：

```rust
match s {
    other => println!("{other}"),
}
```

如果 `s` 是 `String`，这里会 move。若不想 move，匹配引用：

```rust
match &s {
    other => println!("{other}"),
}
```

结构化 pattern 中绑定字段也可能 move：

```rust
match user {
    User { name, age: _ } => println!("{name}"),
}
```

这里 `name` 会被移出。只想观察时，用 `match &user`。

### 9. match Is Not Ordinary Equality

`match` 不是运行时调用 `==`：

- enum variant pattern 检查 tag/discriminant。
- struct/tuple pattern 按类型结构递归拆字段。
- literal/range pattern 会生成比较逻辑。
- binding pattern 和 `_` 匹配所有值。

因此，解构 struct/enum 不要求实现 `PartialEq`。只有显式写 `if x == y` 时才依赖 `PartialEq`。

### 10. if let and let...else

`if let` 用于只关心一个 pattern：

```rust
let config_max = Some(3u8);

if let Some(max) = config_max {
    println!("max = {max}");
}
```

近似等价于：

```rust
match config_max {
    Some(max) => println!("max = {max}"),
    _ => (),
}
```

`if let ... else` 用于一个主 pattern 加一个统一 fallback：

```rust
if let Coin::Quarter(state) = coin {
    println!("State quarter from {state:?}");
} else {
    count += 1;
}
```

`let...else` 用于必须匹配，否则提前退出，并让成功绑定留在后续主路径：

```rust
fn use_value(x: Option<i32>) -> Option<i32> {
    let Some(v) = x else {
        return None;
    };

    Some(v + 1)
}
```

`match` 最完整、最安全；`if let` 更简洁但失去 exhaustive checking；`let...else` 适合系统代码中的 guard / early return。

## Ch6 One-Line Close

Rust Ch6 的闭环是：用 `enum` 定义互斥状态，用 payload 携带状态相关数据，用 `match` / `if let` / `let...else` 根据 pattern 匹配状态、取出 payload，并让编译器检查遗漏分支。

## Practical Takeaway Ideas

1. `enum` 不是“数字枚举”的窄概念，而是 Rust 表达互斥状态和状态相关数据的基础建模工具。
2. Variant payload 是 Ch6 的核心：状态本身和状态携带的数据绑定在一起，减少 `kind + union/struct` 里 tag 和 payload 不一致的风险。
3. `Option<T>` 是“可能没有值”的显式类型；看到 `Option<Bytes>` 时先问：`None` 在业务里到底表示 not found、deleted，还是 not loaded。
4. 如果 `Option<T>` 的 `None` 语义不够精细，就升级成业务 enum，例如 `Found/Deleted/NotFound`。
5. `match` 是 expression，可以返回值；也可以所有 arm 返回 `()`，当作控制流 statement 使用。
6. `match` 的真正价值是 pattern + payload binding + exhaustive checking，不是替代 `if/else` 的表面语法。
7. Catch-all binding 如 `other` 会绑定并遵循 ownership；`_` 只忽略值，不绑定变量。
8. `match &value` 是系统代码里很常见的只读观察方式，避免把 `String`、`Vec`、payload struct 等非 `Copy` 数据 move 出去。
9. `if let` 适合只关心一个 pattern 的短逻辑；`let...else` 适合 guard / early return，把失败路径提前挡掉，让主路径少嵌套。
10. 对 MiniLSM / miniTable / miniOSS 来说，Ch6 给的是状态机、任务类型、查找结果、错误/缺失路径的基础语言。

Guard 的意思是前置条件检查，不是 mutex guard 的所有权释放语义。典型形态是：如果不是期望状态，立刻 `return` / `break` / `continue` / `panic!`；如果是期望状态，把 payload 绑定出来，后面的代码保持主路径。

```rust
fn handle_lookup(value: Option<Bytes>) -> Option<usize> {
    let Some(bytes) = value else {
        return None;
    };

    Some(bytes.len())
}
```

这里 `let...else` 的作用是把 `None` 这个失败/缺失路径提前挡掉。通过检查后，主路径里 `bytes` 一定存在。
