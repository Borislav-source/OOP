class Appliance:
    Month = 30

    def __init__(self, cost: float):
        self.cost = cost

    @property
    def get_monthly_expense(self):
        return self.cost * self.Month

