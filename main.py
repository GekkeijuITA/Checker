# Check the file that are in a folder chosen by the user
from tkinter import *
from tkinter import filedialog

import subprocess
import os
import shutil
import pathlib
import platform

exe_file = "test"

def runprint_output(cmd,file):
    returned_output = subprocess.run(cmd , stdout = subprocess.PIPE)
    output = returned_output.stdout

    if(returned_output.returncode != 0):
        print(output)
    else:
        print(file + " correct")
    print("\n")

def delete_file(file):
    os.remove(file)

def check_file(file):
    cmd = ["g++", "-Wall" , "-std=c++14" , file , "-o" , exe_file]
    runprint_output(cmd,file) 
    delete_file(file)

def subDir(directorySrc,directoryDest):
    for subs in os.listdir(directorySrc):
        path = directorySrc + "/" + subs
        if os.path.isdir(path):
            subDir(path,directoryDest)
        elif subs.endswith(".cpp") or subs.endswith(".h"):
            shutil.copy2(path, directoryDest)

directorySrc = filedialog.askdirectory() # Ask the user to select the folder
directoryDest = pathlib.Path(__file__).parent.resolve() # Get the path of the script

#copy all .cpp files in the same folder of the script
subDir(directorySrc,directoryDest)

# Check the files
for file in os.listdir():
    if file.endswith(".cpp"):
        print("Checking " + file)
        check_file(file)

for file in os.listdir():
    if not file.endswith(".py") and not os.path.isdir(file):
        delete_file(file)