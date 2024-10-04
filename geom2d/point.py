import math

from geom2d.nums import are_close_enough
from geom2d.vector import Vector
from geom2d import nums

class Point:
    """
    Class creates points in 2D plane defined by its coordinates "x" and "y".
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        """
        Computes the Euclidean distance between this point and another Point.
        :param other: Point
        :return: float distance between this and other
        """
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.sqrt(delta_x**2 + delta_y**2)

    def __add__(self, other):
        """
        Creates a Point result of adding "this" and "other" points together.
        :param other: Point
        :return: Point -> this + other
        """
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        """
        Creates a Point result of subtracting "this" and "other" points together.
        :param other: Point
        :return: Vector -> this - other
        """
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def displaced(self, vector: Vector, times=1):
        """
        Creates a Point displaced by a Vector scaled by 'times'
        :param vector: Vector
        :param times: int -> scaled by
        :return: Point -> Point + times * Vector
        """
        scaled_vec = vector.scaled_by(times)
        return Point(
            self.x + scaled_vec.u,
            self.y + scaled_vec.v
        )

    def __eq__(self, other):
        """
        Tests whether two Point objects are equal.
        :param other: Point object
        :return: Boolean -> this == other if both this and other are Point objects
        """
        if self is other:
            return True

        if not isinstance(other, Point):
            return False

        return (nums.are_close_enough(self.x, other.x) and nums.are_close_enough(self.y, other.y))

    def __str__(self):
        """
        Create a string representation of this Point.
        :return: string -> "(x, y)
        """
        return f'({self.x}, {self.y})'