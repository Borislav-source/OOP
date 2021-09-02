class Caretaker:
    def __init__(self, name: str, age: int, salary):
        self.name = name
        self.salary = salary
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'
