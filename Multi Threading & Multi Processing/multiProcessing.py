### run Multiple Processes
### Tasks that are heavy on the CPU usage (e.g. mathematical opearation, data processing)

import multiprocessing
import time

def square():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i**2}")
    
def cube():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i**3}")
        
        
        
if __name__ == "__main__":
    
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)
    
    t = time.time()
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    fTime = time.time() - t
    print(fTime)