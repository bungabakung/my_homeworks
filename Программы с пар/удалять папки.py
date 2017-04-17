import os
import shutil

for root, dirs, files in os.walk('C:\\Users\\student\\Documents\\Новая папка', topdown = False):
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))
shutil.rmtree('C:\\Users\\student\\Documents\\Новая папка')
