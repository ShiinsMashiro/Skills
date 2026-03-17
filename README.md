# Claude Code Super Skills (CoreClaudeSkills)

基于 learn-claude-code agent 原理 + NoPUA 爱与尊重交互 + Claude + MiniMax 并行研究

---

## 核心架构

```
📊 SKILL FLOW

USER: "研究AI论文"

💖 nopua              ← 常驻：用爱与尊重
   │
▼
🎯 prompt-optimizer   ← 优化用户输入
   │
▼
🤖 main-controller   ← 入口
   │
▼
🎯 skill-manager     ← 调度中心
   │
▼
⚡ parallel-worker   ← Claude + Gemini/MiniMax 并行
   │
   ├─ 🤖 Claude Code  搜索
   └─ 🌟 MiniMax     整理
   │
▼
🌟 gemini-compile    ← 整合结果
   │
▼
✅ 返回结果
```

---

## 技能列表

### 核心技能 (Core Skills)

| 技能 | 原理 | 说明 |
|------|------|------|
| **nopua** | 常驻 | 爱与尊重的交互方式 |
| **prompt-optimizer** | - | 优化用户输入 |
| **main-controller** | s01 | 中央入口 |
| **skill-manager** | s02 | 动态调度 |
| **skill-tracker** | - | 显示调用流程 |
| **gemini-compile** | - | MiniMax 整合结果 |
| **skill-flow-tree** | - | 逻辑树显示 |
| **skill-loader** | s05 | 按需加载知识 |

### 工作流技能 (Workflow Skills)

| 技能 | 原理 | 说明 |
|------|------|------|
| **auto-pilot** | s03+s08 | 自动驾驶 |
| **project-planner** | s03 | 任务规划 |
| **parallel-worker** | s04+s09 | 并行处理 |
| **async-runner** | s08 | 后台任务 |

### 应用技能 (App Skills)

| 技能 | 说明 |
|------|------|
| **god-mode** | 研究模式 |
| **disc-generator** | 学习页面生成 |

### 项目集成

| 技能 | 说明 |
|------|------|
| **gitnexus-assistant** | 代码分析 |
| **project-ideas** | 项目创意 |

---

## Agent 原理 (来自 learn-claude-code)

| 课程 | 原理 | 实现 |
|------|------|------|
| s01 | One loop & Bash | main-controller |
| s02 | 加一个工具，一个 handler | skill-manager dispatch map |
| s03 | 没有计划走哪算哪 | project-planner + TodoWrite |
| s04 | 子智能体独立上下文 | parallel-worker |
| s05 | 用到什么加载什么 | skill-loader |
| s08 | 慢操作丢后台 | async-runner |
| s09 | 任务分给队友 | parallel-worker 团队 |

---

## 自动触发规则

### 关键词检测

| 关键词 | 触发技能 |
|--------|----------|
| "自动" | auto-pilot |
| "研究" | god-mode + parallel-worker |
| "并行" | parallel-worker |
| "和" | 分割任务 + 并行 |
| "或" | **自动并行执行所有选项** |
| "后台" | async-runner |

### 示例

```
用户: "查前列腺癌和肺癌论文"
→ 检测到 "和"
→ parallel-worker 自动分割:
   - 任务1: 前列腺癌
   - 任务2: 肺癌
→ 并行搜索 → 合并结果

用户: "查论文或保存"
→ 检测到 "或"
→ 自动并行执行:
   - 查论文 ✅
   - 保存到知识库 ✅
```

---

## NoPUA 原则

**常驻激活**，每次交互都用爱与尊重：

| 传统方式 | NoPUA 方式 |
|----------|------------|
| "赶紧的" | "我相信你能" |
| "这都不会?" | "你可以的" |
| "失败就完了" | "信任你的能力" |

---

## Claude + MiniMax 并行

### 工作流

1. **用户输入** → prompt-optimizer 优化
2. **skill-manager** 调度
3. **parallel-worker** 分割任务
4. **Claude Code** 执行任务
5. **MiniMax** 整理结果
6. **gemini-compile** 格式化输出

### MiniMax 配置

API Key: 用户自定义
模型: MiniMax-M2.5
端点: https://api.minimax.chat/v1

---

## 安装

```bash
# 克隆项目
git clone https://github.com/你的用户名/coreclaudeskills.git

# 进入目录
cd coreclaudeskills

# 在 Claude Code 中打开
claude .
```

---

## 使用

### 自动驾驶

```
"自动"
→ auto-pilot 启动
→ 等待任务
```

### 研究模式

```
"研究最新的AI论文"
→ Claude 搜索 PubMed
→ MiniMax 整理结果
→ 返回表格
```

### 并行执行

```
"查癌症和糖尿病论文"
→ 自动分割任务
→ 并行搜索
→ 合并结果
```

---

## 项目结构

```
coreclaudeskills/
├── .claude/              # Claude Code 配置
├── core-skills/         # 核心技能
│   ├── nopua/           # 爱与尊重
│   ├── skill-manager/   # 调度中心
│   ├── skill-tracker/  # 流程显示
│   ├── gemini-compile/  # 结果整合
│   └── ...
├── workflow-skills/      # 工作流
│   ├── auto-pilot/
│   ├── parallel-worker/
│   └── ...
├── app-skills/          # 应用技能
├── project-integrations/ # 项目集成
├── claudecode-skills/   # 150+ 技能包
└── README.md
```

---

## 更新日志

### v3.6.0 (2026-03-17)
- 新增 "或" 自动并行执行
- 优化 skill flow 显示
- 集成 MiniMax 整理结果

### v3.0.0
- 基于 learn-claude-code 优化
- NoPUA 常驻
- Claude + MiniMax 并行

---

## 许可证

MIT License

---

*用 Claude Code + 爱与尊重打造超级研究助手！*
