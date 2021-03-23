import functools


def logged(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        input_str = ', '.join(list(map(str, args))) + ', '.join(f'{value}' for key, value in kwargs.items())
        return f'you called {func.__name__}({input_str})\nit returned {result}'
    return decorator


# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
