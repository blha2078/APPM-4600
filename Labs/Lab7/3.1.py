import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():

    f = lambda x: 1 / (1 + (10 * x)**2)

    ''' interval'''
    a = -1
    b = 1

    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a, b, Neval+1)

    ''' create vector with exact values'''
    fex = f(xeval)

    # List to store errors for each N
    errors_l = []
    errors_dd = []
    errors_mo = []

    for N in range(0, 11):  # N from 0 to 10
        ''' create equispaced interpolation nodes'''
        xint = np.linspace(a, b, N+1)

        ''' create interpolation data'''
        yint = f(xint)

        '''Initialize and populate the first columns of the 
         divided difference matrix. We will pass the x vector'''
        y = np.zeros((N + 1, N + 1))

        for j in range(N + 1):
            y[j][0] = yint[j]

        y = dividedDiffTable(xint, y, N + 1)
        ''' evaluate lagrange poly '''
        yeval_l = np.array([eval_lagrange(x, xint, yint, N) for x in xeval])
        yeval_dd = np.array([evalDDpoly(x, xint, y, N) for x in xeval])
        yeval_monomial = eval_monomial(xeval, xint, yint, N)

        errors_l.append(abs(yeval_l - fex))
        errors_dd.append(abs(yeval_dd - fex))
        errors_mo.append(abs(yeval_monomial - fex))

        ''' plot results for current N '''
        # plt.plot(xeval, yeval_l, label=f'N={N}')
        # plt.plot(xeval, yeval_dd, label=f'N={N}')
        plt.plot(xeval, yeval_monomial, label=f'N={N}')

    plt.plot(xeval, fex, 'c.-', label='Exact')
    plt.legend()
    plt.title('Monomial Evaluation for Different N')
    plt.show()

    ''' plot errors for each N'''
    plt.figure()
    for i in range(11):
        # plt.semilogy(xeval, errors_l[i], label=f'N={i}')
        # plt.semilogy(xeval, errors_dd[i], label=f'N={i}')
        plt.semilogy(xeval, errors_mo[i], label=f'N={i}')

    plt.legend()
    plt.ylabel('Error')
    plt.title('Errors for Monomial')
    plt.show()

def eval_monomial(xeval, xint, yint, N):
   V = np.vander(xint)
   V_inv = np.linalg.inv(V)
   a = V_inv @ yint

   yeval = np.polyval(a, xeval)

   return yeval


def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
    


''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

       

driver()        
