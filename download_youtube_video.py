from yt_dlp import YoutubeDL

def download_youtube_video(url, output_path='.', resolution='best'):
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save video with title as filename
            'format': f'bv*[height<={resolution}]+ba/b[height<={resolution}]',  # Download specific resolution
            'merge_output_format': 'mp4',  # Ensure the output is in mp4 format
            'verbose': True,  # Add verbose output for debugging
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',  # Ensure the output is in mp4 format
                'preferedformat': 'mp4',
            }],
        }
        
        # Download the video
        print(f"Downloading video in {resolution}p...")
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)  # Extract video info and download
            filename = ydl.prepare_filename(info_dict)  # Get the filename of the downloaded file
            print(f"Download completed! File saved as: {filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # URL of the YouTube video
    video_url = input("Enter the YouTube video URL: ")
    
    # Optional: Specify the output directory (default is current directory)
    output_directory = input("Enter the output directory (leave blank for current directory): ") or '.'
    
    # Ask for the desired resolution
    resolution = input("Enter the desired resolution (720, 1080, 1440, 2160, or 'best' for the best available): ")
    
    # Validate the resolution input
    valid_resolutions = ['720', '1080', '1440', '2160', 'best']
    if resolution not in valid_resolutions:
        print("Invalid resolution. Defaulting to 'best'.")
        resolution = 'best'
    
    # Download the video
    download_youtube_video(video_url, output_directory, resolution)