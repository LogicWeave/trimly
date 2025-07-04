from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("trimly")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

# File and Directory Configuration
DEFAULT_TEMP_DIRECTORY = "storage/tmp"
PROCESSED_FILE_PREFIX = "trimmed_"
DEFAULT_OUTPUT_AUDIO_FORMAT = ".wav"

# Supported Media Formats
SUPPORTED_AUDIO_FORMATS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".flac",
    ".ogg"
}

# Audio Processing Defaults
DEFAULT_SILENCE_THRESHOLD_DB = -45.0
DEFAULT_MIN_SILENCE_DURATION_SECONDS = 0.05
DEFAULT_START_SILENCE_KEEP_DURATION_SECONDS = 0.1

# Processing Limits and Validation Ranges
MIN_SILENCE_THRESHOLD_DB = -100.0
MAX_SILENCE_THRESHOLD_DB = 0.0
MIN_PROCESSING_SILENCE_DURATION_SECONDS = 0.001
MAX_PROCESSING_SILENCE_DURATION_SECONDS = 10.0
MAX_INPUT_FILE_SIZE_MB = 200.0
PROCESSING_OPERATION_TIMEOUT_SECONDS = 300

# FFmpeg Configuration
FFMPEG_SILENCE_FILTER_TEMPLATE = (
    "silenceremove=start_periods=1:start_silence={start_silence}:"
    "start_threshold={threshold}dB:stop_periods=-1:stop_silence={min_silence}:"
    "stop_threshold={threshold}dB:detection=peak"
)