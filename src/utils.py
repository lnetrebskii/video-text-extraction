import pytesseract
import cv2

def extract_text_from_frames(frames):
    raw_texts = []
    for frame in frames:
        img = cv2.imread(frame)
        text = pytesseract.image_to_string(img)
        raw_texts.append(text)
    return "\\n".join(raw_texts)
