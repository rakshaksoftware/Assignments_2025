from ultralytics import YOLO

model = YOLO("yolov8n.pt") 
train_results=model.train(data="data.yaml", epochs=3) 

img = "checkimage/bus.jpg" 
results = model.predict(source=img, save=True)  

