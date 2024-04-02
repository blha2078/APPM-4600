def eval_legendre(n, x):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, x]
    else:
        p0 = 1
        p1 = x
        p = [p0, p1]
        for i in range(2, n + 1):
            pn = ((2 * i - 1) * x * p1 - (i - 1) * p0) / i
            p.append(pn)
            p0 = p1
            p1 = pn
        return p

# Example usage:
n = 4
x = 0.5
legendre_values = eval_legendre(n, x)
print("Legendre polynomials evaluated at x =", x, ":", legendre_values)