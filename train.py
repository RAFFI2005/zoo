from ultralytics import YOLO


model = YOLO('yolo11l.pt')
results = model.train(data='dataset', epochs=20, imgsz=640, device=[0,1,2,3])

