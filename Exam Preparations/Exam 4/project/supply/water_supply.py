from project.supply.supply import Supply


class WaterSupply(Supply):
    Needs = 40

    def __init__(self):
        super().__init__(needs_increase=self.Needs)
