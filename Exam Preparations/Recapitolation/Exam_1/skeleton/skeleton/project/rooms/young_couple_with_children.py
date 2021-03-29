from project.people.child import Child
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *args):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=2)
        self.children = [*args]
        self.members_count += len(self.children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
