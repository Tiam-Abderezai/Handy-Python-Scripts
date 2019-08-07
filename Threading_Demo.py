# This script shows the usage of "threading" module to demonstrate concurrency.
# It's goal is to run 2 functions at the same time.

import threading
import time

# Defines function1 that uses while-loop to print function1 every 1 sec
def function1():
    while True:
        print "function1"
        time.sleep(1)
# Defines function2 that uses for-loop to print function2 every 1 sec
def function2():
    for b in range(1, 100000):
        print "function2"
        time.sleep(1)

# Defines main function that runs 2 functions as 2 separate threads simultaneously
def main():
    threading.Thread(target=function1).start()
    threading.Thread(target=function2).start()

# Runs main function
main()
