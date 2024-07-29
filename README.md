# Video Text Extraction for English Learners

This project extracts text from video files, cleans the text using ChatGPT, and extracts words suitable for English learners of B1 and higher levels.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/video-text-extraction.git
   cd video-text-extraction
   ```
2. Install the dependencies:

    ```sh
    python3 -m venv .venv
    . .venv/bin/activate
    pip3 install -r requirements.txt
    ```
3. Install Tesseract OCR:
   * macOS:
    ```sh
    brew install tesseract
    ```
    * Windows:
    Download the installer from https://github.com/UB-Mannheim/tesseract/wiki and follow the installation instructions.

## Usage
1. Set your OpenAI API key as an environment variable:
    * macOS/Linux:
    ```sh
    export OPENAI_API_KEY=your_openai_api_key
    ```

    * Windows:
    ```sh
    set OPENAI_API_KEY=your_openai_api_key
    ```
    Replace your_openai_api_key with your actual OpenAI API key.
2. Place your video file in the example directory.
3. Run the main script:
    ```sh
    python src/main.py --video example/example_video.mp4
    ```

## Directory Structure
    * `src/`: Source code for processing the video.
    * `data/`: Directories to save raw texts and frames.
    * `example/`: Example video file.
## License
MIT License