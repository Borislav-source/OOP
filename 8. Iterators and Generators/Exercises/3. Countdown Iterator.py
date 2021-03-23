# class countdown_iterator:
#     def __init__(self, count: int):
#         self.count = count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count < 0:
#             raise StopIteration
#         value = self.count
#         self.count -= 1
#         return value
#
#
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")


# def countdown_generator(count):
#     while True:
#         if count < 0:
#             return
#         yield count
#         count -= 1
#
#
# iterator = countdown_generator(10)
# for item in iterator:
#     print(item, end=" ")