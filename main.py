import os
import platform
#os.system('ls') 
system = platform.system();

if system == 'Windows':
    os.system('echo Hello Windows')
elif system == 'Linux':
    os.system('echo Hello Linux')
else:
    os.system('echo Hello Apple')