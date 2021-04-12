from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    Initial_comfort = 5
    Initial_price = 10

    def __init__(self):
        super().__init__(self.Initial_comfort, self.Initial_price)