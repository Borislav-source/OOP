from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, budget=salary, members_count=1)
        self.budget = salary
        self.room_cost = 10
        self.appliances = [TV()]
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
  #   def expenses(self):
  #       the_expenses = sum(map(lambda x: x.get_monthly_expenses(), self.appliances)) + self.room_cost
  #       if the_expenses < 0:
  #           raise ValueError('Expenses cannot be negative')
  #       return the_expenses