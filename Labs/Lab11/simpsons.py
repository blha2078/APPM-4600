# Same style as trapezoidal
def composite_simpson(a, b, f, N):
    h = (b - a) / N
    result = f(a) + f(b)

    for i in range(1, N):
        x = a + i * h
        weight = 2 if i % 2 == 0 else 4  # Alternating weights
        result += weight * f(x)

    # Multiply by h/3 for final appx
    result *= h / 3

    return result

# Example usage:
# Define the function to be integrated
def f(x):
    return x**2

a = 0
b = 1

N = 100

# Calculate the integral using composite Simpson's rule
integral_approx = composite_simpson(a, b, f, N)
print("Approximation of integral:", integral_approx)