import unittest
from project.hero import Hero


class HeroTests(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(username='Bogdan', level=80, health=12.5, damage=1.0)
        self.enemy = Hero(username='Vicky', level=10, health=2, damage=1.0)

    def test_hero_if_all_attributes_are_set(self):
        self.assertEqual('Bogdan', self.hero.username)
        self.assertEqual(80, self.hero.level)
        self.assertEqual(12.5, self.hero.health)
        self.assertEqual(1.0, self.hero.damage)

    def test__hero__battle_if_name_equals_username_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero__battle_if_hero_health_is_equal_or_less_than_zero_raise_error(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero__battle_if_enemy_health_is_equal_or_less_than_zero_raise_error(self):
        self.enemy.health = -1
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Vicky. He needs to rest", str(ex.exception))

    def test_hero_battle__if_both_players_health_is_equal_or_less_than_zero_draw(self):
        self.hero.health = 0.5
        self.enemy.health = 0.5
        result = self.hero.battle(self.enemy)
        expected_result = 'Draw'
        self.assertEqual(expected_result, result)

    def test_hero_battle__if_enemy_health_equal_or_less_than_zero_hero_wins(self):
        self.hero.health = 100.5
        result = self.hero.battle(self.enemy)
        expected_result = 'You win'
        self.assertEqual(expected_result, result)

    def test_hero_battle__if_hero_health_equal_or_less_than_zero_hero_loose(self):
        self.hero.health = 12.5
        self.hero.damage = 0
        result = self.hero.battle(self.enemy)
        expected_result = 'You lose'
        self.assertEqual(expected_result, result)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(7, self.enemy.health)
        self.assertEqual(6.0, self.enemy.damage)

    def test_hero_printing_the_summary_of_the_class(self):
        self.hero.battle(self.enemy)
        result = self.hero.__str__()
        expected_result = f"Hero Bogdan: 81 lvl\n" \
                          f"Health: 7.5\n" \
                          f"Damage: 6.0\n"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
