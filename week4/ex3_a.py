
def AcomputeDiffOp(fi:list,h:float)->float:
    """
        computes the difference operator a at x0
        @fi the list of function values 
        @h the distance for the equispaced points
        @x0 the point to evaluate the operator at
        assuming fi[0] = f_-2 in this case
    """
    assert len(fi)==3

    return (fi[0]-4*fi[1]+3*fi[2])/(2*h)

def BcomputeDiffOp(fi:list,h:float)->float:
    """
        computes the difference operator a at x0
        @fi the list of function values 
        @h the distance for the equispaced points
        @x0 the point to evaluate the operator at
        assuming fi[0] = f_-1 in this case
    """
    assert len(fi)==4

    return (-2*fi[0]-3*fi[1]+6*fi[2]-fi[3])/(6*h)

def CcomputeDiffOp(fi:list,h:float)->float:
    """
        computes the difference operator a at x0
        @fi the list of function values 
        @h the distance for the equispaced points
        @x0 the point to evaluate the operator at
        assuming fi[0] = f_-1 in this case
    """
    assert len(fi)==3

    return (-fi[0]-2*fi[1]+fi[2])/(h**2)



if __name__ == "__main__":
    pass