# almost_equal
def almost_equal(a, b, eps) -> bool:
    """
    Perform equality for two floating numbers
    
    Args:
    ----------
    a: float
        The first floating number
    b: float
        The second floating number
    eps: float
        Comparison tolerance
        
    Return:
    ----------
    Return true if the absolute difference between a and b
    is smaller than or equal to eps, else, return False
    For example:
    1. almost_equal(1, 1.001, 0.001) --> True
    2. almost_equal(1, 1.001, 0.0001) --> False
    """
    
    abs_diff = abs(a-b)
    if abs_diff <= eps:
        return True
    else:
        return False
    