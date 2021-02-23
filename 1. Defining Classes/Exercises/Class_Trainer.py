from project import *


class Trainer:
    pokemon = []
    names = []

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        details = Pokemon.pokemon_details(pokemon)
        return f"Caught {details}"

    def release_pokemon(self, name):
        if name == pokemon.name:
            self.pokemon.remove(pokemon)
            return f"You have released {name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"""Pokemon Trainer {self.name}
Pokemon count {len(self.pokemon)}
"""
        for poke in self.pokemon:
            data += f"- {Pokemon.pokemon_details(poke)}\n"
        return data


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())