from project.player.player import Player


class Advanced(Player):
    Initial_Health = 250

    def __init__(self, username):
        super().__init__(username, health=self.Initial_Health)
