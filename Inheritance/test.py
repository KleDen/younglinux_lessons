import unittest

from Classes import Hero, Solder


class TestHeroArgs(unittest.TestCase):
    def test_correct_values(self):
        Bob = Hero()
        Bob.lvlup(4)
        self.assertEqual(Bob.lvl, 5)

    def test_incorrect_values(self):
        Bob = Hero()
        self.assertRaises(TypeError, Bob.lvlup, 'foo')
        self.assertRaises(TypeError, Bob.lvlup, 1.3)
        self.assertRaises(ValueError, Bob.lvlup, -1)

class TestSolderClass(unittest.TestCase):
    def test_follow_method(self):
        Bob = Hero()
        Mark = Solder()
        self.assertEqual(Mark.follow(Bob), "Иду за героем из команды Unnamed")



if __name__ == '__main__':
    unittest.main()
