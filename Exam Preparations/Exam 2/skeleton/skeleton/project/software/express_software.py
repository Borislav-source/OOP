from project.software.software import Software


class ExpressSoftware(Software):
    Type = 'Express'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, ExpressSoftware.Type, capacity_consumption, memory_consumption)
        self.memory_consumption *= 2
