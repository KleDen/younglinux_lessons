from definitions import Room

r1 = Room(6, 2, 2.7)

r1.addWD(2, 2)
r1.addWD(1, 1)
r1.addWD(1, 2)
r1.addWD(5, 1)
r1.get_square()

print(r1.workSurface())
# ИНТЕРФЕЙС
# ТЕСТЫ