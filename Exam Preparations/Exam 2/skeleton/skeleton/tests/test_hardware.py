import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware(name='HDD', type='PowerHardware', capacity=200, memory=200)
        self.software = Software("HDD", "LightSoftware", 0, 10)

    def test_hardware_if_all_attributes_are_set(self):
        self.assertEqual('HDD', self.hardware.name)
        self.assertEqual('PowerHardware', self.hardware.type)
        self.assertEqual(200, self.hardware.capacity)
        self.assertEqual(200, self.hardware.memory)

    def test_hardware_install_if_there_is_enough_capacity_and_memory(self):
        self.hardware.install(self.software)
        self.assertTrue(self.software in self.hardware.software_components)

    def test_hardware_install_if_there_is_NOT_enough_capacity_and_memory(self):
        self.software.memory_consumption = 250
        with self.assertRaises(Exception) as ex:
            self.hardware.install(self.software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    def test_hardware_uninstall_if_software_is_in_software_components(self):
        self.hardware.install(self.software)
        self.assertTrue(self.software in self.hardware.software_components)
        self.hardware.uninstall(self.software)
        self.assertTrue(self.software not in self.hardware.software_components)


