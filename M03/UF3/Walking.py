#FileListDirectoriesAndFiles.py

#!/usr/bin/python
"""
Mòdul  os  per "caminar" pels directoris.

Mòdul glob (The glob module finds all the pathnames matching a specified pattern )
"""



import os



# traverse root directory,

#and list directories as dirs and files as files

for root, dirs, files in os.walk("."):

   path = root.split(os.sep)

   print((len(path) - 1) * '---', os.path.basename(root))

   for file in files:

       print(len(path) * '---', file)

#Mostrar les carpetes i fitxers recursivament
#OsPath.py
home = os.path.expanduser("~")

print(home)

# Note: If '/' is there in the end of {path}, the behavior is different

path = "/."



# This give the head of the path

print(f"The dirname path is: {os.path.dirname(path)}")



# This gives the tail of the path

print(f"The basename path is: {os.path.basename(path)}")

#OsPath.py

# ...

#Template for general crawling:

for root, dir_names, file_names in os.walk(path):

   print(f"The root is {root}")

   print(f"The directory name is: {dir_names}")

   print(f"The file names are: {file_names}")

   print(f"*"*10)

   # FileGlob.py

   # Python program to find files recursively using Python

   """

   Using Glob() function to find files recursively

   We can use the function glob.glob() or glob.iglob() directly from glob module to retrieve paths recursively from inside

   the directories/files and subdirectories/subfiles.



   Syntax:

      glob.glob(pathname, *, recursive=False)

      glob.iglob(pathname, *, recursive=False)



   Note: When recursive is set True “**” followed by path separator('./**/') will match any files or directories.

   """

   import glob

   # Returns a list of names in list files.

   print("Using glob.glob()")

   files = glob.glob('./**/*.py', recursive=True)

   for file in files:
      print(file)