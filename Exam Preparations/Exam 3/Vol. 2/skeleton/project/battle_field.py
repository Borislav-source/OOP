from project.player.beginner import Beginner


class BattleField:

    @staticmethod
    def fight(attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead')
        BattleField.health_bonus(attacker)
        BattleField.health_bonus(enemy)

        while not attacker.is_dead and not enemy.is_dead:
            enemy.take_damage(attacker.sum_of_damage_points())
            attacker.take_damage(enemy.sum_of_damage_points())

    @staticmethod
    def health_bonus(player):
        if isinstance(player, Beginner):
            player.health += 40
            for card in player.card_repository.cards:
                card.damage_points += 30
        player.health += player.sum_of_health_points()
