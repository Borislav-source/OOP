class PlayerRepository:
    def __init__(self):
        self.players = []
        self.players_names = []
        self.count = len(self.players)

    def add(self, player):
        if player.username in self.players_names:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.players_names.append(player.username)

    def remove(self, player: str):
        if not player:
            raise ValueError("Player cannot be an empty string!")
        the_player = self.find(player)
        self.players.remove(the_player)
        self.players_names.remove(the_player.username)

    def find(self, username: str):
        for player in self.players:
            if player.username == username:
                return player
