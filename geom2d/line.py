from geom2d.point import Point
from geom2d.vector import Vector

class Line:
    def __init__(self, base: Point, direction: Vector):
        self.base = base
        self.direction = direction

    