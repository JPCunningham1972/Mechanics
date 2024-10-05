from geom2d.point import Point
from geom2d.vector import Vector

def make_vector_between(p:Point, q: Point):
    """
    Creates a Vector from Point:p and Point:q
    :param p: Point
    :param q: Point
    :return: Vector q - p
    """
    return q - p

def make_versor(u: float, v:float):
    """
    Creates a unit vector from two floats
    :param u: float
    :param v: float
    :return: Vector - Unit Vector
    """
    return Vector(u, v).normalized()

def make_versor_between(p:Point, q: Point):
    """
    Creates a unit vector from Point:p and Point:q
    :param p: Point
    :param q: Point
    :return: Vector - Unit Vector
    """
    return make_vector_between(p, q).normalized()