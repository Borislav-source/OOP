from project.player.player import Player


class Beginner(Player):
    Initial_Health = 50

    def __init__(self, username):
        super().__init__(username, health=self.Initial_Health)
