import unittest

from geom2d.point import Point
from geom2d.vector import Vector

class TestPoint(unittest.TestCase):
    p = Point(1, 2)
    q = Point(4, 6)
    u = Vector(2, 4)

    def test_distance_to(self):
        expected = 5
        actual = self.p.distance_to(self.q)
        self.assertAlmostEqual(expected, actual)

    def test_plus(self):
        expected = Point(5, 8)
        actual = self.p + self.q
        self.assertEqual(expected, actual)

    def test_minus(self):
        expected = Vector(-3, -4)
        actual = self.p - self.q
        self.assertEqual(expected, actual)

    def test_displaced(self):
        times = 2
        expected = Point(5, 10)
        actual = self.p.displaced(self.u, times)
        self.assertEqual(expected, actual)

    def test_equal(self):
        self.assertTrue(self.p == self.p)
