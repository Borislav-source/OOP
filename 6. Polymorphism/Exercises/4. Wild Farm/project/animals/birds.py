from project.animals.animal import Bird


class Owl(Bird):
    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food):
        if not food.__class__.__name__ == 'Meat':
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity

