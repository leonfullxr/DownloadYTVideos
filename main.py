import os
from pytube import Playlist, YouTube
from pytube.cli import on_progress

def download_video_as_mp3(video_url, download_path):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    
    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

    if audio_stream:
        # Download the audio stream as an MP3 file to the specified path
        audio_stream.download(output_path=download_path, filename=f'{yt.title}.mp3')
        print(f"Downloaded: {yt.title}.mp3")
    else:
        print(f"No audio stream found for {yt.title}")

def download_video_as_mp4(video_url, download_path):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    
    # Get the highest quality video stream with audio
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    if video_stream:
        # Download the video stream as an MP4 file to the specified path
        video_stream.download(output_path=download_path, filename=f'{yt.title}.mp4')
        print(f"Downloaded: {yt.title}.mp4")
    else:
        print(f"No video stream found for {yt.title}")

def download_from_playlist(playlist_url, format_choice, download_path):
    # Create a Playlist object
    playlist = Playlist(playlist_url)
    print(f"Total Videos in Playlist: {len(playlist)}")

    # Download each video in the chosen format
    for video_url in playlist.video_urls:
        if format_choice == 'mp3':
            download_video_as_mp3(video_url, download_path)
        elif format_choice == 'mp4':
            download_video_as_mp4(video_url, download_path)

def download_from_single_video(video_url, format_choice, download_path):
    if format_choice == 'mp3':
        download_video_as_mp3(video_url, download_path)
    elif format_choice == 'mp4':
        download_video_as_mp4(video_url, download_path)

url = input("Enter YouTube URL (Playlist or Single Video): ")
format_choice = input("Enter the format to download (mp3/mp4): ").strip().lower()

# Create the download directory based on the chosen format
if format_choice == 'mp3':
    download_path = 'songs'
elif format_choice == 'mp4':
    download_path = 'videos'
else:
    print("Invalid format choice. Please enter either 'mp3' or 'mp4'.")
    exit()

# Ensure the download directory exists
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Check if the URL is a playlist or a single video
try:
    playlist = Playlist(url)
    is_playlist = True
except Exception:
    is_playlist = False

if is_playlist:
    download_from_playlist(url, format_choice, download_path)
else:
    download_from_single_video(url, format_choice, download_path)
