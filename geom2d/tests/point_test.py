import unittest

from geom2d.point import Point
from geom2d.vector import Vector

class TestPoint(unittest.TestCase):

    def test_distance_to(self):
        p = Point(1, 1)
        q = Point(3,4)
        expected = 3.605551275463989
        actual = p.distance_to(q)
        self.assertAlmostEqual(expected, actual)

    def test_plus(self):
        p = Point(1, 1)
        q = Point(3, 4)
        expected = Point(4, 5)
        actual = p + q
        self.assertEqual(expected, actual)

    def test_minus(self):
        p = Point(1, 1)
        q = Point(3, 4)
        expected = Vector(-2, -3)
        actual = p - q
        self.assertEqual(expected, actual)

    def test_displaced(self):
        times = 2
        v = Vector(2, 2)
        p = Point(1,1)
        expected = Point(5, 5)
        actual = p.displaced(v, times)
        self.assertEqual(expected, actual)

    def test_equal(self):
        p = Point(1,1)
        q = Point(1,1)
        r = "the"
        s = Point(2,2)
        self.assertTrue(p == p)
        self.assertFalse(p == r)
        self.assertTrue(p == q)
        self.assertFalse(p == s)
