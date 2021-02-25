class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.names = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        details = pokemon.pokemon_details()
        return f"Caught {details}"

    def release_pokemon(self, name):
        for pokemon in self.pokemon:
            if pokemon.name == name:
                self.pokemon.remove(pokemon)
                return f"You have released {name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"""Pokemon Trainer {self.name}
Pokemon count {len(self.pokemon)}
"""
        for poke in self.pokemon:
            data += f"- {poke.pokemon_details()}\n"
        return data
