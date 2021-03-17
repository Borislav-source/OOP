class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.light_softwares = []
        self.express_softwares = []

    def install(self, software):
        if software.memory_consumption <= self.memory and software.capacity_consumption <= self.capacity:
            self.software_components.append(software)
            if software.type == 'Light':
                self.light_softwares.append(software)
            else:
                self.express_softwares.append(software)
            return
        raise Exception('Software cannot be installed')

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

    def used_memory(self):
        memory = 0
        for software in self.software_components:
            memory += software.memory_consumption
        return int(memory)

    def used_capacity(self):
        capacity = 0
        for software in self.software_components:
            capacity += software.capacity_consumption
        return int(capacity)
