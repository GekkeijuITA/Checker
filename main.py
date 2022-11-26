# Check the file that are in a folder chosen by the user
from tkinter import *
from tkinter import filedialog

import subprocess
import os
import shutil
import pathlib
import platform

exe_file = "test"

def add_label(listBox,text,fg,bg):
    listBox.insert(END , text)
    listBox.pack()
    #label = Label(window, text = text , fg = fg, bg = bg)
    #label.pack()

def runprint_output(cmd,file,listBox):
    returned_output = subprocess.run(cmd , stdout = subprocess.PIPE, stderr = subprocess.STDOUT, text=True)
    output = returned_output.stdout

    if(returned_output.returncode != 0):
        add_label(listBox,file + ": " + str(output),"red","white")
    else:
        add_label(listBox,file + ": " + "No error","green","white")

def delete_file(file):
    os.remove(file)

def check_file(file,system,listBox):
    cmd = "echo Nothing found"
    if system == "Windows":
        cmd = 'g++ -Wall -std=c++14 ' + file +  ' -o ' + exe_file
    elif system == 'Linux':
        cmd = "echo Not supported yet"
    else:
        cmd = "clang++ -Werror -Wno-error=unused-variable -Wall -W " + file
    runprint_output(cmd,file,listBox) 
    #delete_file(file)

def subDir(directorySrc,directoryDest):
    for subs in os.listdir(directorySrc):
        path = directorySrc + "/" + subs
        if os.path.isdir(path):
            subDir(path,directoryDest)
        elif subs.endswith(".cpp") or subs.endswith(".h"):
            shutil.copy2(path, directoryDest)

def update(window):
    window.after(1000, update)

width = 500
height = 500

main = Tk()
main.title("Check file")
main.geometry(str(width) + "x" + str(height))

listBox = Listbox(main, width = width, height = height)
scrollbarY = Scrollbar(main)
scrollbarX = Scrollbar(main, orient = HORIZONTAL)

scrollbarX.pack(side = BOTTOM, fill = X)
scrollbarY.pack(side = RIGHT, fill = Y)

listBox.config(yscrollcommand = scrollbarY.set , xscrollcommand = scrollbarX.set)
scrollbarY.config(command = listBox.yview)
scrollbarX.config(command = listBox.xview)

directorySrc = filedialog.askdirectory() # Ask the user to select the folder
directoryDest = pathlib.Path(__file__).parent.resolve() # Get the path of the script

#copy all .cpp files in the same folder of the script
subDir(directorySrc,directoryDest)

# Check the files
for file in os.listdir():
    if file.endswith(".cpp"):
        print("Checking " + file)
        check_file(file,platform.system(),listBox)

# Delete the all files
for file in os.listdir():
    if file.endswith(".h") or file.endswith(".cpp"):
        delete_file(file)
delete_file(exe_file + ".exe")
main.mainloop()