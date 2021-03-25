class PlayerRepository:

    def __init__(self):
        self.players = []
        self.players_names = []

    @property
    def count(self):
        return len(self.players)

    def add_player(self, player):
        if player.username in self.players_names:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.players_names.append(player.username)

    def find_player(self, username):
        for player in self.players:
            if player.username == username:
                return player

    def remove_player(self, player):
        if not player:
            raise ValueError("Player cannot be an empty string!")
        player_obj = self.find_player(player)
        self.players.remove(player_obj)
        self.players_names.remove(player)

