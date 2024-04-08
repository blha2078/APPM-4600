def composite_trapezoidal(a, b, f, N):
     # Width of subinterval
    h = (b - a) / N 
    # Initial Result
    result = 0.5 * (f(a) + f(b))

    # Sum middle points N - 1 times
    for i in range(1, N):
        result += f(a + i * h)

    # Final appx
    result *= h

    return result

# Define the function to be integrated
def f(x):
    return x**2

# [a, b]
a = 0
b = 1

N = 100

# Calculate the integral using composite Trapezoidal rule
integral_approx = composite_trapezoidal(a, b, f, N)
print("Approximation of integral:", integral_approx)
