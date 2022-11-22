import subprocess
import platform

# Get the OS and change the command accordingly
system = platform.system();
if system == 'Windows':
    cmd = "echo Hello Windows"
elif system == 'Linux':
    cmd = "echo Hello Linux"
else:
    cmd = "clang++ -Werror -Wno-error=unused-variable -Wall -W main.cpp"

# Run the command and print the output
returned_output = subprocess.check_output(cmd)
print('Output:', returned_output.decode('utf-8'))