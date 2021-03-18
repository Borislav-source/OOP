from project.player.beginner import Beginner


class BattleField:
    @staticmethod
    def fight(player_one, player_two):
        if player_one.is_dead or player_two.is_dead:
            raise ValueError('Player is dead')
        if isinstance(player_one, Beginner):
            player_one.health += 40
            for card in player_one.card_repository.cards:
                card.damage_points += 30
        if isinstance(player_two, Beginner):
            player_two.health += 40
            for card in player_two.card_repository.cards:
                card.damage_points += 30
        player_one.health += sum(list(map(lambda x: x.health_ponts, player_one.card_repository.cards)))
        player_two.health += sum(list(map(lambda x: x.health_ponts, player_two.card_repository.cards)))
        player_two.take_damage(sum(list(map(lambda x: x.damage_points, player_one.card_repository.cards))))
        if player_one.is_dead or player_two.is_dead:
            return
        player_one.take_damage(sum(list(map(lambda x: x.damage_points, player_two.card_repository.cards))))
        if player_one.is_dead or player_two.is_dead:
            return
