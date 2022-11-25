# Check the file that are in the same folder of the script for now
from tkinter import *

import subprocess
import platform
import os
import tkinter , tkCostants , tkFileDialog


def runprint_output(cmd):
    returned_output = subprocess.run(cmd , stdout = subprocess.PIPE)
    output = returned_output.stdout.decode('utf-8')
    if(output != ""):
        print(output)
    else:
        print("Correct")

def check_files(file,system):
    cmd = "echo Nothing found"
    if file.endswith(".cpp"):
        if system == "Windows":
            cmd = 'g++ -Wall -std=c++14 ' + file +  ' -o a'
        elif system == 'Linux':
            cmd = "echo Not supported yet"
        else:
            cmd = "clang++ -Werror -Wno-error=unused-variable -Wall -W " + file
        runprint_output(cmd) 

root = Tk()
root.directory = tkFileDialog.askdirectory()
print(root.directory)
#for file in os.listdir():
#    check_files(file,platform.system())
