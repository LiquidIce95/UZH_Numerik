from week5.ex2_c import *
import math
from matplotlib import pyplot as plt

if __name__ == "__main__":
    a = 0
    B = [2**(-n) for n in range(1,8)]
    f = lambda x : math.e**x
    ErrorMidpoint = [abs((math.e**b -1)- midpoint_rule(f,a,b)) for b in B]
    ErrorSimpson = [abs((math.e**b -1)- simpsons_method(f,a,b)) for b in B]
    ErrorTrapezoidal = [abs((math.e**b -1)- trapezoidal_method(f,a,b)) for b in B]
    ReferenceCurves=[[h**p for p in range(1,8)] for h in B]

    plt.plot(B,ErrorMidpoint,label="Error of midpoint with repsect to h")
    plt.plot(B,ErrorSimpson,label="Error simposons with repsect to h")
    plt.plot(B,ErrorTrapezoidal,label="Error trapezoidal with repsect to h")

    bound = lambda x : math.e**x * x**5 * 1/60

    bounds = [bound(h) for h in B]

    for Curve in ReferenceCurves:
        plt.plot(B,Curve,linestyle='dotted')

    
    plt.plot(B,bounds,label="max error for trapezoidal")

    plt.title('Error of difference operator of h')
    plt.xlabel('distance h')
    plt.ylabel('errors')
    plt.xscale('log',base=2)
    plt.yscale('log',base=2)
    plt.legend()
    plt.grid(True)
    plt.show()

    """
    conclusions
    of course task1 holds since the plottet bound from task1 e is above the simposons curve
    in parallel, also simposons has the smallest error 

    trapezoidal and midpoint are parallel to each other 
    """
