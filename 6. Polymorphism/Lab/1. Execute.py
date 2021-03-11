def execute(func, *args):
    return func(*args)


def say_hello(*args):
    name, my_name = args
    print(f'Hello, {name}, I am {my_name}')


def say_bye(name):
    return print(f'Bye, {name}')


execute(say_hello, "Peter", "George")
execute(say_bye, "Peter")
