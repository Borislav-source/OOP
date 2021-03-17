from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *args):
        super().__init__(family_name, budget=salary_one + salary_two)
        self.budget = salary_one + salary_two
        self.room_cost = 30
        self.children = list(args)
        self.members_count = len(self.children) + 2
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
    #     return self.__expenses
    #
    # def calculate_expenses(self, args):
    #     for lst in args:
    #         for el in lst:
    #             if isinstance(el, Child):
    #                 self.__expenses += el.cost
    #             else:
    #                 self.__expenses += el.get_monthly_expenses()
    #     return self.__expenses

    # @property
    # def expenses(self):
    #     the_expenses = (sum(map(lambda x: x.get_monthly_expenses(), self.appliances))) * self.members_count
    #     if the_expenses < 0:
    #         raise ValueError('Expenses cannot be negative')
    #     return the_expenses
    #
    # @property
    # def children_costs(self):
    #     return sum(map(lambda x: x.cost, self.children))


