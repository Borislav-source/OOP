from project.appliances.appliance import Appliance


class Laptop(Appliance):
    def __init__(self):
        super().__init__(cost=1)
        self.cost = 1

    def get_monthly_expenses(self):
        return self.cost * self.MONTH
