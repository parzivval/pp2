"""Write a Python program to list only directories, files and all directories, files in a specified path"""
""" import os
path=r'C:\Users\Бахытжан\Desktop\pp2\testfolder'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Only files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("All directories and files :")
print([ name for name in os.listdir(path)]) """
"""Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path"""
""" import os
print('Exist:', os.access(r'C:\Users\Бахытжан\Desktop\pp2\testfolder', os.F_OK))
print('Readable:', os.access(r'C:\Users\Бахытжан\Desktop\pp2\testfolder', os.R_OK))
print('Writable:', os.access(r'C:\Users\Бахытжан\Desktop\pp2\testfolder', os.W_OK))
print('Executable:', os.access(r'C:\Users\Бахытжан\Desktop\pp2\testfolder', os.X_OK)) """
"""Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path"""
""" import os
print("Test a path exists or not:")
path = r'C:\Users\Бахытжан\Desktop\pp2\testfolder\a.docx'
print(os.path.exists(path))
path = r'C:\Users\Бахытжан\Desktop\pp2\testfolder\b.xlsx'
print(os.path.exists(path))
print("File name of the path:")
print(os.path.basename(path))
print("Directory name of the path:")
print(os.path.dirname(path)) """
"""Write a Python program to count the number of lines in a text file"""
"""with open(r"d.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)"""
"""Write a Python program to write a list to a file"""
""" numbers = [1, 2, 3]
with open(r'd.txt', "w") as file:
        for n in numbers:
                file.write("%s\n" % n)
content=open(r'd.txt')
print(content.read())
 """
"""Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt"""
""" import string
alphabet=string.ascii_lowercase
for letter in alphabet:
    with open(letter+".txt",'w') as file:
        file.write(letter) """
"""Write a Python program to copy the contents of a file to another file """
""" from shutil import copyfile
copyfile('d.txt', 'e.txt') """
"""Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not."""
import os
path=input("Enter the path to file: ")
print('Exist:', os.access(path, os.F_OK))
os.remove(path)