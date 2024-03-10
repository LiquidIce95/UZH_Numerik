from ex1_a import evaluationPointsPn,nevilleDP
import math
from matplotlib import pyplot as plt

Intervallstart = -3

def equidist(n:int)->list:
    return [(Intervallstart)+(2*(-Intervallstart)/n)*i for i in range(0,n+1)]

def compute2(f :callable,pointdistri:callable,l:int,p:int)->list:
    """
        @params f is the function to be interpolated
        @params pointdistri is the function which returns the list of points
        @params l is the highest power of 2 for the list of 
            interpolation polynomials degree
        @params p is the number of points which get evaluated
        @returns the list of the max errors
    """
    N = [2**j for j in range(1,l+1)]

    X = [ pointdistri(n) for n in N]

    X2 = [(Intervallstart)+(2*(-Intervallstart)/p)*i for i in range(0,p+1)]

    fY2 = [f(x) for x in X2]

    """these are the evaluations of the polynomials"""
    PolysY2 = [evaluationPointsPn(f,X[n],X2) for n in range(0,len(N))]


    """plotting"""
    plt.plot(X2, fY2, label='f(x)')


    for i in range(0,len(PolysY2)):

        plt.plot(X2, PolysY2[i], label=f'Poly N={N[i]}')

    plt.title('Function and Neville Polynomial Approximations')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":

  compute2(lambda x: math.e**-x**2,equidist,5,500)

  """the runge phenomena seems to have imporoved"""
