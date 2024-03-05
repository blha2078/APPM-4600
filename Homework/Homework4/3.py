import numpy as np
import time
from numpy.linalg import inv, norm

# Define routines for the new system
def evalF(xyz):
    x, y, z = xyz
    F = np.zeros(3)
    
    F[0] = x + np.cos(x * y * z) - 1
    F[1] = (1 - x)**(1/4) + y + 0.05 * z**2 - 0.15 * z - 1
    F[2] = -x**2 - 0.1 * y**2 + 0.01 * y + z - 1
    
    return F

def evalJ(xyz):
    x, y, z = xyz
    J = np.array([
        [1 - y * z * np.sin(x * y * z), -x * z * np.sin(x * y * z), -x * y * np.sin(x * y * z)],
        [-0.25 * (1 - x)**(-3/4), 1, 0.1 * z - 0.15],
        [-2 * x, -0.2 * y + 0.01, 1]
    ])
    
    return J

# Newton's method
def Newton(x0, tol, Nmax):
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
        J = evalJ(x0)
        try:
            Jinv = inv(J)
        except np.linalg.LinAlgError:
            print("Singular matrix encountered. Stopping iteration.")
            return [x0, 1, its]
            
        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)
       
        if norm(x1 - x0) < tol:
            xstar = x1
            ier = 0
            return [xstar, ier, its]
           
        x0 = x1
    
    xstar = x1
    ier = 1
    return [xstar, ier, its]

# use routines
x0 = np.array([0.1, 0.1, -0.1])
Nmax = 100
tol = 1e-6

t = time.time()
for j in range(20):
    [xstar, ier, its] = Newton(x0, tol, Nmax)
elapsed = time.time() - t
print("Approximate root:", xstar)
print("Error message:", "Success" if ier == 0 else "Failure")
print("Number of iterations:", its)
print("Time taken (average over 20 runs):", elapsed / 20, "seconds")
