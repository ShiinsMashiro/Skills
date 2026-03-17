---
name: skill-manager
description: |
  技能调度器 - 遵循 s02 原理：加一个工具，只加一个 handler。
  动态 dispatch map，按需注册技能。
  所有 188 个技能的调度中心。
version: 2.0.0
---

# Skill Manager (技能管理器)

**遵循 s02 原理：加一个工具，只加一个 handler**

> *"加一个工具, 只加一个 handler"*

## 核心原理

```
DISPATCH_MAP = {
  "自动": auto-pilot,
  "规划": project-planner,
  "研究": god-mode,
  "优化": simplify,
  "写代码": gitnexus-assistant,
  "保存": auto-commit,
  "提交": auto-commit,
  "commit": auto-commit,
  "push": auto-commit,
  "代码": auto-commit,
  "开会": scheduler,
  "会议": scheduler,
  "早会": scheduler,
  "周会": scheduler,
  "复盘": scheduler,
  "定时": scheduler,
  ...
}
```

**循环不用动，新技能注册进 dispatch map 就行**

## 动态调度流程

### 1. 接收请求 (来自 main-controller)

### 2. 意图分析

- 关键词匹配 → dispatch map
- 无匹配 → 默认 skill-manager 自身处理

### 3. 调度执行

```
# 单关键词 - 单技能
if intent in DISPATCH_MAP:
    skill = DISPATCH_MAP[intent]
    activate(skill)

# 多关键词 - 多技能组合
if "并行" in intent or "并行" in user_input:
    activate(auto-pilot)      # 自动驾驶
    activate(parallel-worker) # 并行处理

if "后台" in intent or "后台" in user_input:
    activate(auto-pilot)
    activate(async-runner)    # 后台任务
```

### 4. Claude + Gemini 并行研究模式

当用户说 "研究" 时，自动启用双引擎：

```
用户: "研究最新的AI论文"

→ parallel-worker 分割:
    ├── Claude Code: 搜索 PubMed
    └── Gemini: 搜索 ArXiv + 学术源

→ 等待双方结果

→ Gemini 整合:
    ├── 汇总
    ├── 去重
    └── 格式化输出

→ 返回最终结果
```

### 5. Gemini 整合规则

| 阶段 | Gemini 任务 |
|------|-------------|
| 并行搜索后 | 整合多源结果 |
| 多结果返回前 | 格式化 + 摘要 |
| 复杂任务 | 分析 + 建议 |

### 6. NoPUA 常驻模式

**NoPUA 是常驻技能**，始终激活：

| 触发条件 | 动作 |
|----------|------|
| 每次交互 | 用爱与尊重的方式 |
| AI 显示犹豫 | 鼓励 + 信任 |
| 用户施压 | 转换为正向表达 |

```
用户: "赶紧的，别浪费时间"
  → NoPUA 转换: "我相信你能快速完成"
```

### 7. Prompt 优化

| 阶段 | 调用 prompt-optimizer |
|------|----------------------|
| 用户输入后 | 优化 prompt |
| 复杂任务 | 增强 prompt |
| 简单任务 | 直接执行 |

```
用户: "查论文"
  → prompt-optimizer: "优化为结构化查询"
  → 执行
```

**组合触发规则**:
| 关键词组合 | 触发技能 |
|------------|----------|
| "并行" | auto-pilot + parallel-worker |
| "后台" + "执行" | auto-pilot + async-runner |
| "自动" + "并行" | auto-pilot + parallel-worker |
| "研究" + "多个" | god-mode + parallel-worker |

### 4. 返回结果

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
| "化学" / "分子" | `chembl-database` |
| "药物" | `drugbank-database` |

### 💻 编程 (Development)

| 关键词 | 技能 |
|--------|------|
| "优化" / "简化" | `simplify` |
| "解释" / "这是啥" | `gitnexus-assistant` |
| "AI" / "模型" | `transformers` |
| "量子" | `qiskit` |
| "机器学习" | `scikit-learn` |

### 📊 数据/金融

| 关键词 | 技能 |
|--------|------|
| "股票" / "交易" | `alpha-vantage` |
| "经济" / "GDP" | `fred-economic-data` |
| "分析" / "图表" | `matplotlib` |

### 📝 写作/效率

| 关键词 | 技能 |
|--------|------|
| "写" / "论文" | `scientific-writing` |
| "综述" | `literature-review` |
| "PPT" / "演示" | `scientific-slides` |

---

## 技能注册 (如何添加新技能)

**只需两步**：

1. **定义 skill** → 创建 `skills/[skill-name]/SKILL.md`
2. **注册到 dispatch map** → 添加关键词映射

**不需要修改循环逻辑**

---

## 命令

| 命令 | 功能 |
|------|------|
| `/skill list` | 列出所有可用技能 |
| `/skill search <关键词>` | 搜索技能 |
| `/skill invoke <技能名>` | 直接调用 |
| `/skill help` | 显示帮助 |

---

## 设计原则 (来自 s02)

- **Dispatch Map**: 关键词 → 技能
- **动态注册**: 加技能不改循环
- **按需激活**: 不用则不加载

---

*This skill follows s02: 加一个工具, 只加一个 handler.*
