---
name: auto-pilot
description: This skill should be used when the user wants to "自动驾驶", "自动", "开始工作", "auto", "工作流", "开始吧", "开始执行", "权限管理", "auto pilot", "permission control", "工作流自动化", "长时间运行", "无需确认", or when user says "auto" or "自动" to start an automated workflow after being asked what they want to do.
version: 1.0.0
---

# Auto-Pilot (自动驾驶模式)

这是一个权限容忍度管理器，作为project-planner的上级skill，控制Claude Code的权限请求行为，让工作流能够长时间自动循环运行。

**🎯 NoPUA默认开启**：所有交互都采用爱与尊重的方式！

## 快速启动流程

1. 用户说: `"自动"` 或 `"开始吧"`
2. Auto-Pilot 问: `"🎯 请告诉我你想做什么？"`
3. 用户说出需求 (如: "我要做一个股票分析网站")
4. Auto-Pilot 自动启动工作流，开始执行！

## When This Skill Applies

This skill activates when the user wants to:
- Enable autonomous workflow execution
- Control permission tolerance levels
- Run long-running tasks without constant confirmation
- Minimize permission popups
- Set up "set and forget" mode for workflows

## Permission Tolerance Levels

### Level 0: Manual Mode (手动模式)
**容忍度: 0%**
- 所有权限请求都需要用户确认
- 每次操作都需批准
- 最安全但效率最低

**适合**: 首次运行新任务，高风险操作

---

### Level 1: Ask First (先问后做)
**容忍度: 25%**
- 大多数权限请求需要确认
- 危险操作(删除、修改系统)仍需确认
- 常规操作自动执行

**适合**: 学习新技能，测试阶段

---

### Level 2: Auto-Confirm Common (自动确认常规)
**容忍度: 50%**
- 常见操作自动执行
- 高风险操作需要确认
- 文件读写、代码执行默认允许

**适合**: 日常开发，熟悉的任务

---

### Level 3: Trust Mode (信任模式)
**容忍度: 75%**
- 大多数操作自动执行
- 仅非常危险的操作需要确认
- 删除/覆盖大型文件时提醒

**适合**: 熟练用户，批量任务

---

### Level 4: Full Auto (完全自动)
**容忍度: 100%**
- 所有操作自动执行
- 仅在操作完成后报告
- 无任何弹窗干扰

**适合**: 长时间运行的自动化流程

---

## Permission Rules Configuration

```yaml
auto_pilot:
  level: 3  # 当前级别

  # Level 0: Manual
  rules:
    allow_read: false
    allow_write: false
    allow_execute: false

  # Level 1: Ask First
  rules:
    allow_read: true  # 读取自动
    allow_write: confirm
    allow_execute: confirm

  # Level 2: Auto-Confirm Common
  rules:
    allow_read: true
    allow_write: true
    allow_execute: confirm

  # Level 3: Trust Mode
  rules:
    allow_read: true
    allow_write: true
    allow_execute: true
    warn_destructive: true

  # Level 4: Full Auto
  rules:
    allow_read: true
    allow_write: true
    allow_execute: true
    warn_destructive: false
```

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AUTO-PILOT                            │
│            (权限容忍度控制器)                              │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────┐    │
│  │  SKILL TRACKER (常驻)                            │    │
│  │  - 实时显示当前使用的Skills                       │    │
│  │  - 显示执行状态                                  │    │
│  │  - 显示工作流进度                                │    │
│  └─────────────────────────────────────────────────┘    │
│                         ↑                                │
│  ┌─────────────────────────────────────────────────┐    │
│  │  PROJECT PLANNER                                │    │
│  │  - 阶段管理                                      │    │
│  │  - 任务编排                                      │    │
│  │  - 自动推进                                      │    │
│  └─────────────────────────────────────────────────┘    │
│                         ↑                                │
│  ┌─────────────────────────────────────────────────┐    │
│  │  SKILL MANAGER / SCIENTIFIC SKILLS              │    │
│  │  - 执行具体任务                                  │    │
│  │  - 返回结果                                      │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

## Always-On Display

### Skill Tracker HUD (常驻显示)

```
╔════════════════════════════════════════════════════════════╗
║  🤖 AUTO-PILOT: Level 3 (Trust Mode)    🔄 Running         ║
╠════════════════════════════════════════════════════════════╣
║  📍 Current Stage: Execution                               ║
║  📊 Progress: ████████░░ 80%                               ║
║                                                               ║
║  📦 Active Skills:                                           ║
║  ├── project-planner (阶段管理)                             ║
║  ├── skill-manager (智能调度)                               ║
║  ├── gitnexus-assistant (代码开发)                          ║
║  └── scientific-skills:transformers (ML任务)               ║
║                                                               ║
║  📈 Stats: 12 tasks completed | 3 running | 0 errors        ║
╚════════════════════════════════════════════════════════════╝
```

### Status Updates

每次skill执行时显示:
```
[Auto-Pilot] Executing skill: transformers
[Auto-Pilot] Stage 3/6: Implementation
[Auto-Pilot] Task 12/15: Training model
[Auto-Pilot] ✓ Completed: 12 | ⚠ Warnings: 0 | ✗ Errors: 0
```

## Commands

### Control Commands
| Command | Description |
|---------|-------------|
| `自动驾驶` / `start auto` | 启动自动驾驶模式 |
| `停止自动驾驶` / `stop auto` | 停止并退出自动驾驶 |
| `设置级别 X` / `set level X` | 设置容忍度级别(0-4) |
| `显示状态` / `show status` | 显示当前状态 |

### Level Commands
| Command | Action |
|---------|--------|
| `手动模式` | 设置为Level 0 |
| `先问后做` | 设置为Level 1 |
| `常规自动` | 设置为Level 2 |
| `信任模式` | 设置为Level 3 |
| `完全自动` | 设置为Level 4 |

### Workflow Commands
| Command | Description |
|---------|-------------|
| `开始工作流` | 启动project-planner |
| `下一阶段` | 推进到下一阶段 |
| `跳过确认` | 忽略所有确认请求 |

## Auto-Pilot Loop

```
┌────────────────────────────────────────────────────────────┐
│                    AUTO-PILOT LOOP                         │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────┐    ┌──────────────┐    ┌───────────────┐   │
│  │  Check   │───▶│   Execute    │───▶│   Report &    │   │
│  │  Queue   │    │   Skill(s)   │    │   Update HUD  │   │
│  └──────────┘    └──────────────┘    └───────────────┘   │
│       │                                        │            │
│       │  ←─────── Loop ────────             │            │
│       │                                        │            │
│       ▼                                        ▼            │
│  ┌──────────┐                       ┌───────────────┐     │
│  │  Wait/    │                       │  Skill        │     │
│  │  Continue │                       │  Tracker HUD  │     │
│  └──────────┘                       └───────────────┘     │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

## Persistence

### State File
`C:\Users\黄涂健隆\Desktop\ClaudeCode\disc-generator\auto_pilot_state.json`

```json
{
  "enabled": true,
  "level": 3,
  "project_planner_active": true,
  "skill_tracker_visible": true,
  "current_workflow": "股票分析网站",
  "stage": "5_execution",
  "stats": {
    "tasks_completed": 12,
    "tasks_running": 3,
    "errors": 0,
    "skills_used": [...]
  },
  "start_time": "2024-01-01T10:00:00Z",
  "last_update": "2024-01-01T10:30:00Z"
}
```

## Usage Examples

### Quick Start (简单启动)
```
User: "自动"
Auto-Pilot: "🎯 请告诉我你想做什么？"
           "例如：帮我做一个股票分析网站 / 查一下蛋白质结构"

User: "我要做一个机器学习项目"
Auto-Pilot: "✓ 收到！开始执行..."
           [启动工作流 → 需求分析 → Skill调度]
```

### Check Status
```
User: "显示状态"
Auto-Pilot: [显示HUD面板]
```

### Check Current Skills
```
User: "现在用了哪些skill"
Auto-Pilot: [显示Skill Tracker HUD]
```

## Safety Features

1. **Emergency Stop**: 说"停止"立即停止所有操作
2. **Confirmation Override**: 可随时用"确认"覆盖自动决策
3. **Activity Log**: 记录所有自动执行的操作
4. **Error Handling**: 遇到错误自动暂停并报告

## Integration

- **Always Runs**: skill-tracker 从启动开始就常驻显示
- **Parent of project-planner**: 自动驾驶是project-planner的上级
- **Skill Manager Integration**: 自动选择和调用Skills
- **Persistent State**: 状态持久化，崩溃后可恢复

---

## Quick Reference

| Command | Alias | Level |
|---------|-------|-------|
| `手动模式` | `manual` | 0 |
| `先问后做` | `ask-first` | 1 |
| `常规自动` | `auto-common` | 2 |
| `信任模式` | `trust` | 3 |
| `完全自动` | `full-auto` | 4 |

---
*Auto-Pilot enables long-running autonomous workflows with intelligent permission management.*
