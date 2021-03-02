class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.id_generator()-1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def id_generator():
        Trainer.id += 1
        return Trainer.id

    @staticmethod
    def get_next_id():
        return Trainer.id
