import os
import shutil

path = "D:/foldercopy/"
dest = "D:/folderdest/"

ls_files = os.listdir(path)

print(ls_files)
for i in ls_files :
    shutil.copy(path + i, dest)