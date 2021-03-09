class Person:

    def __init__(self, name):
        self.__name = name

    def get_info(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


g = Person('Gogo')
g.age = 15
print(g.__dict__)
g.name = 'Ivan'
print(g.__dict__)
print(g.name)
print(hasattr(Person, "name"))
print(hasattr(Person, "get_info"))
print(getattr(g, "age", None))
setattr(g, "age", 12)
print(getattr(g, "age", None))
delattr(g, "age")
print(hasattr(Person, "age"))

