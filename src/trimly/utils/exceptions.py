class TrimlyError(Exception):
    """
    Base exception for all Trimly-related operational errors.

    All custom exceptions raised within the Trimly application should
    inherit from this base class. This allows for a single `except TrimlyError:`
    block to catch all application-specific errors.
    """
    pass


class FFmpegNotFoundError(TrimlyError):
    """
    Raised when the FFmpeg executable cannot be found in the system's PATH.

    This indicates that FFmpeg is either not installed or its location
    is not correctly configured in the environment variables, which is
    a prerequisite for Trimly's audio processing functionalities.
    """
    pass


class UnsupportedFormatError(TrimlyError):
    """
    Raised when an audio file's format is not supported by Trimly.

    This exception is typically raised when attempting to process an audio file
    with an extension or internal format that is not recognized or handled
    by the application's supported audio formats list.
    """
    pass