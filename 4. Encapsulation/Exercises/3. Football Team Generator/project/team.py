class Team:
    __name: str
    __rating: int
    __players = []

    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
