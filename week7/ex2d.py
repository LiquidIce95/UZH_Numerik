from math import pi,sqrt


def quadFormulaExC(f:callable)->float:
  x = [sqrt(-8*pi+4+2*pi**3)/2]
  x.append(-x[0])

  lamb = [pi/(x[0]-x[1])+x[1]*2,pi/(x[0]-x[1])+x[0]*2]

  return lamb[0]*f(x[0])+ lamb[1]*f(x[1])

def quadFromulaExD(f:callable)->float:
  return pi/2 * f(pi/2 - pi/(2*sqrt(3)) + pi/2 * f(pi/2 + pi/(2*sqrt(3))))



if __name__ == "__main__":
  pass

  