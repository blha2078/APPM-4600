import numpy as np
import matplotlib.pyplot as plt

# Function to compute the manipulated expression: -2*sin(x + delta/2)*sin(delta/2)
def manipulated_expression(x, delta):
    return -2 * np.sin(x + delta/2) * np.sin(delta/2)

# Function to compute cos(x + delta) - cos(x)
def original_expression(x, delta):
    return np.cos(x + delta) - np.cos(x)

# Values of x
x_values = [np.pi, 1e6]

# delta between 10^{-16} to 1 using logspace
delta_values = np.logspace(-16, 0, endpoint=False, num=100)

# Plotting
plt.figure(figsize=(12, 8))

# Calculating the differences
for x in x_values:
    differences = np.abs(manipulated_expression(x, delta_values) - original_expression(x, delta_values))
    plt.loglog(delta_values, differences, label=f'x = {x}')

plt.title('Difference between Expressions for Different Values of x and δ')
plt.xlabel('δ')
plt.ylabel('|Manipulated - Original|')
plt.legend()
plt.grid(True)
plt.savefig('Q5b.png')
plt.show()
