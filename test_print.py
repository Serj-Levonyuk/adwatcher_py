import time
import os
# time.sleep(10)
print("4321")
# stream = os.popen('adb connect 127.0.0.1:5555')
stream = os.popen('ping -c 10 127.0.0.1')
output = stream.read()
print(output)
