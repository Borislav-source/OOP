class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1)]
for i in range(len(animals)):
    animal = animals[i]
    # price = prices[i]
    print(animal.name)
