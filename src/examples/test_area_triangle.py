import unittest
import numpy as np
import area_triangle as trA

class test_area_triangle(unittest.TestCase):
    def test_area_tr(self):
        """"Test the area values against a reference for b >= 0 and h >= 0."""
        self.assertEqual(trA.area_tr(10,12),60)
        self.assertEqual(trA.area_tr(8,6),24)
        self.assertEqual(trA.area_tr(8,3),12)
        self.assertNotEqual(trA.area_tr(3,3),10)


    def test_values(self):
        """Make sure value errors are not negative"""
        self.assertRaises(ValueError,trA.area_tr,-5,-1)
