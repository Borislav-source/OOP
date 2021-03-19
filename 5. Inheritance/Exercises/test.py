class Person:
    pass


class Animal:
    pass


a = Animal()
p = Person()

lst = [a, p]

for el in lst:
    if not isinstance(el, Animal):
        print(el)
    else:
        print(1)