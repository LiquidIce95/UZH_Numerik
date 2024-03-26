
from week5.ex2_b import midpoint_rule,simpsons_method,trapezoidal_method
import math


if __name__=="__main__":
    a=0
    b=1
    f = lambda x : math.e**x
    methods = [midpoint_rule,simpsons_method,trapezoidal_method]
    print([abs((math.e-1) - method(f,a,b)) for method in methods])
"""the simpsons_method is the most precise in this case
    becuase it has accuracy 3 and we had exactly 3 points which gives
    a polynomial of degree 4 so thats why a slight inaccuracy is
    introduced"""