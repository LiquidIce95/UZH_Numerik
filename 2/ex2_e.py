from ex2_d import chebishevPoints,equidist,w
from ex2_b import compute
import math




if __name__ == "__main__":
    Errors1 = compute(lambda x : math.exp(-x**2),equidist,5,500)
    Errors2 = compute(lambda x : math.exp(-x**2),chebishevPoints,5,500)
    print([(Errors1[k],Errors2[k]) for k in range(0,len(Errors1))])
    
    """observations:
        at the lower degrees the change of point distribution 
        seems not to change much, but at the higher degrees
        the improvements are large
        """