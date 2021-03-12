class Person:
    def __init__(self, name=None, surname=None):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        new_person = Person()
        new_person.name = self.name
        new_person.surname = other.surname
        return new_person

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __add__(self, other):
        return self.people + other.people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f'Group {self.name} with members {", ".join(man.__repr__() for man in self.people)}'

