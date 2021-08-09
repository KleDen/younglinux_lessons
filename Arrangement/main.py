from Arrangement.Room_io import room_input, wallpapers_input, win_door_input
from definitions import Room

width, length, height = room_input()
wallpapers_width, wallpapers_length = wallpapers_input()
# Getting parameters of whole room and wallpaper rolls
room2 = Room(width, length, height)

windoors = int(input("How many objects you will not cover with wallpapers? "))
for i in range(windoors):
    wd_wid, wd_len = win_door_input()
    room2.addWD(wd_wid, wd_len)

print("area of the room is: ", room2.get_square())
print("area of work surface is: ", room2.workSurface())
print("You need", room2.wallpapers(wallpapers_width, wallpapers_length), "rolls of wallpaper to cover the room")
