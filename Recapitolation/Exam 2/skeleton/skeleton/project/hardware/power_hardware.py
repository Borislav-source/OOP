from hardware.hardware import Hardware


class PowerHardware(Hardware):
    Type = 'Power'

    def __init__(self, name, capacity, memory):
        super().__init__(name, PowerHardware.Type, capacity, memory)
        self.capacity *= 0.25
        self.memory *= 1.75
