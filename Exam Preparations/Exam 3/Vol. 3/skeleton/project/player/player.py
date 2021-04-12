from abc import ABC
from project.card.card_repository import CardRepository


class Player(ABC):
    def __init__(self, username: str, health: int):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.__health = value

    @property
    def is_dead(self):
        return self.__health <= 0

    def take_damage(self, damage_points):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.__health -= damage_points

    @property
    def player_damage_points(self):
        damage_points = 0
        for card in self.card_repository.cards:
            damage_points += card.damage_points
        return damage_points
