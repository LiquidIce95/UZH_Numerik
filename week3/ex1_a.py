from week2.Ex2_a import nevilleDP

"""nevilleDP is the neville algorithm"""
def evaluationPointsPn(f:callable, nodalPoints : list,evalPoints:list)->list:
  """ 
    We solve the problem foreach intervall, where we interpolate the endpoints 
    and the mitdpoint, which do the evaluation with the neville algorithm
    ASSUPTION: at least two nodal points
  """
  nodalPoints.sort()
  evalPoints.sort()
  def midpoint(a,b):return (a+b)/2

  m = len(nodalPoints)-1

  """this selection of points ensures that the degree is 2 of each spline polynomial ( because there are 3 algebraic points foreach intervall)"""
  interpolationPoints = [[nodalPoints[j],midpoint(nodalPoints[j],nodalPoints[j+1]),nodalPoints[j+1]] for j in range(0,m)]

  """foreach spline polynomial we create a list with the evaluations of f for its intervall points"""
  evalOfFunction = [[f(x) for x in X] for X in interpolationPoints]


  """forach  spline polynomial we make a list with all the points it has to evaluate ( those in its intervall)"""
  EvalPointsOfIntervalls = [[ep for ep in evalPoints if nodalPoints[j] <= ep <nodalPoints[j+1]] for j in range(0,m)]

  """need to account for the last point"""
  EvalPointsOfIntervalls[-1] += [ep for ep in evalPoints if ep == nodalPoints[-1]]

  assert len(evalOfFunction)==len(interpolationPoints)==len(EvalPointsOfIntervalls)

  """we use neville Algorithm to compute the evaluations"""
  """foreach spline polynomial, evaluate all points in its intervall"""
  evaluationsPn = [nevilleDP(interpolationPoints[j],evalOfFunction[j],x)  for j in range(0,m) for x in EvalPointsOfIntervalls[j]]  

  assert len(evaluationsPn)==len(evalPoints)

  return evaluationsPn


if __name__ == "__main__":
  pass