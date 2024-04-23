from week8.ex1b import *
from unittest import TestCase,main



class TestSuite(TestCase):
  def test1(self):
    f = func
    df = dfunc
    epsilon = 10**(-10)
    maxiter = 100
    x0 = -0.75

    args = newtonMethodArgument(f,df,x0,epsilon,maxiter)
    result = newtonMethod(args)
    print(result)
    pass

  def test2(self):
    f = func
    df = dfunc
    epsilon = 10**(-10)
    maxiter = 100
    x0 = 0.75

    args = newtonMethodArgument(f,df,x0,epsilon,maxiter)
    result = newtonMethod(args)
    print(result)
    pass

  def test3(self):
    f = func
    df = dfunc
    epsilon = 10**(-10)
    maxiter = 100
    x0 = 1.25

    args = newtonMethodArgument(f,df,x0,epsilon,maxiter)
    result = newtonMethod(args)
    print(result)
    pass


if __name__ == "__main__":
  main()

  """
  first starting point: 100 iterations and didnt even reach the tolerance
  second and third starting point: 7 
  """