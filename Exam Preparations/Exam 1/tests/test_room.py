import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self) -> None:
        self.room = Room(name='Tsvetkovy', budget=250, members_count=4)

    def test_room_if_all_attributes_are_set_properly(self):
        self.assertEqual('Tsvetkovy', self.room.family_name)
        self.assertEqual(250, self.room.budget)
        self.assertEqual(4, self.room.members_count)

    def test_room_expenses_property_returns_the_expenses(self):
        result = self.room.expenses()
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
