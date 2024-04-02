import numpy as np
import matplotlib.pyplot as plt

def barycentric_lagrange_interpolation(x_data, y_data, x):
    n = len(x_data)
    p = 0
    for j in range(n):
        w = compute_barycentric_weight(x_data, j)
        p += w * y_data[j] / (x - x_data[j])
    return p

def compute_barycentric_weight(x_data, j):
    w = 1
    n = len(x_data)
    for k in range(n):
        if j != k:
            w *= 1 / (x_data[j] - x_data[k])
    return w

# Define the function to be interpolated: 1 + (16x)^2
def f(x):
    return 1 / (1 + (16 * x) ** 2)

# Define the number of points and the range of x
n = 20
h = 2 / n
x_data = np.array([-1 + (i - 1) * h for i in range(1, n + 2)])
y_data = f(x_data)

# Define a finer grid for plotting
x_plot = np.linspace(-1, 1, 1001)
y_plot = f(x_plot)

# Evaluate the interpolated values on the finer grid
y_interpolated = [barycentric_lagrange_interpolation(x_data, y_data, x) for x in x_plot]

# Plot the data points and the function
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label='f(x)', color='blue')
plt.plot(x_data, y_data, 'o', label='Data points', color='red')
print(x_data)
print(y_data)
plt.plot(x_plot, y_interpolated, label='Interpolated polynomial', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Barycentric Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()
