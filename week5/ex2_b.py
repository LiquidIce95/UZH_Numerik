
def midpoint_rule(f:callable,a:float,b:float)->float:
    """
    @f is the function whose integral is approximated
    @a is left edge of intervall
    @b is right edge of intervall
    @returns an approximation of an integral
    """
    return (b-a)*f((a+b)/2)


def trapezoidal_method(f:callable,a:float,b:float)->float:
    """
    @f is the function whose integral is approximated
    @a is an extremum of f
    @b is an extremum of f
    @returns an approximation of an integral
    """
    return (b-a)*(f(a)+f(b))/2
    

def simpsons_method(f:callable,a:float,b:float)->float:
    """
    @f is the function whose integral is approximated
    @a is an extremum of f
    @b is an extremum of f
    @returns an approximation of an integral
    """
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6
    


if __name__ == "__main__":
    pass