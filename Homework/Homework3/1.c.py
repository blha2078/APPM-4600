import numpy as np
import bisection_example as bisection

# use routines    
f = lambda x: 2 * x - np.sin(x) - 1
a = 0
b = 2
tol = 1e-9

[astar,ier, iterations] = bisection.bisection(f,a,b,tol)
print('the approximate root is',astar)
print('iterations taken:', iterations)
print('the error message reads:',ier)
print('f(astar) =', f(astar))