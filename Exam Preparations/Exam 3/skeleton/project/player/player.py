from abc import ABC, abstractmethod
from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self, username: str, health: int):
        self.username = Player.username(username)
        self.health = Player.health(health)
        self.card_repository = CardRepository()
        self.is_dead = bool

    @property
    def is_dead(self):
        return self.calculate_property()

    def calculate_property(self):
        if self.health <= 0:
            return True
        return False

    @staticmethod
    def username(username):
        if username == '':
            raise ValueError("Player's username cannot be an empty string. ")

    @staticmethod
    def health(health):
        if health <= 0:
            raise ValueError("Player's health bonus cannot be less than zero. ")

    @staticmethod
    def damage_is_valid(damage):
        if damage < 0:
            return False

    @abstractmethod
    def take_damage(self, damage_points: int):
        pass

    @is_dead.setter
    def is_dead(self, value):
        self._is_dead = value

