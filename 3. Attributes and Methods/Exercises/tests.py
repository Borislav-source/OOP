# class MyClass():
#     class_variable = 'Peppy'
#
#     def __init__(self, i_var):
#         self.instance_variable = i_var
#
#
# bobby = MyClass('2')
# cvety = MyClass(55)
# print(MyClass.__dict__)
# print(bobby.__dict__)
# print(MyClass.class_variable)
# print(hasattr(MyClass, 'class_variable'))
# print(getattr(MyClass, 'class_variable'))
# setattr(bobby, 'Kolyo', 5)
# print(getattr(bobby, 'Kolyo'))
# delattr(MyClass, 'class_variable')
# print(hasattr(MyClass, 'class_variable'))
# print(type(MyClass))
# print(type(bobby))
# try:
#     print(getattr(MyClass, 'class_variable'))
# except AttributeError:
#     print('MyClass has no such attribute')
#
# s = [1, 2, 3]
# print(s.__contains__('2'))
#
#
# class Robot:
#     counter = 0
#
#     def __init__(self):
#         type(self).counter += 1
#
#     @staticmethod
#     def robot_instances():
#         return Robot.counter
#
#
# print(Robot.robot_instances())
# x = Robot()
# print(Robot.robot_instances())
# y = Robot()
# print(Robot.robot_instances())
# print(x.robot_instances())
# print(y.robot_instances())
# print(type(Robot))
# print(type(x))
# print(type(y))
import datetime
date = '12.02.2012'
day, month, year = date.split('.')
datetime_object = datetime.datetime.strptime(month, "%m")
month_name = datetime_object.strftime("%B")
print(year)
print(day)
print(month_name)