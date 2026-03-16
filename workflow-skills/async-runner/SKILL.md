---
name: async-runner
description: This skill should be used when the user wants to "异步执行", "后台运行", "定时任务", "schedule", "background task", "cron job", "延迟执行", "async", "run in background", "定时", or wants to execute commands asynchronously or schedule tasks using Claude's config directory.
version: 1.0.0
---

# Async Runner (异步执行器)

这是一个异步任务执行器，可以在后台运行命令、定时执行任务、延迟执行。

## When This Skill Applies

This skill activates when the user wants to:
- Run commands in background (异步后台运行)
- Schedule tasks to run later (定时执行)
- Execute long-running tasks without blocking (长时间任务)
- Set up cron-like scheduled tasks (定时任务)
- Run multiple tasks in parallel (并行执行)

## Features

### 1. 后台运行 (Background Execution)
```bash
# 在后台运行Python脚本
run python script.py

# 后台运行并实时输出
run --watch python app.py
```

### 2. 定时执行 (Scheduled Execution)
```bash
# 5分钟后执行
delay 5m python backup.py

# 每天下午3点执行
schedule 15:00 python daily_report.py
```

### 3. 定时任务 (Cron-like)
```bash
# 每小时执行
cron 0 * * * python hourly_task.py

# 每天凌晨2点
cron 0 2 * * python nightly_backup.py
```

### 4. 并行执行 (Parallel Execution)
```bash
# 并行运行多个任务
parallel python task1.py && python task2.py && python task3.py
```

## Configuration

任务配置存储在:
`C:\Users\黄涂健隆\Desktop\ClaudeCode\disc-generator\async_tasks\`

```
async_tasks/
├── config.json          # 全局配置
├── tasks/              # 任务脚本
│   ├── backup.py
│   ├── report.py
│   └── monitor.py
├── schedules/          # 定时任务配置
│   ├── hourly.json
│   └── daily.json
└── logs/               # 执行日志
    └── task_*.log
```

## Task Configuration Format

```json
{
  "name": "backup_task",
  "command": "python backup.py",
  "schedule": "0 2 * * *",
  "enabled": true,
  "timeout": 3600,
  "notify_on_complete": true
}
```

## Usage Examples

### 简单后台运行
```
User: "在后台运行这个Python脚本"
Bot: 启动后台进程，返回PID
```

### 延迟执行
```
User: "10分钟后提醒我开会"
Bot: 设置定时器，10分钟后发送提醒
```

### 定时任务
```
User: "每天早上9点执行数据同步"
Bot: 创建定时任务配置
```

### 查看运行中的任务
```
User: "显示正在运行的任务"
Bot: 列出所有后台进程
```

## Commands

| Command | Description |
|---------|-------------|
| `run <command>` | 后台运行命令 |
| `run --watch <command>` | 后台运行并监控输出 |
| `delay <time> <command>` | 延迟执行 |
| `schedule <time> <command>` | 定时执行 |
| `cron <schedule> <command>` | Cron定时任务 |
| `tasks` | 列出所有任务 |
| `kill <task_id>` | 停止任务 |
| `logs <task_id>` | 查看任务日志 |

## Time Format

| Format | Example | Description |
|--------|---------|-------------|
| `5m` | 5分钟后 | 分钟 |
| `1h` | 1小时后 | 小时 |
| `14:00` | 今天14:00 | 具体时间 |
| `tomorrow 9:00` | 明天9点 | 明天 |

## Integration with Claude Code

使用 `run_in_background` 参数执行：
```python
# 在后台运行
run_in_background=True
# 命令会在后台执行，不阻塞主对话
```

---

*This skill enables asynchronous task execution and scheduling capabilities.*
