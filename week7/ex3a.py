from math import sqrt,e

"""
set x(t) = (b-a)/2 * t + (a+b)/2 and g(t) = f(x(t)) for t in [-1,1]
then g is a function on [-1,1] 
then one can derive the formula
below
"""
def node3GausQuad(f:callable,a:float, b:float)->float:
  return (b-a)/2 * ( (5/9) * f((a+b)/2 - sqrt(3/5) * (b-a)/2) + (8/9) * f((a+b)/2) + (5/9) * f((a+b)/2 + sqrt(3/5) * (b-a)/2) )


if __name__ == "__main__":
  pass