from Person import definitions
from Person.definitions import Person

Salt = Person("Jake", "Miller", 3)
Tequila = Person("Mike", "Smith")
Lime = Person("Guy", "Family", 2)
workers = [Salt, Tequila, Lime]

weakest = definitions.Person.find_weakest(workers)

workers.remove(weakest)

for human in workers:
    print(human.getinfo())

x = input()
