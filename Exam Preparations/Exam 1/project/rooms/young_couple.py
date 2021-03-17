from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2)
        self.budget = salary_one + salary_two
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()]
    #
    # @property
    # def expenses(self):
    #     self.the_exp = self.calculate_expenses(self.appliances, self.children)
    #     return self.the_exp
    #
    # def calculate_expenses(self, *args):
    #     for lst in args:
    #         for el in lst:
    #             if isinstance(el, Child):
    #                 self.the_exp += el.cost
    #             else:
    #                 self.the_exp += el.get_monthly_expenses()
    #     return self.the_exp * self.members_count

    # @property
    # def expenses(self):
    #     the_expenses = (sum(map(lambda x: x.get_monthly_expenses(), self.appliances)) * self.members_count)
    #     if the_expenses < 0:
    #         raise ValueError('Expenses cannot be negative')
    #     return the_expenses

# young_couple = YoungCouple("Johnsons", 150, 205)
# print(young_couple.expenses)
