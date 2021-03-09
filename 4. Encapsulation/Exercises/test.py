class Person:
    __name = str

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
print(hasattr(Person, "name"))
print(hasattr(Person, "get_info"))
print(getattr(g, "age", None))
setattr(g, "age", 12)
print(getattr(g, "age", None))
delattr(g, "age")
print(hasattr(Person, "age"))
