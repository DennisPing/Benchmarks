from time import time

def fib_memo(n, memo):
    if n < 2:
        return n
    if memo[n] == 0:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def main():
    n = 92
    memo = [0] * (n+1)
    acc = 0
    for _ in range(5):
        t0 = time()
        print(fib_memo(n, memo))
        acc += (time() - t0)
    print(f"Time taken: {round(acc/5, 3)}")
    
if __name__ == "__main__":
    main()