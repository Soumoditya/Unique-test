import subprocess
import os
import time

# Config shit
RTSP_URL = "rtsp://example.com/kolkata-cctv-feed"  # Replace with real feed URL
OUTPUT_DIR = "docs"  # Where the stream files go
HLS_PLAYLIST = f"{OUTPUT_DIR}/stream.m3u8"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print("Created output dir. Ready to fuck shit up.")

def start_stream():
    # FFmpeg command to convert RTSP to HLS
    cmd = [
        "ffmpeg",
        "-i", RTSP_URL,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-f", "hls",
        "-hls_time", "10",
        "-hls_list_size", "6",
        "-hls_segment_filename", f"{OUTPUT_DIR}/stream%d.ts",
        HLS_PLAYLIST
    ]
    print(f"Startin’ the stream, motherfuckers! Command: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    ensure_output_dir()
    while True:
        try:
            start_stream()
        except Exception as e:
            print(f"Stream fucked up: {e}. Retryin’ in 5...")
            time.sleep(5)
