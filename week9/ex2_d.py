from week9.ex2_c import *
    
    

def solveQRHouseHolder(A,y):
    """
    # Solve the system with QR decomposition
    @param A square matrix that defines the equation.
    @param y right-hand side of the equation.
    @return the solution of the equation.
    """
    Q,R = decomposeQRHouseHolder(np.copy(A))
    # y = Ax = QRx; hence we solve the system Rx = Q^-T y=:b

    b:np.ndarray= np.dot(y,Q.transpose())
    
    x=solveUpperTriangularSystem(R,b)
    
    return x

def solveQR(A,y):
    """
    # Solve the system with QR decomposition
    @param A square matrix that defines the equation.
    @param y right-hand side of the equation.
    @return the solution of the equation.
    """
    Q,R = computeQRmatrices(np.copy(A))
    # y = Ax = QRx; hence we solve the system Rx = Q^-T y=:b
    
    b:np.ndarray= np.dot(y,Q.transpose())
    
    x=solveUpperTriangularSystem(R,b)
    
    return x


if __name__ == "__ma)in__":
  pass