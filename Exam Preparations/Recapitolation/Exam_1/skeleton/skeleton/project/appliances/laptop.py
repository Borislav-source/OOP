from project.appliances.appliance import Appliance


class Laptop(Appliance):
    cost = 1.00

    def __init__(self):
        super().__init__(cost=self.cost)