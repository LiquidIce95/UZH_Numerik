from matplotlib import pyplot as plt
from Ex2_a import neville
import math

if __name__ == "__main__":
    
    """ IMPORTANT: we only go to 2**4 because otherwise it takes too long"""
    N = [2**j for j in range(1,4)]

    X = [[(-5)+(10/n)*i for i in range(0,n+1)] for n in N]
    Y = [[math.cos(x) for x in X[n]] for n in range(0,len(X))]

    
    X2 = [(-5)+(10/500)*i for i in range(0,500+1)]

    fY2 = [math.cos(x) for x in X2]

    """neville(X[n],Y[n],x) are the polynomials P_n"""
    PolysY2 = [[neville(X[n],Y[n],x) for x in X2] for n in range(0,len(N))]


    Errors = [max([abs(fY2[j] - PolysY2[n][j]) for j in range(0,len(fY2))]) for n in range(0,len(PolysY2))]

    print(Errors)

    # Plotting
    # plt.figure(figsize=(10, 6))
    plt.plot(X2, fY2, label='cos(x)')


    for i in range(0,len(PolysY2)):

        plt.plot(X2, PolysY2[i], label=f'Poly N={N[i]}')

    plt.title('Cosine Function and Neville Polynomial Approximations')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()



    """observations:
        with increasing degree the polynomials get more precise, which can be
        observed with the errros"""
