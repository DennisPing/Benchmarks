from numba import njit, typed
from time import time

@njit
def fib_memo(n, memo):
    if n < 2:
        return n
    if memo[n] == 0:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def main():
    n = 47
    memo = [0] * (n+1)
    memo = typed.List(memo)
    acc = 0
    for i in range(6):
        t0 = time()
        print(fib_memo(n, memo))
        if i >= 1:
            acc += (time() - t0)
    print(f"Time taken: {round(acc/5, 3)}")
    
if __name__ == "__main__":
    main()