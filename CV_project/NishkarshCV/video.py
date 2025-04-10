from ultralytics import YOLO
import cv2

# Load the model
model = YOLO("best.pt")

# Load video
cap = cv2.VideoCapture("testvdo.mp4")  # Replace with your video path
width = int(cap.get(3))
height = int(cap.get(4))
out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            conf = float(box.conf)
            if conf > 0.6:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])
                label = f"{model.names[cls]} {conf:.2f}"

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)

    out.write(frame)

    # Optional: Show live
    cv2.imshow("YOLOv8 Detection (Filtered)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
