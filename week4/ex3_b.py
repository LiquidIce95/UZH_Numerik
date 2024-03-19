from week4.ex3_a import AcomputeDiffOp,BcomputeDiffOp,CcomputeDiffOp
from matplotlib import pyplot as plt

def computeValues(f:callable,h:float,x0:float)->list:
    """
    @f function whose derivative to approximate
    @h increment of point districution
    @x0 point at which to approximate
    @returns tupel with the values for diff operator A,B,C
    """

    fiA = [f(x0-2*h+j*h) for j in range(0,3)]
    AValue = AcomputeDiffOp(fiA,h)

    fiB = [f(x0-h + j*h) for j in range(0,4)]
    BValue = BcomputeDiffOp(fiB,h)

    fiC = [f(x0-h + j*h) for j in range(0,2)]
    CVAlue = CcomputeDiffOp(fiC,h)

    return AValue,BValue,CVAlue

def computeErrors(f:callable,h:float,x0:float,d:callable)->list:
    """
    @f function whose derivative to approximate
    @h increment of point districution
    @x0 point at which to approximate
    @d is the derivative of f
    @returns tupel with the Errors for diff operator A,B,C
    """
    Value = computeValues(f,h,x0)

    Errors = [abs(V - d(x0)) for V in Value]

    return Errors



def plotErrors(values :list)->None:
    """
    @values tupesl (error,h) which will be plotted
    """
    yValues = [val[0] for val in values]
    xValues = [val[1] for val in values]
    


if __name__ == "__main__":
    pass