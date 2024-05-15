import time
import os
import subprocess
import shlex

# time.sleep(10)
print("4321")
# stream = os.popen('adb connect 127.0.0.1:5555')
# stream = os.popen('ping -c 10 127.0.0.1')
# output = stream.read()
# print(output)
arg=shlex.split("adb exec-out screencap -p")
process = subprocess.Popen(arg,
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print(len(stdout))
