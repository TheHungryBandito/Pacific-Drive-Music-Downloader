from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import sys
import subprocess

if getattr(sys, 'frozen', False):
    # If bundled, use the path to the extracted folder
    ffmpeg_path = os.path.join(sys._MEIPASS, 'ffmpeg.exe')
else:
    # If running from source code, use the local path to ffmpeg
    ffmpeg_path = os.path.join(os.getenv("USERPROFILE"), "Downloads\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe")

if not os.path.exists(ffmpeg_path):
    print(f"Error: ffmpeg not found at {ffmpeg_path}")
    sys.exit(1)

SAVE_PATH = os.path.join(os.getenv("LOCALAPPDATA"),"PenDriverPro\\Custom\\Radio")

def main():
    link = input("Enter the video url: ")

    try:
        yt = YouTube(link, on_progress_callback=on_progress)
        print ("Video title: ", yt.title)
    except Exception as e:
        print ("Connection error: ", e)
        return
    
    audio_stream = yt.streams.get_audio_only()
    try:
        print("Downloading audio...")
        out_file = audio_stream.download(output_path=SAVE_PATH)
        print("Audio downloaded successfully!")
    except Exception as e:
        print ("Error downloading audio: ", e)
        return
    
    try:
        print("Converting to mp3...")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        subprocess.run([ffmpeg_path, '-i', out_file, new_file])
        os.remove(out_file)
        print("Conversion complete!")
    except Exception as e:
        print ("Error converting audio to mp3: ", e)
        return

    print("Audio saved to: ", new_file)
    user_input = input("Would you like to download another song? (y/n): ")
    if user_input.lower() == 'y':
        main()
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
