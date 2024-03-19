import numpy as np
import matplotlib.pyplot as plt

# Exercise 3(a): Implementation of difference operators

def Da(fi, h):
    """
    Differential operator Da, approximating f'(x0).
    fi: Array of values [f_{-2}, f_{-1}, f_0]
    h: Distance between mesh nodes
    """
    return (fi[0] - 4*fi[1] + 3*fi[2]) / (2*h)

def Db(fi, h):
    """
    Differential operator Db, approximating f'(x0).
    fi: Array of values [f_{-1}, f_0, f_1, f_2]
    h: Distance between mesh nodes
    """
    return (-2*fi[0] - 3*fi[1] + 6*fi[2] - fi[3]) / (6*h)

def Dc(fi, h):
    """
    Differential operator Dc, approximating f''(x0).
    fi: Array of values [f_{-1}, f_0, f_1]
    h: Distance between mesh nodes
    """
    return (fi[0] - 2*fi[1] + fi[2]) / (h**2)

def D_plus(fi, h):
    """
    Simple forward difference operator, approximating f'(x0).
    fi: Array of values [f_0, f_1]
    h: Distance between mesh nodes
    """
    return (fi[1] - fi[0]) / h

# Function and its derivatives
f = lambda x: 1 / (0.4 * x)
f_prime = lambda x: -1 / (0.4 * x**2)
f_double_prime = lambda x: 2 / (0.4 * x**3)

# Point x0 and range of h values
x0 = 10
h_values = [2**(-n) for n in range(61)]

# Computing errors
errors_a = []
errors_b = []
errors_c = []
errors_plus = []

for h in h_values:
    fi_a = [f(x0 - 2*h), f(x0 - h), f(x0)]
    fi_b = [f(x0 - h), f(x0), f(x0 + h), f(x0 + 2*h)]
    fi_c = [f(x0 - h), f(x0), f(x0 + h)]
    fi_plus = [f(x0), f(x0 + h)]
    
    D_a_val = Da(fi_a, h)
    D_b_val = Db(fi_b, h)
    D_c_val = Dc(fi_c, h)
    D_plus_val = D_plus(fi_plus, h)
    
    error_a = abs(D_a_val - f_prime(x0))
    error_b = abs(D_b_val - f_prime(x0))
    error_c = abs(D_c_val - f_double_prime(x0))
    error_plus = abs(D_plus_val - f_prime(x0))
    
    errors_a.append(error_a)
    errors_b.append(error_b)
    errors_c.append(error_c)
    errors_plus.append(error_plus)

# Plotting errors in logarithmic scale
def plot_log_errors(h_values, errors, title):
    plt.plot(np.log2(h_values), np.log2(errors), label=title)
    plt.xlabel('log2(h)')
    plt.ylabel('log2(Error)')
    plt.grid(True)
    plt.legend()

plt.figure(figsize=(12, 8))
# plot_log_errors(h_values, errors_a, "Error Da(h)")
# plot_log_errors(h_values, errors_b, "Error Db(h)")
# plot_log_errors(h_values, errors_c, "Error Dc(h)")
plot_log_errors(h_values, errors_plus, "Error D+(h)")
plt.title("Logarithmic scale of errors")
plt.show()
