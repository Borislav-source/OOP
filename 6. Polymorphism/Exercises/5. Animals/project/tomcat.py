from project.cat import Cat


class Tomcat(Cat):
    Gender = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.Gender)

    # def __repr__(self):
    #     return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return 'Hiss'
