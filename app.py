import gradio as gr
from trimly import trim_audio, clean_tmp

clean_tmp()

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
