import unittest

import geom2d.nums as nums

class TestNums(unittest.TestCase):
    def test_are_close_enough(self):
        a = 1.23456789010
        b = 1.23456789011
        c = 1.23456789111
        self.assertTrue(nums.are_close_enough(a,b))
        self.assertFalse(nums.are_close_enough(a,c))

    def test_is_close_to_zero(self):
        a = 0.0000000000999
        b = 0.000000000111
        self.assertTrue(nums.is_close_to_zero(a))
        self.assertFalse(nums.is_close_to_zero(b))

    def test_is_close_to_one(self):
        a = 0.99999999999
        b = 1.09
        self.assertTrue(nums.is_close_to_one(a))
        self.assertFalse(nums.is_close_to_one(b))
