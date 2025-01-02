import yt_dlp
import os

def download_video(video_url, output_path="downloads", resolution="720p"):
    """
    Downloads a YouTube video in MP4 format with specified resolution.

    :param video_url: URL of the YouTube video.
    :param output_path: Path where the downloaded video will be saved.
    :param resolution: Desired resolution (e.g., '720p', '1080p').
    """
    # Ensure output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # yt-dlp options for video download
    ydl_opts = {
        'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best',  # Combine video and audio
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save with video title as file name
        'merge_output_format': 'mp4',  # Ensure output is a single MP4 file
        'noplaylist': True,  # Avoid downloading playlists
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Video download completed successfully at {resolution}!")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_audio(video_url, output_path="downloads", bitrate="192"):
    """
    Extracts audio from a YouTube video and saves it as an MP3 file.

    :param video_url: URL of the YouTube video.
    :param output_path: Path where the downloaded audio will be saved.
    :param bitrate: Desired MP3 bitrate (e.g., '128', '192', '256', '320').
    """
    # Ensure output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # yt-dlp options for audio extraction
    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio available
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save with video title as file name
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Convert to MP3
                'preferredquality': bitrate,  # Set audio quality
            }
        ],
        'noplaylist': True,  # Avoid downloading playlists
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Audio download completed successfully at {bitrate} kbps!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("=== YouTube Downloader ===")
    video_url = input("Enter YouTube video URL: ").strip()
    choice = input("What do you want to download? (video/mp4 or audio/mp3): ").strip().lower()

    if choice == "video" or choice == "mp4":
        resolution = input("Enter desired resolution (e.g., '720p', '1080p', default is '720p'): ").strip() or "720p"
        download_video(video_url, resolution=resolution)
    elif choice == "audio" or choice == "mp3":
        bitrate = input("Enter desired MP3 bitrate (e.g., '128', '192', '256', '320', default is '192'): ").strip() or "192"
        download_audio(video_url, bitrate=bitrate)
    else:
        print("Invalid choice! Please enter 'video' or 'audio'.")
