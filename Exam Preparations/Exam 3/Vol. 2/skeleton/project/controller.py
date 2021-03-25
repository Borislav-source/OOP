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
    def check_player_type(type_):
        if type_ == 'Beginner':
            return Beginner
        return Advanced

    @staticmethod
    def check_card_type(type_):
        if type_ == 'MagicCard':
            return MagicCard
        return TrapCard

    def add_player(self, type_: str, username: str):
        player = self.check_player_type(type_)(username)
        self.player_repository.add_player(player)
        return f"Successfully added player of type {type_} with username: {username}"

    def add_card(self, type_, name):
        card = self.check_card_type(type_)(name)
        self.card_repository.add_card(card)
        return f"Successfully added card of type {type_}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find_player(username)
        card = self.card_repository.find_card(card_name)
        player.card_repository.add_card(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        attacker = self.player_repository.find_player(attack_name)
        enemy = self.player_repository.find_player(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ''
        for player in self.player_repository.players:
            result += f'Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}\n'
            for card in player.card_repository.cards:
                result += f'### Card: {card.name} - Damage: {card.damage_points}\n'
        return result


# controller = Controller()
# controller.add_player('Beginner', 'b')
# controller.add_card('MagicCard', 'm')
# controller.add_player_card('b', 'm')
# print(controller.report())
# controller.add_player('Advanced', 'BogDan')
# controller.add_card('TrapCard', 'Sila')
# controller.add_player_card('BogDan', 'Sila')
# print(controller.report())
# print(controller.fight('BogDan', 'b'))
# print(controller.report())