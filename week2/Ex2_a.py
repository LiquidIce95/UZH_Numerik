import numpy as np

def neville(x : list,y : list, xx:float):
    """
        naive implementation, very slow
        @params x the abscisses of f
        @params y the values of f
        @params xx is the evaluationpoint
    """
    assert len(x)==len(y)

    """x,y,xx are taken from context of neville function"""
    def nevilleRec(i,j):
        if i==j:
            return y[i]
        else:
            return ((xx-x[j])*nevilleRec(i,j-1)+ (x[i]-xx)*nevilleRec(i+1,j))/(x[i]-x[j])
        
    return nevilleRec(0,len(x)-1)

def nevilleDP(xi, yi, xx):
    """Algorithm with Dynamic programming, much faster"""
    n = len(xi)
    p = np.zeros((n, n))
    p[:, 0] = yi

    for j in range(1, n):
        for i in range(n - j):
            p[i, j] = ((xx - xi[i + j]) * p[i, j - 1] - (xx - xi[i]) * p[i + 1, j - 1]) / (xi[i] - xi[i + j])
    
    return p[0, n-1]

if __name__ == "__main__":
    x = [0,1,2,3,4,5,6,7]
    y = [y**2 for y in x]

    xx = 1/2

    print(neville(x,y,xx))