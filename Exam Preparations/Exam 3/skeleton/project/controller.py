from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    @staticmethod
    def check_player_type(type):
        if type == Beginner:
            return Beginner
        else:
            return Advanced

    def add_player(self, type: str, username: str):
        p_type = self.check_player_type(type)
        player = p_type(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    @staticmethod
    def check_card_type(type):
        if type == MagicCard:
            return MagicCard
        else:
            return TrapCard

    def add_card(self, type: str, name: str):
        c_type = self.check_card_type(type)
        card = c_type(name)
        self.card_repository.cards.append(card)
        return "Successfully added card of type {type}Card with name: {name}"

    def find_player(self, name):
        for player in self.player_repository.players:
            if player.username == name:
                return player

    def find_card(self, name):
        for card in self.card_repository.cards:
            if card.name == name:
                return card

    def add_player_card(self, username: str, card_name: str):
        player = self.find_player(username)
        card = self.find_card(card_name)
        player.card_repository.cards.append(card)
        return "Successfully added card of type {type}Card with name: {name}"

    def fight(self, player_one, player_two):
        BattleField.fight(player_one, player_two)
        return f"Attack user health {player_one.health} - Enemy user health {player_two.health}"