import os
from dataclasses import dataclass, field
from typing import Set, Optional

from ..constants import (
    DEFAULT_TEMP_DIRECTORY,
    PROCESSED_FILE_PREFIX,
    DEFAULT_OUTPUT_AUDIO_FORMAT,
    SUPPORTED_AUDIO_FORMATS,
    DEFAULT_SILENCE_THRESHOLD_DB,
    DEFAULT_MIN_SILENCE_DURATION_SECONDS,
    DEFAULT_START_SILENCE_KEEP_DURATION_SECONDS,
    MIN_SILENCE_THRESHOLD_DB,
    MAX_SILENCE_THRESHOLD_DB,
    MIN_PROCESSING_SILENCE_DURATION_SECONDS,
    MAX_PROCESSING_SILENCE_DURATION_SECONDS,
    MAX_INPUT_FILE_SIZE_MB,
    PROCESSING_OPERATION_TIMEOUT_SECONDS,
    FFMPEG_SILENCE_FILTER_TEMPLATE
)

def _parse_env_float(var: str, default: float) -> float:
   value = os.getenv(var)
   if value is None:
      return default
   try:
      return float(value)
   except ValueError:
      raise ValueError(f"Invalid float value for {var}: {value}")


def _parse_env_str(var: str, default: str) -> str:
   return os.getenv(var, default)


@dataclass(frozen=True)
class TrimlyConfig:
   """
   Configuration settings for the Trimly application.

   This dataclass holds default and configurable parameters for file handling,
   audio processing, and operational limits.
   """

   # Directory and File Settings
   temp_directory: str = DEFAULT_TEMP_DIRECTORY
   processed_file_prefix: str = PROCESSED_FILE_PREFIX
   output_audio_format: str = DEFAULT_OUTPUT_AUDIO_FORMAT
   supported_audio_formats: Set[str] = field(default_factory=lambda: SUPPORTED_AUDIO_FORMATS)

   # Audio Processing Defaults
   default_silence_threshold_db: float = DEFAULT_SILENCE_THRESHOLD_DB
   default_min_silence_duration_seconds: float = DEFAULT_MIN_SILENCE_DURATION_SECONDS
   default_start_silence_keep_duration_seconds: float = DEFAULT_START_SILENCE_KEEP_DURATION_SECONDS

   # Operational Limits
   max_input_file_size_mb: float = MAX_INPUT_FILE_SIZE_MB
   processing_operation_timeout_seconds: int = PROCESSING_OPERATION_TIMEOUT_SECONDS

   # Validation Ranges
   min_silence_threshold_db: float = MIN_SILENCE_THRESHOLD_DB
   max_silence_threshold_db: float = MAX_SILENCE_THRESHOLD_DB
   min_processing_silence_duration_seconds: float = MIN_PROCESSING_SILENCE_DURATION_SECONDS
   max_processing_silence_duration_seconds: float = MAX_PROCESSING_SILENCE_DURATION_SECONDS

   # FFMPEG Silence Filter Template
   ffmpeg_silence_filter_template: str = FFMPEG_SILENCE_FILTER_TEMPLATE


   @classmethod
   def from_env(cls) -> "TrimlyConfig":
      """
      Create a TrimlyConfig instance, overriding default settings with values
      from environment variables if available.

      Environment variable names are expected to be prefixed with 'TRIMLY_'.
      For example, 'TRIMLY_TEMP_DIRECTORY' will override 'temp_directory'.
      """
      return cls(
         # Load basic directory and file-related settings
         temp_directory=os.path.abspath(_parse_env_str("TRIMLY_TEMP_DIRECTORY", DEFAULT_TEMP_DIRECTORY)),
         processed_file_prefix=_parse_env_str("TRIMLY_FILE_PREFIX", PROCESSED_FILE_PREFIX),

         # Load default silence processing thresholds
         default_silence_threshold_db=_parse_env_float("TRIMLY_SILENCE_THRESHOLD_DB", DEFAULT_SILENCE_THRESHOLD_DB),
         default_min_silence_duration_seconds=_parse_env_float("TRIMLY_MIN_SILENCE_DURATION", DEFAULT_MIN_SILENCE_DURATION_SECONDS),
         default_start_silence_keep_duration_seconds=_parse_env_float("TRIMLY_KEEP_START_DURATION", DEFAULT_START_SILENCE_KEEP_DURATION_SECONDS),

         # Load configurable validation limits
         min_silence_threshold_db=_parse_env_float("TRIMLY_MIN_SILENCE_DB", MIN_SILENCE_THRESHOLD_DB),
         max_silence_threshold_db=_parse_env_float("TRIMLY_MAX_SILENCE_DB", MAX_SILENCE_THRESHOLD_DB),
         min_processing_silence_duration_seconds=_parse_env_float("TRIMLY_MIN_SILENCE_DUR", MIN_PROCESSING_SILENCE_DURATION_SECONDS),
         max_processing_silence_duration_seconds=_parse_env_float("TRIMLY_MAX_SILENCE_DUR", MAX_PROCESSING_SILENCE_DURATION_SECONDS),
      )


   def validate(self, threshold: float = None, min_silence: float = None, start_silence: float = None) -> None:
      """
      Validate configuration settings and optionally runtime parameters to ensure they are within acceptable ranges
      and follow required formats.

      Args:
          threshold: Optional silence threshold in dB to validate
          min_silence: Optional minimum silence duration in seconds to validate
          start_silence: Optional start silence keep duration in seconds to validate

      Raises:
         ValueError: If any configuration setting or parameter fails validation.
      """
      errors = []

      # Ensure start silence keep duration is within the allowed silence duration range
      if not (self.min_processing_silence_duration_seconds <= self.default_start_silence_keep_duration_seconds <= self.max_processing_silence_duration_seconds):
         errors.append(
            f"Default start silence keep duration ({self.default_start_silence_keep_duration_seconds}s) must be "
            f"between {self.min_processing_silence_duration_seconds}s and {self.max_processing_silence_duration_seconds}s."
         )

      # Ensure minimum silence duration is within the configured bounds
      if not (self.min_processing_silence_duration_seconds <= self.default_min_silence_duration_seconds <= self.max_processing_silence_duration_seconds):
         errors.append(
            f"Default minimum silence duration ({self.default_min_silence_duration_seconds}s) must be "
            f"between {self.min_processing_silence_duration_seconds}s and {self.max_processing_silence_duration_seconds}s."
         )

      # Ensure silence threshold is within the dB range limits
      if not (self.min_silence_threshold_db <= self.default_silence_threshold_db <= self.max_silence_threshold_db):
         errors.append(
            f"Default silence threshold ({self.default_silence_threshold_db} dB) must be "
            f"between {self.min_silence_threshold_db} dB and {self.max_silence_threshold_db} dB."
         )

      # Validate runtime parameters if provided
      if threshold is not None:
          if not (self.min_silence_threshold_db <= threshold <= self.max_silence_threshold_db):
              errors.append(
                  f"Silence threshold ({threshold} dB) must be between "
                  f"{self.min_silence_threshold_db} dB and {self.max_silence_threshold_db} dB."
              )

      # Validate minimum silence duration if provided
      if min_silence is not None:
          if not (self.min_processing_silence_duration_seconds <= min_silence <= self.max_processing_silence_duration_seconds):
              errors.append(
                  f"Minimum silence duration ({min_silence}s) must be between "
                  f"{self.min_processing_silence_duration_seconds}s and {self.max_processing_silence_duration_seconds}s."
              )

      # Validate start silence duration if provided
      if start_silence is not None:
          if not (self.min_processing_silence_duration_seconds <= start_silence <= self.max_processing_silence_duration_seconds):
              errors.append(
                  f"Start silence duration ({start_silence}s) must be between "
                  f"{self.min_processing_silence_duration_seconds}s and {self.max_processing_silence_duration_seconds}s."
              )

      # Raise exception if any config validation checks fail
      if errors:
         raise ValueError("Configuration validation failed:\n" + "\n".join(f"- {error}" for error in errors))
   
   
   # Ensure temp_directory is always an absolute path, even if TrimlyConfig is instantiated directly
   def __post_init__(self):
      object.__setattr__(self, "temp_directory", os.path.abspath(self.temp_directory))


# Global Configuration Management
_config: Optional[TrimlyConfig] = None


def get_config() -> TrimlyConfig:
   """
   Retrieves the global configuration instance for the application.

   If the configuration has not been loaded yet, it attempts to create it
   from environment variables and then validates it.

   Returns:
      The singleton TrimlyConfig instance.

   Raises:
      ValueError: If the configuration loaded from environment variables
                  or defaults fails validation.
   """
   global _config
   if _config is None:
      _config = TrimlyConfig.from_env()
      _config.validate()
      os.makedirs(_config.temp_directory, exist_ok=True)
   return _config


def set_config(config: TrimlyConfig) -> None:
   """
   Sets the global configuration instance to a new TrimlyConfig object.

   The provided configuration instance is validated before being set.

   Args:
      config: The new TrimlyConfig instance to set.

   Raises:
      ValueError: If the provided configuration fails validation.
   """
   global _config
   config.validate()
   _config = config


def reset_config() -> None:
   """
   Resets the global configuration instance.

   The next call to `get_config()` will reload the configuration
   from environment variables and defaults.
   """
   global _config
   _config = None
      