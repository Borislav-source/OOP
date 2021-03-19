# Iterator
class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iteration = 0
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration >= self.count:
            raise StopIteration
        self.iteration += 1
        self.value += self.step
        return self.value - self.step

# Generator
# def take_skip(step, count):
#     n = 0
#     value = 0
#     while n < count:
#         n += 1
#         yield value
#         value += step

#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)


