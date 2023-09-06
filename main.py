from pytube import Playlist
from pytube import YouTube
from pytube.cli import on_progress

def download_video_as_mp3(video_url):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    
    # Get the best audio stream (usually in the highest quality)
    audio_stream = yt.streams.filter(only_audio=True).first()

    if audio_stream:
        # Download the audio stream as an MP3 file
        audio_stream.download(filename=f'{yt.title}.mp3')
        print(f"Downloaded: {yt.title}.mp3")
    else:
        print(f"No audio stream found for {yt.title}")

playlist_url = input("Enter Playlist URL: ")

# Create a Playlist object
playlist = Playlist(playlist_url)
print(f"Total Videos: {len(playlist)}")

# Download each video as an MP3
for video_url in playlist.video_urls:
    download_video_as_mp3(video_url)

