import sympy as sp

x = sp.symbols('x')

p0 = 1
p1 = x
p2 = x**2
p3 = x**3
print(p0,p1,p2,p3)

w = sp.Abs(x)

print(w)

# Define the integral with the weight function
def weighted_inner_product(p, q):
    return sp.integrate(p * q * w, (x, -1, 1))

# Construct the orthogonal polynomials using Gram-Schmidt process
def gram_schmidt(polys, w):
    ortho_polys = []
    for p in polys:
        ortho_p = p
        for q in ortho_polys:
            proj = weighted_inner_product(p, q) / weighted_inner_product(q, q)
            ortho_p = ortho_p - proj * q
        ortho_polys.append(sp.simplify(ortho_p))
    return ortho_polys


# Initial set of polynomials
polys = [p0, p1, p2, p3]

# Perform Gram-Schmidt process
ortho_polys = gram_schmidt(polys, w)

# Simplify the polynomials
ortho_polys = [sp.simplify(p) for p in ortho_polys]

print(ortho_polys)

# Find the roots of the last orthogonal polynomial π3
roots = sp.solve(ortho_polys[3], x)

# Construct the Lagrange interpolating polynomials
def lagrange_interpolant(points, k):
    x = sp.symbols('x')
    n = len(points)
    Lk = 1
    for j in range(n):
        if j != k:
            Lk *= (x - points[j]) / (points[k] - points[j])
    return sp.simplify(Lk)

# Compute the weights for the Gaussian quadrature
def gaussian_quadrature_weights(roots, w):
    weights = []
    for root in roots:
        Lk = lagrange_interpolant(roots, roots.index(root))
        weight = sp.integrate(Lk**2 * w, (x, -1, 1))
        weights.append(sp.simplify(weight))
    return weights

# Find the roots and weights for the Gaussian quadrature
quadrature_roots = [float(root) for root in roots]
quadrature_weights = gaussian_quadrature_weights(roots, w)

# Display the roots and weights
quadrature_roots, quadrature_weights


print(quadrature_weights)


def taylor_series(f, x, x0, n):
    """
    Calculate the n-th order Taylor series expansion of function f at point x0.
    
    :param f: sympy function to be expanded
    :param x: sympy variable
    :param x0: point around which to expand
    :param n: order of the Taylor expansion
    :return: n-th order Taylor series expansion of f around x0
    """
    taylor_expansion = 0
    for i in range(n + 1):
        term = (f.diff(x, i).subs(x, x0) / sp.factorial(i)) * (x - x0)**i
        taylor_expansion += term
    return sp.simplify(taylor_expansion)

# Example usage:
x = sp.symbols('x')
f = sp.sin(x)
taylor_expansion_5th_order = taylor_series(f, x, 0, 5)
print("\n",taylor_expansion_5th_order)


print(sp.diff(f,x,2))
print(sp.integrate(f,x))


def function(x):
    return 3*sp.cos(x)+x**3



a = sp.symbols('a')

print(function(a))
print(function(0))