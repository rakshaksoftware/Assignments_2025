from ultralytics import YOLO

model = YOLO("runs/detect/train9/weights/best.pt") 
model.export(format="onxx")