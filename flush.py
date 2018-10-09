import sys
import time
for i in range(10):
    sys.stdout.write("\r{0}".format(str(i)))
    sys.stdout.flush()
