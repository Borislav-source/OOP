class Exercise:
    text = 'Bobby'


print(Exercise.text)
x = Exercise()
print(x.text)
x.text = 'Vicky'
y = Exercise()
print(y.text)
print(x.text)
print(Exercise.text)
y.text = 'Boyko'
print(y.text)
Exercise.text = 'Madlena'
print(Exercise.text)
t = Exercise()
print(t.text)
Exercise.name = "Dobri"
print(Exercise.name)
print(Exercise)
y.name = 'Gogo'
print(Exercise.name)
print(y.name)


class MyClass:
    number = 743

    def say_hello(self):
        return 'Hello'


x = MyClass()
print(x.say_hello())