import subprocess

from .exceptions import FFmpegNotFoundError


def check_ffmpeg_availability() -> bool:
    """
    Verifies the availability of the FFmpeg executable in the system's PATH.

    This function attempts to run the `ffmpeg -version` command silently
    to determine if FFmpeg is installed and accessible. It's a crucial
    pre-check for any operation relying on FFmpeg.

    Returns:
        bool: True if FFmpeg is successfully found and executable.

    Raises:
        FFmpegNotFoundError: If the FFmpeg executable is not found,
                             the command fails, or the check times out,
                             indicating FFmpeg is either not installed
                             or not properly configured in the system's PATH.
    """
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.DEVNULL, # Suppress standard output
            stderr=subprocess.DEVNULL, # Suppress standard error
            timeout=10,                # Set a timeout to prevent hanging
            check=True                 # Raise CalledProcessError if command returns non-zero exit code
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as e:
        raise FFmpegNotFoundError(
            f"FFmpeg is not installed or not found in system PATH. Details: {e}"
        ) from e