from week5.ex2_b import *
from math import e

def equidistantPoints(a:float,b:float,n:int)->list:
    """
    @a left edge of intervall
    @b right edge of intervall
    @n number of subintervalls
    @returns the equidistant points which make the subintervalls

    """
    points = [a]
    h = (b-a)/n
    for j in range(1,n+1):
        points.append(points[j-1]+h)

    return points

def midpoint_composite(f:callable,L:float,R:float,n:int)->float:
    """
    @f function whose integral is approximated
    @L left edge of intervall
    @R right edge of intervall
    @n number of subintervalls
    @returns the approximated integral
    """

    Points = equidistantPoints(L,R,n)

    Integrals = [midpoint_rule(f,Points[j],Points[j+1]) for j in range(n)]

    return sum(Integrals)


def trapezoidal_composite(f:callable,L:float,R:float,n:int)->float:
    """
    @f function whose integral is approximated
    @L left edge of intervall
    @R right edge of intervall
    @n number of subintervalls
    @returns the approximated integral
    """

    Points = equidistantPoints(L,R,n)

    Integrals = [trapezoidal_method(f,Points[j],Points[j+1]) for j in range(n)]

    return sum(Integrals)

def simpsons_composite(f:callable,L:float,R:float,n:int)->float:
    """
    @f function whose integral is approximated
    @L left edge of intervall
    @R right edge of intervall
    @n number of subintervalls
    @returns the approximated integral
    """

    Points = equidistantPoints(L,R,n)

    Integrals = [trapezoidal_method(f,Points[j],Points[j+1]) for j in range(n)]

    return sum(Integrals)


if __name__ == "__main__":
    f = lambda x : e**x
    a,b = 0,1
    n = 100
    I = e-1

    ErrorMidpoint = abs(I-midpoint_composite(f,a,b,n))
    ErrorTrapezoidal = abs(I-trapezoidal_composite(f,a,b,n))
    ErrorSimpsons = abs(I-simpsons_composite(f,a,b,n))

    print(ErrorMidpoint,ErrorSimpsons,ErrorSimpsons)

    """
    Error of midpoint is smallest, since e**x-1 on subintervalls is close to x
    which can be best approximated with midoint (area of triangle)
    Errors of Trapezoidal and Simposons are equal
    """