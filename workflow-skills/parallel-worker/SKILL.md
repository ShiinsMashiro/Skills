---
name: parallel-worker
description: This skill should be used when the user wants to "并行执行", "多任务", "parallel", "任务分割", "task split", "隔离执行", "isolated", "context isolation", "worker pool", "多线程", "并行处理" or when skill-manager needs to distribute tasks across multiple workers with context isolation.
version: 1.0.0
---

# Parallel Worker (并行任务处理器)

这是一个并行任务处理器，支持任务分割、上下文隔离、物理隔离执行。由skill-manager调度。

## When This Skill Applies

This skill activates when:
- User has multiple independent tasks to run in parallel
- Large task needs to be split into smaller pieces
- Tasks need to run in isolated contexts
- Need parallel processing for speed
- skill-manager dispatches this for multi-task scenarios

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   SKILL MANAGER                              │
│              (任务分发中央调度)                               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               PARALLEL WORKER                               │
│         (任务分割 + 上下文隔离 + 物理隔离)                    │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │  Worker 1  │  │  Worker 2   │  │  Worker N   │       │
│  │ Context A  │  │ Context B   │  │ Context N   │       │
│  │  Isolated  │  │  Isolated   │  │  Isolated   │       │
│  └─────────────┘  └─────────────┘  └─────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

## Features

### 1. 任务分割 (Task Splitting)
```python
# 输入: 大任务
large_task = "分析这1000个基因的表达数据"

# 自动分割成:
tasks = [
    "分析基因1-200",
    "分析基因201-400",
    "分析基因401-600",
    "分析基因601-800",
    "分析基因801-1000"
]
```

### 2. 上下文隔离 (Context Isolation)
```python
# 每个worker有独立的上下文
worker_1 = Worker(context={"task": "A", "data": [...]})
worker_2 = Worker(context={"task": "B", "data": [...]})

# 上下文不会相互污染
```

### 3. 物理隔离 (Physical Isolation)
```python
# 可以指定运行环境
worker_1.run(environment="python3.9")
worker_2.run(environment="python3.10")
worker_3.run(environment="r-base")

# 或使用容器隔离
worker_1.run(container="data-analysis:v1")
```

### 4. 并行执行 (Parallel Execution)
```python
# 同时启动多个worker
results = await parallel_run(
    workers=[w1, w2, w3, w4],
    max_parallel=4  # 最大并行数
)
```

## Task Configuration

```json
{
  "task_id": "batch_001",
  "split_strategy": "auto",  // auto, manual, chunk
  "chunk_size": 100,
  "isolation": {
    "type": "context",  // context, process, container
    "timeout": 3600
  },
  "workers": [
    {
      "id": "worker_1",
      "task": "处理前25%",
      "context": {...}
    }
  ]
}
```

## Usage Examples

### Example 1: 并行处理多个独立任务
```
User: "帮我查一下AAPL, MSFT, GOOGL这三只股票的信息"
Skill-Manager → Parallel-Worker:
  → 分割成3个独立查询任务
  → 分配给3个workers并行执行
  → 汇总结果返回
```

### Example 2: 大任务分割
```
User: "分析这500个蛋白质的结构"
Skill-Manager → Parallel-Worker:
  → 分割成10个任务，每个50个蛋白质
  → 启动10个workers并行处理
  → 合并所有结果
```

### Example 3: 隔离环境执行
```
User: "用不同版本的Python运行这个测试"
Skill-Manager → Parallel-Worker:
  → 创建3个隔离worker
  → 分别用Python 3.8, 3.9, 3.10运行
  → 收集对比结果
```

## Worker Types

| Type | Isolation Level | Use Case |
|------|----------------|----------|
| `light` | 最低 | 快速简单任务 |
| `context` | 中等 | 独立上下文 |
| `process` | 高 | 进程隔离 |
| `container` | 最高 | 完全隔离环境 |

## Commands

| Command | Description |
|---------|-------------|
| `parallel <tasks>` | 并行执行多个任务 |
| `split <task> into <n>` | 分割任务 |
| `isolate <task>` | 隔离执行 |
| `workers` | 查看可用workers |
| `status` | 查看所有任务状态 |

## Integration with Skill-Manager

```
Skill-Manager 分析任务
    │
    ├──→ 单一任务 → 直接执行
    │
    └──→ 多任务/大任务 → Parallel-Worker
                              │
                              ├──→ 任务分割
                              ├──→ 创建Workers
                              ├──→ 并行执行
                              └──→ 结果汇总
```

## Output Format

```json
{
  "status": "completed",
  "total_tasks": 10,
  "completed": 10,
  "failed": 0,
  "results": [...],
  "execution_time": "45.2s"
}
```

---

*This skill enables parallel processing with task splitting and context isolation.*
