from math import pi,sqrt


def quadFormulaExC(f:callable)->float:
  return f((pi+sqrt(pi**2 -8))/2)+f((pi-sqrt(pi**2-8))/2)

def quadFromulaExD(f:callable)->float:
  return pi/2 * f(pi/2 - pi/(2*sqrt(3)) + pi/2 * f(pi/2 + pi/(2*sqrt(3))))



if __name__ == "__main__":
  pass

  