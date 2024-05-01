"""week9 being week of submission"""
from week9.ex2_a import *



def decomposeQRHouseHolder(A:np.ndarray)->Union[np.ndarray,np.ndarray]:
    """
    @A the matrix to decompose
    @returns the Q,R matricies of QR decomposition
    """
    m, n = A.shape
    Q:np.ndarray = np.eye(m) 
    R:np.ndarray = A.copy()

    for j in range(m):
        x = R[j:, j].copy()
        norm = np.linalg.norm(x)
        rho = -np.sign(x[0])
        u=x.copy()
        u[0]=u[0] - rho * norm
        beta=2/np.linalg.norm(u)**2

        R[j:, :] = R[j:, :] - beta * np.outer(u, u).dot(R[j:, :])
        Q[:, j:] = Q[:, j:] - beta * Q[:, j:].dot(np.outer(u, u))
        
        for indx in range(j+1,m+1):
            R[indx:, j]=0
        
    return Q, R
  



  

if __name__ == "__ma)in__":
  pass