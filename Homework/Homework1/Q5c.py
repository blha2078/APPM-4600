import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Taylor expansion approximation: δf'(x) + δ^2/(2!)f''(x)
def taylor_approximation(x, delta):
    # Since ξ is somewhere in [x, x+δ], we will pick x+(δ/2) for the second derivative
    return delta * -np.sin(x) #+ (delta**2) / 2 * (-np.cos(x + delta/2))


# Function to compute cos(x + delta) - cos(x)
def original_expression(x, delta):
    return np.cos(x + delta) - np.cos(x)

# Values of x
x_values = [np.pi, 1e6]

# delta between 10^{-16} to 1 using logspace
delta_values = np.logspace(-16, 0, endpoint=False, num=100, base=10)

# Plotting
plt.figure(figsize=(12, 8))

# Calculating the differences
for x in x_values:
    differences = np.abs(taylor_approximation(x, delta_values) - original_expression(x, delta_values))
    plt.loglog(delta_values, differences, label=f'x = {x}')

plt.title('Difference between Actual Expression and Taylor Approximation for Different Values of x and δ')
plt.xlabel('δ')
plt.ylabel('|Taylor Appx. - Original|')
plt.legend()
plt.grid(True)
plt.savefig('Q5c.png')
plt.show()
