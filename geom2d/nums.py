import math
"""
Package to determine relative equality of floats
"""

def are_close_enough(a, b, tolerance = 1e-10):
    """
    Test whether two floats "a" amd "b" are comparatively close to
    each other with respect to the given tolerance.

    :param a: float
    :param b: float
    :param tolerance: float default 1e-10
    :return: Boolean are as close to each other.
    """
    return math.fabs(a-b) < tolerance

def is_close_to_zero(a, tolerance = 1e-10):
    """
    Test whether float "a" is comparatively close to zero with respect to
    a given tolerance.

    :param a: float
    :param tolerance: float default 1e-10
    :return: Boolean "a" is close to zero
    """
    return are_close_enough(a, 0.0, tolerance)

def is_close_to_one(a, tolerance = 1e-10):
    """
    Test whether float "a" is comparatively close to one with respect to
    a given tolerance.

    :param a:float
    :param tolerance:float default 1e-10
    :return: Boolean "a" is close to one
    """
    return are_close_enough(a, 1.0, tolerance)