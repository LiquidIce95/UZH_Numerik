from week7.ex3b import compositeNode3GaussQuad
from week5.ex3_a_b import midpoint_composite,simpsons_composite,trapezoidal_composite
from math import e
from matplotlib import pyplot as plt

if __name__ == "__main__":
  NumOfPoints = [2**n for n in range(1,10)]
  f = lambda x : e**x
  a,b = 0,1
  I = e

  errNode3GaussQuad = [abs(I - compositeNode3GaussQuad(f,a,b,m)) for m in NumOfPoints]
  errSimps = [abs(I - simpsons_composite(f,a,b,m)) for m in NumOfPoints]
  errMidp = [abs(I - midpoint_composite(f,a,b,m)) for m in NumOfPoints]
  errTrap = [abs(I - trapezoidal_composite(f,a,b,m)) for m in NumOfPoints]


  refCurves = [ [h**p for p in range(1,10)]  for h in NumOfPoints]

  plt.plot(NumOfPoints,errNode3GaussQuad,label="3 node gauss quadrature")
  plt.plot(NumOfPoints,errSimps,label="Simpsons")
  plt.plot(NumOfPoints,errMidp,label="midpoint")
  plt.plot(NumOfPoints,errTrap,label="Trapezoidal")

  for curve in refCurves:
    plt.plot(NumOfPoints,curve,linestyle='dotted')
  
  plt.title('Error of composite Integration with repsect to number of points')
  plt.xlabel('number of points')
  plt.ylabel('errors')
  plt.xscale('log',base=2)
  plt.yscale('log',base=2)
  plt.legend()
  plt.grid(True)
  plt.show()


  """
  analysis:
  
  """