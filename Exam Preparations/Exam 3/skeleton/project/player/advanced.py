from project.player.player import Player


class Advanced(Player):
    Health = 250

    def __init__(self, username: str):
        super().__init__(username, Advanced.Health)
        self.username = username
        self.health = Advanced.Health

    def take_damage(self, damage_points: int):
        if self.damage_is_valid(damage_points):
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points
        self.check_if_dead()

