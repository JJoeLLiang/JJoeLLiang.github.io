from pydub import AudioSegment
import os

def flac_to_mp3(input_path, output_folder, bitrate="192k"):
    """
    将指定路径的 FLAC 文件（单个文件或目录中的所有文件）转换为 MP3 文件。
    
    参数：
        input_path (str): 输入的 FLAC 文件路径或目录路径。
        output_folder (str): 输出 MP3 文件保存的文件夹路径。
        bitrate (str): 输出 MP3 的比特率，默认 "192k"。
    """
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 判断输入路径是文件还是目录
    if os.path.isfile(input_path):
        # 如果是文件，直接转换
        filenames = [input_path]
    elif os.path.isdir(input_path):
        # 如果是目录，获取目录中的所有文件
        filenames = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith(".flac")]
    else:
        raise ValueError(f"输入路径 {input_path} 既不是文件也不是目录")
    
    # 遍历所有文件进行转换
    for input_file in filenames:
        # 输出文件路径
        output_path = os.path.join(output_folder, os.path.basename(input_file).replace(".flac", ".mp3"))
        
        # 加载 FLAC 文件
        audio = AudioSegment.from_file(input_file, format="flac")
        
        # 转换为 MP3 并保存
        audio.export(output_path, format="mp3", bitrate=bitrate)
        print(f"成功转换：{input_file} -> {output_path}")

# 示例用法
input_dir_or_file = "public/music/Taylor Swift - Last Christmas.flac"  # 可以是文件路径或目录路径
output_dir = "public/music/"  # 输出文件夹路径
flac_to_mp3(input_dir_or_file, output_dir)