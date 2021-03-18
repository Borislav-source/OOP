class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        if player in self.players:
            raise ValueError(f'Player {player.username} already exists!')
        self.players.append(player)
        self.count += 1

    def remove(self, player):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        self.players.remove(player)
        self.count -= 1

    def find(self, username: str):
        for player in self.players:
            if player.username == username:
                return player
