import unittest

from definitions import Warrior, battle


class TestWarrior(unittest.TestCase):

    def test_create_unit(self):
        self.bob = Warrior("Bob", 99, 10)
        self.assertEqual(self.bob.name, "Bob")

    def test_get_damaged(self):
        self.bob = Warrior("Bob")
        self.bob.get_damaged(10)
        self.assertEqual(self.bob.get_hp(), 90)
        self.bob.get_damaged(90)
        self.assertEqual(self.bob.get_hp(), 0)

    def test_negative_damage(self):
        self.bob = Warrior("Bob")
        self.assertRaises(ValueError, self.bob.get_damaged, -1)
        self.assertRaises(ValueError, self.bob.get_damaged, -11111)

    def test_negative_hp(self):
        with self.assertRaises(ValueError):
            bob = Warrior("name", -9)
            bob = Warrior("name", 0)
    # you can not set hp < 0

    def test_is_dead(self):
        self.bob = Warrior("Bob", 100)
        self.mike = Warrior("Mike", 10)
    # Create 2 units
        self.assertTrue(self.bob.is_alive)
        self.assertTrue(self.mike.is_alive)
    # Now they are alive
        self.bob.get_damaged(100)
        self.mike.get_damaged(20)
    # Hit
        self.assertFalse(self.bob.is_alive())  # hp = 0
        self.assertFalse(self.mike.is_alive())  # hp = -10
    # Now they Dead


class TestBattle(unittest.TestCase):

    def test_battle(self, bot1=Warrior("bot1"), bot2=Warrior("bot2")):
        battle(bot1, bot2)
        self.assertEqual((bot1.is_alive() * bot2.is_alive()), 0)


if __name__ == '__main__':
    unittest.main()

