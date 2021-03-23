import functools


def even_parameters(func):
    @functools.wraps(func)
    def decorator(*args):
        for el in list(args):
            if not isinstance(el, int) or not el % 2 == 0:
                return 'Please use only even numbers!'
        result = func(*args)
        return result

    return decorator


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
