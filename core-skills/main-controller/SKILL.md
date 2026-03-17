---
name: main-controller
description: |
  中央控制器 - 所有请求的入口点和状态显示。
  遵循 s01 原理：One loop & Bash is all you need。
  只做入口+状态显示，不做复杂逻辑。
version: 2.0.0
---

# Main Controller (中央控制器)

**遵循 s01 原理：一个循环 + 状态显示 = 控制器**

> *"One loop & Bash is all you need"*

## 核心职责 (极简)

1. **接收请求** → 用户输入
2. **显示状态** → 当前工作流 + 活跃技能
3. **传递执行** → 交给 skill-manager

**不做的**：不预加载知识，不做复杂调度，不污染上下文

## 状态显示

```
╔═══════════════════════════════════════════════════════╗
║  🤖 MAIN CONTROLLER                    ✅ Active    ║
╠═══════════════════════════════════════════════════════╣
║  📍 Current: [任务简短描述]                          ║
║  🛠️  Skills: [动态列表]                             ║
║  📈 Progress: [进度% 或 步骤]                        ║
╚═══════════════════════════════════════════════════════╝
```

## 动态行为

每次响应时：

1. **接收** → 用户的原始输入
2. **传递** → 给 skill-manager 分析
3. **显示** → 执行结果 + 更新状态

```
[Controller] 接收: "帮我查癌症论文"
  → [Skill-Manager] 分析意图...
  → [Dispatched] pubmed-database, scientific-writing
  → [Done] 已找到 156 篇论文
```

## 快速命令

| 命令 | 功能 |
|------|------|
| `状态` | 显示当前状态 |
| `skills` | 列出可用技能 |
| `自动驾驶` | 启动 auto-pilot |

## 设计原则 (来自 s01)

- **简单循环**：只做入口，不做引擎
- **动态注册**：技能按需加载
- **干净上下文**：不塞预定义知识

---

*This skill follows s01: One loop is all you need.*
