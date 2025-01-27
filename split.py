import os
import shutil


dirs = ['data/buffalo', 'data/elephant', 'data/rhino', 'data/zebra']
image_dirs = []
label_dirs = []
new_dirs = []

for dir in dirs:
    os.makedirs(os.path.join('data', dir), exist_ok=True)
    os.makedirs(os.path.join('data', dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join('data', dir, 'labels'), exist_ok=True)

for dir in dirs:
    for filename in os.listdir(dir):
        if filename.endswith(('.jpg', 'JPG')):
            shutil.move(os.path.join(dir, filename), os.path.join('data', dir, 'images', filename))
        if filename.endswith('.txt'):
            shutil.move(os.path.join(dir, filename), os.path.join('data', dir, 'labels', filename))