from week8.ex3b import *

def createMatricesAndVectors2(n_values):
  A_matrices = {}
  b_vectors = {}
  x_solutions = {}

  for n in n_values:
      A = np.eye(n)

      for k in range(1,n):
         A -= k*np.eye(n,k=-k)
        
      for k in range(n):
         A[k,n-1]=1
      

      b = np.full(n, 1.5)
      
      x = np.full(n,0)
      x[n-1]=1.5


      A_matrices[n] = A
      b_vectors[n] = b
      x_solutions[n] = x
  
  return A_matrices,b_vectors,x_solutions




if __name__ == "__main__":
  A_matrices,b_vectors,x_solutions = createMatricesAndVectors2([1,2,3, 4, 5,52,101])

  for size in A_matrices:
     print(f"for n={size} the error is :",test(A_matrices[size],b_vectors[size],x_solutions[size],gaussian_elimination))
  
  """you can see in the console which one is for """