class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []

    @property
    def expenses(self):
        expenses = self.calculate_expenses(self.children, self.appliances)
        if expenses < 0:
            raise ValueError("Expenses cannot be negative")
        return expenses

    @staticmethod
    def calculate_expenses(*args):
        sum_ = 0
        for lst in args:
            for el in lst:
                sum_ += el.get_monthly_expense
        return sum_
