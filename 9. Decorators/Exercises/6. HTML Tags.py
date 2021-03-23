def tags(tag):
    def wrapper(func):
        def decorator(*args):
            result = func(*args)
            return f'<{tag}>{result}</{tag}>'
        return decorator
    return wrapper


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
