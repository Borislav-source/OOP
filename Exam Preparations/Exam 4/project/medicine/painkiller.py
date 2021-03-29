from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    Health_increase = 20

    def __init__(self):
        super().__init__(health_increase=self.Health_increase)
