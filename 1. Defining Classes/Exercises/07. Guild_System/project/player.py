class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        data = f"Name: {self.name}\n"
        data += f"Guild: {self.guild}\n"
        data += f"HP: {self.hp}\n"
        data += f"MP: {self.mp}\n"

        for skill in self.skills:
            data += f"==={skill} - {self.skills[skill]}\n"

        return data
