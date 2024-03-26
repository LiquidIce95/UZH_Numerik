from week5.ex3_a_b import *
from matplotlib import pyplot as plt
from math import e

if __name__ == "__main__":
    a = 0
    B = [2**(n) for n in range(1,10)]
    f = lambda x : e**x
    Integral = e-1

    ErrorMidpoint = [abs(Integral - midpoint_rule(f,a,b)) for b in B]
    ErrorSimpson = [abs(Integral - simpsons_method(f,a,b)) for b in B]
    ErrorTrapezoidal = [abs(Integral - trapezoidal_method(f,a,b)) for b in B]

    refFunction = [1/m for m in B]

    plt.plot(B,ErrorMidpoint,label="Error of midpoint with repsect to h")
    plt.plot(B,ErrorSimpson,label="Error simposons with repsect to h")
    plt.plot(B,ErrorTrapezoidal,label="Error trapezoidal with repsect to h")
    plt.plot(B,refFunction,label="reference function")

    plt.title('Error of difference operator of h')
    plt.xlabel('distance h')
    plt.ylabel('errors')
    plt.xscale('log',base=2)
    plt.yscale('log',base=2)
    plt.legend()
    plt.grid(True)
    plt.show()

    """Conclusions"""