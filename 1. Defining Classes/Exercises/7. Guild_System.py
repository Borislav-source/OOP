class Player:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        data = f"""Name: {self.name}
Guild: {self.guild}
HP: {self.hp}
MP: {self.mp}
"""
        for skill in self.skills:
            data += f"==={skill} - {self.skills[skill]}\n"

        return data


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player} is already in the guild."
        elif Player.guild == 'Unaffiliated':
            self.players.append(player)
            Player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            return f"Player {player} is in another guild."

    def kick_player(self, player_name: str):
        for pl in self.players:
            if pl.name == player_name:
                self.players.remove(pl)
                pl.guild = 'Unaffiliated'
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        data = f"""Guild: {self.name}
"""
        for pl in self.players:
            data += f"{Player.player_info(pl)}\n"
        return data


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("A", 3))
print(player.add_skill("A", 3))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(player.add_skill("Shield Break", 20))
# print(guild.kick_player(player))
# print(guild.guild_info())

