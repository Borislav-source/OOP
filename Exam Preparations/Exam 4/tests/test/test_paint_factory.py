import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory(name='Sharo', capacity=5)

    def test_paint_factory_if_all_attributes_are_set_correctly(self):
        self.assertEqual('Sharo', self.factory.name)
        self.assertEqual(5, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual({}, self.factory.products)
        # self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_paint_factory_add_ingredient_if_is_NOT_in_ingredients_list(self):
        with self.assertRaises(Exception) as ex:
            self.factory.add_ingredient('pink', 5)
        self.assertEqual("Ingredient of type pink not allowed in PaintFactory", str(ex.exception))

    def test_paint_factory_add_ingredient_if_capacity_is_NOT_enough(self):
        with self.assertRaises(Exception) as ex:
            self.factory.add_ingredient('white', 10)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_paint_factory_add_ingredient_if_ingredient_type_NOT_in_ingredients_dict(self):
        self.assertTrue('white' not in self.factory.ingredients)
        self.factory.add_ingredient('white', 3)
        self.assertTrue('white' in self.factory.ingredients)
        self.assertEqual(3, self.factory.ingredients['white'])

    def test_paint_factory_remove_ingredient_if_ingredient_type_NOT_in_ingredients_dict(self):
        with self.assertRaises(Exception) as ex:
            self.factory.remove_ingredient('white', 3)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_paint_factory_remove_ingredients_if_quantity_is_bigger_than_capacity(self):
        self.factory.ingredients['white'] = 5
        with self.assertRaises(Exception) as ex:
            self.factory.remove_ingredient('white', 6)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_paint_factory_remove_ingredients_if_all_conditions_are_covered(self):
        self.factory.ingredients['white'] = 5
        self.factory.remove_ingredient('white', 3)
        self.assertEqual(2, self.factory.ingredients['white'])
#
#
# from abc import ABC, abstractmethod
#
#
# class Factory(ABC):
#     @abstractmethod
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.ingredients = {}
#
#     @abstractmethod
#     def add_ingredient(self, type, quantity):
#         """Add products to the factory"""
#         pass
#
#     @abstractmethod
#     def remove_ingredient(self, type, quantity):
#         """Remove products from the factory"""
#         pass
#
#     def can_add(self, value):
#         return self.capacity - sum(self.ingredients.values()) - value >= 0
#
#     def __repr__(self):
#         result = ""
#         result += f"Factory name: {self.name} with capacity {self.capacity}.\n"
#         for ingredient in self.ingredients:
#             result += f"{ingredient}: {self.ingredients[ingredient]}\n"
#         return result
#
#
# class PaintFactory(Factory):
#     def __init__(self, name, capacity):
#         super().__init__(name, capacity)
#
#     def add_ingredient(self, product_type, product_quantity):
#         if product_type in ["white", "yellow", "blue", "green", "red"]:
#             if self.can_add(product_quantity):
#                 if product_type not in self.ingredients:
#                     self.ingredients[product_type] = 0
#                 self.ingredients[product_type] += product_quantity
#             else:
#                 raise ValueError("Not enough space in factory")
#         else:
#             raise TypeError(f"Ingredient of type {product_type} not allowed in {self.__class__.__name__}")
#
#     def remove_ingredient(self, product_type, product_quantity):
#         if product_type in self.ingredients:
#             if self.ingredients[product_type] - product_quantity >= 0:
#                 self.ingredients[product_type] -= product_quantity
#             else:
#                 raise ValueError("Ingredients quantity cannot be less than zero")
#         else:
#             raise KeyError("No such ingredient in the factory")
#
#     @property
#     def products(self):
#         return self.ingredients
#
#
# # from project.factory.paint_factory import PaintFactory
# # class Test:
# #    pass
