from project.appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self):
        super().__init__(cost=0.7)
        self.cost = 0.7

    def get_monthly_expenses(self):
        return self.cost * self.MONTH
