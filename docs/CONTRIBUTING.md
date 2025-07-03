# Contributing to Trimly

Thanks for your interest in contributing to **Trimly** — a simple tool for cleaning up audio by trimming silence using FFmpeg. This guide outlines how you can get involved.

##  Code of Conduct

Please make sure to review and follow our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

##  Getting Started

1. **Fork the repo**  
2. **Clone your fork locally:**

   ```bash
   git clone https://github.com/YOUR-USERNAME/trimly.git
   cd trimly
   ```

3. **Create a new branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

1. Install dependencies in a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Make your changes in `app.py` or wherever needed.

3. Test the Gradio app locally:

   ```bash
   python app.py
   ```

4. Use clear, conventional commit messages:

   ```bash
   git commit -m "feat: add new feature to improve trimming options"
   ```

5. Push your changes:

   ```bash
   git push origin feature/your-feature-name
   ```

6. Submit a Pull Request to the main `LogicWeave/trimly` repo.


## PR Guidelines

* Keep pull requests focused and minimal
* Include a short summary of what you’ve changed
* Feel free to open a Draft PR early for discussion or feedback
* Always test your UI changes before submitting

## Reporting Bugs

If you find a bug:

1. Open a GitHub issue
2. Describe what went wrong and steps to reproduce it
3. Include the OS, Python version, FFmpeg version, etc.
