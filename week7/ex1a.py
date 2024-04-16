


def bisectionMethod(f:callable,a:float,b:float,epsilon:float,maxiter:int)->float:
  """
    Implementation of the algorithm from the script
    @f the function
    @a extremum
    @b extremum
    @epsilon is the tolerance
    returns the approximated root of f whose error should be at most (b-a)/2**n
  """
  A,B = [a],[b]
  e = b-a

  x = []
  n = 0

  while n < maxiter and  abs(e) > epsilon:
    x.append(1/2 *(A[n]+B[n]))

    if f(x[n])*f(A[n]) > 0:
      A.append(x[n])
      B.append(B[n])
    else:
      A.append(A[n])
      B.append(x[n])
    
    n += 1
    e = B[n]-A[n]

  return (B[-1]+A[-1])/2
  



if __name__ == "__main__":
  pass