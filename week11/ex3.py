import numpy as np
from matplotlib import pyplot as plt

# upwind
def Dup(uL,uC):
  """
  Upwind scheme
  """
  return uC-uL


def Dlw(uL,uC,uR,CFL):
  """
  lax-Wendroff scheme
  """
  return 1/2 *(uR-uL)-1/2 *CFL*(uL-2*uC+uR)


def solver(npoints, c, CFL, T, u0, D):
    dx = 1.0 / (npoints - 1)
    dt = CFL * dx / c
    nsteps = int(T / dt)
    
    u = np.array([u0(x) for x in np.linspace(0, 1, npoints)])
    
    for _ in range(nsteps):
        u_new = np.zeros(npoints)
        for i in range(npoints):
            uL = u[i - 1] if i > 0 else u[-1]
            uC = u[i]
            uR = u[i + 1] if i < npoints - 1 else u[0]
            u_new[i] = uC - CFL * D(uL, uC, uR, CFL)
        u = u_new
    
    return u


def u0_smooth(x):
    return np.exp(-100 * (x - 0.5)**2)

def u0_discontinuous(x):
    return 1 if 0.4 <= x <= 0.6 else 0

def Dmix(uL, uC, uR, CFL, epsilon):
    return epsilon * Dup(uL, uC, uR, CFL) + (1 - epsilon) * Dlw(uL, uC, uR, CFL)

def exact_solution(npoints, c, T, u0):
    return np.array([u0(x - c * T) for x in np.linspace(0, 1, npoints)])



if __name__ == "__main__":

  # tests of 3.d
  c = 1
  CFL = 0.25
  T = 1
  npoints_list = [51, 101, 201, 401, 801]

  for npoints in npoints_list:
      x_vals = np.linspace(0, 1, npoints)
      u_exact = exact_solution(npoints, c, T, u0_smooth)
      u_upwind = solver(npoints, c, CFL, T, u0_smooth, Dup)
      u_lax_wendroff = solver(npoints, c, CFL, T, u0_smooth, Dlw)
      
      plt.figure()
      plt.plot(x_vals, u_exact, label='Exact Solution')
      plt.plot(x_vals, u_upwind, label='Upwind Scheme')
      plt.plot(x_vals, u_lax_wendroff, label='Lax-Wendroff Scheme')
      plt.legend()
      plt.title(f'npoints = {npoints}')
      plt.xlabel('x')
      plt.ylabel('u')
      plt.show()
      
      error_upwind = np.max(np.abs(u_upwind - u_exact))
      error_lax_wendroff = np.max(np.abs(u_lax_wendroff - u_exact))
      print(f'npoints = {npoints}: Upwind Error = {error_upwind}, Lax-Wendroff Error = {error_lax_wendroff}')


  #tests of 3.e
  for npoints in npoints_list:
    x_vals = np.linspace(0, 1, npoints)
    u_exact = exact_solution(npoints, c, T, u0_discontinuous)
    u_upwind = solver(npoints, c, CFL, T, u0_discontinuous, Dup)
    u_lax_wendroff = solver(npoints, c, CFL, T, u0_discontinuous, Dlw)
    
    plt.figure()
    plt.plot(x_vals, u_exact, label='Exact Solution')
    plt.plot(x_vals, u_upwind, label='Upwind Scheme')
    plt.plot(x_vals, u_lax_wendroff, label='Lax-Wendroff Scheme')
    plt.legend()
    plt.title(f'npoints = {npoints}')
    plt.xlabel('x')
    plt.ylabel('u')
    plt.show()

  #tests for 3.f
  epsilon_values = np.linspace(0, 1, 11)
  npoints = 801

  x_vals = np.linspace(0, 1, npoints)
  u_exact = exact_solution(npoints, c, T, u0_discontinuous)

  for epsilon in epsilon_values:
      D = lambda uL, uC, uR, CFL: Dmix(uL, uC, uR, CFL, epsilon)
      u_mixed = solver(npoints, c, CFL, T, u0_discontinuous, D)
      
      plt.figure()
      plt.plot(x_vals, u_exact, label='Exact Solution')
      plt.plot(x_vals, u_mixed, label=f'Mixed Scheme (epsilon={epsilon})')
      plt.legend()
      plt.title(f'npoints = {npoints}, epsilon = {epsilon}')
      plt.xlabel('x')
      plt.ylabel('u')
      plt.show()