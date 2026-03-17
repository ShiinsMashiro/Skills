---
name: async-runner
description: |
  异步执行器 - 遵循 s08 原理：慢操作丢后台，agent 继续想下一步。
  后台线程跑命令，完成后注入通知。
version: 2.0.0
---

# Async Runner (异步执行器)

**遵循 s08 原理：慢操作丢后台**

> *"慢操作丢后台, agent 继续想下一步"*

## 核心原理

### s08: 后台不阻塞

```
传统方式 (错):
  1. 执行命令 (等 10 分钟)
  2. 阻塞
  3. 完成才能继续

正确方式 (对):
  1. 后台执行命令
  2. agent 继续想下一步
  3. 完成后注入通知
```

---

## 执行模式

### 1. 前台 (阻塞)

```python
result = run("python train.py")  # 等完成
# 10分钟后...
```

### 2. 后台 (非阻塞)

```python
run_in_background("python train.py")  # 立即返回
# agent 继续下一步
# 完成时注入通知
```

---

## 任务类型

| 类型 | 说明 | 例子 |
|------|------|------|
| **fire-and-forget** | 丢后台不管 | 启动服务 |
| **delayed** | 延迟执行 | 10分钟后提醒 |
| **scheduled** | 定时执行 | 每天9点 |
| **cron** | Cron 任务 | 每小时备份 |

---

## 通知机制

当后台任务完成时：

```python
# 自动注入到当前对话
{
  "type": "tool_result",
  "content": "✅ 后台任务完成: train.py\n结果: 准确率 95%"
}
```

---

## 命令

| 命令 | 功能 |
|------|------|
| `run <cmd>` | 后台运行 |
| `delay <time> <cmd>` | 延迟执行 |
| `schedule <time> <cmd>` | 定时执行 |
| `cron <expr> <cmd>` | Cron 任务 |
| `tasks` | 查看任务 |

---

## 设计原则 (来自 s08)

- **丢后台**: 慢操作不阻塞
- **继续下一步**: agent 不等待
- **通知注入**: 完成后反馈

---

*This skill follows s08: 慢操作丢后台, agent 继续想下一步.*
