# Check the file that are in a folder chosen by the user
from tkinter import *
from tkinter import filedialog

import subprocess
import os
import shutil
import pathlib
import platform

exe_file = "a"

def runprint_output(cmd):
    returned_output = subprocess.run(cmd , stdout = subprocess.PIPE)
    output = returned_output.stdout.decode('utf-8')
    if(output != ""):
        print(output)
    else:
        print("Correct")

def delete_file(file):
    print("Deleting file: " + file)
    os.remove(file)

def check_file(file,system):
    cmd = "echo Nothing found"
    if system == "Windows":
        cmd = 'g++ -Wall -std=c++14 ' + file +  ' -o ' + exe_file
    elif system == 'Linux':
        cmd = "echo Not supported yet"
    else:
        cmd = "clang++ -Werror -Wno-error=unused-variable -Wall -W " + file
    runprint_output(cmd) 
    delete_file(file)

directorySrc = filedialog.askdirectory() # Ask the user to select the folder
directoryDest = pathlib.Path(__file__).parent.resolve() # Get the path of the script

#copy all .cpp files in the same folder of the script
for file in os.listdir(directorySrc):
    if file.endswith(".cpp"):
        print("Copying " + file)
        shutil.copy2(directorySrc + "/" + file, directoryDest)

# Check the files
for file in os.listdir():
    if file.endswith(".cpp"):
        print("Checking " + file)
        check_file(file,platform.system())

os.remove(exe_file + ".exe") 