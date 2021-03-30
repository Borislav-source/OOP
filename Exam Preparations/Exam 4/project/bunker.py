from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = self.sort_the_supplies(self.supplies, FoodSupply)
        if not foods:
            raise IndexError('There are no food supplies left!')
        return foods

    @property
    def water(self):
        waters = self.sort_the_supplies(self.supplies, WaterSupply)
        if not waters:
            raise IndexError('There are no water supplies left!')
        return waters

    @property
    def painkillers(self):
        p_killers = self.sort_the_supplies(self.medicine, Painkiller)
        if not p_killers:
            raise IndexError('There are no painkillers left!')
        return p_killers

    @property
    def salves(self):
        salves_list = self.sort_the_supplies(self.medicine, Salve)
        if not salves_list:
            raise IndexError('There are no salves left!')
        return salves_list

    @staticmethod
    def sort_the_supplies(list_of_objects, instance):
        sorted_supplies = []
        for sup in list_of_objects:
            if isinstance(sup, instance):
                sorted_supplies.append(sup)
        return sorted_supplies

    def __find_type(self, type_):
        if type_ == 'FoodSupply':
            return self.food
        elif type_ == 'WaterSupply':
            return self.water
        elif type_ == 'Painkiller':
            return self.painkillers
        else:
            return self.salves

    def __take_the_last_element_of_certain_type_from_sequence_list(self, type_):
        the_type = self.__find_type(type_)
        return the_type.pop()

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        current_med = self.__take_the_last_element_of_certain_type_from_sequence_list(medicine_type)
        if current_med:
            self.medicine.remove(current_med)
            if survivor.needs_healing:
                survivor.health += current_med.health_increase
                return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        current_sustenance = self.__take_the_last_element_of_certain_type_from_sequence_list(sustenance_type)
        if current_sustenance:
            self.supplies.remove(current_sustenance)
            if survivor.needs_sustenance:
                survivor.needs += current_sustenance.needs_increase
                return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            food = self.food.pop()
            water = self.water.pop()
            food.apply(survivor)
            water.apply(survivor)
