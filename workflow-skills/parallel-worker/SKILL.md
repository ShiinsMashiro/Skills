---
name: parallel-worker
description: |
  并行任务处理器 - 遵循 s04/s09 原理。
  子智能体独立上下文 (s04)，团队协作 (s09)。
version: 2.0.0
---

# Parallel Worker (并行处理器)

**遵循 s04 隔离 + s09 团队原理**

> *"大任务拆小, 每个小任务干净的上下文"* + *"任务太大一个人干不完, 要能分给队友"*

## 核心原理

### s04: 子智能体隔离

```
大问题: "分析 1000 个基因"

拆分成 4 个子任务:
- 子任务 1: 基因 1-250 (独立 context[])
- 子任务 2: 基因 251-500 (独立 context[])
- 子任务 3: 基因 501-750 (独立 context[])
- 子任务 4: 基因 751-1000 (独立 context[])

每个子智能体:
- 有独立 messages[]
- 不污染主对话
- 完成后合并结果
```

### s09: 团队协作

```
1 个 agent 干不完 → 分给 N 个 agent

team = [
  agent_1: {"task": "部分A", "context": {...}},
  agent_2: {"task": "部分B", "context": {...}},
  agent_N: {"task": "部分N", "context": {...}}
]

并行执行 → 汇总结果
```

---

## 隔离级别

| 级别 | 隔离类型 | 使用场景 |
|------|----------|----------|
| `context` | 独立 messages[] | 独立任务 |
| `process` | 独立进程 | 内存隔离 |
| `worktree` | 独立目录 | 代码隔离 |

---

## 执行流程

```
1. 接收大任务
       ↓
2. 分析拆分 (可用 s03 TodoWrite)
       ↓
3. 创建子智能体 (每个独立 context)
       ↓
4. 并行执行
       ↓
5. 汇总结果
       ↓
6. 清理隔离
```

---

## 任务分割

```python
# 自动分割策略
def split(task, strategy="auto"):
    if strategy == "auto":
        # 按数量均分
        return chunks(total, num_workers)
    elif strategy == "dependency":
        # 按依赖关系分
        return topological_split()
```

---

## 命令

| 命令 | 功能 |
|------|------|
| `parallel <tasks>` | 并行执行 |
| `split <task> into N` | 分割任务 |
| `isolate <task>` | 隔离执行 |
| `workers` | 查看 workers |

---

## 设计原则

- **s04**: 子智能体独立 context
- **s09**: 团队分工协作
- **隔离**: 不污染主对话

---

*This skill follows s04 + s09: 隔离 + 团队协作.*
