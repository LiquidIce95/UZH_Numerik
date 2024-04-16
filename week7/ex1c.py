from week7.ex1b import *
from math import e,log

if __name__ == "__main__":
  f = lambda x : log(x)-1
  tols = [10**(-n) for n in range(1,16)]
  Args = [ApproximationArgs(f,2,4,tol,1000) for tol in tols]

  Apro = Approximation()
  for arg in Args:
    Apro.compute(arg)

  Apro.plotApproxErrs(e)