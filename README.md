# Trimly

[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](https://github.com/LogicWeaver/trimly/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Powered by FFmpeg](https://img.shields.io/badge/powered%20by-FFmpeg-red.svg)](https://ffmpeg.org/)
[![Gradio UI](https://img.shields.io/badge/UI-Gradio-ff69b4.svg)](https://www.gradio.app/)

**Silence Trimmer for Voiceovers — powered by FFmpeg, Python & Gradio**

Trimly is a smart, minimalist tool for cutting long pauses and dead air from audio. It’s perfect for podcasters, voice actors, audiobook narrators — or anyone who wants cleaner, tighter voice recordings with zero editing.

🚀 [**Live Demo on Hugging Face Spaces →**](https://huggingface.co/spaces/your-username/trimly)

## Features

- ⚡ Fast silence removal using `ffmpeg` under the hood
- 🎚️ Customizable threshold and minimum pause length
- 🧠 Simple, clean web UI built with Gradio
- 🔊 Works with `.mp3` and `.wav` files
- 🧼 Zero editing experience required

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/LogicWeaver/trimly.git
cd trimly
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install .
```

### 4. Launch the app

```bash
python app.py
```

Trimly will launch in your default browser.

## How It Works

Trimly uses FFmpeg’s `silenceremove` filter to detect and trim silent segments. You control how it behaves:

- **Silence Threshold (dB)**: How quiet is “silent”?
- **Minimum Silence Duration (sec)**: How long before it gets chopped?

This lets you remove awkward gaps from voiceovers with surgical precision.

## Contributing

Contributions are welcome! Whether you're fixing bugs, adding features, or improving documentation, your input helps make Trimly better for everyone.

- Read the [Contributing Guidelines](docs/CONTRIBUTING.md)
- Follow the [Code of Conduct](docs/CODE_OF_CONDUCT.md)

## License

Trimly is released under the MIT License. For the full license text, please see the [LICENSE](LICENSE) file.
