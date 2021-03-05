class Player:
    __name: str
    __endurance: int
    __sprint: int
    __dribble: int
    __passing: int
    __shooting: int

    def __init__(self, name: str, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        result = f'Player: {self.name}\n'
        result += f'Endurance: {self.endurance}\n'
        result += f'Sprint: {self.sprint}\n'
        result += f'Dribble: {self.dribble}\n'
        result += f'Passing: {self.passing}\n'
        result += f'Shooting: {self.shooting}\n'
        return result

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, new_endurance):
        self.__endurance = new_endurance

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, new_dribble):
        self.__dribble = new_dribble

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, new_passing):
        self.__passing = new_passing

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, new_shooting):
        self.__shooting = new_shooting

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, new_sprint):
        self.__sprint = new_sprint
