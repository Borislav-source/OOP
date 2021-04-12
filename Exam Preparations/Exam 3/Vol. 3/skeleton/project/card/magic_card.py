from project.card.card import Card


class MagicCard(Card):
    Init_damage = 5
    Init_health = 80

    def __init__(self, name: str):
        super().__init__(name, damage_points=self.Init_damage, health_points=self.Init_health)
