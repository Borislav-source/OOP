# def recursive_power(num, n, result=1):
#     if n == 1:
#         return result * num
#
#     result = recursive_power(num, n-1, result)
#     return result * num
#
#
# print(recursive_power(2, 10))


def recursive_power(num, n):
    if n == 1:
        return num

    return num * recursive_power(num, n-1)


print(recursive_power(2, 10))