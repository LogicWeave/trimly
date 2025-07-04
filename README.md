# Trimly

**Professional silence removal for voice recordings using FFmpeg**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/LogicWeaver/trimly/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Powered by FFmpeg](https://img.shields.io/badge/powered%20by-FFmpeg-red.svg)](https://ffmpeg.org/)
[![Gradio UI](https://img.shields.io/badge/UI-Gradio-ff69b4.svg)](https://www.gradio.app/)

Trimly is a powerful audio processing tool that automatically removes unwanted silence and dead air from voice recordings, making them cleaner and more professional. Perfect for voiceovers, audiobooks, podcasts, and content creators.

🚀 **[Try Trimly Demo on Hugging Face](https://huggingface.co/spaces/LogicWeaveHF/trimly)**

## ✨ Features

- 🎯 **Intelligent Silence Detection** - Advanced FFmpeg-based silence removal
- 🎛️ **Customizable Parameters** - Fine-tune threshold and duration settings
- 🌐 **Web Interface** - Clean, modern Gradio-based UI
- 📁 **Multiple Formats** - Supports MP3, WAV, M4A, FLAC, OGG
- ⚡ **Fast Processing** - Efficient FFmpeg backend
- 🔧 **Professional Grade** - Robust error handling and validation

## Getting Started

### Prerequisites

- Python 3.10+
- FFmpeg installed and available in PATH

### Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/LogicWeave/trimly.git
   cd trimly
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   # Full installation
   pip install .

   # Or minimal installation (just Gradio)
   pip install gradio
   ```

4. **Install FFmpeg** (if not already installed)

   ```bash
   # Ubuntu/Debian
   sudo apt update && sudo apt install ffmpeg

   # macOS
   brew install ffmpeg

   # Windows
   # Download from https://ffmpeg.org/download.html
   ```

5. **Launch the app**

   ```bash
   python app.py
   ```

   Trimly will launch in your default browser.

## Parameters Guide

**Silence Threshold (dB)**

- **-45 dB**: Good starting point for most recordings
- **-60 dB**: More aggressive, removes quieter background noise
- **-30 dB**: Conservative, only removes obvious silence

**Min Silence Duration (seconds)**

- **0.05s**: Standard for voice recordings
- **0.1s**: Preserves natural pauses
- **0.02s**: Very aggressive trimming

## How It Works

Trimly uses FFmpeg’s `silenceremove` filter to detect and trim silent segments. You control how it behaves:

- **Silence Threshold (dB)**: How quiet is “silent”?
- **Minimum Silence Duration (sec)**: How long before it gets chopped?

This lets you remove awkward gaps from voiceovers with surgical precision.

## Contributing

Contributions are welcome! Whether you're fixing bugs, adding features, or improving documentation, your input helps make Trimly better for everyone.

- Read the [Contributing Guidelines](.github/CONTRIBUTING.md)
- Follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md)

## License

Trimly is released under the MIT License. For the full license text, please see the [LICENSE](LICENSE) file.
