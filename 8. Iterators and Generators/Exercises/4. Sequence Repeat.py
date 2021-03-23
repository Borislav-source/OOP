# With Iterator
class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if 0 == self.number:
            raise StopIteration
        self.number -= 1
        index = self.index
        self.index += 1
        if self.index == len(self.sequence):
            self.index = 0
        return self.sequence[index]
#
#
# result = sequence_repeat('abcd', 10)
# for item in result:
#     print(item, end ='')

# With Generator
# def sequence_repeat(seq, number):
#     index = 0
#     while number > 0:
#         number -= 1
#         yield seq[index]
#         index += 1
#         if index == len(seq):
#             index = 0


# result = sequence_repeat('abcd', 10)
# for item in result:
#     print(item, end ='')
