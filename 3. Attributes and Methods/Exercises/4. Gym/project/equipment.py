class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.id_generator()-1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def id_generator():
        Equipment.id += 1
        return Equipment.id

    @staticmethod
    def get_next_id():
        return Equipment.id
