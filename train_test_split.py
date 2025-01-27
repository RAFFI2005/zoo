import os
import shutil
import random

images_dir = 'dataset/images'
labels_dir = 'dataset/labels'

train_images_dir = 'dataset/train/images'
train_labels_dir = 'dataset/train/labels'
test_images_dir = 'dataset/test/images'
test_labels_dir = 'dataset/test/labels'

os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(test_labels_dir, exist_ok=True)


images_list = os.listdir(images_dir)
labels_list = os.listdir(labels_dir)
 
num_list = list(range(1504)) 
random.shuffle(num_list)

index = int(len(num_list) * 0.8)

num_list_train = num_list[:index]
num_list_test = num_list[index:]   
for filename in num_list_train:
    shutil.copy(os.path.join(images_dir, f"{filename}.jpg"), train_images_dir)
    shutil.copy(os.path.join(labels_dir, f"{filename}.txt"), train_labels_dir)
for filename in num_list_test:
    shutil.copy(os.path.join(images_dir, f"{filename}.jpg"), test_images_dir)
    shutil.copy(os.path.join(labels_dir, f"{filename}.txt"), test_labels_dir)

