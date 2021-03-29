from project.medicine.medicine import Medicine


class Salve(Medicine):
    Health_increase = 50

    def __init__(self):
        super().__init__(health_increase=self.Health_increase)
