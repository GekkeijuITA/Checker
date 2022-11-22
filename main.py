import subprocess
import platform

# Get the OS and change the command accordingly
system = platform.system();
if system == "Windows":
    cmd = "g++ -Wall -std=c++14 **.cpp -o a"
elif system == 'Linux':
    cmd = "echo Not supported yet"
else:
    cmd = "clang++ -Werror -Wno-error=unused-variable -Wall -W main.cpp"

# Run the command and print the output
returned_output = subprocess.run(cmd , stdout = subprocess.PIPE)
returned_output.stdout.decode('utf-8')