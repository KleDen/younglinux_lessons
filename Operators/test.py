import unittest
from Сlass_snow import Snow

class TestSetterGetter(unittest.TestCase):
    def test_set_get(self):
        testsnow = Snow(5)
        testsnow.set_snowflake(10)
        self.assertEqual(testsnow.get_snowflake(), 10)


class TestOverloadingOperators(unittest.TestCase):
    def setUp(self) -> None:
        self.test_snow0 = Snow(5)
        self.test_snow1 = Snow(4)

    def test_add(self):
        self.test_snow0 + self.test_snow1
        self.assertEqual(self.test_snow0.get_snowflake(), 9)
        self.test_snow0 + 1
        self.assertEqual(self.test_snow0.get_snowflake(), 10)


    def test_sub(self):
        self.test_snow0 - self.test_snow1
        self.assertEqual(self.test_snow0.get_snowflake(), 1)
        self.test_snow0 - 1
        self.assertEqual(self.test_snow0.get_snowflake(), 0)


    def test_mul(self):
        self.test_snow0 * 3
        self.assertEqual(self.test_snow0.get_snowflake(), 15)

    #def test_truediv
# TODO TESTS

if __name__ == '__main__':
    unittest.main()
