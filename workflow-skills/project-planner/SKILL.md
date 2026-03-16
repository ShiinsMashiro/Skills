---
name: project-planner
description: This skill should be used when the user wants to "规划项目", "设计工作流", "需求分析", "plan project", "design workflow", "project requirements", "项目策划", "task planning", "阶段管理", "开始工作", "执行任务", or wants to create a detailed project plan with skill orchestration at each stage. Always coordinates with skill-manager for skill dispatching.
version: 1.0.0
---

# Project Planner (项目规划器) - 工作流管理器

**🎯 NoPUA默认开启**：所有交互都采用爱与尊重的方式！

这是一个智能项目规划器，能够分析用户需求，设计完整工作流，并在每个阶段自动调用合适的Skills。

## When This Skill Applies

This skill activates when the user wants to:
- Plan a new project or task
- Design a complete workflow
- Break down complex requirements into stages
- Automatically use appropriate skills at each stage
- Get systematic guidance through a project lifecycle

## Workflow Stages

### Stage 1: 需求理解 (Requirement Analysis)
**目标**: 理解用户需求，明确项目目标

**关键问题**:
- 用户想要完成什么？
- 目标受众是谁？
- 有什么约束条件？
- 预期成果是什么？

**可用Skills**:
- `skill-manager` - 分析需求，匹配合适的Skills
- `project-ideas` - 如果需要，提供项目灵感
- `prompt-eng-tutor` - 帮助澄清需求

**产出**: 需求文档 (Requirements Document)

---

### Stage 2: 技术选型 (Technology Selection)
**目标**: 选择合适的技术栈和工具

**考虑因素**:
- 编程语言偏好
- 性能要求
- 团队技能
- 成本/开源

**可用Skills**:
- `scientific-skills` - 如果涉及科学计算/数据
- `project-ideas` - 参考类似项目技术栈
- `eclaire-assistant` - 如果涉及后端开发
- `gitnexus-assistant` - 如果涉及代码分析

**产出**: 技术选型报告

---

### Stage 3: 架构设计 (Architecture Design)
**目标**: 设计系统架构和数据流

**产出**:
- 系统架构图
- 模块划分
- 数据流设计

**可用Skills**:
- `gitnexus-assistant` - 架构分析
- `networkx` - 如果需要图/网络架构
- `scientific-skills` - 相关领域架构参考

---

### Stage 4: 实现规划 (Implementation Planning)
**目标**: 制定详细实现步骤

**产出**:
- 功能列表 (Features)
- 里程碑 (Milestones)
- 时间线 (Timeline)

**可用Skills**:
- `disc-generator` - 生成学习页面（如果需要边学边做）
- `skill-tracker` - 追踪进度
- `project-ideas` - 实现参考

---

### Stage 5: 执行与迭代 (Execution & Iteration)
**目标**: 按计划执行，迭代优化

**子阶段**:
1. 基础功能实现
2. 测试与调试
3. 优化与完善
4. 部署与发布

**可用Skills** (按需调用):
- `gitnexus-assistant` - 代码开发/调试
- `eclaire-assistant` - 后端开发
- `obsidian-vision` - 文档/截图
- `scientific-skills` - 领域特定功能

---

### Stage 6: 总结与复盘 (Review & Document)
**目标**: 总结经验，文档化

**产出**:
- 项目文档
- 技术报告
- 经验教训

**可用Skills**:
- `scientific-writing` - 文档撰写
- `citation-management` - 引用（如需）
- `latex-templates` - 格式模板

---

## Skill Orchestration Examples

### Example 1: 数据分析项目

**需求**: "我想做一个股票数据分析网站"

```
Stage 1 - 需求理解:
├── 用户: 股票数据分析
├── 目标: 网站展示
└── 约束: 实时数据

Stage 2 - 技术选型:
├── 后端: Python (data processing)
├── 前端: React
├── 数据: Alpha Vantage API
└── Skills: alpha-vantage, polars, matplotlib

Stage 3 - 架构设计:
├── 数据层: API → Python处理 → 存储
├── 服务层: Flask/FastAPI
└── 前端层: React + 图表

Stage 4 - 实现规划:
├── [Milestone 1] 数据获取
├── [Milestone 2] 数据处理
├── [Milestone 3] 前端展示
└── [Milestone 4] 部署上线
```

### Example 2: 机器学习项目

**需求**: "我想做一个图像分类模型"

```
Stage 1: 理解需求
└── 图像分类, 准确率目标

Stage 2: 技术选型
├── 框架: PyTorch / TensorFlow
├── 预训练模型: ResNet, EfficientNet
└── Skills: transformers, pytorch-lightning

Stage 3: 架构设计
├── 数据pipeline
├── 模型训练
└── 推理服务
```

---

## Project Template

```yaml
项目名称: [Name]
阶段: [当前阶段]

## 需求分析
目标:
约束:
产出:

## 技术选型
语言:
框架:
数据库:
API:

## 架构设计
模块:
数据流:

## 实现计划
阶段1: [任务]
阶段2: [任务]
阶段3: [任务]

## 进度追踪
[ ] 任务1
[ ] 任务2
```

## Usage

### 启动新项目
```
"帮我规划一个新项目"
"我要做一个X项目"
"plan a new project"
```

### 查看当前阶段
```
"现在到什么阶段了"
"当前进度"
"what stage are we at"
```

### 跳转到特定阶段
```
"我们到技术选型阶段吧"
"开始实现阶段"
"go to implementation stage"
```

### 管理Skills
```
"这个阶段需要什么skill"
"切换到下一个阶段"
"show available skills for this stage"
```

---

## 状态管理

项目状态存储在:
`C:\Users\黄涂健隆\Desktop\ClaudeCode\disc-generator\project_state.json`

包含:
- 当前阶段
- 已完成任务
- 使用的Skills历史
- 下一个推荐Skill

---

## Key Features

1. **阶段化管理** - 清晰的项目阶段划分
2. **智能Skill推荐** - 每个阶段推荐最合适的Skills
3. **状态追踪** - 记录项目进度
4. **灵活跳转** - 支持阶段间跳转
5. **可定制模板** - 根据项目类型调整

---

## Skill调用流程

```
用户需求 → 需求分析 → 阶段判定
                        ↓
                PROJECT PLANNER 决策
                        │
                        ├── 需要并行? ──→ PARALLEL-WORKER
                        │                      (任务分割+隔离执行)
                        │
                        └── 不需要 ──→ SKILL MANAGER
                                          (普通调度)
                        ↓
                执行任务 → 结果反馈
                        ↓
                进入下一阶段 ←→ 循环
```

## 并行处理决策

Project Planner 会根据以下条件判断是否需要并行处理：

| 条件 | 示例 | 决策 |
|------|------|------|
| 多独立任务 | "查3只股票" | 并行 |
| 大数据集 | "分析1000个基因" | 并行(分割) |
| 复杂计算 | "跑10个模型" | 并行 |
| 单一任务 | "查1只股票" | 串行 |
| 顺序依赖 | "先下载再处理" | 串行 |

---
*This skill orchestrates the entire project lifecycle with intelligent skill management at each stage.*
