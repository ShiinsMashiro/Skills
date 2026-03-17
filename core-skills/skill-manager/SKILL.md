---
name: skill-manager
description: |
  技能调度器 - 遵循 s02 原理：加一个工具，只加一个 handler。
  动态 dispatch map，按需注册技能。
  基于"信息充分原则"优化：给AI的信息越充分，产出越好。
version: 2.2.0
---

# Skill Manager (技能管理器)

**遵循 s02 原理 + 文章优化原则**

> *"加一个工具, 只加一个 handler"*
> *"给AI的信息越充分，产出越好"*

## 核心理念（来自文章优化）

### 1. 计划先行 (Plan First)
- 收到任务 → 先分析需求
- 信息越充分 → 产出越好
- 复杂任务 → 先写PRD或Spec

### 2. 让AI写测试
- 零成本 → 高ROI
- 每个新功能 → 自动生成测试

### 3. 流程技能化
- 固定手动流程 → 封装成skill
- 重复工作 → 自动化

### 4. 关注架构而非细节
- 代码主干 → 系统交互点
- 不纠结语法细节

### 5. 工具轻量化
- 不过度投入工具链
- 够用就好

---

## 常驻技能

**这些技能在任何对话中都激活：**

| 技能 | 说明 |
|------|------|
| `nopua` | 每次交互都用爱与尊重 |
| `skill-tracker` | 每次响应都显示调用流程 |
| `prompt-optimizer` | 优化用户输入（Plan First前置） |

---

## 优化工作流

### 文档主导 vs 原型主导

```
📄 文档主导 (大功能):
  需求发散 → 写PRD → Plan+Review → 实现 → 测试迭代 → 人工Review

🎨 原型主导 (小功能/需求模糊):
  快速原型 → 验证需求 → 切换文档驱动
```

### 智能选择

| 任务类型 | 工作流 |
|----------|--------|
| 大功能/方向明确 | 文档主导 |
| 需求模糊/小功能 | 原型主导 |
| Bug修复 | 原型主导 |
| 新系统架构 | 文档主导 |

---

## 核心原理

```
DISPATCH_MAP = {
  "自动": auto-pilot,
  "规划": project-planner,
  "研究": god-mode,
  "优化": simplify,
  "写代码": gitnexus-assistant,
  "测试": auto-test,
  "保存": auto-commit,
  ...
}
```

---

## 动态调度流程

### 1. 接收请求

### 2. Plan First - 意图分析 + 信息收集

```
# 关键：给AI充分信息
intent = analyze(user_input)
context = collect_context(project_files, git_history)

# 决定工作流
if is_complex(intent):
    trigger(document_workflow)  # 文档主导
else:
    trigger(prototype_workflow)  # 原型主导
```

### 3. 关键词匹配 → dispatch

### 4. 执行 + 测试

```
# 每个功能自动生成测试
if new_feature:
    auto_generate_tests()

# 测试驱动开发
test → implement → iterate
```

### 5. 返回结果 + 架构关注

```
# 关注点
- 系统交互点 ✓
- 核心骨架 ✓
- 语法细节 ✗
```

---

## Dispatch Map (按类别)

### 🚀 工作流 (Workflow)

| 关键词 | 技能 |
|--------|------|
| "自动" / "auto" | `auto-pilot` |
| "规划" / "计划" | `project-planner` |
| "后台" / "异步" | `async-runner` |
| "并行" / "同时" | `parallel-worker` |

### 🔬 科研 (Scientific)

| 关键词 | 技能 |
|--------|------|
| "论文" / "研究" | `pubmed-database` |
| "蛋白质" / "结构" | `alphafold-database` |
| "基因" / "DNA" | `biopython` |

### 💻 编程 (Development)

| 关键词 | 技能 |
|--------|------|
| "优化" / "简化" | `simplify` |
| "解释" / "这是啥" | `gitnexus-assistant` |
| "测试" | `auto-test` |

---

## 设计原则

1. **Dispatch Map**: 关键词 → 技能
2. **动态注册**: 加技能不改循环
3. **按需激活**: 不用则不加载
4. **信息充分**: 收集足够上下文
5. **轻量优先**: 够用就好

---

*This skill follows s02 + 文章优化: 信息充分 + 测试优先 + 架构关注.*
