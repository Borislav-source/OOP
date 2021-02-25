def factorial(num):

    result = 1
    for n in range(num, 0, -1):
        result *= n
    return result


print(factorial(5))


# def factorial(num, result=1):
#     if num == 1:
#         quit(print(result))
#     result *= num
#     factorial(num-1, result)
#     # return result
#
#
# print(factorial(5))


def factorial(num):
    if num == 1:
        return num

    return num * factorial(num-1)
    # return result


print(factorial(5))


def factorial(num):
    if num <= 1:
        return 1
    else:
        a = (factorial(num-1))
        return num * a


print(factorial(5))
