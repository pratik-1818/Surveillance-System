import cv2
import torch
from ultralytics import YOLO
import numpy as np

# Load YOLOv8 model for mask detection
model = YOLO("/home/vmukti/Desktop/Surveillance System/model /best (3).pt")  # Update the path if needed

# Define class names
class_names = ["with mask", "without mask"]

def detect_mask(frame):
    """
    Run YOLO detection on a frame.
    Returns the processed frame and detections.
    """
    results = model(frame)

    detections = []
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        confidences = result.boxes.conf.cpu().numpy()
        class_ids = result.boxes.cls.cpu().numpy().astype(int)

        for box, confidence, class_id in zip(boxes, confidences, class_ids):
            if confidence > 0.6 and class_id < len(class_names):
                x1, y1, x2, y2 = map(int, box)
                class_name = class_names[class_id]
                color = (0, 255, 0) if class_name == "without mask" else (0, 0, 255)
                
                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

                detections.append({
                    "class": class_name,
                    "confidence": float(confidence),
                    "box": [x1, y1, x2, y2]
                })
    
    return frame, detections
