from hardware.heavy_hardware import HeavyHardware
from hardware.power_hardware import PowerHardware
from software.express_software import ExpressSoftware
from software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def _find_hardware(name):
        for hard in System._hardware:
            if hard.name == name:
                return hard

    @classmethod
    def _find_software(cls, soft_name):
        for soft in System._software:
            if soft.name == soft_name:
                return soft

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hard = System._find_hardware(hardware_name)
        if hard not in System._hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hard.install(software)
        except Exception:
            return 'Software cannot be installed'
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hard = System._find_hardware(hardware_name)
        if hard not in System._hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hard.install(software)
        except Exception:
            return 'Software cannot be installed'
        System._software.append(software)

    @staticmethod
    def release_software_component(hard_name: str, soft_name: str):
        hard = System._find_hardware(hard_name)
        software = System._find_software(soft_name)
        if hard and software:
            hard.uninstall(software)

    @classmethod
    def total_hardware_memory_and_capacity(cls):
        memory = 0
        capacity = 0
        for hard in System._hardware:
            memory += hard.memory
            capacity += hard.capacity
        return [int(memory), int(capacity)]

    @classmethod
    def total_software_memory_and_capacity(cls):
        memory = 0
        capacity = 0
        for soft in System._software:
            memory += soft.memory_consumption
            capacity += soft.capacity_consumption
        return [int(memory), int(capacity)]

    @staticmethod
    def analyze():
        total_hard_system = System.total_hardware_memory_and_capacity()
        total_soft_system = System.total_software_memory_and_capacity()
        return f'''System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {total_soft_system[0]} / {total_hard_system[0]} 
Total Capacity Taken: {total_soft_system[1]} / {total_hard_system[1]}'''

    @staticmethod
    def system_split():
        message = ''

        for hard in System._hardware:
            message += f'Hardware Component - {hard.name} \n'
            message += f'Express Software Components: {len(hard.express_software_components)}\n'
            message += f'Light Software Components: {len(hard.light_software_components)}\n'
            message += f'Memory Usage: {int(hard.memory - hard.available_memory())} / {int(hard.memory)} \n'
            message += f'Capacity Usage: {int(hard.capacity - hard.available_capacity())} / {int(hard.capacity)} \n'
            message += f'Type: {hard.Type}\n'
            message += f'Software Components: {", ".join([sof.name for sof in hard.software_components])}\n'

        return message

