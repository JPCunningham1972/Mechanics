from geom2d.point import Point
from geom2d.vectors import make_vector_between, make_versor_between
from geom2d import tparam

class Segment:
    """
    Segment is a 2D segment defined by its start and end point
    """
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    @property
    def direction_vector(self):
        """
         Creates a Vector from Segement:this
        :return:Vector
        """
        return make_vector_between(self.start, self.end)

    @property
    def direction_versor(self):
        """
        Creates unit vector from Segment:this
        :return: Vector unit vector constructed from a Segment object
        """
        return make_versor_between(self.start, self.end)

    @property
    def normal_versor(self):
        """
        Creates a Vector normal to Vector:this
        :return: Vector normal vector constructed from a Segment object
        """
        return self.direction_versor.perpendicular()

    @property
    def length(self):
        """
        Calculates the Euclidean distance from start to end of Segment:this
        :return: float - sqrt(start**2 + end**2)
        """
        return self.start.distance_to(self.end)

    @property
    def middle(self):
        """
        Create a Point which is the mid point of Segment:this
        :return: Point - from midpoint formula
        """
        return self.point_at(tparam.MIDDLE)

    def point_at(self, t: float):
        """
        Creates a Point at t * displacment
        :param t: float (0 <= t <= 1)
        :return: Point - from start to t * displacment
        """
        tparam.ensure_valid(t)
        return self.start.displaced(self.direction_vector, t)

    def closet_point_to(self, p: Point):
        """
        Calculates the nearest Point on Segment:this and create a Point
        :param p: Point
        :return: Point - nearest Point on Segment:this and a Point
        """
        v = make_vector_between(self.start, p)
        d = self.direction_versor
        vs = v.projection_over(d)

        if vs < 0:
            return self.start

        if vs > self.length:
            return self.end

        return self.start.displaced(d, vs)

    def distance_to(self, p: Point):
        """
        Calculates the Euclidean distance from closet point to p on Segment:this
        and Point p
        :param p: Point - point not on segment
        :return: float - Euclidean Distance
        """
        return p.distance_to(self.closet_point_to(p))

    def intersection_with(self, other):
        d1, d2 = self.direction_vector, other.direction_vector

        if d1.is_parallel_to(d2):
            return None

        cross_prod = d1.cross(d2)
        delta = other.start - self.start
        t1 = (delta.u * d2.v - delta.v * d2.u) / cross_prod
        t2 = (delta.u * d1.v - delta.v * d1.u) / cross_prod

        if tparam.is_valid(t1) and tparam.is_valid(t2):
            return self.point_at(t1)

        else:
            return None

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Segment):
            return False
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return f'segment {self.start} to] {self.end}'
