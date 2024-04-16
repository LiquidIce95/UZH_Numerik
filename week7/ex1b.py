from week7.ex1a import *
from math import pi,sin
from matplotlib import pyplot as plt
from copy import deepcopy

class ApproximationArgs:
   def __init__(self,f:callable,a:float,b:float,epsilon:float,maxiter) -> None:
        self.f = f
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.maxiter = maxiter


class Approximation:
    
    def __init__(self) -> None:
        self.approximations = []      

    def compute(self,args:ApproximationArgs)->None:
       newArgs = deepcopy(args)
       self.approximations.append((newArgs,bisectionMethod(newArgs.f,newArgs.a,newArgs.b,newArgs.epsilon,newArgs.maxiter)))

    def getApprox(self)->list:
       return self.approximations
    
    def plotApprox(self)->None:
      xAxis = []
      yAxis = []
      for (data,result) in self.approximations:
        xAxis.append(data.epsilon)
        yAxis.append(result)

      plt.plot(xAxis,yAxis,label='Approximations of pi')
      plt.xscale('log',base=2)
      plt.yscale('log',base=2)
      plt.grid(True)
      plt.legend()
      plt.show()

    def plotApproxErrs(self,target:float)->None:
      xAxis = []
      yAxis = []
      for (data,result) in self.approximations:
        xAxis.append(data.epsilon)
        yAxis.append(abs(result-target))

      plt.plot(xAxis,yAxis,label='Errors between actual value and approximation')
      plt.plot(xAxis,xAxis,label='maxErrors')
      plt.xscale('log',base=2)
      plt.yscale('log',base=2)
      plt.grid(True)
      plt.legend()
      plt.show()


if __name__ == '__main__':
  tols = [10**(-n) for n in range(1,16)]
  Args = [ApproximationArgs(sin,2,4,tol,1000) for tol in tols]
  Aprox = Approximation()
  
  for arg in Args:
     Aprox.compute(arg)

  Aprox.plotApproxErrs(pi)

