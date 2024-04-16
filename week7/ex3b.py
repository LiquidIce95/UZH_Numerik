from week7.ex3a import node3GausQuad

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

def compositeNode3GaussQuad(f:callable,L:float,R:float,n:int)->float:
    """
    @f function whose integral is approximated
    @L left edge of intervall
    @R right edge of intervall
    @n number of subintervalls
    @returns the approximated integral
    """

    Points = equidistantPoints(L,R,n)

    Integrals = [node3GausQuad(f,Points[j],Points[j+1]) for j in range(n)]

    return sum(Integrals)  

if __name__ == "__main__":
  pass