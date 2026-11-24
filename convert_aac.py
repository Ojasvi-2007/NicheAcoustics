import glob
import os
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
input_files = glob.glob("data/raw/*.aac")

if not input_files:
    print("No .aac files found in data/raw/")

for file_path in input_files:
    wav_path = os.path.splitext(file_path)[0] + ".wav"
    cmd = [
        ffmpeg_exe,
        "-y",               # Overwrite if exists
        "-i", file_path,    # Input .aac file
        "-ar", "44100",     # 44.1 kHz sample rate
        "-ac", "1",         # Mono channel
        "-c:a", "pcm_s16le",# 16-bit PCM WAV
        wav_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"Converted: {os.path.basename(file_path)} -> {os.path.basename(wav_path)}")