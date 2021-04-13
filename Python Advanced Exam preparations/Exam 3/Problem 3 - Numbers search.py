def numbers_searching(*args):
    list_of_numbers = list(args)
    result = []
    list_of_duplicates = []
    for number in list_of_numbers:
        if list_of_numbers.count(number) > 1 and number not in list_of_duplicates:
            list_of_duplicates.append(number)
    list_of_duplicates = sorted(list_of_duplicates)
    list_of_numbers = sorted(list_of_numbers)
    for number in range(list_of_numbers[0], list_of_numbers[-1]+1):
        if number not in list_of_numbers:
            result.append(number)
            break
    result.append(list_of_duplicates)
    return result


print(numbers_searching(1, 2))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(51, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 46, 48))
