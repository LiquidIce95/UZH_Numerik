import numpy as np

def forwardStep(A:np.ndarray,M:int,N:int,b:np.ndarray,i:int):
   for j in range(i+1,N):
      r = A[j,i]/A[i,i]
      for k in range(N):
        A[j,k]-= r*A[i,k]
      b[j]-= r*b[i]



def backwardStep(A:np.ndarray,M:int,N:int,b:np.ndarray,i:int,x:np.ndarray):
  x[i] = b[i]
  for j in range(i+1,N):
    x[i] -= A[i,j]*x[j]
    x[i] /= A[i,i]



def gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    M,N = A.shape
    for i in range(N):
      forwardStep(A,M,N,b,i)
    x = np.zeros(M)
    for i in range(M):
       backwardStep(A,M,N,b,i,x)
    return x
      


if __name__ == "__main__":
  pass