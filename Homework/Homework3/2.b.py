import numpy as np
import bisection_example as bisection


def expanded_form(coefficients, a):
    return [coeff * (a ** i) for i, coeff in enumerate(coefficients)]

# Pascal's Triangle constants for (a+b)^9
pascals_triangle_constants = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

resulting_coefficients = expanded_form(pascals_triangle_constants, -5)
print("The resulting coefficients in front of each x term are:", resulting_coefficients)

   
f = lambda x: sum(coeff * x**(9 - i) for i, coeff in enumerate(resulting_coefficients))
a = 4.82
b = 5.2
tol = 1e-4

[astar,ier, iterations] = bisection.bisection(f,a,b,tol)
print('the approximate root is',astar)
print('the error message reads:',ier)
print('f(astar) =', f(astar))

