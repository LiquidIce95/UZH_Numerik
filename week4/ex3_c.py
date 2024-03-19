from week4.ex3_b import computeValue,computeError,plotErrors

def simpleForward(f:callable,x0:float,h:float)->float:
  """
  @f is the functions whose derivative we approximate
  @h is the distance increment for the points
  @x0 is the point at which we want to differentiate
  @returns the value of simple Forward diff operator
  """

  xi = [x0+j*h for j in range(0,2)]
  return (f(xi[1])-f(xi[0]))/h


def SolveTask()->None:
    x0 = 10
    H = [2**(-n) for n in range(0,61)]
    f = lambda x : 1/(0.4*x)
    d = lambda x : (-1)/(0.4*x**2)

    """your values as triplets 0 is a, 1 is b, 2 is c
        where a,b,c are the respective diff operators"""
    ValuesS = [computeValue(f,h,x0,simpleForward) for h in H]

    yErrorsS = [computeError(f,h,x0,d,simpleForward) for h in H]


    plotErrors(H,yErrorsS)

if __name__ == "__main__":
  SolveTask()
  """up to a certain point everything is fine, but then f1/h and f0/h get very 
  large (because h gets very small) so we are subtracting large numbers which are 
  almost equal, which causes significant arithmetic errors."""