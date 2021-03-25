from abc import ABC, abstractmethod
from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.validate_username(value)
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.validate_health(value)
        self.__health = value

    def take_damage(self, damage):
        if damage < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.__health -= damage

    @staticmethod
    def validate_username(name):
        if not name:
            raise ValueError("Player's username cannot be an empty string.")

    @staticmethod
    def validate_health(health):
        if health < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")

    @property
    def is_dead(self):
        return self.__health <= 0

    def sum_of_health_points(self):
        sum_ = 0
        for card in self.card_repository.cards:
            sum_ += card.health_points
        return sum_

    def sum_of_damage_points(self):
        sum_ = 0
        for card in self.card_repository.cards:
            sum_ += card.damage_points
        return sum_
