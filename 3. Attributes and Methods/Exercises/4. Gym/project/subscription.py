class Subscription:
    id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.id_generator()-1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def id_generator():
        Subscription.id += 1
        return Subscription.id

    @staticmethod
    def get_next_id():
        return Subscription.id
