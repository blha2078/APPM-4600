import numpy as np 
import math 

error_term = 10
error_limit = 1e-16
n = -1
x = 9.999999995e-10

f = lambda n: (x**(n+1)) / math.factorial(n + 1)

while error_term / x > error_limit:
    n += 1
    error_term = f(n)
    print(n)
    print(error_term / x)
print("Number of terms required: ", n)