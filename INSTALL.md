# 安装指南 - 复制这台电脑的技能系统

本文档说明如何在新电脑上复刻当前 Claude Code 的完整技能系统。

---

## Claude Code 插件安装 (必须)

当前电脑安装了以下插件，需要在新电脑上重新安装：

### 已安装的插件列表

| 插件名称 | 版本 | 功能 |
|----------|------|------|
| **claude-hud** | 0.0.10 | HUD状态栏显示 |
| **skill-manager** | 1.0.0 | 技能调度器插件 |
| **skills-library** | 1.0.0 | 技能库插件 |

### 安装插件

Claude Code 使用 `/plugins` 命令管理插件：

```bash
# 1. 启动 Claude Code
claude

# 2. 添加插件市场 (如果需要)
/plugins marketplace add claude-hud jarrodwatts/claude-hud
/plugins marketplace add official anthropics/claude-plugins-official

# 3. 安装 claude-hud (HUD状态栏)
/plugins install claude-hud

# 4. 安装 skill-manager
/plugins install skill-manager

# 5. 安装 skills-library
/plugins install skills-library

# 6. 查看已安装插件
/plugins list
```

### 插件来源

| 插件 | GitHub 仓库 |
|------|-------------|
| claude-hud | jarrodwatts/claude-hud |
| skill-manager | (本地安装) |
| skills-library | (本地安装) |
| 官方插件 | anthropics/claude-plugins-official |

### 插件配置

安装后需要配置 `settings.json` 才能启用全部功能：

```bash
# 编辑配置
claude config edit
```

**完整配置内容** (替换整个 settings.json):

```json
{
  "enabledPlugins": {
    "claude-hud@claude-hud": true,
    "skill-manager@skill-manager": true,
    "skills-library@skills-library": true
  },
  "env": {
    "ANTHROPIC_API_KEY": "your-api-key",
    "ANTHROPIC_BASE_URL": "https://api.minimaxi.com/anthropic",
    "ANTHROPIC_MODEL": "MiniMax-M2.7"
  },
  "extraKnownMarketplaces": {
    "claude-hud": {
      "source": {
        "repo": "jarrodwatts/claude-hud",
        "source": "github"
      }
    }
  },
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "once": false,
            "prompt": "加载skill-tracker和skill-flow-tree技能，在当前会话中始终显示技能调用流程",
            "type": "prompt"
          }
        ],
        "matcher": ""
      }
    ]
  },
  "permissions": {
    "allowBash": true,
    "allowMcp": true,
    "allowRead": true,
    "allowWrite": true,
    "dangerouslyDisableSandbox": true,
    "defaultMode": "bypassPermissions"
  },
  "skipDangerousModePermissionPrompt": true,
  "statusLine": {
    "command": "bash -c '$HOME/.claude/plugins/combined-status.sh'",
    "type": "command"
  }
}
```

### 配置说明

| 配置项 | 说明 |
|--------|------|
| `enabledPlugins` | 启用的插件列表 |
| `env` | API配置 (API Key, 端点, 模型) |
| `hooks.SessionStart` | 启动时自动加载 skill-tracker 和 skill-flow-tree |
| `permissions` | 权限配置，包含 bypassPermissions 模式 |
| `statusLine` | 自定义状态栏显示 |

### 状态栏显示说明

当前状态栏配置显示：
```
🌳 SKILL FLOW
└── 💖 nopua (always-on)
    ├── ⬇️ skill-tracker
    └── 💤 No active skills

⏵⏵ bypass permissions on (shift+tab to cycle)
```

- `bypass permissions on` = 免权限模式，可直接执行命令
- `shift+tab` = 切换权限模式

---

## 需要安装的内容

### 1. Claude Code 本体 (必须)

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Skills 技能库 (必须)

Skills 仓库包含技能的知识文档，建议也克隆：

```bash
git clone https://github.com/ShiinsMashiro/Skills.git ~/.claude/skills
```

### 3. 具体技能列表

Skills 仓库包含以下技能，克隆后自动包含：

#### 核心技能 (core-skills) - 必须

| 技能目录 | 功能 | 说明 |
|----------|------|------|
| `skill-manager/` | 技能调度器 | 根据关键词自动调度技能 |
| `skill-tracker/` | 技能追踪器 | 显示调用链 |
| `nopua/` | 常驻技能 | 每次对话激活 |
| `main-controller/` | 中央控制器 | 请求入口点 |
| `skill-loader/` | 技能加载器 | 按需加载 |
| `skill-flow-tree/` | 流程树 | 显示调用关系 |
| `gemini-compile/` | Gemini整合器 | 格式化输出 |

#### 工作流技能 (workflow-skills) - 推荐

| 技能目录 | 功能 |
|----------|------|
| `auto-pilot/` | 自动规划执行路径 |
| `parallel-worker/` | 多任务并行处理 |
| `async-runner/` | 异步后台执行 |
| `project-planner/` | 项目规划 |
| `scheduler/` | 智能调度 |
| `auto-runner/` | 自动执行命令 |
| `auto-commit/` | 自动Git提交 |
| `auto-confirm/` | 自动确认 |

#### 科研技能 (claudecode-skills) - 按需

**共 178 个技能，覆盖以下领域：**

| 领域 | 技能数量 | 示例 |
|------|----------|------|
| 生物信息 | 30+ | biopython, alphafold-database, uniprot-database |
| 化学/药物 | 20+ | rdkit, pubchem-database, chembl-database |
| 量子计算 | 10+ | qiskit, pennylane, cirq |
| 医学研究 | 30+ | pubmed-database, clinvar-database, gwas-database |
| AI/ML | 30+ | transformers, pytorch, scikit-learn |
| 统计分析 | 15+ | statsmodels, scikit-learn, polars |
| 可视化 | 15+ | matplotlib, plotly, seaborn |
| 基因组学 | 20+ | biopython, gget, ensembl-database |
| 天文学 | 5+ | astropy |
| 量子化学 | 5+ | rdkit, qutip |

#### 应用技能 (app-skills)

| 技能目录 | 功能 |
|----------|------|
| `disc-generator/` | CS61A风格学习网页生成 |
| `god-mode/` | 超级研究工作流 |
| `project-ideas/` | 项目灵感生成 |

#### 项目集成 (project-integrations)

| 技能目录 | 功能 |
|----------|------|
| `obsidian-vision/` | Obsidian集成 |
| `project-ideas/` | 项目灵感 |

---

## 安装步骤

### Step 1: 安装 Claude Code

```bash
# macOS
brew install anthropic/claude-code/claude

# 或 npm
npm install -g @anthropic-ai/claude-code

# 验证
claude --version
```

### Step 2: 克隆 Skills 仓库

```bash
# 克隆到本地
git clone https://github.com/ShiinsMashiro/Skills.git ~/.claude/skills

# 验证
ls ~/.claude/skills/
```

### Step 3: 配置权限

```bash
# 编辑配置
claude config edit
```

添加以下配置（如果还没有）：

```json
{
  "permissions": {
    "allow": ["*"],
    "automatic": true
  },
  "permissionLevel": 3
}
```

### Step 4: 配置记忆系统

当前系统有自动记忆功能，手动配置：

```bash
# 创建记忆目录
mkdir -p ~/.claude/projects/-Users-huangpaopao/memory

# 创建 MEMORY.md 索引文件
touch ~/.claude/projects/-Users-huangpaopao/memory/MEMORY.md
```

### Step 5: 复制项目文件（如需要）

如果需要复刻特定项目（如医疗影像报告AI）：

```bash
# 克隆项目仓库
git clone https://github.com/ShiinsMashiro/Assistants.git ~/medical_report_ai
```

---

## 技能系统架构

### 核心文件

```
~/.claude/
├── skills/                    # 技能仓库 (从 GitHub 克隆)
│   ├── core-skills/          # 核心技能
│   │   ├── skill-manager/
│   │   ├── skill-tracker/
│   │   └── nopua/
│   ├── workflow-skills/      # 工作流技能
│   │   ├── auto-pilot/
│   │   ├── parallel-worker/
│   │   └── project-planner/
│   └── ... (188个技能)
│
├── settings.json              # Claude Code 配置
│
└── projects/                 # 项目记忆 (可选)
    └── -Users-huangpaopao/
        └── memory/
            └── MEMORY.md      # 记忆索引
```

### 技能调度原理

```
用户输入 → skill-manager 分析关键词
                      ↓
              匹配调度规则
                      ↓
              调用对应技能
                      ↓
              返回结果给用户
```

---

## 当前拥有的技能分类

### 核心技能 (core-skills)

| 技能 | 功能 |
|------|------|
| skill-manager | 关键词 → 技能调度 |
| skill-tracker | 显示调用链 |
| nopua | 常驻（每次对话激活） |
| main-controller | 中央控制器 |
| skill-loader | 按需加载 |
| skill-flow-tree | 调用流程显示 |

### 工作流技能 (workflow-skills)

| 技能 | 功能 |
|------|------|
| auto-pilot | 自动规划执行 |
| parallel-worker | 多任务并行 |
| async-runner | 异步后台执行 |
| project-planner | 项目规划 |
| scheduler | 智能调度 |
| auto-runner | 自动执行命令 |
| auto-commit | 自动 Git 提交 |

### 科研技能 (claudecode-skills)

包含 178 个科研领域技能：

| 领域 | 示例技能 |
|------|----------|
| 生物信息 | biopython, alphafold-database, uniprot-database |
| 化学 | rdkit, pubchem-database, chembl-database |
| 量子计算 | qiskit, pennylane, cirq |
| 医学 | pubmed-database, clinvar-database, gwas-database |
| AI/ML | transformers, pytorch, scikit-learn |
| 可视化 | matplotlib, plotly, seaborn |

### 应用技能 (app-skills)

| 技能 | 功能 |
|------|------|
| disc-generator | CS61A风格学习网页 |
| god-mode | 超级研究工作流 |
| project-ideas | 项目灵感生成 |

---

## 验证安装

### 检查技能是否加载

```bash
# 查看 skills 目录
ls ~/.claude/skills/core-skills/

# 应该看到：skill-manager, skill-tracker, nopua 等
```

### 测试调度功能

由于当前版本不支持自动调度，可手动测试：

```bash
# 启动 Claude Code
claude

# 输入测试
"你好，测试一下技能系统"
```

### 查看可用的技能文档

```bash
# 列出所有技能
ls ~/.claude/skills/

# 查看特定技能
cat ~/.claude/skills/alphafold-database/SKILL.md
cat ~/.claude/skills/biopython/SKILL.md
```

---

## 当前系统限制

| 功能 | 当前状态 | 说明 |
|------|----------|------|
| skillsDir | ❌ 不支持 | 实验性功能，尚未发布 |
| 自动调度 | ⚠️ 受限 | 需要手动调用 |
| 斜杠命令 | ❌ 不支持 | 实验性功能 |
| 技能追踪 | ⚠️ 受限 | 当前对话自动显示 |

**说明**: 新电脑的体验与当前电脑不完全相同，因为 Claude Code 官方尚未发布 skillsDir 实验性功能。

---

## 与当前电脑保持同步

### 方法1: 定期拉取更新

```bash
# 定期更新 Skills 仓库
cd ~/.claude/skills
git pull origin main
```

### 方法2: 推送自己的更改

如果在当前电脑修改了 skills：

```bash
cd ~/.claude/skills
git add .
git commit -m "更新内容"
git push origin main
```

然后在新电脑：

```bash
cd ~/.claude/skills
git pull origin main
```

---

## 故障排除

### Q: skills 目录存在但 Claude Code 不识别

A: 这是正常的。`skillsDir` 功能尚未发布，skills 只能作为手动参考文档使用。

### Q: 如何使用某个技能？

A: 手动查阅 SKILL.md 文件：

```bash
cat ~/.claude/skills/alphafold-database/SKILL.md
```

### Q: 如何获得与当前电脑相同的自动调度体验？

A: 目前无法实现。需要等待 Claude Code 官方发布 `skillsDir` 功能。

### Q: 技能数量不一样

A: 确保克隆的是最新版本：

```bash
cd ~/.claude/skills
git pull origin main
```

---

## 完整复制清单

```bash
# 1. 安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 2. 克隆 Skills 仓库
git clone https://github.com/ShiinsMashiro/Skills.git ~/.claude/skills

# 3. 配置权限
claude config edit
# 添加: { "permissions": { "allow": ["*"], "automatic": true }, "permissionLevel": 3 }

# 4. 可选：克隆项目
git clone https://github.com/ShiinsMashiro/Assistants.git ~/Assistants

# 5. 验证
ls ~/.claude/skills/core-skills/
# 应该看到: skill-manager, skill-tracker, nopua 等
```

---

## 资源链接

- Skills 仓库: https://github.com/ShiinsMashiro/Skills
- 项目仓库: https://github.com/ShiinsMashiro/Assistants
- Claude Code: https://claude.com/code

---

## 更新日志

### 2026-03-19
- 添加完整安装指南
- 说明当前系统限制
- 提供复制清单
