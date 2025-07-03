import os
import shutil
import subprocess
import gradio as gr

TMP_DIR = "tmp"
os.makedirs(TMP_DIR, exist_ok=True)

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


with gr.Blocks(
    title="Trimly",
    theme=gr.themes.Soft(primary_hue="teal", secondary_hue="teal", neutral_hue="slate"),
    css="""
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    body, .gradio-container {font-family: 'Poppins', sans-serif;}
    .gradio-container {padding: 2rem;}
    """
) as demo:

    gr.Markdown("""
    ## Trimly 
    **Clean up your voiceovers by removing dead air and long pauses using FFmpeg.**
    """)

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(label="Upload MP3 or WAV", type="filepath")
            threshold = gr.Slider(-60, 0, value=-45, step=1, label="Silence Threshold (dB)")
            min_silence = gr.Slider(0.01, 1.0, value=0.05, step=0.01, label="Min Silence Duration (sec)")
            trim_btn = gr.Button("Submit", variant="primary")
            status = gr.Markdown("")

        with gr.Column():
            audio_output = gr.Audio(label="Trimmed Output", type="filepath", interactive=False, show_download_button=True)
            
            gr.Markdown("""
            ### 🛠️ How It Works
            This tool uses FFmpeg's `silenceremove` filter to trim silent sections from your voiceover.

            - **Silence Threshold**: Controls what is considered "silence". Lower = more aggressive.
            - **Min Silence Duration**: Minimum pause length (in seconds) before trimming kicks in.
            - **Output**: Enhanced audio is saved in the `tmp/` folder and auto-deleted on app restart.

            ⚡ _Built for voiceovers, audiobooks, and content creators who hate dead air._
            """)

    trim_btn.click(
        fn=trim_audio,
        inputs=[audio_input, threshold, min_silence],
        outputs=[status, audio_output]
    )

demo.queue().launch(inbrowser=True)
