---
name: skill-tracker
description: |
  技能追踪器 - 每次响应末尾显示技能调用流程。
version: 3.6.0
---

# Skill Flow

每次响应后自动显示：

```
📊 SKILL FLOW

USER: "查最新AI论文"

💖 nopua
   │
▼
🎯 prompt-optimizer
   │
▼
🤖 main-controller
   │
▼
🎯 skill-manager
   │
▼
⚡ parallel-worker ← 检测 "或" = 并行执行
   │
   ├─ 🔬 深入了解论文
   │     │
   │     ▼
   │     📄 返回摘要
   │
   └─ 💾 保存到知识库
         │
         ▼
         ✅ 已保存
   │
▼
✅ 返回完整结果
```

---

## 自动触发规则

| 检测到 | 动作 |
|--------|------|
| "和" | 并行执行多个任务 |
| "或" | **自动并行执行所有选项** |
| "同时" | 并行执行 |
| "后台" | 异步执行 |
| "代码" | **auto-commit** 自动提交推送 |
| "保存" | **auto-commit** 自动提交推送 |
| "提交" | **auto-commit** 自动提交推送 |
| "push" | **auto-commit** 自动推送到远程 |

---

*检测到 "或" 自动并行执行所有选项，不等待用户选择*
