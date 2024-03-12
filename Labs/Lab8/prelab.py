def evaluate_line(x0, fx0, x1, fx1, alpha):
    """
    Calculate y-coordinate at point alpha on the line through (x0, fx0) and (x1, fx1).
    """
    if x1 - x0 == 0:
        raise ValueError("x1 and x0 must be different.")

    # Equation of a line
    result = fx0 + ((fx1 - fx0) / (x1 - x0)) * (alpha - x0)
    
    return result

# Example usage:
x0, fx0 = 2, 5  # coordinates of the first point
x1, fx1 = 5, 12  # coordinates of the second point
alpha = 3  # point at which to evaluate the line

result = evaluate_line(x0, fx0, x1, fx1, alpha)
print(f"The y-coordinate at alpha ({alpha}): {result}")
