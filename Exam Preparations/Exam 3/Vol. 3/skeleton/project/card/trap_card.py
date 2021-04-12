from project.card.card import Card


class TrapCard(Card):
    Init_damage = 120
    Init_health = 5

    def __init__(self, name: str):
        super().__init__(name, damage_points=self.Init_damage, health_points=self.Init_health)
