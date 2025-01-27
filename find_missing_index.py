import os


def find(arr):
    indices = []
    arr.sort()
    i = 1
    while i < len(arr):
        if i not in arr:
            indices.append(i)
        i += 1
    return indices

dirs = ['data/buffalo/labels', 'data/elephant/labels', 'data/rhino/labels', 'data/zebra/labels']


for dir in dirs:
    arr = [int(filename[:filename.find('.')]) for filename in os.listdir(dir)]
    print(f'For directory {dir} these are missing indices:')
    indices = find(arr)
    print(indices)

    for i in indices:
        #os.rename(os.path.join(dir, f"{arr[-1]}.jpg"), os.path.join(dir, f"{i}.jpg"))
        os.rename(os.path.join(dir, f"{arr[-1]}.txt"), os.path.join(dir, f"{i}.txt"))

        arr.pop()



