from matplotlib import pyplot as plt
from Ex2_a import neville,nevilleDP
import math

def equidist(n:int)->list:
    return [(-5)+(10/n)*i for i in range(0,n+1)]

def compute(f :callable,pointdistri:callable,l:int,p:int)->list:
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
    Y = [[f(x) for x in X[n]] for n in range(0,len(X))]

    """these are the polynomials"""
    Polys = [lambda x, j=j : nevilleDP(X[j],Y[j],x) for j in range(len(X))]

    X2 = [(-5)+(10/p)*i for i in range(0,p+1)]

    fY2 = [f(x) for x in X2]

    """these are the evaluations of the polynomials"""
    PolysY2 = [[Polys[n](x) for x in X2] for n in range(0,len(N))]


    Errors = [max([abs(fY2[j] - PolysY2[n][j]) for j in range(0,len(fY2))]) for n in range(0,len(PolysY2))]

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

    return Errors

if __name__ == "__main__":
    print(compute(math.cos,equidist,5,500))
    



    """observations:
        with increasing degree the polynomials get more precise, which can be
        observed with the errros"""
