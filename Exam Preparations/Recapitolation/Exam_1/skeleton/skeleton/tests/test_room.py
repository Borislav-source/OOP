import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self) -> None:
        self.room = Room(name='Tsvetkovy', budget=250, members_count=4)

    def test_room_if_all_attributes_are_set_properly(self):
        self.assertEqual('Tsvetkovy', self.room.family_name)
        self.assertEqual(250, self.room.budget)
        self.assertEqual(4, self.room.members_count)
        self.assertEqual([], self.room.children)

    def test_room_expenses_property_returns_the_expenses(self):
        result = self.room.expenses
        self.assertEqual(0, result)

    def test_room_expenses_property_raises_value_error_if_the_expenses_are_below_zero(self):
        with self.assertRaises(Exception) as ex:
            self.room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_room__set_expenses(self):
        self.room.expenses = 5
        self.assertEqual(5, self.room.expenses)


if __name__ == '__main__':
    unittest.main()
