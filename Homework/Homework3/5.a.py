import numpy as np
import matplotlib.pyplot as plt

# Define the function
f = lambda x : x - 4 * np.sin(2 * x) - 3

# Generate x values for the plot
x_values = np.linspace(-5, 10, 1000)

# Plot the function
plt.plot(x_values, f(x_values), label='f(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--', label='y=0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x - 4sin(2x) - 3')
plt.legend()
plt.grid(True)
plt.show()

