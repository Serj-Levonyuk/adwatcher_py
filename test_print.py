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
# arg=shlex.split("cat test_print.py")
process = subprocess.Popen(arg,
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
b=b'\x2B'
print(stdout)
print(len(stdout))
print(len(list(stdout)))
# print(len(stdout))
