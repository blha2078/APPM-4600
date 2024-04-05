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

def psi_equispaced(x, n):
    psi = 1
    for i in range(n + 1):
        psi *= (x - (-1 + 2 * i / n))
    return psi

def psi_chebyshev(x, n):
    psi = 1
    for i in range(n + 1):
        psi *= (x - np.cos((2 * i + 1) * np.pi / (2 * (n + 1))))
    return psi

n = 18

x_values = np.linspace(-1, 1, 1000)
psi_equispaced_values = np.zeros_like(x_values)
psi_chebyshev_values = np.zeros_like(x_values)

# Calculate Ψn(x) for equispaced nodes
psi_equispaced_values = np.maximum(psi_equispaced_values, np.abs(psi_equispaced(x_values, n)))

# Calculate Ψn(x) for Chebyshev nodes
psi_chebyshev_values = np.maximum(psi_chebyshev_values, np.abs(psi_chebyshev(x_values, n)))

# Plot log10 of Ψn(x) for equispaced and Chebyshev nodes
plt.plot(x_values, np.log10(psi_equispaced_values), label='Equispaced Nodes')
plt.plot(x_values, np.log10(psi_chebyshev_values), label='Chebyshev Nodes')

plt.xlabel('x')
plt.ylabel('log10 |Ψn(x)|')
plt.title('Comparison of Interpolation Errors for n=18')
plt.legend()
plt.grid(True)
plt.show()
