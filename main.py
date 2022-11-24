# Check the file that are in the same folder of the script
import subprocess
import platform
import os

def runprint_output(cmd):
    returned_output = subprocess.run(cmd , stdout = subprocess.PIPE)
    output = returned_output.stdout.decode('utf-8')
    if(output != ""):
        print(output)
    else:
        print("Corretto")

# Get the OS and change the command accordingly
system = platform.system()

# Loop through the files
for file in os.listdir():
    if file.endswith(".cpp"):
        if system == "Windows":
            cmd = "g++ -Wall -std=c++14 " + file +  " -o a"
        elif system == 'Linux':
            cmd = "echo Not supported yet"
        else:
            cmd = "clang++ -Werror -Wno-error=unused-variable -Wall -W " + file
        
        runprint_output(cmd)