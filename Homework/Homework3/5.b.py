import numpy as np

def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]


# FPI function
f = lambda x: -np.sin(2*x) + 1.25 * x - 0.75

Nmax = 1000
tol = 1e-10

x0 = -2
[xstar,ier] = fixedpt(f,x0,tol,Nmax)
print('Root 1:',round(xstar,10))
print('Error message reads:',ier)

x0 = 0
[xstar,ier] = fixedpt(f,x0,tol,Nmax)
print('Root 2:',round(xstar,10))
print('Error message reads:',ier)

x0 = 2
[xstar,ier] = fixedpt(f,x0,tol,Nmax)
print('Root 3:',round(xstar,10))
print('Error message reads:',ier)

x0 = 3
[xstar,ier] = fixedpt(f,x0,tol,Nmax)
print('Root 4:',round(xstar,10))
print('Error message reads:',ier)

x0 = 4.5
[xstar,ier] = fixedpt(f,x0,tol,Nmax)
print('Root 5:',round(xstar,10))
print('Error message reads:',ier)