import ultralytics
from ultralytics import YOLO
import os

# Prints the current working directory.
print(os.getcwd())
model = YOLO("runs\\detect\\train\\weights\\best.pt")

results=model.train(data="config.yaml",epochs=5,batch=64)
