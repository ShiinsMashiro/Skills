---
name: gitnexus-assistant
description: This skill should be used when the user asks about "GitNexus", "代码知识图谱", "代码依赖", "code knowledge graph", "代码调用链", "understand codebase architecture", or wants to analyze code structure and dependencies.
version: 1.0.0
---

# GitNexus Assistant

GitNexus是一个将代码库索引为知识图谱的工具，帮助AI理解代码依赖、调用链、执行流程。

## When This Skill Applies

This skill activates when the user wants to:
- Understand codebase architecture / "How does X work?"
- Know what breaks if I change X (blast radius analysis)
- Debug: "Why is X failing?"
- Refactor code (rename, extract, split)
- Explore code dependencies and relationships
- Index or analyze a codebase

## How to Use

1. First, read the context: `gitnexus://repo/{name}/context`
2. Then match your task to the appropriate skill

## Available Skills in GitNexus

| Task | Skill File |
|------|------------|
| Understand architecture | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius analysis | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Debugging | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Refactoring | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

## Key Features

- **Code Indexing**: 将代码库转换为知识图谱
- **Dependency Tracking**: 追踪所有依赖关系
- **Call Chain Analysis**: 分析调用链
- **Impact Analysis**: 分析修改的影响范围

## Usage Examples

- "分析这个代码库的架构"
- "查找函数X在哪里被调用"
- "如果修改这个函数会影响哪些地方"
- "帮我理解这个项目的结构"

## Note

If the index is stale, run `npx gitnexus analyze` first.
