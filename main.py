# Check the file that are in the same folder of the script
import subprocess
import platform
import os

def runprint_output(cmd):
    returned_output = subprocess.run(cmd , stdout = subprocess.PIPE)
    output = returned_output.stdout.decode('utf-8')
    if(output != ""):
        print(output)
    #else:
    #    print("Corretto")

def check_files(file,system):
    cmd = "echo Nothing found"
    if file.endswith(".cpp") or file.endswith(".h"):
        if system == "Windows":
            cmd = 'g++ -Wall -std=c++14 ' + file +  ' -o a'
        elif system == 'Linux':
            cmd = "echo Not supported yet"
        else:
            cmd = "clang++ -Werror -Wno-error=unused-variable -Wall -W " + file
        runprint_output(cmd) 

def loop(dir,system):
    directory_contents = os.listdir(dir)
    for file in directory_contents:
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            loop(path,system)
        else:
            check_files(path,system) 



# Main
system = platform.system()
directory_contents = os.listdir()
for item in directory_contents:
    if os.path.isdir(item):
        loop(item,system)