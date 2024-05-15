import numpy as np

def infinity_norm(A):
    return np.max(np.sum(np.abs(A), axis=1))

def jacobi(A, b, epsilon, max_iter):
    D = np.diag(np.diag(A)) 
    D_inv = np.diag(1 / np.diag(A))
    N = A - D
    x = np.zeros_like(b, dtype=np.float64)

    print(f"the error bound is {infinity_norm(-D_inv@N)}\n")
    for k in range(max_iter):
        x_new = D_inv @ (b - N @ x)
        if np.linalg.norm(x_new - x, np.inf) < epsilon:
            return x_new, k+1
        x = x_new
    raise ValueError("Jacobi method did not converge within the maximum number of iterations")

if __name__ == "__main__":
  n = 99
  h = 1e-2
  A1 = (1/h**2) * (2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1))
  b1 = np.ones(n)
  b1[-1] -= 1/(2*h**2)

  A2 = np.array([[200, 11, 30, 27], [11, 200, 10, 46], [30, 10, 200, 2], [27, 46, 2, 200]])
  A3 = np.array([[5, 7, 6, 5], [7, 10, 8, 7], [6, 8, 10, 9], [5, 7, 9, 10]])
  b2 = b3 = np.array([1, 2, 3, 4])



  epsilon = 1e-10
  max_iter = 10**5

  # System A1 with parameters
  try:
      x, iters = jacobi(A1, b1, epsilon, max_iter)
      print(f"Jacobi method on A1: converged in {iters} iterations")
  except ValueError as e:
      print(f"Jacobi method on A1: {e}")

  # System A2
  try:
      x, iters = jacobi(A2, b2, epsilon, max_iter)
      print(f"Jacobi method on A2: converged in {iters} iterations")
  except ValueError as e:
      print(f"Jacobi method on A2: {e}")

  # System A3
  try:
      x, iters = jacobi(A3, b3, epsilon, max_iter)
      print(f"Jacobi method on A3: converged in {iters} iterations")
  except ValueError as e:
      print(f"Jacobi method on A3: {e}")




  """
  the first two matrices satisfy the bounds derived from ex3.b so they converge, however 
  for the third matrix it does not satisfy the bound and so we have no garanteed convergence
  as can be seen in the console with the printed error bound, note in the first case (x_0-x) must
  be below 1 to garantee convergence
  """