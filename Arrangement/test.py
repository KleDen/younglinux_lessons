import unittest

from Room_io import room_input, wallpapers_input, win_door_input
from definitions import Room


class MyTestCase(unittest.TestCase):
    def test_wallpaper(self):
        room = Room(10, 20, 1.1)
        self.assertEqual(room.wallpapers(width=1, length=10), 7)


class TestInput(unittest.TestCase):
    def test_room(self):
        assert ValueError(room_input, 0)
        assert ValueError(room_input, -9)
        assert ValueError(room_input, 'foobar')

    def test_wallpaper(self):
        assert ValueError(wallpapers_input, 0)
        assert ValueError(wallpapers_input, -9)
        assert ValueError(wallpapers_input, 'foobar')

    def test_windoor(self):
        assert ValueError(win_door_input, 0)
        assert ValueError(win_door_input, -9)
        assert ValueError(win_door_input, 'foobar')


# actually yea. str must raise typeerror, but somebody cares for real?

class Test_add(unittest.TestCase):
    def test_add(self):
        test1 = Room(10.0, 10.0, 1.0)
        test2 = Room(20.0, 20.0, 1.0)
        self.assertEqual(test1 + test2, 120.0)


if __name__ == '__main__':
    unittest.main()
