class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.calculate_expenses(self.children, self.appliances)

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        sum_ = 0
        for lst in args:
            for el in lst:
                sum_ += el.get_monthly_expenses
        return sum_
