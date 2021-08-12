def room_input() -> [float, float, float]:
    width = float(input("Enter width of the room: "))
    length = float(input("Enter length of the room: "))
    height = float(input("Enter height of the room: "))
    if width <= 0 or length <= 0 or height <= 0:
        raise ValueError("Parameters can't be negative!")
    return width, length, height


def win_door_input() -> [float, float]:
    width = float(input("Enter the width of non-adhesive element: "))
    length = float(input("Enter roll length non-adhesive element: "))
    if width <= 0 or length <= 0:
        raise ValueError("Parameters can't be negative!")
    print("your object is ", width, "x", length)
    return width, length


def wallpapers_input() -> [float, float]:
    width = float(input("Enter the roll width: "))
    length = float(input("Enter roll length: "))
    if width <= 0 or length <= 0:
        raise ValueError("Parameters can't be negative!")
    return width, length
