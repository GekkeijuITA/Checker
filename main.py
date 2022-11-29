# Check the file that are in a folder chosen by the user
from tkinter import *
from tkinter import filedialog

import subprocess
import os
import shutil
import pathlib

exe_file = "test"
files = 0
i = 0

def printProgressBar(iteration , total , prefix = '' , suffix = '' , decimals = 1 , length = 100 , fill = '█' , printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()

def runprint_output(cmd,file):
    returned_output = subprocess.run(cmd , stdout = subprocess.PIPE)
    output = returned_output.stdout

    if(str(returned_output.returncode) != '0'):
        print(file + " correct")

def delete_file(file):
    os.remove(file)

def check_file(file):
    cmd = ["g++", "-Wall" , "-std=c++14" , file , "-o" , exe_file] # compile the file, cross-platform
    runprint_output(cmd,file)

def count_files(directorySrc,directoryDest):
    global files
    for subs in os.listdir(directorySrc):
        path = directorySrc + "/" + subs
        if os.path.isdir(path):
            count_files(path,directoryDest)
        elif subs.endswith(".cpp") or subs.endswith(".h"):
            files+=1

def subDir(directorySrc,directoryDest):
    global i,files
    for subs in os.listdir(directorySrc):
        path = directorySrc + "/" + subs
        if os.path.isdir(path):
            subDir(path,directoryDest)
        elif subs.endswith(".cpp") or subs.endswith(".h"):
            shutil.copy2(path, directoryDest)
            i += 1
            printProgressBar(iteration = i , total = files , prefix = 'Progress:' , suffix = 'Complete' , length = 50)

directorySrc = filedialog.askdirectory() # Ask the user to select the folder
directoryDest = pathlib.Path(__file__).parent.resolve() # Get the path of the script

count_files(directorySrc,directoryDest)
#copy all .cpp files in the same folder of the script
printProgressBar(iteration = 0 , total = files , prefix = 'Progress:' , suffix = 'Complete' , length = 50)
subDir(directorySrc,directoryDest)

# Check the files
for file in os.listdir():
    if file.endswith(".cpp"):
        print("Checking " + file)
        check_file(file)

# Delete all the files
for file in os.listdir():
    if not file.endswith(".py") and not os.path.isdir(file):
        delete_file(file)