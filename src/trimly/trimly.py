import os
import subprocess

TMP_DIR = "tmp"
os.makedirs(TMP_DIR, exist_ok=True)

def clean_tmp():
    for f in os.listdir(TMP_DIR):
        fp = os.path.join(TMP_DIR, f)
        if os.path.isfile(fp):
            os.remove(fp)

def trim_audio(file, threshold, min_silence):
    if file is None:
        return "No file provided", None

    filename = os.path.basename(file)
    name, ext = os.path.splitext(filename)

    if name.startswith("enhanced"):
        return f"⚠️ Skipped '{filename}' (already enhanced).", None

    output_path = os.path.join(TMP_DIR, f"enhanced_{name}.wav")

    cmd = [
        "ffmpeg", "-y", "-i", file,
        "-af", f"silenceremove=start_periods=1:start_silence=0.1:start_threshold={threshold}dB:"
               f"stop_periods=-1:stop_silence={min_silence}:stop_threshold={threshold}dB:detection=peak",
        output_path
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return f"✅ Trimmed successfully → enhanced_{name}.wav", output_path
