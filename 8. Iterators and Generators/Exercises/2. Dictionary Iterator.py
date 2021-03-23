# Made with Iterator


class dictionary_iter:
    def __init__(self, obj):
        self.obj = obj
        self.length = len(self.obj)
        self.keys = list(self.obj)
        self.index = 0
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration == self.length:
            raise StopIteration
        self.iteration += 1
        index = self.index
        self.index += 1
        return self.keys[index], self.obj[self.keys[index]]

# Made with Generator


def dictionary_generator(my_dict):
    for key in my_dict:
        yield key, my_dict[key]


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)


# result = dictionary_generator({1: "1", 2: "2"})
# for x in result:
#     print(x)

