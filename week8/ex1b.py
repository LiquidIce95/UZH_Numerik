import numpy as np
from typing import Union


class newtonMethodArgument:
  """
    A struct holding:
    @f the function whose root should be approximated
    @df its derivative
    @x0 the starting point
    @epsilon the tolerance finish criteria
    @maxiter iteration finish criteria
    """
  def __init__(self,f:callable, df:callable,x0:float,epsilon:float,maxiter:int):
    """
    @f the function whose root should be approximated
    @df its derivative
    @x0 the starting point
    @epsilon the tolerance finish criteria
    @maxiter iteration finish criteria
    """
    assert epsilon > 0
    self.f = f
    self.df = df
    self.x0 = x0
    self.epsilon = epsilon
    self.maxiter = maxiter


def newtonMethod( args : newtonMethodArgument)->Union[float,int]:
  """
  Newtons method for approximating a root
  """
  x0 = args.x0
  f = args.f
  df = args.df
  epsilon = args.epsilon
  maxiter = args.maxiter
  xn = x0
  err = epsilon+1
  j = 1

  while err > epsilon and j < maxiter:
    x0 = xn
    xn = xn - f(xn)/df(xn)
    err = abs(xn-x0)
    j+=1

  return xn,j

def func(x:float):
  if x <= 0: return np.exp(-x**2)
  else: return -x**4 +1

def dfunc(x:float):
  if x<=0: return -2*x*np.exp(-x**2)
  else: return -4*x**3

if __name__ == "__main__":
  pass