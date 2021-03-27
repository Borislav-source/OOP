import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal('Aron', 'Dog', 'Bark')

    def test_mammal__attributes_are_set(self):
        self.assertEqual("Aron", self.mammal.name)
        self.assertEqual('Dog', self.mammal.type)
        self.assertEqual('Bark', self.mammal.sound)

    def test_mammal__make_sound(self):
        result = self.mammal.make_sound()
        expected_result = 'Aron makes Bark'
        self.assertEqual(expected_result, result)

    def test_mammal__get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_result = 'animals'
        self.assertEqual(expected_result, result)

    def test_mammal__get_info(self):
        result = self.mammal.info()
        expected_result = f'Aron is of type Dog'
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
