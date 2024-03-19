from week4.ex3_a import AcomputeDiffOp,BcomputeDiffOp,CcomputeDiffOp
from matplotlib import pyplot as plt

def DiffOpsA(f:callable,x0:float,h:float):
    fiA = [f(x0-2*h+j*h) for j in range(0,3)]
    return AcomputeDiffOp(fiA,h)

def DiffOpsB(f:callable,x0:float,h:float):
    fiB = [f(x0-h + j*h) for j in range(0,4)]
    return BcomputeDiffOp(fiB,h)

def DiffOpsC(f:callable,x0:float,h:float):
    fiC = [f(x0-h + j*h) for j in range(0,2)]
    return CcomputeDiffOp(fiC,h)

"""we write this do reuse in next sub exercise"""
def computeValue(f:callable,h:float,x0:float,do:callable)->float:
    """
    do is the difference operator
    """
    return do(f,x0,h)


def computeValuesABC(f:callable,h:float,x0:float)->list:
    """
    @f function whose derivative to approximate
    @h increment of point districution
    @x0 point at which to approximate
    @returns tupel with the values for diff operator A,B,C
    """

    return computeValue(f,h,x0,DiffOpsA),computeValue(f,h,x0,DiffOpsB),computeValue(f,h,x0,DiffOpsC)

def computeErrors(f:callable,h:float,x0:float,d:callable)->list:
    """
    @f function whose derivative to approximate
    @h increment of point districution
    @x0 point at which to approximate
    @d is the derivative of f
    @returns tupel with the Errors for diff operator A,B,C
    """
    Value = computeValuesABC(f,h,x0)

    Errors = [abs(V - d(x0)) for V in Value]

    return Errors



def plotErrors(xValues:list,yValues :list)->None:
    """
    @values tupesl (error,h) which will be plotted
    """
    assert len(xValues)==len(yValues)

    plt.plot(xValues,yValues,label="Error with repsect to h")
    plt.title('Error of difference operator')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def SolveTask()->None:
    x0 = 10
    H = [2**(-n) for n in range(0,11)]
    f = lambda x : 1/(0.4*x)
    d = lambda x : (-1)/(0.4*x**2)

    """your values as triplets 0 is a, 1 is b, 2 is c
        where a,b,c are the respective diff operators"""
    Values = [computeValuesABC(f,h,x0) for h in H]

    Errors = [computeErrors(f,h,x0,d) for h in H]

    yErrorsA = [Err[0] for Err in Errors]
    yErrorsB = [Err[1] for Err in Errors]
    yErrorsC = [Err[2] for Err in Errors]

    plotErrors(H,yErrorsA)
    plotErrors(H,yErrorsB)
    plotErrors(H,yErrorsC)




if __name__ == "__main__":
    SolveTask()