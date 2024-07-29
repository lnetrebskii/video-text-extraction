import argparse
import os
from pathlib import Path
from capture_frames import capture_frames
from clean_text import clean_text_with_chatgpt
from extract_words import extract_b1_words, save_words_to_csv
from utils import extract_text_from_frames

def main(video_path):
    video_file = Path(video_path)
    output_raw_text_file = video_file.with_suffix('.raw.txt')
    output_cleaned_text_file = video_file.with_suffix('.txt')
    output_csv_file = video_file.with_suffix('.csv')

    # Get the API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")

    # Create a directory to save the frames
    frames_dir = video_file.parent / 'frames'
    frames_dir.mkdir(exist_ok=True)

    # Capture frames
    frames = capture_frames(video_path, frames_dir, capture_interval=30)

    # Extract text from frames
    raw_text = extract_text_from_frames(frames)

    # Save the raw text to a text file
    with open(output_raw_text_file, 'w', encoding='utf-8') as raw_text_file:
        raw_text_file.write(raw_text)

    # Clean the text using ChatGPT
    cleaned_text = clean_text_with_chatgpt(raw_text, api_key)

    # Save the cleaned text to a text file
    with open(output_cleaned_text_file, 'w', encoding='utf-8') as cleaned_text_file:
        cleaned_text_file.write(cleaned_text)

    # Extract words suitable for English learners of B1 and higher levels
    words = extract_b1_words(cleaned_text, api_key)

    # Save words to a CSV file
    save_words_to_csv(words, output_csv_file)

    print(f"Raw text has been saved to {output_raw_text_file}")
    print(f"Cleaned text has been saved to {output_cleaned_text_file}")
    print(f"Words have been saved to {output_csv_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process video to extract text and words for English learners.")
    parser.add_argument("--video", type=str, required=True, help="Path to the video file")
    args = parser.parse_args()

    main(args.video)
