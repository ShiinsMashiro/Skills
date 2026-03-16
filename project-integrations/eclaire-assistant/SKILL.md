---
name: eclaire-assistant
description: This skill should be used when the user asks about "eclaire", "AI助手后端", "backend development", "fullstack", "nodejs backend", "typescript", "database", "authentication", or wants to work with the eclaire AI assistant backend.
version: 1.0.0
---

# Eclaire Assistant

Eclaire是一个完整的AI助手后端项目，包含数据库、认证、队列、AI集成等功能。

## When This Skill Applies

This skill activates when the user wants to:
- Work with the eclaire backend codebase
- Understand the architecture
- Add new features
- Fix bugs
- Modify authentication
- Work with database
- Handle AI integration
- Manage queues and jobs

## Project Structure

```
eclaire/
├── apps/
│   └── backend/
│       ├── src/
│       │   ├── config/         # 配置
│       │   ├── db/            # 数据库
│       │   ├── lib/           # 核心库
│       │   │   ├── agent/     # AI Agent
│       │   │   ├── services/ # 各种服务
│       │   │   ├── queue/    # 队列
│       │   │   └── ...
│       │   └── index.ts      # 入口
│       └── scripts/          # 脚本
├── docker/                   # Docker配置
└── ...
```

## Key Features

- **Database**: PostgreSQL with Prisma
- **Authentication**: JWT + 加密
- **AI Integration**: 支持多种AI服务
- **Queue System**: 任务队列和定时任务
- **File Processing**: 文件处理
- **API**: RESTful API

## Usage Examples

- "eclaire项目是做什么的"
- "如何在eclaire中添加新功能"
- "eclaire的数据库结构是怎样的"
- "帮我理解eclaire的认证流程"

## Tech Stack

- Node.js / TypeScript
- PostgreSQL
- Docker
- Various AI SDKs
