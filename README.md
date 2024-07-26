## Ollama Text Summarization Projeect

This project provides a Python command-line tool that utilizes the Ollama API and the Qwen2-0.5B model to summarize text from a file or directly from user input.

### Prerequisites

* **Operating System:** Any operating system that supports Python (Windows, macOS, Linux)
* **Python:** Version 3.6 or later (check with `python --version` in your terminal)
* **Ollama Server:** You'll need a locally running Ollama server.
    * Download and install Ollama from [here](https://ollama.com/download). Follow the installation instructions for your OS.

### Installation

**Download the Qwen2-0.5B model:** 

   ```bash
   ollama run qwen2:0.5b
   ```

### Project Setup

1. **Create a project folder:**

   ```bash
   mkdir Ollama-Text-Summarization
   cd Ollama-Text-Summarization
   ```

2. **Create a Python virtual environment (optional, recommended):**

   - **Using `venv`:**

     ```bash
     python -m venv ollama-env
     source ollama-env/bin/activate
     ```

   - **Using `virtualenv`:**

     ```bash
     virtualenv ollama-env
     source ollama-env/bin/activate
     ```

3. **Activate the virtual environment (if you created one).**

4. **Install dependencies within the virtual environment:**

   ```bash
   pip install -r requirements.txt  # Assuming you have a requirements.txt file (optional)
   ```

### Usage

1. **Create a Python script:** (Save this code as `app.py`)

   ```python
   # ... (Insert the code from your previous response) ...
   ```

2. **Run the script:**

   - **With text input:**

     ```bash
     python app.py "The quick brown fox..."
     ```

   - **With a text file:**

     ```bash
     python app.py -t book.txt
     ```

**Example Output:**

```
. Summary of text pasted:
This is a concise summary of the key points in the text.  # (This will be replaced by the actual summary)
```

### Additional Notes

* The provided code handles potential errors like missing input and summarizes text with a clear indication of the source (file or pasted text).
* You can experiment with different prompts to fine-tune the summary style and focus.
* Make sure your Ollama server is running and the Qwen2-0.5B model is installed locally for the script to function correctly.