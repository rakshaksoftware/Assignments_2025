from ultralytics import YOLO

model = YOLO('best1.pt')

#for best1.pt label is "Red and White Bullseye"

img = "checkimage/bus.jpg" 
results = model.predict(source=img , save=True)
for r in results:
    print(r.boxes)  

img2 = "checkimage/blue_bullseye.png"
results2 = model.predict(source=img2 , save=True)

for r in results2:
    print(r.boxes)  

img3 = "checkimage/red_bullseye.jpg"
results3 = model.predict(source=img3 , save=True)

for r in results3:
    print(r.boxes) 


