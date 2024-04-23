import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time

def show_error(A, b, x, s, time):
     test = np.matmul(A,x)
     r = la.norm(test-b)
     
     print(s, ' time: ', round(time, 3), ' Result: ', r)

def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 100
 
     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)
  
     # standard solve()
     start_time = time.time()
     standard = scila.solve(A,b)
     end_time = time.time()
     test = np.matmul(A,standard)
     r = la.norm(test-b)
     
     print('Standard time: ', round(end_time - start_time, 6), ' Result: ', r)

     # LU 
     start_time = time.time()
     factored = scila.lu_factor(A)
     print('factor time for LU: ', time.time() - start_time)
     LU = scila.lu_solve(factored, b)
     end_time = time.time()
     test = np.matmul(A,LU)
     r = la.norm(test-b)
     print('LU time: ', round(end_time - start_time, 3), ' Result: ', r)
     

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)


     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
          
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       
