from ultralytics import YOLO

model=YOLO(r"runs\detect\train22\weights\best.pt")

model.predict(source=0, conf=0.5, show=True)
