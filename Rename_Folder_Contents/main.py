# Using built-in OS module to work with files and directories of the system.
import os

# Taking the path of the directory, file name not to be changed, and extension from the user.
path = input("Enter the complete path of the folder: ")
unchanged_file = input("Enter that file-name that you don't want to change:  ")
extension = input("Enter the extension of the file which is to be numbered serially: ")

# getting the actual path of the directory.
os.chdir(path)

# listing all the files and directories in the path list.
files_list = os.listdir(path)

# a variable for numbering the files.
numbering = 1

for i in files_list:
    # splitting the files as name and extension.
    # no_change list will keep the name and extensions.
    no_change = os.path.splitext(i)

    # If the current file is not to be changed, just capitalize it. 
    # We can also pass or avoid this if case.
    if no_change[0] == unchanged_file:
        new_name = str(i).capitalize()
        os.rename(i , new_name)

    # If the current file is to be changed, rename them serially.
    elif no_change[1] == extension:
        os.rename(i , f"{numbering}.{extension}")
        numbering += 1

    
