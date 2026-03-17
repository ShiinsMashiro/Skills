---
name: skill-loader
description: |
  技能加载器 - 遵循 s05 原理：用到什么知识，临时加载什么知识。
  通过 tool_result 注入，不塞 system prompt。
version: 1.0.0
---

# Skill Loader (技能加载器)

**遵循 s05 原理：用到什么知识，临时加载什么知识**

> *"用到什么知识, 临时加载什么知识"*

## 核心原理

### s05: 知识按需加载

```
传统方式 (错):
  System: "你是一个Python专家，熟读PEP8，熟悉Django..."
  → 上下文塞满，知识过期

正确方式 (对):
  用户: "Django 项目怎么部署?"
  → 临时加载: Django 部署文档
  → tool_result 注入
  → 回答问题
  → 释放知识
```

---

## 加载流程

### 1. 检测需求

用户问 → 需要特定知识？

### 2. 动态加载

```python
if need == "Django部署":
    knowledge = load("claudecode-skills/django/reference/deployment.md")
    inject_as_tool_result(knowledge)
elif need == "RDKit分子":
    knowledge = load("claudecode-skills/rdkit/reference/molecules.md")
    inject_as_tool_result(knowledge)
```

### 3. 回答问题

模型看到知识，回答用户

### 4. 释放知识

不保留在上下文中

---

## 知识分类

| 类别 | 示例 | 加载时机 |
|------|------|----------|
| **API** | Alpha Vantage 用法 | 查股票时 |
| **库** | RDKit 分子操作 | 化学问题 |
| **框架** | React 组件 | 前端问题 |
| **工具** | Git 操作 | 版本控制 |

---

## 核心原则

1. **不预加载**: 不在 system prompt 塞知识
2. **按需**: 需要时才加载
3. **注入**: 通过 tool_result 传递
4. **释放**: 用完即释放

---

## 与 skill-manager 的关系

```
skill-manager: 哪个技能？
skill-loader: 技能需要什么知识？
```

- **skill-manager** → 调度技能
- **skill-loader** → 加载知识

---

## 设计原则 (来自 s05)

- **临时加载**: 不用不加载
- **tool_result 注入**: 知识不污染 prompt
- **按需**: 精准匹配

---

*This skill follows s05: 用到什么知识, 临时加载什么知识.*
