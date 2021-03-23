import functools


def make_bold(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<b>{result}</b>'
    return decorator


def make_italic(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<i>{result}</i>'
    return decorator


def make_underline(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<u>{result}</u>'
    return decorator


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
