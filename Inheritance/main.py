import random

from Classes import Hero, Solder

Jaina = Hero(team="Blue")
Rexar = Hero(team="Red")

red_team = []
blue_team = []

for solders in range(10):
    team = random.choice(["Red", "Blue"])
    if team == "Red":
        red_team.append(Solder(team))
    else:
        blue_team.append(Solder(team))

if len(red_team) == len(blue_team):
    print("Draw!!!")
elif len(red_team) > len(blue_team):
    Rexar.lvlup()
    print(f"Red team win! Rexar reach Lvl {Rexar.lvl}!")
else:
    Jaina.lvlup()
    print(f"Blue team win! Jaina reach Lvl {Jaina.lvl}!")

red_team[0].follow(Rexar)
print(Rexar.uid, red_team[0].uid)
# print(f"Red team has {len(red_team)} solders")
# print(f"Blue team has {len(blue_team)} solders")
