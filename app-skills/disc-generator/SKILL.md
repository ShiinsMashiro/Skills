---
name: disc-generator
description: |
  讨论课页面生成器 - 生成 CS61A 风格的学习网页。
  交互式练习、Monaco Editor 代码编辑器、可折叠解答。
version: 2.0.0
---

# Disc Generator (学习页面生成器)

**生成交互式学习网页，类似 CS61A 讨论课**

## 核心功能

### 1. 输入

```python
{
  "topic": "递归 (Recursion)",
  "level": "intermediate",
  "num_exercises": 5
}
```

### 2. 输出

生成完整的 HTML 页面：
- 章节组织结构
- 概念讲解
- 编程练习 (Monaco Editor)
- 可折叠解答
- 学习目标

---

## 工作流

```
1. 接收主题
       ↓
2. 生成概念讲解
       ↓
3. 生成练习题
       ↓
4. 生成测试用例
       ↓
5. 打包 HTML
```

---

## 使用

```
"帮我生成一个学习'递归'的页面"
"生成 Python 函数练习页面"
```

---

## 设计原则

- **s02**: 一个 skill 专注一件事
- **按需**: 只生成用户需要的内容

---

*专注生成交互式学习页面.*
