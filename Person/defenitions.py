class Person:
    def __init__(self, name: str, surname: str, skill=1):
        self.name = name
        self.surname = surname
        self.skill = skill

    def getinfo(self):
        return self.name, self.surname, self.skill

    def __del__(self):
        print("Goodbye mr.",self.surname, self.name)
