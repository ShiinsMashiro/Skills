---
name: video-transcript
description: |
  视频转文稿技能 - 使用 Whisper AI 将视频/音频转写为文字。
  支持 Bilibili、YouTube、本地视频。
  自动生成学习笔记。
version: 2.0.0
---

# Video Transcript (视频转文稿)

**使用 Whisper AI 将视频/音频转写为文字**

## 支持的平台

| 平台 | 方法 | 说明 |
|------|------|------|
| Bilibili | yt-dlp + Whisper | 需要 BV 号 |
| YouTube | yt-dlp + Whisper | 直接下载 |
| 本地视频 | Whisper | 支持 mp4, mp3, wav |

## 安装依赖

```bash
# 安装 yt-dlp (下载视频)
pip install yt-dlp

# 安装 Whisper
pip install openai-whisper

# 或安装 ffmpeg (系统依赖)
# Ubuntu: sudo apt install ffmpeg
# Windows: 下载 ffmpeg.exe 并加入 PATH
```

## 核心功能

### 1. Bilibili 视频转写

```python
import subprocess
import whisper

# 步骤1: 下载视频/音频
def download_bilibili_audio(bv_id, output_path="audio"):
    """下载 Bilibili 视频音频"""
    cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", f"{output_path}/%(title)s.%(ext)s",
        f"https://www.bilibili.com/video/{bv_id}"
    ]
    subprocess.run(cmd, check=True)

# 步骤2: Whisper 转写
def transcribe_audio(audio_path, model="base"):
    """使用 Whisper 转写音频"""
    model = whisper.load_model(model)
    result = model.transcribe(audio_path, language="zh")

    # 提取文本
    text = result["text"]
    segments = result["segments"]

    return text, segments
```

### 2. 完整工作流

```python
def bilibili_to_transcript(bv_id, output_file="transcript.md"):
    """Bilibili 视频完整转写流程"""

    # 1. 下载音频
    print("📥 下载视频音频...")
    audio_path = download_bilibili_audio(bv_id)

    # 2. 转写
    print("🎙️ 使用 Whisper 转写中...")
    text, segments = transcribe_audio(audio_path)

    # 3. 生成带时间戳的文稿
    print("📝 生成文稿...")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# {bv_id} - 视频文稿\n\n")
        f.write(f"> 转写时间: {datetime.now()}\n\n")
        f.write("---\n\n")

        for seg in segments:
            start = seg["start"]
            end = seg["end"]
            content = seg["text"]

            # 格式化时间 [00:00 - 00:30]
            time_str = f"[{format_time(start)} - {format_time(end)}]"
            f.write(f"{time_str} {content}\n\n")

        # 4. 生成摘要
        f.write("---\n\n")
        f.write("## 完整文本\n\n")
        f.write(text)

    print(f"✅ 文稿已保存到: {output_file}")
    return output_file

def format_time(seconds):
    """格式化时间"""
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"
```

### 3. 命令行使用

```bash
# 下载单个视频并转写
python video_transcript.py BV1SHcfzKEu6

# 下载整个播放列表
python video_transcript.py --playlist "https://www.bilibili.com/video/BV1SHcfzKEu6"

# 指定模型 (tiny, base, small, medium, large)
python video_transcript.py BV1SHcfzKEu6 --model small
```

## 文稿格式

```markdown
# BV1SHcfzKEu6 - 视频文稿

> 转写时间: 2024-01-15 10:30:00

---

[00:00 - 00:30] 欢迎来到密歇根大学的 Python 数据科学编程课程。

[00:30 - 01:00] 在这门课程中，我们将学习 Python 的基础知识...

---

## 完整文本

欢迎来到密歇根大学的 Python 数据科学编程课程。在这门课程中，我们将学习 Python 的基础知识，包括变量、数据类型、控制流、函数等...
```

## 集成 disc-generator

```
视频 → video-transcript → 文稿 → disc-generator → 学习网页
```

获取文稿后，结合 disc-generator 生成练习页面。

---

## 实际使用示例

```python
# 示例：转写第一个视频
bv_id = "BV1SHcfzKEu6"

# 第1集: Python编程基础入门 (212秒)
transcript_file = bilibili_to_transcript(bv_id)

# 生成的学习页面将包含:
# - 视频内容摘要
# - 代码示例提取
# - 知识点总结
```

---

## 注意事项

1. **网络**: 下载视频需要稳定的网络连接
2. **存储**: 视频文件可能较大，确保有足够空间
3. **时间**: 转写时间取决于视频长度和模型选择
4. **准确性**: Whisper 识别准确率受音频质量影响

---

*视频转文稿，让学习更高效！*
