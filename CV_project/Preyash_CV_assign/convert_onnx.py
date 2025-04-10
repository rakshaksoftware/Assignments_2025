from ultralytics import YOLO

model = YOLO('best.pt')

model.export(format='onnx')

# I'm not able to convert to .onnx format in my laptop