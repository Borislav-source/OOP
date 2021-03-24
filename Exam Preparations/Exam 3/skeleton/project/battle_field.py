from project.player.beginner import Beginner


class BattleField:
    @staticmethod
    def fight(attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead')
        if isinstance(attacker, Beginner):
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30
        if isinstance(enemy, Beginner):
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30
        attacker.health += sum(list(map(lambda x: x.health_ponts, attacker.card_repository.cards)))
        enemy.health += sum(list(map(lambda x: x.health_ponts, enemy.card_repository.cards)))
        enemy.take_damage(sum(list(map(lambda x: x.damage_points, attacker.card_repository.cards))))
        if attacker.is_dead or enemy.is_dead:
            return
        attacker.take_damage(sum(list(map(lambda x: x.damage_points, enemy.card_repository.cards))))
        if attacker.is_dead or enemy.is_dead:
            return
