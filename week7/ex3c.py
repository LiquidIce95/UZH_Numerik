from week7.ex3b import compositeNode3GaussQuad,composite_quadrature
from week5.ex3_a_b import midpoint_composite,simpsons_composite,trapezoidal_composite
from math import e
from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":
  n_list = np.arange(1,10)
  m_list = np.power(2, n_list)
  h_list = 1./m_list  

  f = np.exp
  a,b = 0,1
  I = np.exp(1)-1

  errNode3GaussQuad = [abs(I - composite_quadrature(f,a,b,m)) for m in m_list]
  errSimps = [abs(I - simpsons_composite(f,a,b,m)) for m in m_list]
  errMidp = [abs(I - midpoint_composite(f,a,b,m)) for m in m_list]
  errTrap = [abs(I - trapezoidal_composite(f,a,b,m)) for m in m_list]


  refCurves = [h_list**p for p in range(2,7)]

  plt.plot(h_list,errNode3GaussQuad,label="3 node gauss quadrature")
  plt.plot(h_list,errSimps,label="Simpsons")
  plt.plot(h_list,errMidp,label="midpoint")
  plt.plot(h_list,errTrap,label="Trapezoidal")

  for j in range(len(refCurves)):
    plt.plot(h_list,refCurves[j],linestyle='dotted',label=f"p={j+2}")
  
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
  the 3 node gauss quadrature is best with algebraic convergence of order p = 6 as can be seen from the diagram
  """