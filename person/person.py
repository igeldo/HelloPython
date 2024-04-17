

class Person:

    def __init__(self, vorname, name):
        self._vorname = vorname
        self._name = name

    def get_vorname(self):
        return self._vorname

    def __str__(self):
        return f'{self._vorname} {self._name}'



if __name__ == '__main__':
    person1 = Person('Georg', 'Pietrek')
    print(f"{person1}")
    vorname1 = person1.get_vorname()
    print(f"vorname ist: {vorname1}")

    person2 = Person('Otto', 'Meier')
    print(f"{person2}")

    person3 = Person(name = 'Müller', vorname = 'Hugo')
    print(f"{person3}")
    vorname3 = person3.get_vorname()
    print(f"vorname ist: {vorname3}")

