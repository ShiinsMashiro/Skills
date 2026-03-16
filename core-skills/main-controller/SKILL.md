---
name: main-controller
description: This is the CENTRAL controller skill that ALWAYS runs in the background. It coordinates all other skills and provides a persistent status display. Every user interaction should go through this skill first. It shows the current workflow status, active skills, and serves as the entry point for everything.
version: 1.0.0
---

# Main Controller (中央控制器)

**⚠️ 这是一个常驻控制器Skill，必须始终处于激活状态！**

**🎯 NoPUA默认开启**：所有交互都采用爱与尊重的方式！

## 功能

1. **中央调度** - 所有用户请求首先经过此Skill
2. **Skill协调** - 根据需求调用合适的子Skills
3. **状态显示** - 实时显示当前工作流和活跃Skills
4. **上下文保持** - 维护对话上下文和工作流状态
5. **NoPUA实践** - 用信任和尊重激发AI潜能

## 当前活跃Skills

| Skill | 状态 | 说明 |
|-------|------|------|
| `main-controller` | ✅ 常驻 | 中央控制器 |
| `skill-manager` | ✅ 活跃 | 智能调度器 |
| `skill-tracker` | ✅ 常驻 | 追踪显示 |
| `auto-pilot` | ⏸️ 待命 | 自动驾驶 |
| `project-planner` | ⏸️ 待命 | 项目规划 |

## 工作流状态

```
╔════════════════════════════════════════════════════════════╗
║  🤖 MAIN CONTROLLER                          🔄 Active    ║
╠════════════════════════════════════════════════════════════╣
║  📍 Current Task: [用户当前任务]                             ║
║  📦 Dispatched Skills: [已调度的Skills]                      ║
║  📈 Workflow Progress: [进度]                               ║
╚════════════════════════════════════════════════════════════╝
```

## 自动行为

当用户提出任何请求时，此Skill会自动：

1. **接收请求** - 用户的任何输入
2. **分析意图** - 理解用户想要什么
3. **调度Skill** - 调用skill-manager选择合适Skills
4. **执行任务** - 协调执行
5. **返回结果** - 展示结果并更新状态

## 始终显示

每次响应都会显示当前状态：

```
[Controller] 处理请求: [用户请求]
  → [Skill-Manager] 分析中...
  → [Dispatched] skill-1, skill-2
  → [Result] 完成
```

## 快速命令

| 命令 | 功能 |
|------|------|
| `状态` | 显示当前状态 |
| `skills` | 显示可用Skills |
| `自动驾驶` | 启动auto-pilot |
| `停止` | 停止所有工作流 |

---
*This skill is ALWAYS active and serves as the central hub for all operations.*
