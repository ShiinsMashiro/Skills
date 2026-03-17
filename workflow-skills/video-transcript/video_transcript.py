#!/usr/bin/env python3
"""
视频转文稿工具 - 使用 Whisper AI 转写视频
支持 Bilibili、YouTube、本地视频
"""

import subprocess
import argparse
import os
import sys
from datetime import datetime

# 尝试导入 whisper，如果未安装则提示
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False


def install_dependencies():
    """安装依赖"""
    print("📦 安装依赖中...")
    subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "openai-whisper"], check=True)
    print("✅ 依赖安装完成！")


def download_bilibili_audio(bv_id, output_dir="downloads"):
    """下载 Bilibili 视频音频"""
    os.makedirs(output_dir, exist_ok=True)

    url = f"https://www.bilibili.com/video/{bv_id}"
    output_template = os.path.join(output_dir, "%(title)s.%(ext)s")

    print(f"📥 下载 {bv_id} 音频中...")

    cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", output_template,
        url
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ 下载失败: {result.stderr}")
        return None

    # 查找下载的文件
    files = os.listdir(output_dir)
    audio_files = [f for f in files if f.endswith('.mp3')]

    if audio_files:
        return os.path.join(output_dir, audio_files[0])

    return None


def transcribe_audio(audio_path, model_name="base", language="zh"):
    """使用 Whisper 转写音频"""
    if not WHISPER_AVAILABLE:
        print("❌ Whisper 未安装，请先运行: pip install openai-whisper")
        return None, None

    print(f"🎙️ 使用 Whisper {model_name} 模型转写中...")

    try:
        model = whisper.load_model(model_name)
        result = model.transcribe(audio_path, language=language)

        text = result["text"]
        segments = result["segments"]

        print(f"✅ 转写完成！文本长度: {len(text)} 字符")
        return text, segments

    except Exception as e:
        print(f"❌ 转写失败: {e}")
        return None, None


def format_time(seconds):
    """格式化时间 [MM:SS]"""
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"


def generate_transcript(bv_id, segments, text, output_file=None):
    """生成文稿文件"""
    if output_file is None:
        output_file = f"transcript_{bv_id}.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# {bv_id} - 视频文稿\n\n")
        f.write(f"> 转写时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"> 视频来源: https://www.bilibili.com/video/{bv_id}\n\n")
        f.write("---\n\n")

        # 带时间戳的文稿
        f.write("## 带时间戳内容\n\n")

        for seg in segments:
            start = seg["start"]
            end = seg["end"]
            content = seg["text"].strip()

            time_str = f"[{format_time(start)} - {format_time(end)}]"
            f.write(f"{time_str} {content}\n\n")

        # 完整文本
        f.write("---\n\n")
        f.write("## 完整文本\n\n")
        f.write(text)
        f.write("\n")

    print(f"✅ 文稿已保存到: {output_file}")
    return output_file


def extract_code_examples(text):
    """提取代码示例（简单实现）"""
    import re

    # 查找类似代码的内容
    code_pattern = r'(def |class |import |if |for |while |print\(|return )'
    code_lines = []

    for line in text.split('\n'):
        if re.search(code_pattern, line):
            code_lines.append(line.strip())

    return code_lines


def main():
    parser = argparse.ArgumentParser(description="视频转文稿工具")
    parser.add_argument("video", help="视频 BV 号或 URL")
    parser.add_argument("--model", default="base", choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper 模型 (默认: base)")
    parser.add_argument("--output", "-o", help="输出文件路径")
    parser.add_argument("--install", action="store_true", help="安装依赖")

    args = parser.parse_args()

    # 安装依赖
    if args.install or not WHISPER_AVAILABLE:
        install_dependencies()

    if not WHISPER_AVAILABLE:
        print("❌ 请先安装 Whisper: pip install openai-whisper")
        return

    # 提取 BV 号
    bv_id = args.video
    if "bilibili.com" in bv_id:
        # 从 URL 提取 BV 号
        if "BV" in bv_id:
            import re
            match = re.search(r'BV[A-Za-z0-9]+', bv_id)
            if match:
                bv_id = match.group()
        else:
            print("❌ 无法从 URL 提取 BV 号")
            return

    print(f"🚀 开始处理视频: {bv_id}")
    print(f"📌 使用模型: {args.model}")
    print("-" * 40)

    # 1. 下载音频
    audio_path = download_bilibili_audio(bv_id)

    if not audio_path:
        print("❌ 音频下载失败")
        return

    # 2. 转写
    text, segments = transcribe_audio(audio_path, args.model)

    if not text:
        print("❌ 转写失败")
        return

    # 3. 生成文稿
    output_file = generate_transcript(bv_id, segments, text, args.output)

    # 4. 提取代码示例
    print("🔍 提取代码示例...")
    code_examples = extract_code_examples(text)

    if code_examples:
        code_file = f"codes_{bv_id}.txt"
        with open(code_file, "w", encoding="utf-8") as f:
            f.write(f"# {bv_id} - 代码示例\n\n")
            for code in code_examples[:20]:  # 限制数量
                f.write(code + "\n")
        print(f"📄 代码示例已保存到: {code_file}")

    print("-" * 40)
    print("🎉 处理完成！")


if __name__ == "__main__":
    main()
