from typing import Union
import numpy as np
from copy import deepcopy

def computeProjection(u:np.ndarray,v:np.ndarray)->np.ndarray:
  """
  @v is a vector
  @u is a vector
  returns the projection described here : https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process
  """
  nominator : float = np.dot(v,u)
  denominator : float = np.dot(u,u)
  factor : float = nominator/denominator

  cu : np.ndarray = deepcopy(u)

  return factor* u


def GramSchmidtOrthogonalizing(A:np.ndarray)->np.ndarray:
  """
  @A the matrix whose columns should be orthogonalized
  returns the orthogonalized matrix formed from A
  """
  A = deepcopy(A)

  m,n = A.shape

  for j in range(1,n):
    projections :list = [computeProjection(A[:,k],A[:,j]) for k in range(0,j)]
    sumProjections :float = sum(projections)
    A[:,j] -= sumProjections


  return A


def computeQRmatrices(A:np.ndarray)->Union[np.ndarray,np.ndarray]:
  Q:np.ndarray = GramSchmidtOrthogonalizing(A)
  R:np.ndarray = np.dot(np.transpose(Q),A)

  return Q,R