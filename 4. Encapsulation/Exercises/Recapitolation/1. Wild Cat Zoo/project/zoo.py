from lion import Lion
from tiger import Tiger
from cheetah import Cheetah
from keeper import Keeper
from caretaker import Caretaker

from vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif price > self.__budget:
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity >= len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def find_worker(self, name: str):
        for worker in self.workers:
            if worker.name == name:
                return worker

    def fire_worker(self, worker_name):
        worker = self.find_worker(worker_name)
        if worker:
            self.workers.remove(worker)
            return f'{worker.name} fired successfully'
        return f'There is no {worker.name} in the zoo'

    def __get_total_of_salaries(self):
        _sum = 0
        for worker in self.workers:
            _sum += worker.salary
        return _sum

    def pay_workers(self):
        if self.__budget >= self.__get_total_of_salaries():
            self.__budget -= self.__get_total_of_salaries()
            return f'You paid your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def __get_total_tend_needed(self):
        _sum = 0
        for animal in self.animals:
            _sum += animal.get_needs()
        return _sum

    def tend_animals(self):
        if self.__budget >= self.__get_total_tend_needed():
            self.__budget -= self.__get_total_tend_needed()
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def __get_count_of_animals(self, name):
        inner_count = 0
        for animal in self.animals:
            if animal.__class__.__name__ == name:
                inner_count += 1
        return inner_count

    def __get_count_of_workers(self, name):
        inner_count = 0
        for animal in self.workers:
            if animal.__class__.__name__ == name:
                inner_count += 1
        return inner_count

    @staticmethod
    def __represent(instance, _list):
        result = ''
        for el in _list:
            if isinstance(el, instance):
                result += f'{el}\n'
        return result

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n' \
                 f'---- {self.__get_count_of_animals("Lion")} Lions:\n' \
                 f'{self.__represent(Lion, self.animals)}' \
                 f'---- {self.__get_count_of_animals("Tiger")} Tigers:\n' \
                 f'{self.__represent(Tiger, self.animals)}' \
                 f'---- {self.__get_count_of_animals("Cheetah")} Cheetahs:\n' \
                 f'{self.__represent(Cheetah, self.animals)}'
        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n' \
                 f'---- {self.__get_count_of_workers("Keeper")} Keepers:\n' \
                 f'{self.__represent(Keeper, self.workers)}' \
                 f'---- {self.__get_count_of_workers("Caretaker")} Caretakers:\n' \
                 f'{self.__represent(Caretaker, self.workers)}' \
                 f'---- {self.__get_count_of_workers("Vet")} Vets:\n' \
                 f'{self.__represent(Vet, self.workers)}'
        return result

# z = Zoo('Zoo', 300, 5, 8)
# leo = Lion('leo', 'male', 5)
# teo = Tiger('leo', 'male', 5)
# leos = Lion('leo', 'male', 5)
# print(z.add_animal(leo, 5))
# print(z.add_animal(leos, 5))
# print(z.add_animal(teo, 5))
# print(z.animals_status())
