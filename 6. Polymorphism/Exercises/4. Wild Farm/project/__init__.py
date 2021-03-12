from project.animals.animal import Bird
from project.animals.birds import Owl, Hen
from project.animals.mammals import Tiger, Mouse, Cat
from project.food import Meat, Vegetable, Fruit, Food

#
#
# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)
# hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)
#
# tiger = Tiger('Diego', 300, 'Australia')
# print(tiger)
# print(tiger.make_sound())
# meat = Meat(10)
# tiger.feed(meat)
# print(tiger)
# veg = Vegetable(6)
# tiger.feed(meat)
# meat = Meat(6)
# tiger.feed(meat)
# print(tiger)
# tiger2 = Tiger('Leo', 200, 'Africa')
# print(tiger2)
# tiger2.feed(meat)
# print(tiger2)
# print(tiger)
#
fruit = Fruit(5)

mice = Cat('Henry', 10, 'Bulgaria')
print(mice)
meat = Meat(10)
print(mice.feed(meat))
print(mice.feed(veg))
print(mice.feed(fruit))
print(mice)

