# Benchmarks
Fun benchmarks for various programming languages

## Numba Library

Numba compiles Python code down to C level machine code. Numba is very useful for number crunching and doing repetitive calculations. However, it is worse for small calculations because it requires extra compile time while native Python can run immediately.

## Recording Time

Python's interpreted nature means that time starts instantly, before Numba compiling even finishes. A compiled language like Go or Java starts recording time after compiling finishes. Therefore, for a trivial function like `"hello world"`, Go will record the completion time as 0.000 sec while Python-Numba will record the completion time as 0.123 sec. The correct workaround is to record time using a shell (Powershell, Bash, Zsh), but I'm too lazy to do that...

To make the comparison fair, I ran the Python-Numba sequence 5 times (1st time to get compiling out of the way). The other 4 times are averaged as the actual result.

## Fibonacci Sequence (Naive)

This is the basic Fibonacci sequence we all learn at school.  
The sequence goes like: 0, 1, 1, 2, 3, 5, 8 ...
The 47th position is 2,971,215,073.

| Language          | n-th number   | Average Time (sec) | Improvement over Slowest |
| ----------------- | ------------- | ------------------ | ------------------------ |
| Python            | 47            | 455.609            | 0                        |
| Python with Numba | 47            | 17.437             | 26x                      |
| Go                | 47            | 13.040             | 35x                      |

*Numba compile time ~= 0.218 seconds*

## Fibonacci Sequence (Memoize)

This is an optimized Fibonacci sequence that uses memoization to avoid recalculating past numbers. Numba is actually slower here than native Python because of the compile time!!

Increasing the n-th number does not change the completion time. For example, n=200 also results in 0.000 sec time. Increasing this number further risks hitting the built-in recursion depth limit or exceeding the `int64` max value.

| Language          | n-th number   | Average Time (sec) | Improvement over Slowest |
| ------------------|---------------|--------------------| ------------------------ |
| Python            | 47            | 0.000              | 0
| Python with Numba | 47            | 0.000              | 0
| Go                | 47            | 0.000              | 0

*Numba compile time ~= 0.218 seconds*

## Conclusions

For Python, get an instant 26x speed increase by typing the decorator `@njit` (which stands for `NoPython=True`).

## Restrictions

1. The `@njit` function cannot be in a class.
2. The `@njit` function cannot use external Python libraries with the exception of Numpy.
3. The `@njit` function cannot do type casting inside. For example, no `str(x)` or `int(x)`.
4. Iterables or collections must be explicitly stated for the sake of type-safety. 
    - Iterables that are passed in as parameters for functions must be pre-instantiated with Numba. For example, `typed.List()`, `typed.Dict()`, etc.
    - It's often easier to trick the compiler rather than guess the correct syntax.
5. In order to use `@njit` in a class, you need to use the `@jitclass` decorator instead.
    - This requires you to explicitly write out the data types as a `spec` (just like in other statically typed languages).
    - This step is often painful and time-consuming as you try to guess the correct synatx.
    - My opinion is that if you need to write an entire Python class with `@jitclass`, then you can probably write it faster in another language.
    - Just don't use `@jitclass` until it's further developed...