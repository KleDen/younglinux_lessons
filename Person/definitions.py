class Person:
    def __init__(self, name: str, surname: str, skill=1):
        self.name = name
        self.surname = surname
        self.__skill = skill

    def __str__(self):
        return f"Person({Person.get_skill})"

    def getinfo(self):
        return self.name, self.surname, self.__skill

    def __del__(self):
        print("Goodbye mr.", self.surname, self.name)

    def get_skill(self):
        return self.__skill

    @staticmethod
    def find_weakest(workers: list):
        weakest = min(workers, key=Person.get_skill)
        return weakest
