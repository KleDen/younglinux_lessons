import unittest

from definitions import Room


class MyTestCase(unittest.TestCase):
    def test_wallpaper(self):
        room = Room(10, 20, 1.1)
        self.assertEqual(room.wallpapers(width=1, length=10), 7)


class TestWorkSurfase(unittest.TestCase):
    def test_positive(self):
        room = Room(10, 10, 1)
        room.addWD(1, 10)
        self.assertEqual(room.workSurface(), 30.0)

    def test_Errors(self):
        room = Room(10, 10, 1)
        room.addWD(4, 10)
        self.assertRaises(ValueError, room.workSurface)  # Raises error when __area <= 0


class TestWallpapers(unittest.TestCase):
    def test_wallpapers(self):
        room = Room(10, 10, 1)

        room.addWD(1, 10)
        self.assertEqual(room.wallpapers(1, 2), 15)  # WorkSurface = 30

        room.addWD(1, 10)
        self.assertEqual(room.wallpapers(1, 3), 7)  # WorkSurface = 20


class TestAdd(unittest.TestCase):
    def test_add(self):
        test1 = Room(10.0, 10.0, 1.0)
        test2 = Room(20.0, 20.0, 1.0)
        self.assertEqual(test1 + test2, 120.0)


if __name__ == '__main__':
    unittest.main()
