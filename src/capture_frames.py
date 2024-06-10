import cv2
from pathlib import Path

def capture_frames(video_path, output_dir, capture_interval=30):
    cap = cv2.VideoCapture(video_path)
    frames = []
    success, image = cap.read()
    count = 0

    while success:
        if count % capture_interval == 0:
            frame_path = output_dir / f"frame_{count}.png"
            cv2.imwrite(str(frame_path), image)
            frames.append(str(frame_path))
            print(f"Captured frame at count: {count}")
        success, image = cap.read()
        count += 1

    cap.release()
    return frames
