import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + (16 * x) ** 2)

def barycentric_weights(x):
    n = len(x)
    w = np.ones(n)
    for j in range(n):
        for k in range(n):
            if k != j:
                w[j] *= (x[j] - x[k])
        w[j] = 1 / w[j]
    return w

def barycentric_lagrange(x, y, z):
    n = len(x)
    w = barycentric_weights(x)
    p = np.zeros_like(z)
    for i in range(len(z)):
        numerator = np.sum(w / (z[i] - x) * y)
        denominator = np.sum(w / (z[i] - x))
        p[i] = numerator / denominator
    return p

# n_values = range(2, 21)  # Values of n from 2 to 20
n_values = range(15, 20)
for n in n_values:
    # Generate Chebyshev nodes
    xi = np.cos((2 * np.arange(n + 1) + 1) * np.pi / (2 * (n + 1)))
    fi = f(xi)

    # Plot data points
    plt.plot(xi, fi, 'o', label=f'n={n}')

    # Interpolate polynomial
    x_finer = np.linspace(-1, 1, 1001)
    p = barycentric_lagrange(xi, fi, x_finer)

    # Plot interpolated polynomial
    plt.plot(x_finer, p, label='Interpolated Polynomial')

    # Plot original function
    plt.plot(x_finer, f(x_finer), label='f(x)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Barycentric Lagrange Interpolation with Chebyshev Nodes')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Stop iteration if the maximum value of p(x) is about 100
    if np.max(p) > 100:
        break
