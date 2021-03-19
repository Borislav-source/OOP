from project.appliances.appliance import Appliance


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.exp = 0
        self.children = []
        self.appliances = []

    @property
    def expenses(self):
        if self.exp == 0:
            self.exp = self.calculate_expenses(self.children, self.appliances)
        if self.exp < 0:
            raise ValueError("Expenses cannot be negative")
        return self.exp

    def calculate_expenses(self, *args):
        for lst in args:
            for el in lst:
                if not isinstance(el, Appliance):
                    self.exp += el.cost * 30
                else:
                    self.exp += el.get_monthly_expense() * self.members_count
        return self.exp
