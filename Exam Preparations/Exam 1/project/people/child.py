class Child:
    def __init__(self, food_cost: int, *args):
        self.food_cost = food_cost
        self.toys_cost = list(args)
        self.cost = (food_cost + sum(self.toys_cost))
