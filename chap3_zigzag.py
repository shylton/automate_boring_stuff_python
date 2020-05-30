import time
import sys

indent = 0  # how many spaces to indent
indentIncreasing = True

print('CTRL-C to exit')

try:
    while True:
        print(' '*indent, end='')
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:  # change direction
                indentIncreasing = False
        else:  # decrease spaces
            indent = indent - 1
            if indent == 0:  # change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
            
