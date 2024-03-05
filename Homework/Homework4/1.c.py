# get libraries
import numpy as np
from numpy.linalg import inv 
from numpy.linalg import norm 

# define routines
def evalF(xy):
    x, y = xy
    F = np.zeros(2)
    
    F[0] = 3*x**2 - y**2
    F[1] = 3*x*y**2 - x**3 - 1
    
    return F

def evalJ(xy):
    x, y = xy
    J = np.array([
        [6*x, -2*y],
        [3*y**2 - 3*x**2, 6*x*y - 3*x**2]
    ])
    return J

def Newton(xy0, tol, Nmax):
    ''' inputs: xy0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xy_star = approx root, ier = error message, its = num its'''

    for its in range(Nmax):
        J = evalJ(xy0)
        try:
            Jinv = inv(J)
        except np.linalg.LinAlgError:
            print("Singular matrix encountered. Stopping iteration.")
            return [xy0, 1, its]
            
        F = evalF(xy0)
        xy1 = xy0 - Jinv.dot(F)
       
        if norm(xy1 - xy0) < tol:
            xy_star = xy1
            ier = 0
            return [xy_star, ier, its]
           
        xy0 = xy1
    
    xy_star = xy1
    ier = 1
    return [xy_star, ier, its]

# Initial guess
xy0 = np.array([1, 1])
tol = 1e-10
Nmax = 100

# Run Newton's method
[xystar, ier, its] = Newton(xy0, tol, Nmax)

# Display results
print("Approximate root:", xystar)
print("Error message:", "Success" if ier == 0 else "Failure")
print("Number of iterations:", its)
