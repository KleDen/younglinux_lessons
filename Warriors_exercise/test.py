import unittest

from definitions import Warrior



# проверить что жив/не жив. Проверить разное начальное здоровье.
# Попытка нанесения отрицательного урона должна бросать ValueError.
# Проверить, что воин мёртв и при отрицательном здоровье, и при нуле.
class TestWarrior(unittest.TestCase):
    def setUp(self) -> None:
        self.bob = Warrior("Bob", 99, 10)

    def test_create_unit(self):
        self.assertEqual(self.bob.name, "Bob")

    def test_get_damaged(self):
        self.bob.get_damaged(9)
        self.assertEqual(self.bob.hp, 90)
        self.bob.get_damaged(90)
        self.assertEqual(self.bob.hp, 0)

    def test_negative_damage(self):
        self.assertRaises(ValueError, self.bob.get_damaged, -5)
        self.assertRaises(ValueError, self.bob.get_damaged, -111)

    def test_is_alive(self):
        self.assertTrue(self.bob.is_alive)



if __name__ == '__main__':
    unittest.main()
