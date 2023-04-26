import yt_dlp
import subprocess

# Define the URL of the YouTube video you want to play
video_url = 'https://www.youtube.com/watch?v=VIDEO_ID'

# Create a yt_dlp options dictionary
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'prefer_ffmpeg': True,
    'keepvideo': False,
    'outtmpl': 'downloads/%(title)s.%(ext)s',  # Specify the output template for downloaded files
}

# Create a yt_dlp YoutubeDL instance
ydl = yt_dlp.YoutubeDL(ydl_opts)

# Extract video information
info = ydl.extract_info(video_url, download=False)

# Get the audio URL from the info dictionary
audio_url = info['formats'][0]['url']

# Create a subprocess to play the audio using ffmpeg
subprocess.run(['ffmpeg', '-i', audio_url, '-acodec', 'mp3', '-f', 'mp3', '-'], shell=True)