from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
from backend.helmet import detect_helmet  # YOLO detection for helmets
from backend.mask import detect_mask  # YOLO detection for masks
from backend.weapon import detect_weapon  # YOLO detection for weapons

app = FastAPI()

previous_frame = None  # Store the last frame for static detection

def detect_tampering(frame):
    """
    Detects camera tampering:
    - Full or Partial Black screen detection (camera covered)
    - Static frame detection (camera frozen)
    """
    global previous_frame

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get frame dimensions
    height, width = gray_frame.shape

    # **Define Regions (Top/Bottom or Left/Right)**
    top_half = gray_frame[:height // 2, :]
    bottom_half = gray_frame[height // 2:, :]
    left_half = gray_frame[:, :width // 2]
    right_half = gray_frame[:, width // 2:]

    # **Black Frame Detection (Full or Partial)**
    avg_brightness = np.mean(gray_frame)
    avg_top = np.mean(top_half)
    avg_bottom = np.mean(bottom_half)
    avg_left = np.mean(left_half)
    avg_right = np.mean(right_half)

    if avg_brightness < 10:  # **Entire screen black**
        return frame, "Camera Fully Covered (Black Screen Detected)"
    
    if avg_top < 10:
        return frame, "Top Half Covered"

    if avg_bottom < 10:
        return frame, "Bottom Half Covered"

    if avg_left < 10:
        return frame, "Left Half Covered"

    if avg_right < 10:
        return frame, "Right Half Covered"

    # **Static Frame Detection (Frozen Camera)**
    if previous_frame is not None:
        diff = cv2.absdiff(previous_frame, gray_frame)
        non_zero_count = np.count_nonzero(diff)
        if non_zero_count < 1000:  # If very few pixel changes, camera may be frozen
            return frame, "Camera Frozen (No Movement Detected)"

    previous_frame = gray_frame  # Update previous frame
    return frame, None  # No tampering detected

def generate_frames(detection_func=None, tampering=False):
    """
    Captures frames from the laptop camera and applies detection or tampering checks.
    """
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Use Laptop Camera

    if not cap.isOpened():
        print("Error: Could not open laptop camera")
        return None

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 15)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame")
            break

        if tampering:
            frame, tamper_msg = detect_tampering(frame)
            if tamper_msg:
                cv2.putText(frame, tamper_msg, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        elif detection_func:
            frame, _ = detection_func(frame)

        _, encoded_frame = cv2.imencode('.jpg', frame)
        frame_bytes = encoded_frame.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

@app.get("/")
def home():
    return {"message": "Helmet, Mask, Weapon & Tampering Detection API is Running!"}

@app.get("/helmet_feed/")
def helmet_feed():
    return StreamingResponse(generate_frames(detect_helmet), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/mask_feed/")
def mask_feed():
    return StreamingResponse(generate_frames(detect_mask), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/weapon_feed/")
def weapon_feed():
    return StreamingResponse(generate_frames(detect_weapon), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/tampering_feed/")
def tampering_feed():
    """
    Endpoint for camera tampering detection.
    """
    return StreamingResponse(generate_frames(tampering=True), media_type="multipart/x-mixed-replace; boundary=frame")
