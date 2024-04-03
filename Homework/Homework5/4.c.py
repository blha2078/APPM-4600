import numpy as np
import matplotlib.pyplot as plt

# Data points
data_points = np.array([[0, 1], [1, 4], [2, 2], [3, 6]])

# Interpolation line 1: p(x) = a1*x + a0 (with a0 = a1 = 1.3)
a0_1 = 1.3
a1_1 = 1.3
x_values = np.linspace(0, 3, 100)
y_values_1 = a1_1 * x_values + a0_1

# Interpolation line 2: p(x) = a1*x + a0 (with a0 = 1.2573 and a1 = 1.2427)
a0_2 = 1.2427
a1_2 = 1.2573
y_values_2 = a1_2 * x_values + a0_2

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(data_points[:, 0], data_points[:, 1], color='red', label='Data Points')
plt.plot(x_values, y_values_1, label='Interpolation Line 1: a0 = a1 = 1.3')
plt.plot(x_values, y_values_2, label='Interpolation Line 2: a0 = 1.2573, a1 = 1.2427')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation with Different Parameters')
plt.legend()
plt.grid(True)
plt.show()
