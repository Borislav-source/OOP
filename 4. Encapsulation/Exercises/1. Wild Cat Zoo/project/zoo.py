class Zoo:
    def __init__(self, name: str, budget: int, animlal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if self.__animal_capacity > len(self.animals) and price > self.__budget:
            return "Not enough budget"
        elif self.__animal_capacity > len(self.animals) and price < self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def find_worker(self, name: str):
        for worker in self.workers:
            if worker.name == name:
                return worker

    def fire_worker(self, worker_name: str):
        worker = self.find_worker(worker_name)
        if not worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker.name} fired successfully"

    def salaries_sum(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        return salaries

    def pay_workers(self):
        if not self.salaries_sum() <= self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= self.salaries_sum()
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tendency_summer(self):
        money = 0
        for animal in self.animals:
            money += animal.get_needs()
        return money

    def tend_animals(self):
        if not self.tendency_summer() <= self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= self.tendency_summer()
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        result = f'You have {len(self.animals)} animals\n'
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            else:
                cheetahs.append(animal)
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f'{lion}\n'
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f'{tiger}\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        for cheetah in cheetahs:
            result += f'{cheetah}\n'
        return result.strip()

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        result = f'You have {len(self.workers)} workers\n'
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
            else:
                vets.append(worker)
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f'{keeper}\n'
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f'{caretaker}\n'
        result += f'----- {len(vets)} Vets:\n'
        for vet in vets:
            result += f'{vet}\n'
        return result.strip()

