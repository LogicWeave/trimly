from pathlib import Path
from typing import Union

from .exceptions import TrimlyError, UnsupportedFormatError
from ..configs import get_config


def validate_audio_file(file_path: Union[str, Path]) -> Path:
    """
    Validates that the given audio file exists, is a file, and has a supported format.

    Args:
        file_path (Union[str, Path]): Path to the audio file.

    Returns:
        Path: The validated Path object.

    Raises:
        TrimlyError: If the file does not exist or is not a file.
        UnsupportedFormatError: If the file format is not supported.
    """
    path = Path(file_path)

    if not path.exists():
        raise TrimlyError(f"File not found: {path}")

    if not path.is_file():
        raise TrimlyError(f"Path is not a file: {path}")

    supported_formats = get_config().supported_audio_formats
    if path.suffix.lower() not in supported_formats:
        raise UnsupportedFormatError(
            f"Unsupported file format: {path.suffix}. Supported formats: {', '.join(supported_formats)}"
        )

    return path
