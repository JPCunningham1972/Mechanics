import unittest
import math

from geom2d.vector import Vector

class TestVector(unittest.TestCase):
    u = Vector(1,2)
    v = Vector(4, 6)

    def test_plus(self):
        expected = Vector(5,8)
        actual = self.u + self.v
        self.assertEqual(expected,actual)

    def test_minus(self):
        expected = Vector(-3, -4)
        actual = self.u - self.v
        self.assertEqual(expected, actual)

    def test_norm(self):
        expected = 2.23606797749979
        actual = self.u.norm
        self.assertAlmostEqual(expected, actual)

    def test_is_normal(self):
        self.assertFalse(self.u.is_normal)

