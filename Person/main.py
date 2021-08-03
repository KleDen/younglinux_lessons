from Person import definitions
from Person.definitions import Person

Salt = Person("Jake", "Miller", 3)
Tequila = Person("Mike", "Smith")
Lime = Person("Guy", "Family", 2)

weakest = definitions.Person.find_weakest([Salt, Tequila, Lime])
print("он признает что weakest это", Tequila, 'но не удаляет его')
del weakest
print(Tequila, Salt, Lime)

x = input()
