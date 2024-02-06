import numpy as np 
import bisection_example as bisection 


def f(x):
    return (x**2) * (x - 1)

Nmax = 100
tol = 1e-3


a = 0.5
b = 2
print('Results: ', bisection.bisection(f, a, b, tol, Nmax))

