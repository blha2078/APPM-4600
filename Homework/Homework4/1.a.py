import numpy as np

# Define the functions f and g
def f(x, y):
    return 3 * x**2 - y**2

def g(x, y):
    return 3 * x * y**2 - x**3 - 1

# Define the iteration matrix
iteration_matrix = np.array([
    [1/6, 1/18],
    [0, 1/6]
])

# Initial values
x0, y0 = 1, 1

# Number of iterations
num_iterations = 100

# Perform iterations
for n in range(num_iterations):
    # Multiply the iteration matrix by f and g
    result = np.dot(iteration_matrix, np.array([f(x0, y0), g(x0, y0)]))
    
    # Update values
    x0 -= result[0]
    y0 -= result[1]
    
    print(f"Iteration {n + 1}: x = {x0}, y = {y0}")

# Check the convergence
if abs(f(x0, y0)) < 1e-6 and abs(g(x0, y0)) < 1e-6:
    print("Converged successfully.")
else:
    print("Did not converge.")
