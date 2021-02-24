
class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild == 'Unaffiliated':
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            return f"Player {player} is in another guild."

    def kick_player(self, player):
        for pl in self.players:
            if pl.name == player:
                self.players.remove(pl)
                pl.guild = 'Unaffiliated'
                return f"Player {player} has been removed from the guild."
        return f"Player {player.name} is not in the guild."

    def guild_info(self):
        data = f"""Guild: {self.name}
"""
        for pl in self.players:
            data += f"{Player.player_info(pl)}\n"
        return data
