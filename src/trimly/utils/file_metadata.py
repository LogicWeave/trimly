from pathlib import Path
from typing import Union, Dict

from ..configs import get_config


def format_file_size(size_bytes: int) -> str:
    """
    Convert a file size in bytes to a human-readable string.

    Args:
        size_bytes (int): File size in bytes.

    Returns:
        str: Human-readable file size (e.g., '1.5 MB').
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def get_file_info(file_path: Union[str, Path]) -> Dict[str, Union[str, int, bool]]:
    """
    Retrieve metadata and validation info about a given audio file.

    Args:
        file_path (Union[str, Path]): Path to the file.

    Returns:
        Dict[str, Union[str, int, bool]]: Metadata including name, size, extension, and support status.
    """
    path = Path(file_path)

    if not path.exists():
        return {"exists": False}

    stat = path.stat()
    supported_formats = get_config().supported_audio_formats

    return {
        "exists": True,
        "name": path.name,
        "size": stat.st_size,
        "size_formatted": format_file_size(stat.st_size),
        "extension": path.suffix,
        "is_supported": path.suffix.lower() in supported_formats,
    }
