import os
path=input("Enter the path to file: ")
print('Exist:', os.access(path, os.F_OK))
os.remove(path)