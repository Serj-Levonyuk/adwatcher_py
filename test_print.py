import time
import os
# time.sleep(10)
print("4321")
# stream = os.popen('adb connect 127.0.0.1:5555')
stream = os.popen('ping 127.0.0.1 -c 10')
output = stream.read()
print(output)
