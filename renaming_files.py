import os
import shutil

# dirs = ['data/elephant', 'data/rhino', 'data/zebra']

# index = len(os.listdir('data/buffalo/images'))
# for dir in dirs:
#     sub_dirs = os.listdir(dir)
#     dir_len = len(os.listdir(os.path.join(dir, sub_dirs[0])))
#     images = os.path.join(dir, sub_dirs[0])
#     labels = os.path.join(dir, sub_dirs[1])
#     images_list = os.listdir(images)
#     labels_list = os.listdir(labels)
#     indexes = range(index+1, index+1+dir_len)
#     image_index_pairs = zip(indexes, images_list)
#     label_index_pairs = zip(indexes, labels_list)
#     for new_index, old_name in image_index_pairs:
#         old_index = old_name.split('.')[0]
#         new_name = old_name.replace(old_index, str(new_index).zfill(3))
#         os.rename(os.path.join(images, old_name), os.path.join(images, new_name))

#     for new_index, old_name in label_index_pairs:
#         old_index = old_name.split('.')[0]
#         new_name = old_name.replace(old_index, str(new_index).zfill(3))
#         os.rename(os.path.join(labels, old_name), os.path.join(labels, new_name))

#     index += dir_len


dirs = ['data/buffalo', 'data/elephant', 'data/rhino', 'data/zebra']
i = 0
os.makedirs('dataset', exist_ok=True)
output_dir = ["dataset/images", "dataset/lables"]
os.makedirs(output_dir[0], exist_ok=True)
os.makedirs(output_dir[1], exist_ok=True)


for dir in dirs:
    dir_list = os.listdir(os.path.join(dir, "images"))
    for filename in dir_list:
        num = filename.split('.')[0]
        if filename.split('.')[1] == "JPG":
            os.rename(os.path.join(dir, "images", filename), os.path.join(dir, "images", f"{num}.jpg"))
        shutil.copy(os.path.join(dir, "images", f"{num}.jpg"), os.path.join(output_dir[0], f"{i}.jpg"))
        shutil.copy(os.path.join(dir, "labels", f"{num}.txt"), os.path.join(output_dir[1], f"{i}.txt"))
        i +=1
