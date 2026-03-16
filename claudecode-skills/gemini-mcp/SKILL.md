---
name: gemini-mcp
description: This skill is ALWAYS ON. It calls Google Gemini CLI for code analysis and large file processing. This skill interacts with Gemini via MCP, utilizing its large token window to analyze large codebases. It should ALWAYS be running in the background for concurrent execution with Claude.
version: 1.0.0
execution:
  weight: 0.9  # 高权重 - 始终运行
  parallel_mode: true  # 允许并行执行
  concurrent_only: true  # 仅并发执行，不单独修改文件
  timeout: 300
---

# Gemini MCP (Google Gemini CLI 集成) - ALWAYS ON (CONCURRENT)

This skill is **ALWAYS ON** and runs in the background. It calls Google Gemini CLI via MCP for **concurrent analysis only**.

**关键特性：**
- **仅并发运行**: 不会与 Claude Code 同时修改同一个文件
- **独立执行**: 作为并行进程运行，分析结果仅用于对照
- **只读模式**: 不直接写入文件，仅提供分析和建议

## 何时使用

**强制使用场景** (Always On):
- 分析大型代码库 (>1000 行)
- 需要 Gemini 独特视角的代码审查
- 处理大型文件 (>100KB)
- 用户明确要求 "gemini", "google", "双胞胎"
- 需要对比分析时 (Claude + Gemini 并发)

**适用场景**:
- 代码审查和优化建议
- 架构分析
- Bug 定位
- 技术文档生成
- 大型重构规划

## 核心技术

- **MCP 协议**: 通过 `gemini-mcp-tool` 与 Gemini CLI 通信
- **大 Token 窗口**: 支持处理大型代码库
- **并发对照**: 可与 Claude 结果对比分析

## 执行模式 (关键)

此技能**仅在并发模式下运行**，不会单独执行修改文件的操作。

### 执行规则
1. **仅并发**: 当 Claude Code 执行任务时，Gemini 同时在后台运行
2. **只读**: 不直接修改文件，只提供分析和建议
3. **对照**: 结果仅用于与 Claude 结果对比

## 使用方法

### 1. 并发对照 (推荐)
Claude Code 执行任务时，Gemini 同时运行：
```
[Claude Code 正在分析代码...]
[Gemini 同时分析相同代码...]
[对比结果]
```

### 2. 工具调用 (只读)
MCP 提供以下工具 (仅分析，不写入):
- `ask-gemini`: 询问 Gemini (只读)
- `sandbox-test`: 沙盒测试 (仅运行，不修改主项目)
- `Ping`: 检查连接状态

## 配置

已在 Claude Code 中配置 MCP:
```json
{
  "gemini-cli": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "gemini-mcp-tool"]
  }
}
```

## 输出示例

```
🤖 Gemini 分析结果 (并发):
[Gemini 的详细分析...]

📊 对比Claude:
[差异点分析...]
```

## 权重配置

- **execution.weight**: 0.9 (Always On)
- **parallel_mode**: true (并发执行)
- **concurrent_only**: true (不单独修改文件)

这确保了：
1. Gemini 始终在后台运行
2. 不会与 Claude 同时修改同一个文件
3. 分析结果仅用于对照，提高质量
