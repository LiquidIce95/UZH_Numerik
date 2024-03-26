from week5.ex2_b import midpoint_rule,simpsons_method,trapezoidal_method
import math
from matplotlib import pyplot as plt

if __name__ == "__main__":
    a = 0
    B = [2**(-n) for n in range(1,8)]
    f = lambda x : math.e**x
    ErrorMidpoint = [abs((math.e -1)- midpoint_rule(f,a,b)) for b in B]
    ErrorSimpson = [abs((math.e -1)- simpsons_method(f,a,b)) for b in B]
    ErrorTrapezoidal = [abs((math.e -1)- trapezoidal_method(f,a,b)) for b in B]
    ReferenceCurves=[[h**p for p in range(1,8)] for h in B]

    plt.plot(B,ErrorMidpoint,label="Error of midpoint with repsect to h")
    plt.plot(B,ErrorSimpson,label="Error simposons with repsect to h")
    plt.plot(B,ErrorTrapezoidal,label="Error trapezoidal with repsect to h")

    for Curve in ReferenceCurves:
        plt.plot(B,Curve)

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
    """
