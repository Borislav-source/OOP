def list_manipulator(sequence: list, *args):
    command, info, *values = args
    if command == 'remove':
        value = 1
        if values:
            value = values[0]
        if info == 'beginning':
            sequence = sequence[value:]
        else:
            sequence = sequence[:-value]
        return sequence

    if info == 'beginning':
        sequence = values + sequence
    else:
        sequence = sequence + values
    return sequence


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
