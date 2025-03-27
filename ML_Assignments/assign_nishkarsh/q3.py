import cv2
import os
from ultralytics import YOLO

# Initialize model and paths
model = YOLO("yolov8n.pt")  # Pre-trained YOLO model
image_paths = [
    "C:/Users/nishk/Downloads/Documents/free-photo-of-black-and-white-urban-street-scene-in-japan.jpeg",
    "C:/Users/nishk/Downloads/Documents/download (1).jpeg",
    "C:/Users/nishk/Downloads/Documents/download.jpeg"
]

output_dir = "YOLOresults"

# Create output directory if missing
os.makedirs(output_dir, exist_ok=True)

for image_path in image_paths:
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print(f"⚠️ Skipping missing image: {image_path}")
        continue

    print(f"🔍 Processing: {os.path.basename(image_path)}")
    
    # Run object detection
    results = model(img)
    
    # Process detections
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        labels = result.boxes.cls.cpu().numpy()
        conf_scores = result.boxes.conf.cpu().numpy()

        # Draw annotations
        for i, (box, label_idx, conf) in enumerate(zip(boxes, labels, conf_scores)):
            x1, y1, x2, y2 = map(int, box)
            label = model.names[int(label_idx)]
            
            # Draw bounding box and label
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, 
                       f"{label}: {conf:.2f}", 
                       (x1, y1-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 
                       0.6, 
                       (0, 0, 255), 
                       2)

        # Save processed image
        output_path = os.path.join(output_dir, f"detected_{os.path.basename(image_path)}")
        cv2.imwrite(output_path, img)
        print(f"💾 Saved results to: {output_path}")

# Display results summary
print("\n🎯 Detection Complete - Showing Results:")
for image_path in image_paths:
    result_path = os.path.join(output_dir, f"detected_{os.path.basename(image_path)}")
    img = cv2.imread(result_path)
    
    if img is not None:
        img = cv2.resize(img, (0, 0), fx=5, fy=5)
        cv2.imshow("Object Detection Preview", img)
        cv2.waitKey(0)  # Display each image for 2 seconds
    else:
        print(f"⚠️ Missing result file: {result_path}")

cv2.destroyAllWindows()
