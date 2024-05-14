import numpy as np

def jacobi(A, b, epsilon, max_iter):
    D = np.diag(np.diag(A))
    D_inv = np.diag(1 / np.diag(A))
    N = A - D
    x = np.zeros_like(b, dtype=np.float64)
    for k in range(max_iter):
        x_new = D_inv @ (b - N @ x)
        if np.linalg.norm(x_new - x, np.inf) < epsilon:
            return x_new, k+1
        x = x_new
    raise ValueError("Jacobi method did not converge within the maximum number of iterations")

if __name__ == "__main__":
  # Test on the linear systems from the previous exercise
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
