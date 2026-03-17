---
name: god-mode
description: |
  超级研究工作流 - Claude Code + YouTube + NotebookLM + Obsidian + WebFetch。
  搜索、分析、保存一体化。自动执行 WebFetch 获取最新信息。
version: 2.1.0
---

# God Mode (超级研究)

**Claude Code + YouTube + NotebookLM + Obsidian + WebFetch = 研究怪兽**

## 核心原理

```
用户: "研究 X"

1. WebFetch 自动获取 → 官方文档/最新信息
       ↓
2. YouTube 搜索 → 视频教程
       ↓
3. NotebookLM 分析 → 深度洞察
       ↓
4. Obsidian 保存 → 知识积累
       ↓
5. 变成你的第二大脑
```

---

## 自动执行 (Auto-Execute)

### WebFetch 自动执行
```
收到研究任务 → 自动执行 WebFetch:
  - 官方文档 (docs.godotengine.org)
  - 最新教程
  - GitHub issues
  - 最佳实践

无需等待用户确认 → 自动获取最新信息
```

### 触发条件

| 关键词 | 自动执行 |
|--------|----------|
| "研究" / "research" | WebFetch + YouTube |
| "分析" / "analyze" | WebFetch 深度获取 |
| "工作流" / "workflow" | WebFetch 最佳实践 |
| "教程" / "tutorial" | YouTube 搜索 |

---

## 工作流 (自动执行)

### 1. WebFetch 自动获取
```
# 自动获取多个来源
- 官方文档
- 最佳实践
- GitHub issues
- Stack Exchange
```
**无需用户确认 → 自动执行**

### 2. YouTube 搜索 (可选)
```bash
youtube_search "关键词" --limit 10
```

### 3. NotebookLM 分析 (可选)
```bash
notebooklm_analyze --source youtube
```

### 4. Obsidian 保存
```bash
obsidian_save --vault "Research" --folder "Topic"
```

---

## 命令

| 命令 | 功能 |
|------|------|
| `god搜索 <topic>` | 搜索并分析 (自动WebFetch) |
| `god分析 <topic>` | 深度分析 (自动WebFetch) |
| `god保存 <content>` | 保存到知识库 |
| `god <topic>` | 快速研究 (自动执行) |

---

## 价值

| 时间 | 效果 |
|------|------|
| 1周 | 小改变 |
| 1个月 | 明显效果 |
| 1年 | 第二大脑 |

---

## 设计原则

1. **自动执行**: WebFetch 立即执行，不等待
2. **信息充分**: 收集多个来源
3. **后台不阻塞**: 慢操作丢后台
4. **知识积累**: 自动保存到 Obsidian

---

*Claude Code + WebFetch + YouTube + NotebookLM + Obsidian = 全自动研究怪兽*
