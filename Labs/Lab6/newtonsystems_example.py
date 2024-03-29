import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt;

def driver():

    x0 = np.array([1, 0])

    Nmax = 100
    tol = 1e-10


    # t = time.time()
    # for j in range(20):
    #   [xstar,xlist,ier,its] =  SlackerNewton(x0,tol,Nmax);
    # elapsed = time.time()-t
    # print(xstar);
    # err2 = np.sum((xlist-xstar)**2,axis=1);
    # plt.plot(np.arange(its),np.log10(err2[0:its]));
    # plt.show();

    h_mult = 1e-3
    t = time.time()
    for j in range(20):
      [xstar,xlist,ier,its] =  AppxNewton(x0,tol,Nmax,h_mult);
    elapsed = time.time()-t;
    print(xstar);
    err = np.sum((xlist-xstar)**2,axis=1);
    plt.plot(np.arange(its),np.log10(err[0:its]));
    plt.show();


def evalF(x):

    F = np.zeros(2)
    F[0] = 4*x[0]**2 + x[1]**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])

    # F[0] = 3*x[0]-math.cos(x[1]*x[2])-1/2
    # F[1] = x[0]-81*(x[1]+0.1)**2+math.sin(x[2])+1.06
    # F[2] = np.exp(-x[0]*x[1])+20*x[2]+(10*math.pi-3)/3
    return F

def evalJ(x):
    J = np.array([[8*x[0], 2*x[1]],
        [-1 - np.sin(x[0] - x[1]), 1 + np.sin(x[0] - x[1])]])
    return J


def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    xlist = np.zeros((Nmax+1,len(x0)));
    xlist[0] = x0;

    for its in range(Nmax):
       J = evalJ(x0);
       F = evalF(x0);

       x1 = x0 - np.linalg.solve(J,F);
       xlist[its+1]=x1;

       if (norm(x1-x0) < tol*norm(x0)):
           xstar = x1
           ier =0
           return[xstar, xlist,ier, its];

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,xlist,ier,its];

def AppxNewton(x0,tol,Nmax,h_mult):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    xlist = np.zeros((Nmax+1,len(x0)));
    xlist[0] = x0;

    h0 = min(h_mult * x0[0], .000000000001)
    h1 = min(h_mult * x0[0], .000000000001)

    for its in range(Nmax):
    #    J = evalJ(x0);
       F = evalF(x0);
       F_0_h = evalF([x0[0] + h0, x0[1]])
       F_1_h = evalF([x0[0], x0[1] + h1])
       J = [[(F_0_h[0] - F[0]) / h0, (F_0_h[1] - F[1]) / h0],
            [(F_1_h[0] - F[0]) / h1, (F_1_h[1] - F[1]) / h1]]

       x1 = x0 - np.linalg.solve(J,F);
       xlist[its+1]=x1;

       if (norm(x1-x0) < tol*norm(x0)):
           xstar = x1
           ier =0
           return[xstar, xlist,ier, its];

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,xlist,ier,its];

def SlackerNewton(x0,tol,Nmax):

    ''' Slacker Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    xlist = np.zeros((Nmax+1,len(x0)));
    xlist[0] = x0;

    J = evalJ(x0);
    for its in range(Nmax):
       ## Every three iterations update J
       if its % 3 == 0: J = evalJ(x0);

       F = evalF(x0)
       x1 = x0 - np.linalg.solve(J,F);
       xlist[its+1]=x1;

       if (norm(x1-x0) < tol*norm(x0)):
           xstar = x1
           ier =0
           return[xstar,xlist, ier,its];

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,xlist,ier,its];

if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver();
