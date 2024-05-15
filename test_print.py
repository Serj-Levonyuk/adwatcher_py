import time
import os
# time.sleep(10)
print("4321")
stream = os.popen('adb connect 127.0.0.1:5555')
output = stream.read()
print(output)
