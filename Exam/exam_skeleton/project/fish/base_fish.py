class BaseFish:
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.validate_species(value)
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.validate_price(value)
        self.__price = value

    @staticmethod
    def validate_name(value):
        if not value:
            raise ValueError("Fish name cannot be an empty string.")

    @staticmethod
    def validate_species(value):
        if not value:
            raise ValueError("Fish species cannot be an empty string.")

    @staticmethod
    def validate_price(value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")

    def eat(self):
        self.size += 5