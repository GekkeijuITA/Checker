from tkinter import filedialog

import subprocess
import os
import shutil
import pathlib

# Global variables
exe_file = "test"
files = 0
i = 0
cpp = 0
output = {}

# Credits: https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters/13685020
def printProgressBar(iteration , total , prefix = '' , suffix = '' , decimals = 1 , length = 100 , fill = '█' , printEnd = "\r"): 
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()

def delete_file(file): # Delete passed file
    os.remove(file)

def check_file(file): # Run the command and add errors in global dictionary
    global output
    cmd = ["g++", "-Wall" , "-std=c++14" , file , "-o" , exe_file] # compile the file, cross-platform
    returned_output = subprocess.run(cmd , stdout=subprocess.PIPE, stderr=subprocess.PIPE , text = True)
    if returned_output.stderr != "":
        output[file] = returned_output.stderr

def count_files(directorySrc): # Count the number of files in the folder
    global files
    for subs in os.listdir(directorySrc):
        path = directorySrc + "/" + subs
        if os.path.isdir(path): # Subfolder
            count_files(path)
        elif subs.endswith(".cpp") or subs.endswith(".h"):
            if subs.endswith(".cpp"):
                global cpp
                cpp += 1
            files+=1

def subDir(directorySrc,directoryDest): # Search and copy all the files in the folder
    global i,files
    for subs in os.listdir(directorySrc):
        path = directorySrc + "/" + subs
        if os.path.isdir(path): # Subfolder
            subDir(path,directoryDest)
        elif subs.endswith(".cpp") or subs.endswith(".h"):
            shutil.copy2(path, directoryDest)
            i += 1
            printProgressBar(iteration = i , total = files , prefix = 'Copying files:' , suffix = 'Complete' , length = 50)

def count_items(dictionary): # Count items in a dictionary
    count = 0
    for key,value in dictionary.items():
        count += 1
    return count

directorySrc = filedialog.askdirectory() # Ask the user to select the folder
directoryDest = pathlib.Path(__file__).parent.resolve() # Get the path of the script

count_files(directorySrc)
if(files == 0):
    print("No .cpp or .h files found")
    exit()

subDir(directorySrc,directoryDest) # Copy all .cpp files in the same folder of the script
i = 0
print("\n")

# Check the files
for file in os.listdir():
    if file.endswith(".cpp"):
        i += 1
        printProgressBar(iteration = i , total = cpp , prefix = 'Checking files:' , suffix = 'Complete' , length = 50)
        check_file(file)

print("\n")

# Print the errors
if count_items(output) != 0:
    print("Errors:")
    for key in output:
        print("\n-------------- " + key + " --------------\n")
        print(output[key])
else:
    print("No errors found")

# Delete all the files
for file in os.listdir():
    if not file.endswith(".py") and not os.path.isdir(file):
        delete_file(file)

exit()