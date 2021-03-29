class Appliance:
    Month = 30

    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        return round(self.cost * self.Month, 2)

    @property
    def get_monthly_expenses(self):
        return round(self.cost * self.Month, 2)
