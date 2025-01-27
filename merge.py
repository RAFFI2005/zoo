import os
import shutil


image_dirs = ['data/elephant/images', 'data/rhino/images', 'data/zebra/images', 'data/buffalo/images']
label_dirs = ['data/elephant/labels', 'data/rhino/labels', 'data/zebra/labels', 'data/buffalo/labels']

dataset = 'dataset'
images = 'dataset/images'
labels = 'dataset/labels'
os.makedirs(images, exist_ok=True)
os.makedirs(labels, exist_ok=True)

for image_dir in image_dirs:
    image_list = os.listdir(image_dir)
    for image_name in image_list:
        shutil.copy(os.path.join(image_dir, image_name), os.path.join(images, image_name))

for label_dir in label_dirs:
    label_list = os.listdir(label_dir)
    for label_name in label_list:
        shutil.copy(os.path.join(label_dir, label_name), os.path.join(labels, label_name))
