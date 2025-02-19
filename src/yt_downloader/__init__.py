from .main import YouTubeDownloader

def download(url, output_dir="downloads"):
    """
    Downloads a YouTube video and its thumbnail.  This is a convenience
    function that uses the YouTubeDownloader class.

    Args:
        url: The URL of the YouTube video.
        output_dir: The base output directory (default: "downloads"). A
                    subdirectory will be created in the current working
                    directory.

    Returns:
        True if both downloads were successful, False otherwise.
    """
    downloader = YouTubeDownloader(output_dir=output_dir)
    return downloader.download_video_and_thumbnail(url)


def main() -> None:
    video_url = input("Enter the YouTube video URL: ")
    if download(video_url):
        print("Download successful!")
    else:
        print("Download failed.")
