# Trimly

**Silence Trimmer for Voiceovers — powered by FFmpeg + Python + Gradio**

Trimly is a lightweight, no-nonsense tool that automatically removes long pauses and dead air from audio files. Ideal for podcasters, voiceover artists, audiobook producers — or anyone who values clean, punchy audio.

---

## Features

- 🧠 FFmpeg-powered silence removal
- 🧰 Customizable threshold and pause length
- 🎛️ Intuitive web UI (built with Gradio)
- 🔄 Works with `.wav` and `.mp3` files
- 🧼 Cleans up audio with zero editing skills required

---

## Installation

**1. Clone the Repo**

```bash
git clone https://github.com/LogicWeave/trimly.git
cd trimly
```

**2. Create a Virtual Environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install Requirements**

```bash
pip install -r requirements.txt
```

**4. Run the App**

```bash
python app.py
```

This will launch the app in your browser.

---

## How It Works

Trimly uses FFmpeg’s `silenceremove` filter to analyze and remove silent parts from your audio. You control how silence is detected with:

- **Silence Threshold (dB)** – How quiet a segment must be to count as silence
- **Min Silence Duration (sec)** – How long a pause must be before trimming kicks in

The result? Cleaner, tighter audio — instantly.

## Contributing

Contributions are welcome! Whether you're fixing bugs, adding features, or improving documentation, your input helps make Trimly better for everyone.

- Read the [Contributing Guidelines](docs/CONTRIBUTING.md)
- Follow the [Code of Conduct](docs/CODE_OF_CONDUCT.md)

## License

Trimly is released under the MIT License. For the full license text, please see the [LICENSE](LICENSE) file.
