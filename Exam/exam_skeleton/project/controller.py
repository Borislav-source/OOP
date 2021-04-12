from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        type_ = self.find_type_of_aquarium(aquarium_type)
        if not type_:
            return "Invalid aquarium type."
        aquarium = type_(aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    @staticmethod
    def find_type_of_aquarium(type_):
        if type_ == 'FreshwaterAquarium':
            return FreshwaterAquarium
        elif type_ == 'SaltwaterAquarium':
            return SaltwaterAquarium
        else:
            return None

    def add_decoration(self, decoration_type: str):
        type_ = self.validate_type_decoration(decoration_type)
        if not type_:
            return "Invalid decoration type."
        decoration = type_()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    @staticmethod
    def validate_type_decoration(type_):
        if type_ == 'Plant':
            return Plant
        elif type_ == 'Ornament':
            return Ornament
        else:
            return None

    def __find_aquarium(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__find_aquarium(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        type_ = self.validate_type_of_fish(fish_type)
        aquarium = self.__find_aquarium(aquarium_name)
        if not type_:
            return f"There isn't a fish of type {fish_type}."
        if aquarium.__class__.__name__ == 'FreshwaterAquarium' and fish_type == 'SaltwaterFish':
            return "Water not suitable."
        elif aquarium.__class__.__name__ == 'SaltwaterAquarium' and fish_type == 'FreshwaterFish':
            return "Water not suitable."
        fish = type_(fish_name, fish_species, price)
        result = aquarium.add_fish(fish)
        return result

    @staticmethod
    def validate_type_of_fish(type_):
        if type_ == 'FreshwaterFish':
            return FreshwaterFish
        elif type_ == 'SaltwaterFish':
            return SaltwaterFish
        else:
            return None

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        for fish in aquarium.fish:
            fish.eat()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        sum_ = 0
        for fish in aquarium.fish:
            sum_ += fish.price
        for decoration in aquarium.decorations:
            sum_ += decoration.price
        return f"The value of Aquarium {aquarium_name} is {sum_:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += f'{aquarium}\n'
        return result