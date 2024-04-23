import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time

def show_error(A, b, x, s, runtime):
    test = np.matmul(A, x)
    r = la.norm(test - b)
    print(s, ' time:', round(runtime, 3), ' Result:', r)

def driver():
    ''' create matrix for testing different ways of solving a square linear system'''
    # Size of the system
    N = 1000

    # Right hand side
    b = np.random.rand(N, 1)
    A = np.random.rand(N, N)

    # standard solve()
    start_time = time.time()
    standard = scila.solve(A, b)
    end_time = time.time()
    r_standard = la.norm(np.matmul(A, standard) - b)
    print('Standard solve time:', round(end_time - start_time, 3), ' Result:', r_standard)

    # QR factorization
    start_time = time.time()
    Q, R = scila.qr(A)
    Qb = np.matmul(Q.T, b)
    x_qr = scila.solve_triangular(R, Qb)
    end_time = time.time()
    qr_solve_time = end_time - start_time
    show_error(A, b, x_qr, 'QR factorization', qr_solve_time)

    # Normal equation
    start_time = time.time()
    A_normal_eq = np.matmul(A.T, A)
    b_normal_eq = np.matmul(A.T, b)
    x_normal_eq = scila.solve(A_normal_eq, b_normal_eq)
    end_time = time.time()
    normal_eq_solve_time = end_time - start_time
    show_error(A, b, x_normal_eq, 'Normal equation', normal_eq_solve_time)

    ''' Create an ill-conditioned rectangular matrix '''
    N = 10
    M = 5
    A = create_rect(N, M)
    b = np.random.rand(N, 1)

def create_rect(N, M):
    ''' this subroutine creates an ill-conditioned rectangular matrix'''
    a = np.linspace(1, 10, M)
    d = 10**(-a)

    D2 = np.zeros((N, M))
    for j in range(0, M):
        D2[j, j] = d[j]

    # create matrices needed to manufacture the low rank matrix
    A = np.random.rand(N, N)
    Q1, R = la.qr(A)
    A = np.random.rand(M, M)
    Q2, R = la.qr(A)

    B = np.matmul(Q1, D2)
    B = np.matmul(B, Q2)
    return B

if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver()
