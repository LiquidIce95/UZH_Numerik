from week8.ex3c import *

def swapRows(A:np.ndarray,i1:int,i2:int)->None:
   c = A[[i1,i1],:]
   A[[i1,i1],:] = A[[i2,i2],:]
   A[[i2,i2],:] = c

def findMaxRowIndex(A:np.ndarray,StartIndex:int)->int:
  M,N = A.shape

  maxi = A[StartIndex,StartIndex]
  index = StartIndex
  for j in range(StartIndex+1,N):
      aji = A[j,StartIndex]
      if abs(aji) > abs(maxi):
        maxi = aji
        index = j

  return index



def gaussianEliminationPivoting(A:np.ndarray,b:np.ndarray)->np.ndarray:
  M,N = A.shape

  for i in range(M):
     swapIndex = findMaxRowIndex(A,i)
     if swapIndex != i :swapRows(A,i,swapIndex)
     forwardStep(A,M,N,b,i)
  x = np.zeros(M) 
  for i in range(M-1,-1,-1):
     backwardStep(A,M,N,b,i,x)
  return x
  


    



if __name__ == "__main__":
  A_matrices,b_vectors,x_solutions = createMatricesAndVectors([2,3, 4, 5,101,300])
  print("first test set\n")
  for size in A_matrices:
     print(f"for n={size} the error is :",test(A_matrices[size],b_vectors[size],x_solutions[size],gaussianEliminationPivoting))

  A_matrices,b_vectors,x_solutions = createMatricesAndVectors2([1,2,3, 4, 5,52,101])
  print("second test set\n")
  for size in A_matrices:
     print(f"for n={size} the error is :",test(A_matrices[size],b_vectors[size],x_solutions[size],gaussianEliminationPivoting))

  """Yes the error got much smaller :=)"""