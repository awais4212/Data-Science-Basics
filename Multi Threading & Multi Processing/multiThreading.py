# MultiThreading
# When to use MultiThreading
# I\O bounds tasks that need I/O opearations (eg: file opearations, network)

import threading
import time

def printNum():
    for num in range(5):
        time.sleep(2)
        print(f"Number: {num}")

def printLetter():
    for letter in "abcdef":
        time.sleep(2)
        print(f"Letter: {letter}")

# Created 2 Threads      
t1 = threading.Thread(target= printNum)
t2 = threading.Thread(target= printLetter)
        
t = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
totalTime = time.time() - t
print(totalTime)        