class Person:
    def __init__(self, name: str, surname: str, skill=1):
        self.name = name
        self.surname = surname
        self.__skill = skill

    def getinfo(self):
        return self.name, self.surname, self.__skill

    def __del__(self):
        print("Goodbye mr.", self.surname, self.name)

    @staticmethod
    def find_weakest(workers: list):
        weakest = workers[0]
        for worker in workers:
            if worker.__skill <= weakest.__skill:
                weakest = worker
        return weakest
