from project.supply.supply import Supply


class FoodSupply(Supply):
    Needs = 20

    def __init__(self):
        super().__init__(needs_increase=self.Needs)
