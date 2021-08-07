import unittest
from definitions import Triangle


class TestHidenAttr(unittest.TestCase):
    def test_private_attribute(self):
        test_triangle = Triangle(1, 10)
        with self.assertRaises(AttributeError):
            test_triangle.width
        with self.assertRaises(AttributeError):
            test_triangle.height



if __name__ == '__main__':
    unittest.main()
