import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train('BDJ', 50)

    def test_train_if_all_attributes_are_set_correctly(self):
        self.assertEqual(self.train.name, 'BDJ')
        self.assertEqual(self.train.capacity, 50)
        self.assertEqual(self.train.passengers, [])

    def test_train_add_passenger_if_no_capacity(self):
        self.train.capacity = 0
        with self.assertRaises(Exception) as ex:
            self.train.add('Gosho')
        self.assertEqual("Train is full", str(ex.exception))

    def test_train_add_passenger_if_passenger_is_already_on_train(self):
        self.train.passengers = ['Gosho']
        with self.assertRaises(Exception) as ex:
            self.train.add('Gosho')
        self.assertEqual("Passenger Gosho Exists", str(ex.exception))

    def test_train_add_passenger_if_everything_is_fine(self):
        self.assertEqual([], self.train.passengers)
        result = self.train.add('Gosho')
        self.assertEqual("Added passenger Gosho", result)
        self.assertIn('Gosho', self.train.passengers)

    def test_train_remove_passenger_if_he_is_not_in_train_exceptions(self):
        with self.assertRaises(Exception) as ex:
            self.train.remove('Gosho')
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_train_remove_passenger_if_everything_is_fine(self):
        self.train.passengers = ['Gosho']
        self.assertEqual(['Gosho'], self.train.passengers)
        result = self.train.remove('Gosho')
        self.assertEqual("Removed Gosho", result)
        self.assertNotIn('Gosho', self.train.passengers)


if __name__ == '__main__':
    unittest.main()