import time
import os
# time.sleep(10)
print("321")
stream = os.popen('whoami')
output = stream.read()
print(output)
