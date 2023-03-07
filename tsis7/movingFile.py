import os, shutil
path=input('way to ur file')
if os.path.exists(path):
    new=input('New path')
    new_location= shutil.move(path, new)
else:
    print("path not exist!")
