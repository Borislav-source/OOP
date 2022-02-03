from hardware.hardware import Hardware


class HeavyHardware(Hardware):
    Type = 'Heavy'

    def __init__(self, name, capacity, memory):
        super().__init__(name, HeavyHardware.Type, capacity, memory)
        self.capacity *= 2
        self.memory *= 0.75
