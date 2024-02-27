import numpy as np

def f(x):
    return np.cos(x)

# forward difference approximation
def forward_difference(f, x_val, h):
    return (f(x_val + h) - f(x_val)) / h

# centered difference approximation
def centered_difference(f, x_val, h):
    return (f(x_val + h) - f(x_val - h)) / (2 * h)

# derivative of f(x) = cos(x)
def f_prime(x):
    return -np.sin(x)

# Perform calculations for different values of h
h_values = 0.01 * 2**(-np.arange(0, 10, dtype=float))

for h in h_values:
    # forward difference
    forward_diff_result = forward_difference(f, np.pi/2, h)
    
    # centered difference
    centered_diff_result = centered_difference(f, np.pi/2, h)
    
    print(f"For h = {h}:")
    print(f"Forward Difference Approximation: {forward_diff_result}")
    print(f"Centered Difference Approximation: {centered_diff_result}")
    print()

# order
print("Order of Forward Difference Approximation: linear")
print("Order of Centered Difference Approximation: linear")
