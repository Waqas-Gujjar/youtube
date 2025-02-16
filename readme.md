# YouTube Video Downloader

A Python script to download YouTube videos in various resolutions using `yt-dlp`.

## Description

This script allows you to download YouTube videos by providing a URL and specifying your desired resolution (720p, 1080p, 1440p, 2160p, or "best" available). The output is saved as an MP4 file in your chosen directory.

## Features

- Download videos in specific resolutions (up to 4K).
- Automatic conversion to MP4 format.
- Customizable output directory.
- Error handling and verbose logging for troubleshooting.
- User-friendly command-line interface.

## Requirements

- Python 3.6+
- `yt-dlp` (Python library)
- `ffmpeg` (for merging video/audio streams)

## Installation

1. **Install Python**:  
   Ensure Python is installed from [python.org](https://www.python.org/).

2. **Install Dependencies**:
   ```bash
   pip install yt-dlp