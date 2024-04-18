import numpy as np
import matplotlib.pyplot as plt

# Exercise 2. a)

def midpoint_rule(f,a,b):
	m = (a+b)/2.
	return (b-a)*f(m)

def trapezoidal_rule(f,a,b):
	return (b-a)/2.*(f(a)+f(b))

def simpsons_method(f,a,b):
	m = (a+b)/2.
	return (b-a)/6.*(f(a)+4.*f(m)+f(b))


# Exercise 2. b)

def f(x): return np.exp(x)
exact_value = np.exp(1.)-1.
print("Midpoint rule: Error = " + str(abs(exact_value-midpoint_rule(f,0.,1.))))
print("Trapezoidal rule: Error = " + str(abs(exact_value-trapezoidal_rule(f,0.,1.))))
print("Simpson's method: Error = " + str(abs(exact_value-simpsons_method(f,0.,1.))))



# Exercise 2. c)

n_list = np.arange(8)
h_list = 1./np.power(2, n_list)
Error_midpoint = []
Error_trapezoidal = []
Error_simpsons = []
for h in h_list:
	exact_value = np.exp(h)-1.
	Error_midpoint.append(abs(exact_value-midpoint_rule(f,0.,h)))
	Error_trapezoidal.append(abs(exact_value-trapezoidal_rule(f,0.,h)))
	Error_simpsons.append(abs(exact_value-simpsons_method(f,0.,h)))

plt.loglog(h_list, Error_midpoint, label='midpoint')
plt.loglog(h_list, Error_trapezoidal, label='trapezoidal')
plt.loglog(h_list, Error_simpsons, label='Simpson')
plt.loglog(h_list, np.power(h_list, 3), ls='dashed', label='ref, p=3')
plt.xlabel('h')
plt.ylabel('Error')
plt.loglog(h_list, 0.01*np.power(h_list, 5), ls='dashed', label='ref, p=5')
plt.loglog(h_list, *np.power(h_list, 5), ls='dashed', label='ref, p=5')
plt.grid()
plt.legend()
plt.show()
# plt.savefig('Convergence_simple_quadratures.pdf')
# plt.close()


# Exercise 3.a)

def midpoint_composite(f,L,R,n):
	Q = 0.
	# We first loop over the intervals
	for i in range(n):
		a = L + i*(R-L)/n
		b = a + (R-L)/n
		Q = Q + midpoint_rule(f,a,b)

	return Q


def trapezoidal_composite(f,L,R,n):
	Q = 0.
	# We first loop over the intervals
	for i in range(n):
		a = L + i*(R-L)/n
		b = a + (R-L)/n
		Q = Q + trapezoidal_rule(f,a,b)

	return Q


def simpsons_composite(f,L,R,n):
	Q = 0.
	# We first loop over the intervals
	for i in range(n):
		a = L + i*(R-L)/n
		b = a + (R-L)/n
		Q = Q + simpsons_method(f,a,b)

	return Q


# # Exercise 3.b)
def f(x): return np.exp(x)
exact_value = np.exp(1.)-1.
print("Midpoint rule: Error = " + str(abs(exact_value-midpoint_composite(f,0.,1.,100))))
print("Trapezoidal rule: Error = " + str(abs(exact_value-trapezoidal_composite(f,0.,1.,100))))
print("Simpson's method: Error = " + str(abs(exact_value-simpsons_composite(f,0.,1.,100))))


# # Exercise 3.c)
n_list = np.arange(10)
m_list = np.power(2, n_list)
h_list = 1./m_list
Error_midpoint = []
Error_trapezoidal = []
Error_simpsons = []
exact_value = np.exp(1.)-1.
for m in m_list:
	Error_midpoint.append(abs(exact_value-midpoint_composite(f,0.,1.,m)))
	Error_trapezoidal.append(abs(exact_value-trapezoidal_composite(f,0.,1.,m)))
	Error_simpsons.append(abs(exact_value-simpsons_composite(f,0.,1.,m)))

plt.loglog(h_list, Error_midpoint, label='midpoint')
plt.loglog(h_list, Error_trapezoidal, label='trapezoidal')
plt.loglog(h_list, Error_simpsons, label='Simpson')
plt.loglog(h_list, h_list**2, ls='dashed', label='ref, p=2')
plt.loglog(h_list, 0.01*h_list**4, ls='dashed', label='ref, p=4')
plt.xlabel('h')
plt.ylabel('Error')
plt.grid()
plt.legend()
plt.show()
# plt.savefig('Convergence_composite_quadratures.pdf')
# plt.close()
