from classes import Cylinder

a = Cylinder(1, 2)

print(a.get_area())
a.dia = 2
print(a.get_area())

print(a.make_area(2, 2))
