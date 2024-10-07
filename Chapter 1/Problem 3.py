# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

#Specify the directory you want ti list
directory_path = '/MCA_SEM_4'

#List all the files and directories in the specified path
content = os.listdir(directory_path)    #listdir is the function used to list the conntent using OS module

print(content)
