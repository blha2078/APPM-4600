import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial coefficients
coefficients = [1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512]

# (i)
x_values = np.arange(1.920, 2.081, 0.001)
# Use numpy to create y values
y_values = np.polyval(coefficients, x_values)

plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values)
plt.title("1 (i): p(x) From Expanded Coefficients")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.grid(True)
plt.savefig("plot_using_coefficients.png")

# (ii)
# Getting y vals directly from expression
y_values_alternative = (x_values - 2) ** 9

plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values_alternative)
plt.title("1 (ii): p(x) Using (x - 2)^9")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.grid(True)
plt.savefig("plot_using_expression.png")

# # (iii) Calculate the difference between the two plots
# difference = y_values - y_values_alternative

# plt.figure(figsize=(10, 5))
# plt.plot(x_values, difference, label="Difference (Coefficients - (x - 2)^9)")
# plt.title("Difference Between the Two Plots")
# plt.xlabel("x")
# plt.ylabel("Difference")
# plt.legend()
# plt.grid(True)
# plt.show()
