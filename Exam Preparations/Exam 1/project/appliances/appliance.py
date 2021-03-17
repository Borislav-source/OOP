class Appliance:
    MONTH = 30

    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expenses(self):
        return self.cost * self.MONTH
