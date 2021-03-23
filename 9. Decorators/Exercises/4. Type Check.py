import functools


def type_check(type):
    def my_func(func):
        @functools.wraps(func)
        def decorator(*args):
            if not isinstance(*args, type):
                return 'Bad Type'
            return func(*args)

        return decorator
    return my_func


# @type_check(int)
# def times2(num):
#     return num * 2
#
#
# print(times2(2))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

