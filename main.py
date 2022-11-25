# Check the file that are in the same folder of the script for now
from tkinter import *
from tkinter import filedialog

import subprocess
import platform
import os
import shutil
import pathlib


def runprint_output(cmd):
    returned_output = subprocess.run(cmd , stdout = subprocess.PIPE)
    output = returned_output.stdout.decode('utf-8')
    if(output != ""):
        print(output)
    else:
        print("Correct")

def check_files(file,system):
    cmd = "echo Nothing found"
    if system == "Windows":
        cmd = 'g++ -Wall -std=c++14 ' + file +  ' -o a'
    elif system == 'Linux':
        cmd = "echo Not supported yet"
    else:
        cmd = "clang++ -Werror -Wno-error=unused-variable -Wall -W " + file
    runprint_output(cmd) 

directorySrc = filedialog.askdirectory() # Ask the user to select the folder
directoryDest = pathlib.Path(__file__).parent.resolve() # Get the path of the script

#copy all .cpp files in the same folder of the script
for file in os.listdir(directorySrc):
    if file.endswith(".cpp"):
        shutil.copy2(directorySrc + "/" + file, directoryDest)

# Check the files (to fix)
#for file in os.listdir():
#    if file.endswith(".cpp"):
#        check_files(file,platform.system())

# Delete all the files
    for file in os.listdir():
        if file.endswith(".cpp"):
            os.remove(file)