from numba import njit, typed
from time import time

@njit
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def main():
    n = 47
    acc = 0
    for i in range(6):
        t0 = time()
        print(fib(n))
        if i >= 1:
            acc += (time() - t0)
    print(f"Time taken: {round(acc/5, 3)}")
    
if __name__ == "__main__":
    main()