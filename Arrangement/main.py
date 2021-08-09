from Arrangement.Room_io import room_input, wallpapers_input, win_door_input
from definitions import Room

width, length, height = room_input()
wallpapers_width, wallpapers_length = wallpapers_input()
# ^ Getting parameters of whole room and wallpaper rolls

width_wd, length_wd = win_door_input()




room2 = Room(width, length, height)

print("area of work surface is: ", room2.workSurface())
print(room2.wallpapers(wallpapers_width, wallpapers_length))
# ^ Printing results
