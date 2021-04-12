class BaseAquarium:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self.__name = value

    @staticmethod
    def validate_name(value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")

    def calculate_comfort(self):
        sum_ = 0
        for decoration in self.decorations:
            sum_ += decoration.comfort
        return sum_

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if not self.fish:
            result += 'Fish: none\n'
        else:
            result += f"Fish: {' '.join(fish.name for fish in self.fish)}\n"
            result += f'Decorations: {len(self.decorations)}\n'
            result += f'Comfort: {self.calculate_comfort()}'
        return result