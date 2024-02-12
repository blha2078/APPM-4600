import numpy as np
import fixedpt_example as fp 

def analyze_convergence(approximations, x_true):
    n = len(approximations)

    errors = [abs(a[0] - x_true) for a in approximations]
    print('errors ', errors)

    linear = []
    quadratic = []


    for i in range(n - 1):
        linear.append(abs(errors[i + 1] / errors[i]))
        quadratic.append(abs(errors[i + 1] / errors[i]**2))

    print('linear ', linear)
    print('quad ', quadratic)
    return linear, quadratic



# test functions 
f = lambda x: (10 / (x + 4)) ** (1 / 2)
# fixed point is alpha1 = 1.4987....

Nmax = 100
tol = 1e-10

# test f1 '''
x0 = 1.5
x_true = 1.3652300134140976
[approximations,ier] = fp.fixedpt(f,x0,tol,Nmax)
print('Value found: ', approximations[-1][0])
print('Iterations: ', len(approximations))
print('Error message reads:',ier)

analyze_convergence(approximations, x_true)