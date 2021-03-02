class Gym:
    id = 1

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []
        self.id = self.id_generator()-1

    @staticmethod
    def id_generator():
        Gym.id += 1
        return Gym.id

    @staticmethod
    def find_subscription(id, subscriptions):
        for sub in subscriptions:
            if sub.id == id:
                return sub

    @staticmethod
    def find_customer(id, customers):
        for cus in customers:
            if cus.id == id:
                return cus

    @staticmethod
    def find_trainer(id, trainers):
        for trainer in trainers:
            if trainer.id == id:
                return trainer

    @staticmethod
    def find_plan(id, plans):
        for plan in plans:
            if plan.id == id:
                return plan

    @staticmethod
    def find_equipment(id, equipments):
        for equipment in equipments:
            if equipment.id == id:
                return equipment

    def add_customer(self, customer: object):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: object):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: object):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: object):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: object):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.find_subscription(subscription_id, self.subscriptions)
        customer = self.find_customer(subscription.customer_id, self.customers)
        trainer = self.find_trainer(subscription.trainer_id, self.trainers)
        plan = self.find_plan(subscription.exercise_id, self.plans)
        equipment = self.find_equipment(plan.equipment_id, self.equipment)
        result = ''
        result += f'{subscription.__repr__()}\n'
        result += f'{customer.__repr__()}\n'
        result += f'{trainer.__repr__()}\n'
        result += f'{equipment.__repr__()}\n'
        result += f'{plan.__repr__()}'
        return result
