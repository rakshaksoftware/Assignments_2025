from ultralytics import YOLO
import cv2

# Loading the model
model = YOLO("best.pt") 

# Loading the image
image_path = "test13.jpg"  
results = model(image_path)

# Get image for annotation
image = cv2.imread(image_path)

if image is None:
    raise ValueError(f"Image not found at path: {image_path}")


for result in results:
    boxes = result.boxes
    for box in boxes:
        conf = float(box.conf)
        if conf > 0.8:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            cls = int(box.cls[0])  
            label = f"{model.names[cls]} {conf:.2f}"

            # Draw the bounding box and label on the image
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 255, 0), 2)

# Show the image
cv2.imshow("YOLOv8 Detection (Filtered)", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result
cv2.imwrite("output13.jpg", image)
