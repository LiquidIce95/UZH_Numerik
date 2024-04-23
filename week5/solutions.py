import numpy as np
import matplotlib.pyplot as plt
import math

#Ex. 1a
#Bisectrion method code
def bisection(f, a, b, eps, max_iter):
    #Check if a or b are the roots (just in case)
    if (f(a) == 0): return a
    if (f(b) == 0): return b
    #Bad case
    if (f(a) * f(b) > 0):
        print('The root may not be in (a,b)')
        return
    #Calculate the number of iterations we will need
    need_iter = min(math.log2((b - a) / eps) // 1 + 1, max_iter)
    iter = 0
    #Main loop
    while (iter < need_iter):
        mid = 0.5 * (a + b)
        if (f(mid) == 0): return mid
        if (f(a) * f(mid) < 0): b = mid
        else: a = mid
        iter+=1
    return mid

#Ex. 1b
def f_sin(x):
    return math.sin(x)

powers = np.arange(1, 16, 1)
#array of tolerances for calculating Pi
tols = np.power(10.0, -powers)
pi_res = np.zeros(15)
for i in range(15):
    pi_res[i] = bisection(f_sin, 2.0, 4.0, tols[i], 1000)
#Plot for the errors
plt.loglog(tols, abs(pi_res - math.pi), label='Pi_approx')
#Reference plot
plt.loglog(tols, tols, '--')
plt.xlabel('tolerance')
plt.ylabel('Pi error')
#plt.savefig("errors_pi.png")
plt.show()

#The most accurately computed Pi
pi = pi_res[14]

#Ex. 1c
def f_ln(x):
    return math.log(x) - 1.0

powers = np.arange(1, 16, 1)
#array of tolerances for calculating e
tols = np.power(10.0, -powers)
e_res = np.zeros(15)
for i in range(15):
    e_res[i] = bisection(f_ln, 2.0, 3.0, tols[i], 1000)
#Plot for the errors
plt.loglog(tols, abs(e_res - math.exp(1)), label='e_approx')
#Reference plot
plt.loglog(tols, tols, '--')
plt.xlabel('tolerance')
plt.ylabel('e error')
#plt.savefig("errors_e.png")
plt.show()

#The most accurately computed e
e = e_res[14]


#Ex. 2d

#2-node Gauss quadrature for w = 1 on [0,pi]
def gauss_simple_1(f):
    return 0.5 * pi * (f(0.5 * pi - 0.5 * pi/math.sqrt(3.0)) + f(0.5 * pi + 0.5 * pi/math.sqrt(3.0)))

#2-node Gauss quadrature for w = sin x on [0,pi]
def gauss_simple_sin(f):
    return f(0.5 * (pi - math.sqrt(pi **2 - 8.0))) + f(0.5 * (pi + math.sqrt(pi **2 - 8.0)))

#Ex. 2e

#f functions f(x) to integrate
def f_sin_exp(x):
    return math.exp(x) * math.sin(x)

def f_exp(x):
    return math.exp(x)

#The exact value of the \int_0^{\pi} e^x sin(x) dx
I = 0.5 * (1 + e**pi)

#Simple formulas from the previous homework
def central_simple(f, a, b):
    return (b - a) * f(0.5 * (a+b))

def trap_simple(f, a, b):
    return 0.5 * (b - a) * (f(a) + f(b))

def simpson(f, a, b):
    return (b - a) * (f(a) + 4.0 * f(0.5 * (a + b)) + f(b)) / 6.0

#The errors for all 5 cases
err = np.zeros(5)
err[0] = abs(gauss_simple_sin(f_exp) - I)
err[1] = abs(gauss_simple_1(f_sin_exp) - I)
err[2] = abs(trap(f_sin_exp, 0, pi) - I)
err[3] = abs(central(f_sin_exp, 0, pi) - I)
err[4] = abs(simpson(f_sin_exp, 0, pi) - I)

print(err)

#Ex. 3a

# Simple integration through the Gauss-Legendre quadrature rule with three points
def gausslegendre_simple(f,a,b):
    x=[-math.sqrt(3/5), 0, math.sqrt(3/5)] #nodes
    w=[5/9, 8/9, 5/9] #weights
    
    I=0
    for indq in range(len(x)):
        I = I + (b-a)/2 * w[indq] * f( (b+a)/2 + x[indq] * (b-a)/2 )
    return I

#Ex. 3b

# Composite integration through the Gauss-Legendre quadrature rule with three points
def gausslegendre_comp(f,L,R,n): 
    
    #Size of a cell
    dx=(R-L)/n
    
    #Center of the cells
    cc=np.arange(L+dx/2,R,dx)
    
    I=0
    #Integration
    for indc in range(len(cc)):
        I=I+gausslegendre_simple(f,cc[indc]-dx/2,cc[indc]+dx/2)
    return I

#Ex. 3c

#Extrema
L = 0
R = 1

#Exact integral in [0,1]
I=e-1

#n for the convergence analysis
n_vec=np.arange(8)
m_vec=np.power(2,n_vec) #number of cells for the convergence analysis
h_vec = (R - L) / (np.power(2,n_vec)) 

#Vector of the errors
errors_gl=np.zeros(len(n_vec))

indi=-1 #index for storing the errors
for m in m_vec:
    indi=indi+1
    errors_gl[indi]=abs(gausslegendre_comp(f_exp,L,R,m)-I)

plt.loglog(h_vec,errors_gl,label='Gauss-Legendre')
plt.loglog(h_vec,errors_gl[0]/(h_vec[0]**1.0)*np.power(h_vec, 1.0),"--",label='ref, p = 1')
plt.loglog(h_vec,errors_gl[0]/(h_vec[0]**2.0)*np.power(h_vec, 2.0),"--",label='ref, p = 2')
plt.loglog(h_vec,errors_gl[0]/(h_vec[0]**3.0)*np.power(h_vec, 3.0),"--",label='ref, p = 3')
plt.loglog(h_vec,errors_gl[0]/(h_vec[0]**4.0)*np.power(h_vec, 4.0),"--",label='ref, p = 4')
plt.loglog(h_vec,errors_gl[0]/(h_vec[0]**5.0)*np.power(h_vec, 5.0),"--",label='ref, p = 5')
plt.loglog(h_vec,errors_gl[0]/(h_vec[0]**6.0)*np.power(h_vec, 6.0),"--",label='ref, p = 6')

#NB: The multiplication factor errors_gl[0]/(h_vec[0]**1.0) is used to
#shift the reference lines so to make them pass from the first point (h_vec[0],errors_gl[0])
plt.grid()
plt.xlabel("h")
plt.ylabel("intergration error")
plt.legend(loc="lower right")
#plt.savefig("convergencegl.png")
plt.show()





