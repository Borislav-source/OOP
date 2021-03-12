from project.cat import Cat


class Kitten(Cat):
    Gender = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.Gender)

    # def __repr__(self):
    #     return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return 'Meow'
