from project.card.card import Card


class MagicCard(Card):
    Damage_points = 5
    Health_points = 80

    def __init__(self, name):
        super().__init__(name, MagicCard.Damage_points, MagicCard.Health_points)
        self.name = name
        self.damage_points = MagicCard.Damage_points
        self.health_points = MagicCard.Health_points
