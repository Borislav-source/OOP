from abc import ABC, abstractmethod


class Card(ABC):
    @abstractmethod
    def __init__(self, name: str, damage_points: int, health_points: int):
        self.name = self.name()
        self.damage_points = self.damage_points()
        self.health_points = self.health_points()

    @staticmethod
    def name(name):
        if name == '':
            raise ValueError("Card's name cannot be an empty string.")

    @staticmethod
    def damage_points(points):
        if points < 0:
            raise ValueError("Card's damage points cannot be less than zero.")

    @staticmethod
    def health_points(points):
        if points < 0:
            raise ValueError("Card's HP cannot be less than zero.")
