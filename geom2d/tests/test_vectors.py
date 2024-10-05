import unittest
from math import expm1

from geom2d.vector import Vector
from geom2d.point import Point
import geom2d.vectors as vectors

class TestVectors(unittest.TestCase):
    def test_make_vector_between(self):
        p = Point(1,1)
        q = Point(4,4)
        expected = Vector(3,3)
        actual = vectors.make_vector_between(p,q)
        self.assertEqual(expected, actual)

    def test_make_versor(self):
        x = 3
        y = 4
        expected = Vector(0.6, 0.8)
        actual = vectors.make_versor(x,y)
        self.assertEqual(expected, actual)

    def test_make_versor_between(self):
        p = Point(1, 1)
        q = Point(4, 4)
        expected = Vector(0.7071067811865476, 0.7071067811865476)
        actual = vectors.make_versor_between(p,q)
        self.assertEqual(expected, actual)