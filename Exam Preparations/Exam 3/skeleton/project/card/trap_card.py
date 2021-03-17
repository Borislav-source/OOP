from project.card.card import Card


class TrapCard(Card):
    Damage_points = 120
    Health_points = 85

    def __init__(self, name):
        super().__init__(name, TrapCard.Damage_points, TrapCard.Health_points)
        self.name = name
        self.damage_points = TrapCard.Damage_points
        self.health_points = TrapCard.Health_points
