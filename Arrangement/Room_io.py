def room_input():
    width = float(input("Enter width of the room: "))
    length = float(input("Enter length of the room: "))
    height = float(input("Enter height of the room: "))
    return width, length, height


def win_door_input():
    width = float(input("Enter the width of non-adhesive element: "))
    length = float(input("Enter roll length non-adhesive element: "))
    print("your object is ", width, "x", length)
    return width, length


def wallpapers_input():
    width = float(input("Enter the roll width: "))
    length = float(input("Enter roll length: "))
    return width, length
