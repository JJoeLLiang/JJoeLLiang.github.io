from pydub import AudioSegment
import os

def extract_mp3_from_mp4(input_file, output_file):
    """
    从 MP4 文件中提取音频并保存为 MP3 文件。

    参数：
        input_file (str): 输入的 MP4 文件路径。
        output_file (str): 输出的 MP3 文件路径。
    """
    # 加载 MP4 文件
    audio = AudioSegment.from_file(input_file, format="mp4")
    
    # 导出为 MP3 格式
    audio.export(output_file, format="mp3")
    print(f"成功提取音频：{input_file} -> {output_file}")

# 示例用法
input_mp4 = "public/music/88rising; Stephanie Poetri; 王嘉尔 - I Love You 3000 II.flac"  # 输入的 MP4 文件路径
output_mp3 = "public/music"  # 输出的 MP3 文件路径
extract_mp3_from_mp4(input_mp4, output_mp3)