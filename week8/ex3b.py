from week8.ex3a import *

def createMatricesAndVectors():
  n_values = [1,2,3, 4, 5,101,300]
  A_matrices = {}
  b_vectors = {}
  x_solutions = {}

  for n in n_values:
      A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
      A[0, 0] = 1
      A[n-1, n-1] = 1

      b = np.full(n, 10**-4)
      b[-1] = 0.5
      b[0] = 0

      A_matrices[n] = A
      b_vectors[n] = b

      x = 0.5 * 10**-4 * np.array([(i - 1)**2 for i in range(1, n+1)])
      x_solutions[n] = x
  
  return A_matrices,b_vectors,x_solutions

def test(A:np.ndarray,b:np.ndarray,xSol:np.ndarray)->float:
  x :np.ndarray = gaussian_elimination(A,b)

  errors = [abs(x[i]-xSol[i]) for i in range(xSol.shape[0])]
  return max(errors)



if __name__ == "__main__":
  A_matrices,b_vectors,x_solutions = createMatricesAndVectors()

  for size in A_matrices:
     print(f"for n={size} the error is :",test(A_matrices[size],b_vectors[size],x_solutions[size]))
  
  """you can see in the console which one is for """