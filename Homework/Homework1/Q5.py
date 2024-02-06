# FUnction to compute the difference between two numbers, given their errors
def compute_difference(x1, x2, delta_x1, delta_x2):
    # Exact computation
    y_exact = x1 - x2

    # Approximations
    x1_hat = x1 + delta_x1
    x2_hat = x2 + delta_x2
    y_approx = x1_hat - x2_hat

    # Error due to approximation
    error = (delta_x1 - delta_x2)

    return y_exact, y_approx, error

# playing with small and large values
x_small = 0.01
x_large = 1e6

delta_x1 = 0.001
delta_x2 = 0.001

y_small_exact, y_small_approx, error_small = compute_difference(x_small, x_small, delta_x1, delta_x2)
y_large_exact, y_large_approx, error_large = compute_difference(x_large, x_large, delta_x1, delta_x2)

print(f"Exact value (small): {y_small_exact}")
print(f"Approximate value (small): {y_small_approx}")
print(f"Error (small): {error_small}")

print("\n")

print(f"Exact value (large): {y_large_exact}")
print(f"Approximate value (large): {y_large_approx}")
print(f"Error (large): {error_large}")
