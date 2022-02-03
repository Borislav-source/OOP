from software.software import Software


class LightSoftware(Software):
    Type = 'Light'

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, LightSoftware.Type, capacity_consumption, memory_consumption)
        self.capacity_consumption *= 1.5
        self.memory_consumption *= 0.5
