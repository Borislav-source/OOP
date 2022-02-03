from software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type_ = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.light_software_components = []
        self.express_software_components = []

    def install(self, software: Software):
        if software.memory_consumption <= self.available_memory() \
                and software.capacity_consumption <= self.available_capacity():
            self.software_components.append(software)
            if software.type == 'Light':
                self.light_software_components.append(software)
            else:
                self.express_software_components.append(software)
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
            if software.type == 'Light':
                self.light_software_components.remove(software)
            else:
                self.express_software_components.remove(software)

    def available_memory(self):
        used_memory = 0
        for soft in self.software_components:
            used_memory += soft.memory_consumption
        return self.memory - used_memory

    def available_capacity(self):
        used_capacity = 0
        for soft in self.software_components:
            used_capacity += soft.capacity_consumption
        return self.capacity - used_capacity
