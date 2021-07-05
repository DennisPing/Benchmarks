from time import time

def naive_fib(n):
    if n < 2:
        return n
    return naive_fib(n-1) + naive_fib(n-2)

def main():
    n = 47
    acc = 0
    for _ in range(5):
        t0 = time()
        print(naive_fib(n))
        acc += (time() - t0)
    print(f"Time taken: {round(acc/5, 3)}")
    
if __name__ == "__main__":
    main()