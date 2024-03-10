from matplotlib import pyplot as plt
from ex2_b import equidist
import numpy as np
import math


def w(n:int,x:float,X:list)->float:
    prev = (x-X[0])
    for j in range(1,n+1):
        prev *= (x-X[j])
    return prev

def chebishevPoints(n:int)->list:
    return [(-5)*math.cos((2*i+1)*math.pi/(2*(n+1))) for i in range(0,n+1)]




if __name__ == "__main__":

    X = chebishevPoints(10)
    X2 = equidist(10)

    X_eval = list(np.random.uniform(-5, 5, 100))
    X_eval.sort()

    """only 2 possible sets which are not 0 given the information
        from the exercise"""
    Y = [w(10,x,X) for x in X_eval]
    Y2 = [w(10,x,X2) for x in X_eval]

    plt.plot(X_eval,Y,label="chebishew")
    plt.plot(X_eval,Y2,label="equidistant")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()