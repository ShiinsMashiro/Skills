---
name: obsidian-vision
description: This skill should be used when the user asks about "Obsidian截图", "vision recall", "截图知识库", "AI截图", "obsidian plugin", "图片笔记", "视觉记忆", "screenshot OCR", or wants to use or develop the Obsidian Vision Recall plugin.
version: 1.0.0
---

# Obsidian Vision Recall

Obsidian Vision Recall是一个Obsidian插件，自动处理截图并用AI生成描述，帮助建立视觉知识库。

## When This Skill Applies

This skill activates when the user wants to:
- Use the Vision Recall plugin
- Set up the plugin
- Configure AI providers
- Process screenshots automatically
- Build a visual knowledge base
- Develop the plugin

## Features

### Automatic Processing
- **Folder Monitoring**: 自动处理指定文件夹中的截图
- **Periodic Checks**: 定期检查新截图
- **Clipboard Upload**: 从剪贴板快速上传
- **File Upload**: 从文件上传

### AI Integration
- **Multiple Providers**: 支持多种AI提供商
- **Custom Prompts**: 自定义提示词
- **OCR Support**: 文字识别

### Obsidian Integration
- **Deep Links**: 通过深度链接捕获
- **Vault Integration**: 与Obsidian vaults集成
- **Metadata**: 自动添加元数据

## Setup Instructions

1. 安装插件
2. 配置AI Provider (OpenAI, Claude, Ollama, LM Studio等)
3. 设置Intake Folder
4. 开始截图！

## Supported AI Providers

- OpenAI
- Anthropic (Claude)
- Ollama (本地)
- LM Studio (本地)
- Azure OpenAI

## Usage Examples

- "如何安装Vision Recall插件"
- "配置Ollama作为AI提供商"
- "如何自动处理截图"
- "Vision Recall支持哪些AI"

## Documentation

- 官网: https://visionrecall.com/
- 设置指南: `src/docs/`
- Ollama配置: `src/docs/ollama-setup.md`
- LM Studio: `src/docs/lm-studio.md`

## Note

这是一个Obsidian第三方插件，需要从GitHub releases安装。
