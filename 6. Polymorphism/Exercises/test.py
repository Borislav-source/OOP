from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Cat(Animal):
    pass


# animal = Animal('Goncho')
# print(animal)

cat = Cat('Pesho')
print(cat)
