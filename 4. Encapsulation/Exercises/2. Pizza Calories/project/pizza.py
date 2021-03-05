class Pizza:
    __toppings = {}

    def __init__(self, name: str, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_dough):
        self.__dough = new_dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, new_capacity):
        self.__toppings_capacity = new_capacity

    # def __toppings(self, key):
    #     return self.toppings[key]

    def add_topping(self, topping):
        if self.__toppings_capacity <= len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total_weight = self.__dough.weight
        for topping, weight in self.toppings.items():
            total_weight += weight
        return total_weight


