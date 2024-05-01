from week9.ex2_b import *

def backwardStep(A:np.ndarray,M:int,N:int,b:np.ndarray,i:int,x:np.ndarray):
  x[i] = b[i]
  for j in range(i+1,N):
    x[i] -= A[i,j]*x[j]
  x[i] /= A[i,i]

def solveUpperTriangularSystem(R:np.ndarray,y:np.ndarray):
    m,n = R.shape

    x = np.zeros(m)
    for i in range(m-1,-1,-1):
       backwardStep(R,m,n,y,i,x)

    return x



if __name__ == "__ma)in__":
  pass