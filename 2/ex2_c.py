from ex2_b import compute,equidist
import math


if __name__ == "__main__":
    print(compute(lambda x: math.exp(-x**2),equidist,5,500))



    """observations / explanations
        We observe the runge phenomenon where the higher degree polynomial has a larger 
        error around the edges of the function, also that the error is not monotonically
        decreasing, even seems like the error could keep getting larger.
        But there is no contradiction because the n+1 derivative of e**(-x**2) is extremely sensitive
        with respect to the maximum norm, therefor these larger errors are expected
    """
