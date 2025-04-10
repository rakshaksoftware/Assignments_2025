from ultralytics import YOLO
model=YOLO(r"runs\detect\train22\weights\best.pt")

img = r".\Red_and_White.png" 

results = model(img)  # Predict on an image
results[0].show()


