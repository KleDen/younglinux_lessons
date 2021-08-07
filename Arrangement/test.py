import unittest

from definitions import Room


# Cделать тест на Wallpaper
# TEST_DRIVEN_DEVELOPMENT

class MyTestCase(unittest.TestCase):
    def test_wallpaper(self):
        room = Room(10, 20, 1.1)
        print(room.get_square())


        self.assertEqual(room.wallpapers(width=1, length=10), 7)


if __name__ == '__main__':
    unittest.main()
