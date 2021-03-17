from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def exist_hardware(name):
        for hw in System._hardware:
            if hw.name == name:
                return hw

    @staticmethod
    def exist_software(name):
        for sw in System._software:
            if sw.name == name:
                return sw

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.exist_hardware(hardware_name)
        if not hardware:
            return 'Hardware does not exist'
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
        except Exception:
            return 'Software cannot be installed'
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.exist_hardware(hardware_name)
        if not hardware:
            return 'Hardware does not exist'
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
        except Exception:
            return 'Software cannot be installed'
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.exist_hardware(hardware_name)
        software = System.exist_software(software_name)
        if software and hardware:
            hardware.uninstall(software)
            if software.type == 'Light':
                hardware.light_softwares.remove(software)
            else:
                hardware.express_softwares.remove(software)
        else:
            return 'Some of the components do not exist'

    @staticmethod
    def calculate_memory():
        memory = 0
        for hardware in System._hardware:
            memory += hardware.memory
        return int(memory)

    @staticmethod
    def total_used_memory():
        used_memory = 0
        for software in System._software:
            used_memory += software.memory_consumption
        return int(used_memory)

    @staticmethod
    def total_used_space():
        used_capacity = 0
        for software in System._software:
            used_capacity += software.capacity_consumption
        return int(used_capacity)

    @staticmethod
    def total_capacity():
        capacity = 0
        for hardware in System._hardware:
            capacity += hardware.capacity
        return int(capacity)

    @staticmethod
    def analyze():
        result = 'System Analysis\n' \
                  f'Hardware Components: {len(System._hardware)}\n' \
                  f'Software Components: {len(System._software)}\n' \
                  f'Total Operational Memory: {System.total_used_memory()} / {System.calculate_memory()}\n' \
                  f'Total Capacity Taken: {System.total_used_space()} / {System.total_capacity()}'
        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += f'Hardware Component - {hardware.name}\n' \
                      f"Express Software Components: {len(hardware.express_softwares)}\n" \
                      f"Light Software Components: {len(hardware.light_softwares)}\n" \
                      f'Memory Usage: {hardware.used_memory()} / {int(hardware.memory)}\n' \
                      f'Capacity Usage: {hardware.used_capacity()} / {int(hardware.capacity)}\n' \
                      f'Type: {hardware.type}\n' \
                      f'Software Components: ' \
                      f'{", ".join(list(map(lambda x: x.name, hardware.software_components))) if hardware.software_components else None}'
        return result

