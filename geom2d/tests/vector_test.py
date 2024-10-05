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
        w =Vector(3,4)
        expected = 0.8
        actual = w.sine
        self.assertAlmostEqual(expected, actual)

    def test_cosine(self):
        w =Vector(3,4)
        expected = 0.6
        actual = w.cosine
        self.assertAlmostEqual(expected, actual)

    def test_normalize(self):
        w = Vector(3,4)
        expected = Vector(0.6, 0.8)
        actual = w.normalized()
        self.assertEqual(expected, actual)

    def test_with_length(self):
        w = Vector(3,4)
        expected = Vector(1.2, 1.6)
        actual = w.with_length(2)
        self.assertEqual(expected, actual)

    def test_dot_product(self):
        expected = 16
        actual = self.u.dot(self.v)
        self.assertEqual(expected, actual)

    def test_projection_over(self):
        expected =  2.2188007849009166
        actual = self.u.projection_over(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_cross(self):
        expected = -2
        actual = self.u.cross(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_is_perpendicular_to(self):
        w = Vector(-2, 1)
        self.assertTrue(self.u.is_perpendicular_to(w))

    def test_not_perpendicular_to(self):
        self.assertFalse(self.u.is_perpendicular_to(self.v))

    def test_is_parallel_to(self):
        self.assertTrue(self.u.is_parallel_to(self.u))

    def test_not_parallel_to(self):
        self.assertFalse(self.u.is_parallel_to(self.v))

    def test_angle_value_to(self):
        w = Vector(1,1)
        x = Vector(1, 0)
        expected = math.pi / 4
        actual = w.angle_value_to(x)
        self.assertAlmostEqual(expected, actual)

    def test_angle_to(self):
        w = Vector(1, 1)
        x = Vector(1, 0)
        expected = math.pi / 4
        actual = x.angle_to(w)
        self.assertAlmostEqual(expected, actual)

    def test_rotated_radians(self):
        w = Vector(1,0)
        radian = math.pi / 4
        expected = Vector(1/math.sqrt(2), 1/math.sqrt(2))
        actual = w.rotated_radians(radian)
        self.assertAlmostEqual(expected, actual)

    def test_perpendicular(self):
        w = Vector(1,1)
        expected = Vector(-1,1)
        actual = w.perpendicular()
        self.assertAlmostEqual(expected, actual)

    def test_opposite(self):
        w = Vector(1,1)
        expected = Vector(-1,-1)
        actual = w.opposite()
        self.assertAlmostEqual(expected, actual)

    def test_equality(self):
        p = Vector(1, 1)
        q = Vector(1, 1)
        r = "the"
        s = Vector(2, 2)
        self.assertTrue(p == p)
        self.assertFalse(p == r)
        self.assertTrue(p == q)
        self.assertFalse(p == s)
