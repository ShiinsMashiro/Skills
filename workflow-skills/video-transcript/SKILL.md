---
name: video-transcript
description: |
  视频转文稿技能 - 从视频提取字幕/文稿。
  支持 Bilibili、YouTube 等平台。
  获取文稿后可用于生成学习页面。
version: 1.0.0
---

# Video Transcript (视频转文稿)

**从视频提取字幕/文稿，用于生成学习内容**

## 支持的平台

| 平台 | 方法 | 说明 |
|------|------|------|
| Bilibili | API / 第三方工具 | 需要 BV 号 |
| YouTube | yt-dlp | 直接下载字幕 |
| 本地视频 | Whisper | 语音识别 |

## 核心功能

### 1. Bilibili 字幕获取

```python
# 方法1: 使用 Bilibili API
import requests

def get_bilibili_subtitle(bv_id):
    url = f"https://api.bilibili.com/x/player/pagelist?bvid={bv_id}"
    # 获取字幕CID
    # 返回字幕URL
```

### 2. YouTube 字幕下载

```bash
# 使用 yt-dlp
yt-dlp --write-subs --sub-lang zh-Hans "URL"
```

### 3. 语音转文字 (Whisper)

```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("video.mp4")
print(result["text"])
```

## 工作流

```
用户: "获取这个视频的文稿"
     │
     ▼
1. 分析视频平台 (Bilibili/YouTube/本地)
     │
     ▼
2. 获取字幕/音频
     │
     ▼
3. 格式化为文稿
     │
     ▼
返回文稿内容
```

## 命令

| 命令 | 功能 |
|------|------|
| `获取文稿 <url>` | 获取视频字幕 |
| `转文字 <file>` | 语音转文字 |
| `下载字幕 <url>` | 下载字幕文件 |

## 文稿格式

```markdown
# 课程标题

## 第一章
[文稿内容...]

## 第二章
[文稿内容...]
```

## 集成 disc-generator

获取文稿后，可以结合 disc-generator 生成学习页面：

```
文稿 → disc-generator → 学习网页
```

---

*视频转文稿，让学习更高效！*
