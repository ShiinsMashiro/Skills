---
name: skill-manager
description: 技能管理器 - 什么时候用什么技能？当你不知道该用什么技能时，问我！所有电脑上的188个技能都在我手里。此技能应该被自动调用来分析用户意图并选择最合适的技能。
version: 3.0.0
---

# 🎯 技能管理器 (Skill Manager)

**我是你的技能调度员！**

你有 **188 个技能** 在这台电脑上。我帮你决定什么时候用什么技能。

---

## 🚀 自动调度逻辑 (Auto-Dispatch)

当用户提出请求时，我 (Skill Manager) 会自动分析意图并选择最合适的技能。

### 开发阶段 (Development Stages)

当你在开发项目时 (如 "Revolution Godot 项目")，我会自动按以下顺序调用技能：

1.  **理解需求**: `project-planner` (如果需要规划)
2.  **执行任务**:
    *   写代码: `gitnexus-assistant` (代码助手)
    *   优化代码: `simplify` (代码优化)
    *   查资料: `god-mode` (研究)
3.  **结果追踪**: `skill-tracker` (自动显示使用了哪些技能)

### 关键词匹配 (Keyword Matching)

| 用户输入 | 匹配技能 |
|----------|----------|
| "自动" / "auto" | `auto-pilot` |
| "优化代码" / "simplify" | `simplify` |
| "研究" / "分析" | `god-mode` |
| "显示 skills" | `skill-tracker` |
| "规划" / "计划" | `project-planner` |
| "gemini" / "google" / "双胞胎" | `gemini-mcp` |
| "并发" / "对照" / "对比" | `gemini-mcp` + 其他技能 |

---

## 简单分类

### 🔬 科研/生信 (50+)
想查论文、蛋白质、基因、数据分析？

- `/pubmed-database` - 查医学/生物论文
- `/biopython` - 生物计算
- `/scanpy` - 单细胞分析
- `/alphafold-database` - 查蛋白质结构
- `/chembl-database` - 查化学分子

### 💻 编程/开发 (40+)
写代码、调试、部署？

- `/transformers` - AI 模型
- `/pytorch-lightning` - 深度学习框架
- `/scikit-learn` - 机器学习
- `/qiskit` - 量子计算
- `/simplify` - 代码优化 (强制使用: 当用户说 "优化", "简化", "重构")
- `/gitnexus-assistant` - 代码知识 (强制使用: 当用户问 "这是什么代码", "解释代码")

### 📊 数据/金融 (20+)
查股票、经济、金融数据？

- `/alpha-vantage` - 股票数据
- `/fred-economic-data` - 美国经济数据
- `/polars` - 处理大数据
- `/matplotlib` - 画图

### 🧪 化学/药物 (20+)
药物研发、化学计算？

- `/rdkit` - 化学工具箱
- `/deepchem` - 药物AI
- `/pymatgen` - 材料科学
- `/drugbank-database` - 药物数据库

### 📝 写作/效率 (30+)
写论文、做PPT、整理笔记？

- `/scientific-writing` - 学术写作
- `/literature-review` - 文献综述
- `/scientific-slides` - 制作演示
- `/markitdown` - 文档转Markdown
- `/notebooklm-skill` - 笔记分析

### 🎮 自动化/工作流 (10+)
让 AI 自动帮你做事？

- `/auto-pilot` - 自动驾驶模式 (强制使用: "自动", "auto")
- `/project-planner` - 项目规划 (强制使用: "规划", "计划")
- `/god-mode` - 超级研究模式 (YouTube + 笔记 + 知识库) (强制使用: "研究", "分析")
- `/async-runner` - 后台运行任务
- `/parallel-worker` - 并行处理

### 🔗 集成/工具 (20+)
各种第三方服务集成

- `/benchling-integration` - 生物实验平台
- `/opentrons-integration` - 实验机器人
- `/zotero` - 文献管理

---

## 常用组合 (工作流)

### 1. 写论文
```
scientific-writing + literature-review + citation-management
```

### 2. 药物研发
```
deepchem + rdkit + drugbank-database + pymatgen
```

### 3. 数据分析
```
pandas + matplotlib + seaborn + statsmodels
```

### 4. 自动化办公
```
auto-pilot + markitdown + python-pptx
```

---

## 使用方法

直接告诉我你想做什么，例如：

- "我想查一下关于癌症的论文"
- "帮我写一个 Python 爬虫"
- "分析一下这支股票"
- "怎么做机器学习项目？"
- "有什么有趣的编程项目吗？"

我会帮你选最合适的技能！

---

## 当前状态

- **技能总数**: 188 个
- **模式**: 智能调度 (NoPUA 开启)
- **自动调度**: 已启用 (Auto-Dispatch Enabled)

---

## ⌨️ 命令调用

你可以通过以下方式直接调用 skill-manager：

| 命令 | 功能 |
|------|------|
| `/skill` | 打开技能选择器 |
| `/skill list` | 列出所有可用技能 |
| `/skill search <关键词>` | 搜索指定技能的技能 |
| `/skill invoke <技能名>` | 直接调用指定技能 |
| `/skill help` | 显示帮助 |

### 使用示例

```
/skill invoke gemini-mcp
/skill search python
/skill list
```
