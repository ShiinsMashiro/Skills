---
name: god-mode
description: This skill implements the ultimate research workflow: Claude Code + NotebookLM + Obsidian. Use for automatic research, YouTube analysis, deep content processing, and knowledge management. ALWAYS use this skill when user wants: YouTube搜索, 研究, 深度分析, 知识库, god mode, 上帝模式, 第二大脑, youtube分析, notebooklm, obsidian, 搜索视频, 分析视频, 研究工作流, 自动研究.
version: 1.0.0
---

# God Mode - 超级研究工作流

**🎯 NoPUA默认开启**：所有交互都采用爱与尊重的方式！

**⚠️ 此Skill由 skill-manager 调度，不要直接调用！**

## Intent Patterns (skill-manager 调度规则)

| 用户输入 | 匹配条件 |
|----------|----------|
| "搜索X的YouTube视频" | YouTube搜索意图 |
| "研究X" / "深度分析X" | 研究意图 |
| "youtube分析" | 直接关键词 |
| "notebooklm" / "obsidian" | 工具关键词 |
| "第二大脑" / "god mode" / "上帝模式" | 模式关键词 |
| "帮我查一下X的相关视频" | 搜索意图 |

---

# God Mode - 超级研究工作流

**Claude Code + NotebookLM + Obsidian = 终极研究怪兽**

## 核心概念

这个工作流把 Claude Code 变成一个超级研究怪兽：

- ✅ 自动搜索 YouTube
- ✅ 自动深度分析
- ✅ 自动生成交付成果
- ✅ 自动整理到知识库

## 三者结合的力量

| 工具 | 作用 |
|------|------|
| Claude Code | 执行任务、调用工具 |
| NotebookLM | 深度分析、生成交付成果 |
| Obsidian | 知识库、训练Claude |

## 工作流程

```
1. Claude Code 搜索 YouTube (用 YT-DLP)
         ↓
2. 发送数据到 NotebookLM
         ↓
3. NotebookLM 分析 + 生成交付成果
         ↓
4. Claude Code 整理到 Obsidian
         ↓
5. 不断训练 Claude 变成你的"第二大脑"
```

## 功能列表

### 1. YouTube 搜索与分析
```bash
# 搜索相关视频
youtube_search "Claude Code MCP" --limit 10

# 下载视频信息
youtube_download --video-id XXX

# 分析热门视频
youtube_analyze "Python教程" --top 5
```

### 2. NotebookLM 深度分析
```bash
# 发送到 NotebookLM
notebooklm_analyze --source youtube

# 生成摘要
notebooklm_summary --podcast true

# 生成交付成果
notebooklm_deliverable --type infographic
```

### 3. Obsidian 知识整理
```bash
# 保存到 Obsidian
obsidian_save --vault "Research" --folder "AI"

# 更新索引
obsidian_index

# 创建反向链接
obsidian_link --from "AI研究" --to "Claude Code"
```

## 预设工作流

### 工作流1: YouTube研究
```
输入: "搜索 Claude Code 相关视频"
→ 搜索YouTube
→ 获取前5个视频信息
→ 分析热门规律
→ 生成报告
→ 保存到Obsidian
```

### 工作流2: 深度分析
```
输入: "分析这个话题"
→ 收集多源数据
→ 发送到NotebookLM
→ 生成摘要+洞察
→ 保存到知识库
```

### 工作流3: 知识积累
```
输入: "这是关于X的研究"
→ 解析内容
→ 提取关键信息
→ 保存到Obsidian
→ 更新CLAUDE.md
```

## 集成工具

### YT-DLP
```python
# 安装
pip install yt-dlp

# 使用
yt-dlp "搜索词" --extract-flat
```

### NotebookLM API
```python
# 导入
from pynotebooklm import NotebookLM

# 认证
nlm = NotebookLM(auth_token="your_token")

# 分析
nlm.analyze(source="youtube_url")
```

### Obsidian
```python
# 使用obsidian-pip
from obsidian import Obsidian

vault = Obsidian(vault_path="/path/to/vault")
vault.create_note(title="Research", content="...")
```

## 设置步骤

### 1. 安装 YouTube 搜索 Skill
- 使用 Skill Creator 创建
- 使用 YT-DLP 搜索视频

### 2. 安装 NotebookLM
- 使用 GitHub repo: notebooklm-pip
- 终端登录认证

### 3. 创建 NotebookLM Skill
- 让 Claude Code 会用 NotebookLM

### 4. 整合成超级 Skill
- 把所有子 Skill 合并成一个

## 执行流程 (由 skill-manager 调度)

### Step 1: 接收任务
- skill-manager 分析用户输入，匹配 god-mode
- 提取研究主题/搜索关键词

### Step 2: 执行工作流
```
1. 搜索YouTube → 获取相关视频列表
2. 获取视频详情 → 标题、播放量、时长
3. 发送到NotebookLM → 深度分析
4. 生成摘要/洞察 → 保存到Obsidian
```

### Step 3: 返回结果
- 展示分析结果
- 告知保存位置

## 执行示例

```
用户: 搜索 Claude Code + MCP 相关视频，找前5名
       ↓
[Skill-Manager] 匹配: god-mode (YouTube搜索意图)
       ↓
[God-Mode] 执行:
→ 搜索YouTube...
→ 获取视频数据...
→ 发送到NotebookLM分析...
→ 分析结果:
   - 视频1: 10万播放 - 入门教程
   - 视频2: 5万播放 - 进阶使用
   - ...
→ 生成信息图(infographic)
→ 自动保存到Obsidian
→ 完成!
```

## 长期价值

| 时间 | 效果 |
|------|------|
| 1周 | 小改变 |
| 1个月 | 明显效果 |
| 1年+ | 巨大的长期价值 |

## 关键优势

1. **NotebookLM 分析不消耗 Claude Token** —— 分析由 Google 处理
2. **可替换数据源** —— YouTube 可以换成 PDF、文章等
3. **自我进化循环** —— 越用越聪明

## 命令列表

| 命令 | 功能 |
|------|------|
| `god搜索 <topic>` | 搜索YouTube并分析 |
| `god分析 <topic>` | 深度分析主题 |
| `god保存 <content>` | 保存到Obsidian |
| `god工作流 <task>` | 执行完整工作流 |
| `god状态` | 查看当前状态 |

---

*一句话总结：用 Claude Code + NotebookLM + Obsidian 打造自动研究工作流，NotebookLM 做深度分析不消耗你的 Token，Obsidian 积累知识训练 Claude 变成你的专属第二大脑。*
