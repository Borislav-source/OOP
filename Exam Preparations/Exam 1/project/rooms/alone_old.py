from project.rooms.room import Room


class AloneOld(Room):

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, budget=pension, members_count=1)
        self.budget = pension
        self.room_cost = 10
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
