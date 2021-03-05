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
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        self.__rating = new_rating

    # @property
    # def players(self):
    #     return self.__players
    #
    # @players.setter
    # def players(self, new_player):
    #     self.__players.append(new_player)

    def add_player(self, player):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def find_player(self, name):
        for player in self.players:
            if name == player.name:
                return player

    def remove_player(self, player_name: str):
        player = self.find_player(player_name)
        if not player:
            return f"Player {player_name} not found"
        self.players.remove(player)
        return player


