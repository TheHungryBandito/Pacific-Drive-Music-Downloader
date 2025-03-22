# Pacific-Drive-Music-Downloader
Downloads youtube audio, converts it to a playable format and adds it to the custom radio.


## Usage
This application can be run with or without Pacific Drive running.

1. Download the .exe
2. Run the .exe
3. Paste the URL to the YouTube video you would like the audio from
    ![Command line prompt for URL](images\image-1.png)
4. Press "Enter"
5. The application will download the video, convert it to MP3 and save the audio to %Localappdata%\PenDriverPro\Custom\Radio\
6. Follow the prompts to download more audio or close the application
7. Open Pacific Drive (If not already open)
8. Go to "Settings"
9. Go to "Audio"
10. Scroll down to "Local Music" and click "REBUILD DATABASE"
11. Change "Radio Music Source" to "CUSTOM" or "DEFAULT AND CUSTOM" depending on your preferences
    ![Pacific Drive Audio Settings Menu](images\image-2.png)
12. The radio in-game should now be playing the custom music that was downloaded

## Requirements
- Windows PC
- Access to YouTube
- Internet Connection
- Enough space to download and convert the YouTube video

## How it works
1. The user provides it a YouTube URL which it downloads it to the custom radio folder using the pytubefix module.
2. It then extracts the audio stream (.m4a) for the video.
3. It then uses FFMPEG to convert the audio steam (.m4a) to (.mp3)
4. Finally it deletes the orignal (.m4a) file

## Dependencies for development
- [FFMPEG](https://www.ffmpeg.org/download.html) - [ffmpeg-master-latest-win64-gpl-shared](https://github.com/BtbN/FFmpeg-Builds/releases) was used for development
- [UPX](https://upx.github.io/) (For compressing .exe)
- [Python 3.13](https://www.python.org/downloads/)
- Pyinstaller (module)
- Pytubefix (module)

Install modules using command line:

```cmd
pip install pyinstaller
pip install pytubefix
```

## Build command
```cmd
pyinstaller --onefile --strip --upx-dir "C:\Path\To\UPX directory" --hidden-import pytubefix --add-binary "C:\Path\To\ffmpeg.exe;." .\PacificDriveMusicDownloader.py
```