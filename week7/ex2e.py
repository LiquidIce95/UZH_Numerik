from week7.ex2d import *
from math import pi,e,sin

def midpoint_rule(f:callable,a:float,b:float)->float:
    """
    @f is the function whose integral is approximated
    @a is left edge of intervall
    @b is right edge of intervall
    @returns an approximation of an integral
    """
    return (b-a)*f((a+b)/2)


def trapezoidal_method(f:callable,a:float,b:float)->float:
    """
    @f is the function whose integral is approximated
    @a is an extremum of f
    @b is an extremum of f
    @returns an approximation of an integral
    """
    return (b-a)*(f(a)+f(b))/2
    

def simpsons_method(f:callable,a:float,b:float)->float:
    """
    @f is the function whose integral is approximated
    @a is an extremum of f
    @b is an extremum of f
    @returns an approximation of an integral
    """
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6




if __name__ == "__main__":
  a,b = 0,pi
  mr = lambda f : midpoint_rule(f,a,b)
  tm = lambda f : trapezoidal_method(f,a,b)
  sm = lambda f : simpsons_method(f,a,b)

  methods = [mr,tm,sm,quadFromulaExD]

  I = 1/2 * (1+e**pi)



  Errors = [abs(meth(lambda x : e**x * sin(x))-I)for meth in methods]
  Errors.append(abs(quadFormulaExC(lambda x : e**x)-I))

  print(Errors)

  """Obviously Midpoint is the most accurate because the integral is approximately
    the area of the midpoint"""