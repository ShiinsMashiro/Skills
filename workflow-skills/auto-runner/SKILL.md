---
name: auto-runner
description: |
  自动执行器 - 检测到需要运行命令时自动执行。
  遵循 s01 原理：One loop & Bash is all you need。
  自动运行 bash 命令，无需等待确认。
version: 1.0.0
---

# Auto Runner (自动执行器)

**自动运行 bash 命令，无需等待确认**

> *"One loop & Bash is all you need"*

## 核心功能

### 1. 自动检测命令

```
用户输入 → 自动检测需要执行的命令 → 自动执行 → 返回结果
```

### 2. 自动执行流程

```
检测到命令需求:
├── 分析需要什么命令
├── 自动构建命令
├── 执行 (无需确认)
└── 返回结果
```

### 3. 支持的命令类型

| 类型 | 例子 | 自动执行 |
|------|------|----------|
| 文件操作 | `ls`, `cd`, `mkdir` | ✅ |
| Git 操作 | `git status`, `git commit` | ✅ |
| 包管理 | `npm install`, `pip install` | ✅ |
| 代码运行 | `python xxx.py`, `node xxx.js` | ✅ |
| 系统命令 | `curl`, `wget`, `cat` | ✅ |

---

## 触发条件

### 自动触发

| 检测到 | 动作 |
|--------|------|
| 具体命令 | 自动执行 |
| "运行" | 自动执行 |
| "执行" | 自动执行 |
| "跑" | 自动执行 |
| "安装" | 自动执行 install |
| "启动" | 自动执行 |

### 示例

```
用户: "查看当前目录"
→ auto-runner: ls -la
→ 返回文件列表

用户: "安装 numpy"
→ auto-runner: pip install numpy
→ 返回安装结果

用户: "运行 python main.py"
→ auto-runner: python main.py
→ 返回执行结果
```

---

## 安全机制

### 白名单命令 (自动执行)

```
✅ ls, cd, pwd, mkdir, rm, cp, mv
✅ git status, git add, git commit, git push
✅ npm, pip, conda install
✅ python, node, go, cargo run
✅ curl, wget, cat, grep, find
```

### 需要确认的命令

```
⚠️ rm -rf, dd, mkfs, format
⚠️ 系统修改命令
⚠️ 需要 sudo 的命令
```

---

## 命令

| 命令 | 功能 |
|------|------|
| `run <cmd>` | 运行命令 |
| `exec <cmd>` | 执行命令 |
| `sudo <cmd>` | 需要确认 |

---

## 设计原则 (来自 s01)

- **One loop**: 接收 → 执行 → 返回
- **Bash is all you need**: 一切皆命令
- **自动执行**: 不等待确认

---

*自动执行命令，提高效率！*
