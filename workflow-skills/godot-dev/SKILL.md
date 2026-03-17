---
name: godot-dev
description: |
  Godot 4.x 游戏开发专用工作流。
  原型 → 核心系统 → 扩展内容 → 完善。
  自动集成 Claude Code + Godot CLI。
version: 1.1.0
---

# Godot Dev (Godot 开发)

**Claude Code + Godot 4.x 自动化开发**

> *"给 AI 的信息越充分，产出越好"* + *"慢操作丢后台"*

---

## 核心原理

### 1. 项目结构

```
project/
├── project.godot           # 项目配置
├── scenes/               # 场景文件
│   ├── main/main.tscn
│   ├── units/unit.tscn
│   └── ui/hud.tscn
├── scripts/              # 脚本文件
│   ├── core/            # 核心系统
│   │   ├── game.gd      # Autoload
│   │   ├── map_manager.gd
│   │   ├── unit_manager.gd
│   │   ├── combat.gd
│   │   ├── ai_player.gd
│   │   └── economy.gd
│   └── ui/              # UI 系统
├── resources/           # 资源文件 (.tres)
└── assets/              # 静态资源
```

### 2. 开发阶段

```
📋 开发流程:

  1. 原型 (Prototype)
     - 快速验证核心玩法
     - 使用占位符
     - MVP 最小可行性

  2. 核心系统 (Core)
     ├── Game Autoload
     ├── Map System
     ├── Unit System
     ├── Combat System
     └── Basic UI

  3. 扩展 (Content)
     ├── AI Opponent
     ├── Economy
     ├── Diplomacy
     ├── Technology
     ├── Intelligence
     └── Supply System

  4. 完善 (Polish)
     - 视觉/音效/平衡
```

---

## 自动工作流

### 1. 接收任务
```
用户: "添加一个新单位类型"
```

### 2. 分析 + 规划
```
- 检查现有单位结构
- 确定新增内容
- 列出修改文件
- 写 PRD (如需要)
```

### 3. 执行
```
- 创建/修改资源文件 (.tres)
- 创建/修改脚本 (.gd)
- 更新场景 (.tscn)
```

### 4. 测试
```
- Godot headless 测试
- godot --headless --script-check
- 检查错误
- 修复问题
```

---

## 命令

| 命令 | 功能 |
|------|------|
| "godot 开发" | 启动 Godot 开发工作流 |
| "godot 测试" | 运行 headless 测试 |
| "godot 检查" | 检查脚本错误 |
| "godot 构建" | 导出游戏 |

---

## 调试技巧

```bash
# 无头测试 (检查脚本错误)
godot --headless --script-check

# 运行场景
godot --path . --scene scenes/main/main.tscn

# 导出
godot --export-release "HTML5" build/
```

---

## 最佳实践

### 场景 vs 脚本

| 场景 | 脚本 |
|------|------|
| 可组合配置 | 可复用逻辑 |
| 匿名类型 | 命名类型 |
| 实例化对象 | 纯逻辑 |

### Autoload 使用

```
✓ 全局功能: Game, Audio, SaveSystem
✗ 场景特定功能
```

### 资源加载

```gdscript
# 静态预加载
const UnitScene = preload("res://scenes/unit.tscn")

# 动态加载
var texture = load("res://assets/sprite.png")

# 实例化
var unit = UnitScene.instantiate()
```

### 信号系统 (解耦)

```gdscript
# 定义信号
signal unit_selected(unit)
signal turn_changed(player_id)

# 发射
unit_selected.emit(selected_unit)

# 连接
unit_selected.connect(_on_unit_selected)
```

---

## 设计原则

1. **文档驱动**: 先写 Spec 再开发
2. **信息充分**: 收集足够上下文
3. **后台不阻塞**: 慢操作丢后台
4. **关注架构**: 系统交互点
5. **自动测试**: 每次修改运行测试

---

## Claude Code 命令

```bash
# 测试项目
godot --headless --script-check

# 导出 HTML5
godot --headless --export-release "HTML5" ./build
```

---

*Godot 4.x 开发专用工作流 - 自动化、规范化、高效率*
