import numpy as np
import bisection_example as bisection

f = lambda x: x**3 + x - 4
a = 1
b = 4
tol = 1e-3

[astar,ier, iterations] = bisection.bisection(f,a,b,tol)
print('the approximate root is',astar)
print('Iterations taken:', iterations)
print('the error message reads:',ier)
print('f(astar) =', f(astar))