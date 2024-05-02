from week9.ex2_d import *


if __name__ == "__main__":
  
  n=3

  A1 = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
  A1[0, 0] = 1
  A1[n-1, n-1] = 1
  A1[0,1] = 0
  A1[n-1,n-2] = 0

  b1 = np.full(n, 10**-4)
  b1[-1] = 0.5
  b1[0] = 0

  x1 = 0.5 * 10**-4 * np.array([(i - 1)**2 for i in range(1, n+1)])
  
  A2 = np.eye(n)

  for k in range(1,n):
    A2 -= k*np.eye(n,k=-k)
    
  for k in range(n):
    A2[k,n-1]=1
  

  b2 = np.full(n, 1.5)

  x2 = np.full(n,0)
  x2[n-1]=1.5
  
  A3 = np.zeros(n)+np.eye(n,k=-1)*10**(-9)
  A3[0,:] = 1
  b3 = np.full(n,10**(-9))
  b3[0] = 4
  x3 = np.array([1 for i in range(n)])

  """testing"""
  A = [A1,A2,A3]
  b = [b1,b2,b3]
  x = [x1,x2,x3]

  maxErrG = 0
  maxErrH = 0

  for j in range(n):
    sol:np.ndarray = solveQR(A[j],b[j])
    err  = np.linalg.norm(sol-x[j])
    print(f"{err} is the error for  the {j+1}th test for gram schmidt") 

    if err>maxErrG : maxErrG = err

    sol = solveQRHouseHolder(A[j],b[j])
    err  = np.linalg.norm(sol-x[j])

    print(f"{err} is the error for  the {j+1}th test for house holder")

    if err>maxErrH : maxErrH = err


    Q,R = computeQRmatrices(A[j])
    print(f"{np.linalg.norm(np.dot(Q.transpose(),Q)-np.eye(n))} is the error of Q for gramSchmidt")
    Q,R = decomposeQRHouseHolder(A[j])
    print(f"{np.linalg.norm(np.dot(Q.transpose(),Q)-np.eye(n))} is the error of Q for HouseHolder")

    print("next test #########################################")

  print(f"max error of gram schmidt is {maxErrG}")
  print(f"max error of Householder is {maxErrH}")


  """CONCLUSIONS***************************************************************
  gram schmidt is wors for computing Q but better at solving the system of equation as 
  HouseHolder algorithm"""

