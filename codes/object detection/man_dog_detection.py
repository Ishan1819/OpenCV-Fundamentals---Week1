import torch
import cv2

# Load YOLOv5 model (small version, pre-trained on COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Path to image
image_path = "man_and_dog.jpg"  # Your uploaded image file

# Read image
img = cv2.imread(image_path)

# Perform detection
results = model(img)

detections = results.pandas().xyxy[0]  

for i, det in detections.iterrows():
    x1, y1, x2, y2 = int(det['xmin']), int(det['ymin']), int(det['xmax']), int(det['ymax'])
    label = det['name']  # Object name (not hardcoded)
    # conf = det['confidence']

    # Draw rectangle
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
    # Draw label
    cv2.putText(img, f"{label}", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (210, 0, 255), 2)

output_path = "detected_output.jpg"
cv2.imwrite(output_path, img)

print(f"[INFO] Detection done. Saved at {output_path}")
