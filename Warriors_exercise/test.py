import unittest

from definitions import Warrior


# Проверить, что воин мёртв и при отрицательном здоровье, и при нуле.
class TestWarrior(unittest.TestCase):

    def test_create_unit(self):
        self.bob = Warrior("Bob", 99, 10)
        self.assertEqual(self.bob.name, "Bob")

    def test_get_damaged(self):
        self.bob = Warrior("Bob")
        self.bob.get_damaged(9)
        self.assertEqual(self.bob.hp, 91)
        self.bob.get_damaged(90)
        self.assertEqual(self.bob.hp, 1)

    def test_negative_damage(self):
        self.bob = Warrior("Bob")
        self.assertRaises(ValueError, self.bob.get_damaged, -5)
        self.assertRaises(ValueError, self.bob.get_damaged, -111)

    def test_negative_hp(self):
        with self.assertRaises(ValueError):
            bob = Warrior("name", -9)
            bob = Warrior("name", 0)


    def test_is_dead(self):
        self.bob = Warrior("Bob", 100)
        self.assertTrue(self.bob.is_alive)
        self.mike = Warrior("Mike", 10)

        self.mike.get_damaged(20)
        self.bob.get_damaged(100)
        self.assertFalse(self.mike.is_alive())
        self.assertFalse(self.bob.is_alive())


if __name__ == '__main__':
    unittest.main()
