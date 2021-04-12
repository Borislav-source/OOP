from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    Initial_comfort = 1
    Initial_price = 5

    def __init__(self):
        super().__init__(self.Initial_comfort, self.Initial_price)