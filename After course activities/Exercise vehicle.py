class Vehicle:
    Color = 'White'

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def __repr__(self):
        return f'Color: {self.Color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'

    def seating_capacity(self, capacity):
        return f'The seating capacity of a {self.name} is {capacity} passengers'

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return f'The seating capacity of a {self.name} is {capacity} passengers'

    def fare(self):
        return (super().fare()) * 1.1


class Car(Vehicle):
    pass


bus = Bus('42', 80, 500, 50)
print(bus.name, bus.mileage, bus.max_speed)
print(bus.seating_capacity())
print(bus.fare())