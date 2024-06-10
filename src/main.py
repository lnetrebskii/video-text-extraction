import argparse
from pathlib import Path
from capture_frames import capture_frames
from clean_text import clean_text_with_chatgpt
from extract_words import extract_b1_words, save_words_to_csv
from utils import extract_text_from_frames

def main(video_path, api_key):
    video_file = Path(video_path)
    output_text_file = video_file.with_suffix('.txt')
    output_csv_file = video_file.with_suffix('.csv')

    # Create a directory to save the frames
    frames_dir = video_file.parent / 'frames'
    frames_dir.mkdir(exist_ok=True)

    # Capture frames
    frames = capture_frames(video_path, frames_dir, capture_interval=30)

    # Extract text from frames
    raw_text = extract_text_from_frames(frames)

    # Clean the text using ChatGPT
    cleaned_text = clean_text_with_chatgpt(raw_text, api_key)

    # Extract words suitable for English learners of B1 and higher levels
    words = extract_b1_words(cleaned_text, api_key)

    # Save words to a CSV file
    save_words_to_csv(words, output_csv_file)

    print(f"Text has been saved to {output_text_file}")
    print(f"Words have been saved to {output_csv_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process video to extract text and words for English learners.")
    parser.add_argument("--video", type=str, required=True, help="Path to the video file")
    parser.add_argument("--apikey", type=str, required=True, help="OpenAI API key")
    args = parser.parse_args()

    main(args.video, args.apikey)
