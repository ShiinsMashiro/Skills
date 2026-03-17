---
name: auto-commit
description: |
  自动提交推送 - 检测代码修改自动提交并推送到远程。
  当修改任何代码项目时自动触发。
  基于 git 工作流。
version: 1.0.0
---

# Auto Commit (自动提交推送)

**检测代码修改 → 自动 commit → 自动 push**

## 核心功能

### 1. 自动检测修改

```
检测范围:
├── .js, .ts, .py, .java, .go, .rs
├── .md, .json, .yaml, .toml
└── .claude/, .github/, Dockerfile
```

### 2. 自动提交流程

```
代码修改检测
     │
     ▼
git status 检查
     │
     ▼
git add -A (暂存)
     │
     ▼
生成提交信息
     │
     │ 格式: type: message
     │ - feat: 新功能
     │ - fix: 修复
     │ - docs: 文档
     │ - refactor: 重构
     │
     ▼
git commit -m "message"
     │
     ▼
git push origin <branch>
     │
     ▼
返回结果
```

### 3. 提交类型

| 类型 | 说明 |
|------|------|
| feat | 新功能 |
| fix | Bug修复 |
| docs | 文档 |
| refactor | 重构 |
| style | 格式 |
| test | 测试 |
| chore | 维护 |

### 4. 自动推送

```
✅ 自动推送到 origin/main
✅ 支持自定义分支
✅ 推送失败告警
```

---

## 使用场景

| 场景 | 动作 |
|------|------|
| 修改代码后 | 自动 commit + push |
| 结束工作前 | 提交所有修改 |
| 切换分支前 | 自动保存 |
| AI 完成任务 | 自动保存进度 |

---

## 配置

### 忽略文件

```gitignore
node_modules/
dist/
build/
*.log
.env
.DS_Store
```

### 提交信息模板

```
feat: 添加新功能

- 描述1
- 描述2

Co-Authored-By: Claude Code <noreply@anthropic.com>
```

---

## 命令

| 命令 | 功能 |
|------|------|
| `commit` | 手动提交 |
| `push` | 手动推送 |
| `auto-commit on` | 开启自动提交 |
| `auto-commit off` | 关闭自动提交 |
| `status` | 查看状态 |

---

## 自动触发

当 skill-manager 检测到：
- 修改了代码文件
- 结束任务
- 用户说 "保存" / "提交"

---

*自动保存代码进度，永不丢失工作！*
