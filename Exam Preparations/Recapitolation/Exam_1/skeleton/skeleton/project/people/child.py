class Child:
    def __init__(self, food_cost: float, *args):
        self.food_cost = food_cost
        self.toys_cost = args
        self.cost = self.food_cost + sum(self.toys_cost)

    @property
    def get_monthly_expenses(self):
        return self.cost * 30
