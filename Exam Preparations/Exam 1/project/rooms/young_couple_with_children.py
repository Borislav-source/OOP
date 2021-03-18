from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *args):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=0)
        self.children = list(args)
        self.room_cost = 30
        self.members_count = len(self.children) + 2
        self.appliances = [TV(), Fridge(), Laptop()]

