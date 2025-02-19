import time
import sys
# Increase the recursion limit
sys.setrecursionlimit(10005)  # Set this to a higher value as needed

def fibonacci(n: int, mem={0: 0, 1: 1}) -> int:
    if n in mem:
        return mem[n]
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return fibonacci_helper(n, mem)

def fibonacci_helper(n: int, mem: dict) -> int:
    if n in mem:
        return mem[n]
    mem[n] = fibonacci_helper(n - 1, mem) + fibonacci_helper(n - 2, mem)
    return mem[n]

# execution
n = int(input('Enter a positive integer: '))
t1 = time.perf_counter_ns()
f = fibonacci(n)
t2 = time.perf_counter_ns()

print('fibonacci (', n, ') =', f)
print(f'fibonacci ({n}) = {f}')
print(f"The execution time is {t2 - t1} ns.")