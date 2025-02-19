import time
#from time import perf_counter_ns
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

#execution
n=int(input('Enter a positive integer :'))
t1=time.perf_counter_ns()
f=fibonacci(n)
t2=time.perf_counter_ns()

print('fibonacci (',n,')=',f)
print(f'fibonacci ({n}) = {f}')
print(f"The execution time is {t2-t1} ns.")