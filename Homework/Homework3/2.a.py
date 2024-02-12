import numpy as np
import bisection_example as bisection

# part a   
f = lambda x: (x - 5) ** 9
a = 4.82
b = 5.2
tol = 1e-4

[astar,ier, iterations] = bisection.bisection(f,a,b,tol)
print('the approximate root is',astar)
print('the error message reads:',ier)
print('f(astar) =', f(astar))

