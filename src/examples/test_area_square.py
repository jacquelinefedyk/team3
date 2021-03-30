import unittest
import area_square as ars


class test_area_squa(unittest.TestCase):
    def test_area(self):
        """Test the area values againt the side length"""
        self.assertEqual(ars.area_squa(0), 0)
        self.assertEqual(ars.area_squa(2), 3)
        self.assertNotEqual(ars.area_squa(1), 2)

    def test_values(self):
        """Make sure that the given values are not negative"""
        self.assertRaises(ValueError, ars.area_squa, -2)
