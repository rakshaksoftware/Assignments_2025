
from ultralytics import YOLO

model = YOLO('best.pt')

#for best.pt label is "target_red"

model.predict(source=0, conf=0.5, show=True)
 