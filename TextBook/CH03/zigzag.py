import time, sys

indent = 0
increasing = True

try:
    while True:
        print(' ' * indent + '********')
        time.sleep(0.1)
        if increasing:
            indent += 1
            if indent == 20:
                increasing = False
        else:
            indent -= 1
            if indent == 0:
                increasing = True
except KeyboardInterrupt:
    sys.exit()

