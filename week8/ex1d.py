from week8.ex1b import *

def generateSomeResults(args:newtonMethodArgument,start:float,end:float):
  x0List = np.arange(start,end)

  argList = [newtonMethodArgument(args.f,args.df,x0,args.epsilon,args.maxiter) for x0 in x0List]

  results = [(newtonMethod(arg),arg.x0) for arg in argList]

  return results





if __name__ == "__main__":
  arg : newtonMethodArgument = newtonMethodArgument(func,dfunc,1,10**(-10),150)

  res = generateSomeResults(arg,-100,100)

  for appr, x0 in res:
    print(appr,x0,"\n")

  """these tests suggest that for x <=0 it diverges and converges otherwise"""
