from week5.ex3_a_b import *
from matplotlib import pyplot as plt
from math import e

if __name__ == "__main__":
    L = 0
    R = 1
    B = [2**(n) for n in range(1,10)]
    f = lambda x : e**x
    Integral = e-1

    ErrorMidpoint = [abs(Integral - midpoint_composite(f,L,R,b)) for b in B]
    ErrorSimpson = [abs(Integral - simpsons_composite(f,L,R,b)) for b in B]
    ErrorTrapezoidal = [abs(Integral - trapezoidal_composite(f,L,R,b)) for b in B]
    ReferenceCurves=[[h**(-p) for p in range(1,10)] for h in B]


    plt.plot(B,ErrorMidpoint,label="Error of midpoint with repsect to h")
    plt.plot(B,ErrorSimpson,label="Error simposons with repsect to h")
    plt.plot(B,ErrorTrapezoidal,label="Error trapezoidal with repsect to h")

    for Curve in ReferenceCurves:
        plt.plot(B,Curve,linestyle='dotted')

    plt.title('Error of difference operator of h')
    plt.xlabel('distance h')
    plt.ylabel('errors')
    plt.xscale('log',base=2)
    plt.yscale('log',base=2)
    plt.legend()
    plt.grid(True)
    plt.show()

    """Conclusions"""
    """they all converge algebraically
      and simposons and trapezoidal are overlapping"""