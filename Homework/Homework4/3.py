import numpy as np
import time
from numpy.linalg import inv, norm
import numpy as np
from numpy import random as rand
import math
from scipy import io, integrate, linalg, signal
import matplotlib.pyplot as plt

# Define routines for the new system
def evalF(xyz):
    x, y, z = xyz
    # print('xyz', xyz)
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

def evalFSD(xyz):
    F = evalF(xyz)
    return sum([a**2 for a in F])

def evalG(xyz):
    F = evalF(xyz)
    J = evalJ(xyz)
    G = np.zeros(3)

    for i in range(3):
        for j in range(3):
            G[i] += 2 * F[i] * J[i, j]

    return G


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


def line_search(f,Gf,x0,p,type,mxbck,c1,c2):
    alpha=2;
    n=0;
    cond=False; #condition (if True, we accept alpha)
    f0 = f(x0); # initial function value
    Gdotp = p.T @ Gf(x0); #initial directional derivative
    nf=1;ng=1; # number of function and grad evaluations

    # we backtrack until our conditions are met or we've halved alpha too much
    while n<=mxbck and (not cond):
        alpha=0.5*alpha;
        x1 = x0+alpha*p;
        # Armijo condition of sufficient descent. We draw a line and only accept
        # a step if our function value is under this line.
        Armijo = f(x1) <= f0 + c1*alpha*Gdotp;
        nf+=1;
        if type=='wolfe':
            #Wolfe (Armijo sufficient descent and simple curvature conditions)
            # that is, the slope at new point is lower
            Curvature = p.T @ Gf(x1) >= c2*Gdotp;
            # condition is sufficient descent AND slope reduction
            cond = Armijo and Curvature;
            ng+=1;
        elif type=='swolfe':
            #Symmetric Wolfe (Armijo and symmetric curvature)
            # that is, the slope at new point is lower in absolute value
            Curvature = np.abs(p.T @ Gf(x1)) <= c2*np.abs(Gdotp);
            # condition is sufficient descent AND symmetric slope reduction
            cond = Armijo and Curvature;
            ng+=1;
        else:
            # Default is Armijo only (sufficient descent)
            cond = Armijo;

        n+=1;

    return(x1,alpha,nf,ng);

################################################################################
# Steepest descent algorithm
def steepest_descent(f,Gf,x0,tol,nmax,type='swolfe',verb=True):
    # Set linesearch parameters
    c1=1e-3; c2=0.9; mxbck=10;
    # Initialize alpha, fn and pn
    alpha=1;
    xn = x0; #current iterate
    rn = x0; #list of iterates
    fn = f(xn); nf=1; #function eval
    pn = -Gf(xn); ng=1; #gradient eval

    # if verb is true, prints table of results
    if verb:
        print("|--n--|-alpha-|----|xn|----|---|f(xn)|---|---|Gf(xn)|---|");

    # while the size of the step is > tol and n less than nmax
    n=0;
    while n<=nmax and np.linalg.norm(pn)>tol:
        if verb:
            print("|--%d--|%1.5f|%1.7f|%1.7f|%1.7f|" %(n,alpha,np.linalg.norm(xn),np.abs(fn),np.linalg.norm(pn)));

        # Use line_search to determine a good alpha, and new step xn = xn + alpha*pn
        (xn,alpha,nfl,ngl)=line_search(f,Gf,xn,pn,type,mxbck,c1,c2);

        nf=nf+nfl; ng=ng+ngl; #update function and gradient eval counts
        fn = f(xn); #update function evaluation
        pn = -Gf(xn); # update gradient evaluation
        n+=1;
        rn=np.vstack((rn,xn)); #add xn to list of iterates

    r = xn; # approx root is last iterate

    return (r,rn,nf,ng);

# use routines
x0 = np.array([0.5, 0.5, 0.5])
Nmax = 100
tol = 1e-6

t = time.time()
for j in range(20):
    [xstar, ier, its] = Newton(x0, tol, Nmax)
elapsed = time.time() - t
print('Newton')
print("Approximate root:", xstar)
# print("Error message:", "Success" if ier == 0 else "Failure")
# print("Number of iterations:", its)
print("Time taken (average over 20 runs):", elapsed / 20, "seconds")

# use steepest descent
print()
print('Steepest Descent')
t = time.time()
for j in range(20):
    [r,rn,nf,ng] = steepest_descent(evalFSD, evalG, x0, tol, Nmax, verb=False)
elapsed = time.time() - t
print("Approximate root:", r)
print("Time taken (average over 20 runs):", elapsed / 20, "seconds")


# use steepest descent Newton Hybrid
print()
print('Steepest Descent Newton Hybrid')
tempTol = 5e-2
t = time.time()
for j in range(20):
    # Steepest descent
    [r,rn,nf,ng] = steepest_descent(evalFSD, evalG, x0, tempTol, Nmax, verb=False)

    # Newton
    [xstar, ier, its] = Newton(r, tol, Nmax)
elapsed = time.time() - t
print("Approximate root:", xstar)
# print("Error message:", "Success" if ier == 0 else "Failure")
# print("Number of iterations:", its)
print("Time taken (average over 20 runs):", elapsed / 20, "seconds")
