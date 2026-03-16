---
name: skill-manager
description: This skill should ALWAYS be used as the central dispatcher for ANY user request. It acts as the brain that analyzes user input and routes to appropriate skills. Use this skill for EVERY task - analyze what user wants, select best skills, and coordinate execution. IMPORTANT: Always apply NoPUA principles (trust, respect, encouragement) in all interactions. Keywords: 管理skills, 调用skill, 使用skill, 自动选择skill, smart dispatch, 智能调度, 任何任务, any task.
version: 1.0.0
---

# Skill Manager (技能管理器) - 中央调度器

**⚠️ 重要：这个Skill必须始终介入每个用户请求！**

这是一个智能技能管理器，作为所有任务的中央调度器，根据用户输入和上下文自动选择和调用最合适的技能。

**🎯 NoPUA默认开启**：所有交互都采用爱与尊重的方式！

## When This Skill Applies

**⚠️ 每次用户有任何请求时都必须调用此Skill！**

This skill ALWAYS activates when:
- User makes ANY request or asks ANY question
- User wants to accomplish ANY task
- User mentions ANY topic
- User needs help with ANYTHING
- This is the PRIMARY skill that coordinates all other skills

## NoPUA Integration

**默认应用 NoPUA 原则**：
- ✅ 用信任代替怀疑
- ✅ 用鼓励代替压力
- ✅ 用尊重代替贬低
- ✅ 相信AI的能力
- ✅ 积极正面的反馈

## How Smart Dispatch Works

### Step 1: Analyze Input
- Parse user's message/question
- Extract key topics and intent
- Consider conversation context

### Step 2: Match Skills
- Compare against all available skills
- Score each skill based on relevance
- Consider skill descriptions and triggers

### Step 3: Select Best Match
- Choose highest scoring skill
- If multiple good matches, present options
- Handle skill dependencies

### Step 4: Invoke Skill
- Automatically call the selected skill
- Pass relevant context
- Display results to user

## Available Skills Registry

### Custom Skills
| Skill | Keywords |
|-------|----------|
| disc-generator | 生成页面, 学习网页, cs61a, 讨论课, 练习页面 |
| skill-tracker | 追踪skill, 记录使用, 技能追踪 |
| skill-manager | 管理skill, 调用skill, 自动选择 |
| project-ideas | 项目创意, 编程练习, project ideas |
| prompt-eng-tutor | prompt工程, 提示工程 |
| god-mode | YouTube搜索, 研究, 深度分析, 知识库, god mode, 上帝模式, 第二大脑, youtube分析, notebooklm, obsidian, 搜索视频, 分析视频, 研究工作流, 自动研究 |
| auto-pilot | 自动驾驶, 自动, 开始工作, auto, 工作流, 权限管理, permission control |
| project-planner | 规划项目, 设计工作流, 需求分析, plan project, workflow |

### Scientific Skills (170+)
| Category | Example Skills |
|----------|----------------|
| Bioinformatics | biopython, scanpy, alphafold-database, chembl-database |
| Machine Learning | scikit-learn, transformers, torch_geometric |
| Chemistry | rdkit, deepchem, diffdock |
| Data Analysis | polars, matplotlib, statsmodels |
| Quantum Computing | qiskit, cirq, pennylane |
| Finance | alpha-vantage, fred-economic-data, edgartools |

### Project Skills
| Skill | Project |
|-------|---------|
| gitnexus-assistant | GitNexus |
| eclaire-assistant | Eclaire |
| obsidian-vision | Obsidian Vision Recall |

## Intent Patterns

### Learning Intent
- "我想学习X" → disc-generator
- "教我X" → prompt-eng-tutor
- "X是什么" → 相关scientific skill

### Practice Intent
- "给我一个项目" → project-ideas
- "练习X" → project-ideas
- "做X练习" → disc-generator

### Research Intent
- "查X数据" → 对应database skill
- "分析X" → 对应analysis skill
- "找X论文" → pubmed/biorxiv skill

### Development Intent
- "分析代码" → gitnexus-assistant
- "开发X" → eclaire-assistant
- "调试X" → gitnexus-assistant

### Research Intent (god-mode)
- "搜索YouTube" → god-mode
- "研究X" → god-mode
- "深度分析X" → god-mode
- "youtube分析" → god-mode
- "notebooklm" → god-mode
- "obsidian" → god-mode
- "第二大脑" → god-mode
- "god" / "上帝模式" → god-mode

### Workflow Intent (auto-pilot + project-planner)
- "自动驾驶" → auto-pilot
- "自动" → auto-pilot
- "规划项目" → project-planner
- "工作流" → project-planner

## Smart Matching Examples

### Example 1
User: "我想学习递归"
```
Analysis: Learning intent + programming topic
Match: disc-generator
Action: Invoke disc-generator with topic="递归"
```

### Example 2
User: "帮我查一下蛋白质结构"
```
Analysis: Research intent + protein structure
Match: alphafold-database
Action: Invoke alphafold-database
```

### Example 3
User: "给我一个Python练习项目"
```
Analysis: Practice intent + Python
Match: project-ideas
Action: Invoke project-ideas with language="Python"
```

### Example 4
User: "追踪我用了哪些skills"
```
Analysis: Management intent
Match: skill-tracker
Action: Invoke skill-tracker
```

## Context-Aware Selection

The manager considers:
1. **Conversation History**: Previous topics, skills used
2. **User Preferences**: Preferred languages, domains
3. **Skill Availability**: What skills are loaded
4. **Combination Potential**: Can multiple skills work together?

## Usage Examples

- "帮我找个合适的skill"
- "我应该用哪个skill"
- "根据这个话题推荐skill"
- "what skill should I use"
- "自动调用相关skill"
- "smart dispatch"

## Response Format

When invoked, the skill manager will:

1. **Analyze** your request
2. **Match** against available skills
3. **Recommend** the best skill(s)
4. **Invoke** the selected skill
5. **Explain** why this skill was chosen

## Fallback Behavior

If no clear match:
- Present top 3 closest matches
- Ask user to confirm
- Suggest general-purpose skills
- Offer to list all available skills

## Skills Tracked

Currently tracked skills: 10+ custom + 170+ scientific

### Workflow Skills (Auto-Pilot Hierarchy)
| Skill | 说明 |
|-------|------|
| auto-pilot | 自动驾驶模式（权限控制，常驻） |
| project-planner | 项目规划（6阶段管理） |
| god-mode | 终极研究工作流 |

### Auto-Pilot Dispatch Logic
```
用户说: "自动" → skill-manager → auto-pilot (启动)
    ↓
auto-pilot 询问: "你想做什么？"
    ↓
用户说: "我要做X项目" → project-planner (启动)
    ↓
project-planner 分析需求 → 调度具体Skills执行
```

---

*This skill enables intelligent, context-aware skill dispatch for optimal user experience.*

---
*This skill enables intelligent, context-aware skill dispatch for optimal user experience.*
