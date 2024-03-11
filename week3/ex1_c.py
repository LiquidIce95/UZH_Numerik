from week3.ex1_b import PolyEvals,equidist,evaluationPointsPn
from matplotlib import pyplot as plt
import math

def PlotError(f:callable,pointdistri:callable,l:int,p:int,Intervallstart:int)->list:
  """
        @params f is the function to be interpolated
        @params pointdistri is the function which returns the list of points
        @params l is the highest power of 2 for the list of 
            interpolation polynomials degree
        @params p is the number of points which get evaluated
        @returns the list of the max errors
        @Intevallstart computes everything with respect [Intervallstart,-Intervallstart]
        assuming Intervallstart <=0
  """

  N = [(2**n)+1 for n in range(0,p+1)]
  PolyY,X,N = PolyEvals(f,pointdistri,l,p,Intervallstart)

  fY = [f(x) for x in X]

  Errors = []
  for n in range(0,len(N)):

    Errors.append(max([ abs(fY[i]-PolyY[n][i]) for i in range(0,len(X))]))

    """plotting"""


  plt.plot(N, Errors)

  plt.xlabel('n')
  plt.ylabel('Errors')
  plt.legend()
  plt.grid(True)
  plt.yscale('log')
  plt.show()


if __name__ == "__main__":
  PlotError(lambda x: math.e**-x**2,equidist,10,500,-5)