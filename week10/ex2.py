import numpy as np

def infinity_norm(A):
    return np.max(np.sum(np.abs(A), axis=1))

def richardson(A, b, omega, epsilon, max_iter):
    x = np.zeros_like(b, dtype=np.float64)
    for k in range(max_iter):
        r = b - A @ x
        x_new = x + omega * r
        if np.linalg.norm(x_new - x, np.inf) < epsilon:
            return x_new, k+1
        x = x_new
    raise ValueError("Richardson method did not converge within the maximum number of iterations")


def testOne():
  # Test case i
  n = 99
  h = 1e-2
  A1 = (1/h**2) * (2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1))
  b1 = np.ones(n)
  b1[-1] -= 1/(2*h**2)

  omega_values = [
      h**2 / (8 * np.cos(np.pi * h / 2)**2),
      h**2 / (4 * np.cos(np.pi * h / 2)**2),
      h**2 / (2 * np.cos(np.pi * h / 2)**2),
      h**2 / (np.cos(np.pi * h / 2)**2),
      h**2 / (2 * np.cos(np.pi * h / 2)**2) - 1e-8,
      h**2 / 2
  ]

  epsilon = 1e-10
  max_iter = 10**6

  results = []
  for omega in omega_values:
      try:
          x, iters = richardson(A1, b1, omega, epsilon, max_iter)
          results.append((omega, iters))
      except ValueError as e:
          results.append((omega, str(e)))

  # Output the results
  for omega, result in results:
      print(f"omega: {omega}, result: {result}")


def testTwo():
  # Test case ii
  A2 = np.array([[200, 11, 30, 27], [11, 200, 10, 46], [30, 10, 200, 2], [27, 46, 2, 200]])
  A3 = np.array([[5, 7, 6, 5], [7, 10, 8, 7], [6, 8, 10, 9], [5, 7, 9, 10]])
  b2 = b3 = np.array([1, 2, 3, 4])

  omega = 1.5 / infinity_norm(A2)
  try:
      x, iters = richardson(A2, b2, omega, epsilon, 10**5)
      print(f"System A2: converged in {iters} iterations")
  except ValueError as e:
      print(f"System A2: {e}")

  omega = 1.5 / infinity_norm(A3)
  try:
      x, iters = richardson(A3, b3, omega, epsilon, 10**5)
      print(f"System A3: converged in {iters} iterations")
  except ValueError as e:
      print(f"System A3: {e}")

if __name__ == "__main__": 
  testOne()
  """
  from exercise 2.d the first 4 omegas converge or diverge exactly if the omega is
  bounded by the greatest eigenvalue
  the fith test can be bounded by 2/\lambda_max therefore fullfilling the criteria for 
  convergence as well as the sixth test
  """
  # testTwo()
  
