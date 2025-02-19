import yt_dlp
import os
import re


class YouTubeDownloader:
    """Downloads YouTube videos and their thumbnails using yt-dlp."""

    def __init__(self, output_dir="downloads"):
        """
        Initializes the YouTubeDownloader.

        Args:
            output_dir: The base directory for downloads (default: "downloads").
        """
        self.output_base_dir = output_dir
        self.output_dir = os.path.join(os.getcwd(), self.output_base_dir)
        self._create_output_directory()

    def _create_output_directory(self):
        """Creates the output directory if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _sanitize_filename(self, title):
        """Removes invalid characters from a filename."""
        return re.sub(r'[\\/*?:"<>|]', "", title)

    def download_video_and_thumbnail(self, url):
        """Downloads a YouTube video and its thumbnail."""
        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
                'writethumbnail': True,
                'skip_download': False,
                'merge_output_format': 'mp4',
                'quiet': True,  # Suppress unnecessary output
                'no_warnings': True, # Suppress warnings
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                if not info_dict:
                    print("ERROR: Could not extract video information.")
                    return False

                video_title = info_dict.get('title', 'Untitled Video')  # Provide default title
                sanitized_title = self._sanitize_filename(video_title)
                video_ext = info_dict.get('ext', 'mp4')
                video_filename = f"{sanitized_title}.{video_ext}"
                video_filepath = os.path.join(self.output_dir, video_filename)

                thumbnail_url = info_dict.get('thumbnail')
                # No need to pre-download.  yt-dlp will handle it with writethumbnail

                print(f"Downloading video: {video_title}")
                ydl.download([url])  # Download with yt-dlp
                print(f"Video and thumbnail downloaded to: {self.output_dir}") # More concise output


                return True

        except yt_dlp.utils.DownloadError as e:
            print(f"yt-dlp Download Error: {e}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False