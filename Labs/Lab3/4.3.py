import numpy as np 
import fixedpt_example as fp 

x0 = 1
tol = 1e-10
Nmax = 1000

# def f(x):
#     return x * (1 + (7-(x**5)) / x**2)**3

# def f(x):
#     return x - (x**5 - 7) / x**2

def f(x):
    return x - (x**5 - 7) / 5 * x**4

# def f(x):
    return x - (x**5 - 7) / 12

point = 7 ** (1/5)
print('x = 7^(1/5)is a FP: ', point == f(point))
print('Results are: ', fp.fixedpt(f,x0,tol,Nmax))