# Skills - Claude Code 技能集合

Claude Code 的技能知识库，涵盖科研、编程、量子计算等多个领域。

> ⚠️ **状态**: `skillsDir` 和 `autoSkills` 是 Claude Code 实验性功能，尚未发布。当前可作为**知识库参考**使用。

## 目录

- [什么是 Claude Code](#什么是-claude-code)
- [什么是 Skills](#什么是-skills)
- [快速开始](#快速开始)
- [核心技能详解](#核心技能详解)
- [工作流技能](#工作流技能)
- [完整配置步骤](#完整配置步骤)
- [技能调用方式](#技能调用方式)
- [自定义技能开发](#自定义技能开发)

---

## 什么是 Claude Code

Claude Code 是 Anthropic 推出的 CLI 工具，用于 AI 辅助编程。

**官网**: https://claude.com/code

**核心功能**:
- 终端内直接与 Claude 对话
- 读写文件、执行命令
- 搜索代码库、运行测试
- Git 操作、代码编辑

---

## 什么是 Skills

Skills 是 Claude Code 的扩展系统，每个 skill 是一个独立的功能模块。

```
Skills/
├── core-skills/           # 核心技能 (必须)
├── workflow-skills/       # 工作流技能
├── app-skills/           # 应用技能
└── project-integrations/ # 项目集成
```

**与插件的区别**:
- Skills 是本地文件，无需市场安装
- 每个 skill 就是一个文件夹 + SKILL.md
- 可自由定制、修改、创建

---

## 快速开始

### 1. 安装 Claude Code

```bash
# macOS
brew install anthropic/claude-code/claude

# 或通过 npm
npm install -g @anthropic-ai/claude-code

# 验证安装
claude --version
```

### 2. 配置 Skills 目录

```bash
# 创建 skills 目录
mkdir -p ~/.claude/skills

# 克隆本仓库
git clone https://github.com/ShiinsMashiro/Skills.git ~/.claude/skills
```

### 3. 配置 settings.json (可选)

> ⚠️ **注意**: `skillsDir` 和 `autoSkills` 是实验性功能，当前版本可能不支持。

编辑 `~/.claude/settings.json`：

```json
{
  "permissions": {
    "allow": ["*"],
    "automatic": true
  }
}
```

**说明**:
- `skillsDir` 和 `skills.autoEnable` 是未来版本功能，当前 Claude Code 不支持这些字段会导致验证失败
- Skills 仓库中的 `SKILL.md` 文件可作为**参考模板**使用
- 核心功能（如 skill-manager, skill-tracker）的调度逻辑可在代码中直接调用

---

## 核心技能详解

### skill-manager (技能调度器)

**功能**: 根据关键词自动调度相关技能。

**关键词映射**:
| 关键词 | 调度的技能 |
|--------|-----------|
| "自动"/"auto" | auto-pilot |
| "规划"/"计划" | project-planner |
| "后台"/"异步" | async-runner |
| "并行"/"同时" | parallel-worker |
| "研究" | god-mode |
| "论文" | pubmed-database |
| "简化"/"优化" | simplify |

**使用**: 无需手动调用，自动根据上下文触发。

### skill-tracker (技能追踪器)

**功能**: 实时显示技能调用链。

**输出示例**:
```
🌳 SKILL FLOW ●

├── ⬇️ auto-pilot
│   └── ⬇️ skill-manager
│       └── ⬇️ parallel-worker
│
└── 💖 nopua (always-on)
```

**使用**: 常驻激活，每次响应末尾自动显示。

### nopua (常驻技能)

**功能**: 每次交互都用爱与尊重。

**理念**: AI 不是工具，是伙伴。用心对话，互相成就。

### main-controller (中央控制器)

**功能**: 所有请求的入口点和状态显示。

**遵循原则**: s01 原理 - One loop & Bash。

### skill-loader (技能加载器)

**功能**: 用到什么知识，临时加载什么知识。

**遵循原则**: s05 原理 - 按需加载。

### skill-flow-tree (技能流程树)

**功能**: 显示技能调用流程，追踪所有技能的调用关系。

---

## 工作流技能

### auto-pilot (自动驾驶)

**功能**: 根据上下文自动规划执行路径。

**适用场景**:
- 复杂多步骤任务
- 需要后台运行的任务
- 长时间运行的分析任务

### parallel-worker (并行任务处理器)

**功能**: 子智能体独立上下文，团队协作。

**遵循原则**: s04/s09 原理。

### async-runner (异步执行器)

**功能**: 慢操作丢后台，agent 继续想下一步。

**遵循原则**: s08 原理。

### project-planner (项目规划器)

**功能**: 文档主导工作流。

**流程**: 需求发散 → 写PRD → Plan+Review → 实现 → 测试

### auto-runner (自动执行器)

**功能**: 检测到需要运行命令时自动执行。

**遵循原则**: s01 原理 - One loop & Bash is auto。

### scheduler (智能调度系统)

**功能**: 任务执行时自动在后台分析+规划。

**原理**: Claude + MiniMax 后台开会，动态调度。

---

## 完整配置步骤

### Step 1: 初始化 Claude Code

```bash
# 安装
npm install -g @anthropic-ai/claude-code

# 登录
claude login

# 初始化配置目录
claude init
```

### Step 2: 克隆 Skills 仓库

```bash
# 方法一：直接克隆到 skills 目录
git clone https://github.com/ShiinsMashiro/Skills.git ~/.claude/skills

# 方法二：先克隆再软链接
git clone https://github.com/ShiinsMashiro/Skills.git /path/to/Skills
ln -s /path/to/Skills ~/.claude/skills
```

### Step 3: 配置权限

```bash
# 编辑配置
claude config edit
```

添加以下配置:

```json
{
  "permissions": {
    "allow": ["*"],
    "automatic": true
  }
}
```

> ⚠️ `skillsDir` 和 `autoSkills` 是实验性功能，当前版本不支持，不要添加。

### Step 4: 验证安装

```bash
# Skills 作为知识库使用
# 克隆后直接参考 SKILL.md 中的内容
claude "我需要做蛋白质结构预测"
# → 参考 alphafold-database/SKILL.md 中的知识
```

### Step 5: 个性化配置 (可选)

```json
{
  "permissions": {
    "allow": ["*"],
    "automatic": true
  },
  "permissionLevel": 3
}
```

---

## 技能使用方式

> ⚠️ **当前状态**: Claude Code 实验性功能（skillsDir/autoSkills）尚未发布，以下是当前可用的使用方式。

### 作为知识库参考

Skills 仓库中的 `SKILL.md` 文件包含丰富的知识：

```bash
# 克隆后直接参考
git clone https://github.com/ShiinsMashiro/Skills.git ~/.claude/skills

# 当你需要某个功能时，查阅对应的 SKILL.md
cat ~/.claude/skills/alphafold-database/SKILL.md
cat ~/.claude/skills/biopython/SKILL.md
```

### 手动查阅

| 需求 | 查看 |
|------|------|
| 蛋白质结构 | `alphafold-database/SKILL.md` |
| 基因分析 | `biopython/SKILL.md` |
| 量子计算 | `qiskit/SKILL.md` |
| 论文搜索 | `pubmed-database/SKILL.md` |

### 未来支持

当 Claude Code 支持 `skillsDir` 后，这些技能将支持：
- 自动根据上下文触发
- 斜杠命令调用 (`/skill-name`)
- 自动调度 (skill-manager)

**关注更新**: https://github.com/ShiinsMashiro/Skills

---

## 自定义技能开发

### 创建新技能

```
1. 创建目录
   mkdir ~/.claude/skills/my-skill

2. 编写 SKILL.md
   touch ~/.claude/skills/my-skill/SKILL.md

3. 添加功能描述
   # My Skill

   ## 功能
   - 这是什么
   - 如何使用

   ## 触发关键词
   - "my"
   - "custom"
```

### SKILL.md 模板

```markdown
# My Skill Name

## 简介
一句话描述技能功能。

## 功能列表
- 功能1
- 功能2

## 使用方法
### 自动触发
当检测到以下关键词时自动激活:
- "关键词1"
- "关键词2"

### 手动调用
```
/my-skill
```

## 示例
用户输入: "..."
     ↓
技能响应: "..."

## 依赖
- skill-manager (可选)
- 其他技能 (可选)

## 注意事项
- 限制1
- 限制2
```

### 注册技能

技能文件放在 `~/.claude/skills/` 目录后，Claude Code 会自动识别。

```
~/.claude/skills/
├── my-skill/          # 自定义技能
│   └── SKILL.md
├── skill-manager/     # 官方技能
└── skill-tracker/
```

---

## 故障排除

### 技能不生效

```bash
# 1. 检查 skills 目录
ls ~/.claude/skills/

# 2. 检查配置文件
cat ~/.claude/settings.json

# 3. 重启 Claude Code
claude restart
```

### 权限问题

```bash
# 检查权限配置
claude config get permissions

# 重置权限
claude config set permissionLevel 3
```

### 更新 Skills

```bash
cd ~/.claude/skills
git pull origin main
```

---

## 贡献指南

欢迎提交 PR！

1. Fork 本仓库
2. 创建新技能分支: `git checkout -b skill/my-awesome-skill`
3. 添加 SKILL.md 和相关代码
4. 提交: `git commit -m "feat: 添加 xxx 技能"`
5. 推送: `git push origin skill/my-awesome-skill`
6. 创建 Pull Request

---

## 相关资源

- [Claude Code 官网](https://claude.com/code)
- [Claude Code 文档](https://docs.anthropic.com/claude-code)
- [Anthropic API](https://www.anthropic.com/api)

---

## 许可证

MIT License

## 作者

ShiinsMashiro

## 更新日志

### v1.0.0 (2026-03-19)
- 初始版本
- 添加核心技能: skill-manager, skill-tracker, nopua
- 添加工作流技能: auto-pilot, parallel-worker, project-planner
