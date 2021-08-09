from definitions import Room, WinDoor
def room_input():
    width = float(input("Enter width of the room: "))
    length = float(input("Enter length of the room: "))
    height = float(input("Enter height of the room: "))
    return width, length, height

def win_door_input():
    width = float(input("Enter the width of non-adhesive element: "))
    length = float(input("Enter roll length non-adhesive element: "))
    windor = WinDoor(width, length)
    return windor

def ask_for_state():
    answer = str(input("do you want to add new win-door element (y)yes / (n)no"))
    if answer in ('y', 'yes'):
        wd_element = win_door_input()






def wallpapers_input():
    width = float(input("Enter the roll width: "))
    length = float(input("Enter roll length: "))
    return width, length
