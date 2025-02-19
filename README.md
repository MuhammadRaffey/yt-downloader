# YouTube Video Downloader

A Python-based YouTube video and thumbnail downloader using yt-dlp, providing a simple interface to download videos in the best available quality.

## Features

- Download YouTube videos in highest quality (video + audio)
- Automatically download video thumbnails
- Sanitized filenames for compatibility
- Simple command-line interface
- Can be used as a Python package
- Fast dependency management with UV

## Installation

This project uses [UV](https://github.com/astral/uv) as the package manager for superior performance and reliability.

### 1. Install UV (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install the Project

```bash
# Clone the repository
git clone https://github.com/MuhammadRaffey/yt-downloader.git
cd yt-downloader

# Create a new virtual environment with UV
uv venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate

# Install dependencies using UV
uv sync
```

## Development Setup

```bash
# Add new dependencies
uv add yt-dlp

# View dependency tree
uv tree

# Update dependencies
uv sync

# Create/update lockfile
uv lock
```

## Usage

### Command Line Interface

After installation, you can use the downloader directly from the command line:

```bash
uv run download
```

This will prompt you to enter a YouTube URL and download the video to a `downloads` folder in your current directory.

### As a Python Package

```python
from yt_downloader import download

# Download a video
success = download("https://www.youtube.com/watch?v=your_video_id")
if success:
    print("Video downloaded successfully!")

# Specify custom output directory
success = download("https://www.youtube.com/watch?v=your_video_id", output_dir="my_videos")
```

### Using the YouTubeDownloader Class

```python
from yt_downloader import YouTubeDownloader

# Initialize the downloader
downloader = YouTubeDownloader(output_dir="custom_downloads")

# Download a video
success = downloader.download_video_and_thumbnail("https://www.youtube.com/watch?v=your_video_id")
```

## Requirements

- Python 3.11 or higher
- UV package manager
- Dependencies (automatically managed by UV):
  - yt-dlp >= 2025.2.19
  - pytube >= 15.0.0
  - requests >= 2.32.3

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Install development dependencies with `uv sync --editable .`
4. Make your changes
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Author

- Muhammad Raffey ([@MuhammadRaffey](https://github.com/MuhammadRaffey))
- Email: muhammadraffey26@gmail.com
