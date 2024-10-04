import unittest
import math

from geom2d.nums import are_close_enough
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

    def test_scaled_by(self):
        expected = Vector(2, 4)
        actual = self.u.scaled_by(2)
        self.assertEqual(expected, actual)

    def test_norm(self):
        expected = 2.23606797749979
        actual = self.u.norm
        self.assertAlmostEqual(expected, actual)

    def test_is_normal(self):
        w = Vector(1,1)
        self.assertFalse(self.u.is_normal)
        self.assertTrue(w)

    def test_sine(self):
        w =Vector(math.sqrt(3)/2, 1/2)
        expected = math.sin(math.pi / 6)
        actual = w.sine
        self.assertAlmostEqual(expected, actual)

    def test_cosine(self):
        w =Vector(math.sqrt(3)/2, 1/2)
        expected = math.cos(math.pi / 6)
        actual = w.cosine
        self.assertAlmostEqual(expected, actual)

    def test_normalize(self):
        norm = math.sqrt(self.v.u**2 + self.v.v**2)
        expected = Vector(self.v.u / norm, self.v.v / norm)
        actual = self.v.normalized()
        self.assertEqual(expected, actual)