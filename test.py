from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')

detect = model.predict(source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCyZgQ0HvJOM4ClOKaIzYMxrsOgpnzlUiQ5w&s', save=True)
