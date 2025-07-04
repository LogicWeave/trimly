import gradio as gr
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from trimly import Trimly, __version__


def trim_audio(audio_file, threshold, min_silence):
   if audio_file is None:
      print("No audio file provided")
      return None

   try:
      print(f"Processing: {audio_file}")
      print(f"Threshold: {threshold} dB, Min silence: {min_silence}s")

      trimly = Trimly()
      message, output_path = trimly.trim_audio(
         file_path=audio_file,
         threshold=threshold,
         min_silence=min_silence
      )

      if output_path:
         print(f"Success: {output_path}")
         return output_path
      else:
         print(f"Failed: {message}")
         return None

   except Exception as e:
      print(f"Error: {e}")
      return None


def clear_inputs():
   print("Clearing inputs")
   return None, -45, 0.05, None


def interface():
   with gr.Blocks(
      title="Trimly",
      theme=gr.themes.Soft(primary_hue="teal", secondary_hue="teal", neutral_hue="slate"),
      css="""
      @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
      body, .gradio-container {font-family: 'Poppins', sans-serif;}
      .gradio-container {padding: 2rem;}
      """
   ) as demo:

      gr.Markdown(f"""
      ## Trimly v{__version__}
      **Clean up your voiceovers by removing dead air and long pauses using FFmpeg.**
      """)

      with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(label="Upload MP3 or WAV", type="filepath")
            threshold = gr.Slider(-60, 0, value=-45, step=1, label="Silence Threshold (dB)")
            min_silence = gr.Slider(0.01, 1.0, value=0.05, step=0.01, label="Min Silence Duration (sec)")
            
            with gr.Row():
               clear_btn = gr.Button("Clear", variant="secondary")
               trim_btn = gr.Button("Submit", variant="primary")

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

      # Connect functions to buttons
      trim_btn.click(
         fn=trim_audio,
         inputs=[audio_input, threshold, min_silence],
         outputs=audio_output
      )

      clear_btn.click(
         fn=clear_inputs,
         outputs=[audio_input, threshold, min_silence, audio_output]
      )

   return demo


def main():
   app = interface()
   app.queue()
   app.launch(inbrowser=True, share=False)

if __name__ == "__main__":
    main()