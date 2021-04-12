from project.player.beginner import Beginner


class BattleField:

    @staticmethod
    def fight(attacker, enemy):

        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')
        attacker = BattleField.bonuses(attacker)
        enemy = BattleField.bonuses(enemy)
        while not attacker.is_dead and not enemy.is_dead:
            enemy.take_damage(attacker.player_damage_points)
            attacker.take_damage(enemy.player_damage_points)

    @staticmethod
    def bonuses(player):
        if isinstance(player, Beginner):
            player.health += 40
            for card in player.card_repository.cards:
                card.damage_points += 30
        player.health += sum([card.health_points for card in player.card_repository.cards])
        return player
