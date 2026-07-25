import multiprocessing
import sys
import time
import math

sys.set_int_max_str_digits(100000)

def computeFactorial(numbers):
    print(f"Computing Factorial of {numbers}")
    res=math.factorial(numbers)
    return res

if __name__=='__main__':
    numbers = [5000, 2000, 3000]
    
    t=time.time()
    with multiprocessing.Pool() as pool:
        res = pool.map(computeFactorial,numbers)
        
    ft = time.time() - t
    print(f'Result : {res}')
    print(f'Time consumed by it is {ft}')    
