from project.player.player import Player


class Beginner(Player):
    Health = 50

    def __init__(self, username: str):
        super().__init__(username, Beginner.Health)
        self.username = username
        self.health = Beginner.Health

    def take_damage(self, damage_points: int):
        if self.damage_is_valid(damage_points):
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points



