from pathlib import Path
import subprocess
from typing import Union, Optional, Tuple

from .utils.exceptions import TrimlyError, UnsupportedFormatError, FFmpegNotFoundError
from .utils.file_validation import validate_audio_file
from .utils.ffmpeg_availability import check_ffmpeg_availability
from .configs import get_config

class Trimly:
   def __init__(self, config=None):
      self.config = config or get_config()
      self.tmp_dir = self._ensure_tmp_dir()
      self._check_ffmpeg_availability()

   def _ensure_tmp_dir(self) -> Path:
      tmp_path = Path(self.config.temp_directory)
      try:
         tmp_path.mkdir(parents=True, exist_ok=True)
         return tmp_path
      except OSError as e:
         raise TrimlyError(f"Failed to create temporary directory: {e}")

   def _check_ffmpeg_availability(self) -> None:
      return check_ffmpeg_availability()

   def validate_file(self, file_path: Union[str, Path]) -> Path:
      return validate_audio_file(file_path)

   def validate_parameters(self, threshold: float, min_silence: float, start_silence: float) -> None:
      self.config.validate(threshold, min_silence, start_silence)

   def trim_audio(
      self,
      file_path: Union[str, Path],
      threshold: Optional[float] = None,
      min_silence: Optional[float] = None,
      start_silence: Optional[float] = None
   ) -> Tuple[str, Optional[str]]:
      if not file_path:
         return "No file provided", None

      try:
         input_path = self.validate_file(file_path)

         threshold = threshold or self.config.default_silence_threshold_db
         min_silence = min_silence or self.config.default_min_silence_duration_seconds
         start_silence = start_silence or self.config.default_start_silence_keep_duration_seconds

         self.validate_parameters(threshold, min_silence, start_silence)

         output_path = self.tmp_dir / f"{input_path.stem}.wav"

         silence_filter = self.config.ffmpeg_silence_filter_template.format(
                start_silence=start_silence,
                threshold=threshold,
                min_silence=min_silence
            )

         cmd = [
               "ffmpeg", "-y", "-i", str(input_path),
               "-af", silence_filter,
               str(output_path)
         ]

         result = subprocess.run(
               cmd,
               capture_output=True,
               text=True,
               timeout=self.config.processing_operation_timeout_seconds
         )

         if result.returncode != 0:
               error = result.stderr.strip() or "Unknown FFmpeg error"
               return f"Failed to process audio: {error}", None

         if not output_path.exists() or output_path.stat().st_size == 0:
               return "Failed to process audio: Output file missing or empty", None

         return f"Successfully trimmed: {output_path.name}", str(output_path)

      except subprocess.TimeoutExpired:
         return "Processing timed out", None

      except (TrimlyError, UnsupportedFormatError, FFmpegNotFoundError) as e:
         return str(e), None

      except Exception as e:
         return f"Unexpected error: {str(e)}", None
