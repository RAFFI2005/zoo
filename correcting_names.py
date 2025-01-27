import os

images_dir = 'dataset/images'  
index = 285

images_list = os.listdir(images_dir)
images_list = sorted(images_list, key=lambda x: int(x.split('.')[0]))

for image_name in images_list[index:]:

    image_index = int(image_name.split('.')[0])

    new_index = image_index - 1
    new_name = f"{new_index}.txt"
    old_path = os.path.join(images_dir, image_name)
    new_path = os.path.join(images_dir, new_name)
    
    os.rename(old_path, new_path)




