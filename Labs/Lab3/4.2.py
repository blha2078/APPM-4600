import numpy as np 
import bisection_example as bisection 


Nmax = 1000
tol = 1e-5

# def f(x):
#     return (x-1) * (x-3) * (x-5)
# a = 0
# b = 2.4

# def f(x):
#     return (x-1) * (x-3) * (x-1)
# a = 0
# b = 2

def f(x):
    return np.sin(x)
a = 0
b = 3 * np.pi / 4


print('Results: ', bisection.bisection(f, a, b, tol, Nmax))

