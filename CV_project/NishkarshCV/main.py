from ultralytics import YOLO
model = YOLO("yolov8n.pt")  
train_model = model.train(data="data.yaml", epochs=5)  



