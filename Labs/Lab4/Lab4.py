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

def aitkins(approximations, tol):
    res = np.zeros((len(approximations) - 2, 1))
    for i in range(len(approximations) - 2):
        res[i] = approximations[i][0] - (((approximations[i + 1] - approximations[i])**2) / (approximations[i + 2] - 2*approximations[i + 1] + approximations[i]))

        if (abs(res[i] - res[i - 1]) <= tol): return res[:i+1]

    return res

def steffensons(g, x0, tol, Nmax):
    count = 0
    approximations = np.zeros((Nmax, 1))

    while count < Nmax:
        a = x0
        b = g(a)
        c = g(b)

        x1 = a - ((b - a)**2) / (c - 2*b + a)

        approximations[count] = x1

        if abs(x1 - x0) < tol:
            xstar = x1
            ier = 0
            return [approximations[:count+1], ier]

        x0 = x1
        count += 1

    xstar = x1
    ier = 1
    return [approximations, ier]

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



new_approximations = aitkins(approximations, tol)
print('Value found: ', new_approximations[-1][0])
print('Iterations: ', new_approximations)

analyze_convergence(new_approximations, x_true)


steffensons_approximations = steffensons(f,x0,tol,Nmax)[0]
print('Value found: ', steffensons_approximations[-1])
print('Iterations: ', steffensons_approximations)

analyze_convergence(steffensons_approximations, x_true)