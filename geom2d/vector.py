import math

from geom2d import nums

class Vector:
    """
    Vector is a 2D vector defined by its components (u, v)
    """
    def __init__(self,u, v):
        self.u = u
        self.v = v

    def __add__(self, other):
        """
        Creates a vector result of adding Vector:this to Vector:other
        :param other: Vector
        :return: Vector - <this.u + other.u, this.v + other.v>
        """
        return Vector(
            self.u + other.u,
            self.v + other.v
        )
    def __sub__(self, other):
        """
        Creates a vector result of subtracting Vector:this to Vector:other
        :param other: Vector
        :return: Vector - <this.u - other.u, this.v - other.v>
        """
        return Vector(
            self.u - other.u,
            self.v - other.v
        )

    def scaled_by(self, factor):
        """
        Creates a vector result of scaling Vector:this to float:factor
        :param factor: float - scaling factor
        :return: Vector - factor * Vector:this
        """
        return Vector(factor * self.u, factor * self.v)

    @property
    def norm(self):
        """
        Computes the magnitude of the Vector:this
        :return: float - sqrt(this.u**2 + this.v**2)
        """
        return math.sqrt(self.u**2 + self.v**2)

    @property
    def is_normal(self):
        """
        Check to determine if Vector:this is a unit vector
        :return: Boolean - True if Vector:this normal is == 1
        """
        return nums.is_close_to_one(self.norm)

    @property
    def sine(self):
        """
        Calculates the sine of Vector:this
        :return: float  = this.v / norm(this)
        """
        return self.v / self.norm

    @property
    def cosine(self):
        """
        Calculates the cosine of Vector:this
        :return: float  = this.u / norm(this)
        """
        return self.u / self.norm

    def normalized(self):
        """
        Creates a unit vector of Vector:this
        :return: Vector - scaled_by(1.0 / norm(this)
        """
        return self.scaled_by(1.0 / self.norm)

    def with_length(self, length):
        """
        Creates a Vector scaled by float: length
        :param length: float - scaling factor
        :return: Vector - length * unitVector: this
        """
        return self.normalized().scaled_by(length)

    def dot(self, other):
        """
        Calculates the dot product of Vector: this and Vector:other
        :param other: Vector
        :return: float - (this.u * other.u) + (this.v * other.v)
        """
        return(self.u * other.u) + (self.v * other.v)

    def projection_over(self, direction):
        """
        Calculates the magnitude of the horizontal component of Vector:this
        over the norm of Vector:direction
        :param direction: Vector
        :return: float - (this.dot(direction)) / norm(direction)
        """
        return self.dot(direction.normalized())

    def cross(self, other):
        """
        Calculates the magnitude of the z component of resulting vector
        :param other: Vector
        :return: float - (this.u * other.v) - (this.v * other.u)
        """
        return (self.u * other.v) - (self.v * other.u)

    def is_parallel_to(self, other):
        """
        Check to determine if Vector:this is a parallel Vector:other
        :param other: Vector
        :return: Boolean - True if Vector:this is a parallel Vector:other
        """
        return nums.is_close_to_zero(self.cross(other))

    def is_perpendicular_to(self, other):
        """
        Check to determine if Vector:this is a perpendicular Vector:other
        :param other: Vector
        :return: Boolean - True if Vector:this is a perpendicular Vector:other
        """
        return nums.is_close_to_zero(self.dot(other))

    def angle_value_to(self, other):
        """
        Calculates the magnitude of the angle between Vector:this and Vector:other
        :param other: Vector
        :return: float  - angel in radians
        """
        dot_product = self.dot(other)
        norm_product = self.norm * other.norm
        return math.acos(dot_product / norm_product)

    def angle_to(self, other):
        """
        Calculates the angle between Vector:this and Vector:other with sign
        :param other: Vector
        :return: float - angle in radians
        """
        value = self.angle_value_to(other)
        cross_product = self.cross(other)
        return math.copysign(value, cross_product)

    def rotated_radians(self, radians):
        """
        Creates a Vector rotated by float: radians
        :param radians: float
        :return: Vector
        """
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            self.u * cos - self.v * sin,
            self.u * sin - self.v * cos
        )

    def perpendicular(self):
        """
        Creates a Vector perpendicular to Vector:this
        :return: Vector - (-this.v, this.u)
        """
        return Vector(-self.v, self.u)

    def opposite(self):
        """
        Creates a Vector opposite to Vector:this
        :return: Vector - (-this.u, -this.v)
        """
        return Vector(-self.u, -self.v)

    def __eq__(self, other):
        """
        Compares Vector:this to Vector:other for equality
        :param other: Vector
        :return: Boolean - True is Vector:this is Vector:other or if Vector:this is nearly equal to Vector:other
                           False otherwise
        """
        if self is other:
            return True

        if not isinstance(other, Vector):
            return  False

        return nums.are_close_enough(self.u, self.u) and \
            nums.are_close_enough(self.v, other.v)

    def __str__(self):
        return f'({self.u}, {self.v}) with norm {self.norm}'

