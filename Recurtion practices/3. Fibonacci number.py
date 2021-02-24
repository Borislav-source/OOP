from functools import lru_cache
# def fibonacci(num, my_list=[0, 1], n=1):
#     if n == num:
#         return
#     result = my_list[-1] + my_list[-2]
#     my_list.append(result)
#     fibonacci(num, my_list, n+1)
#     return my_list[-1]
#
#
# print(fibonacci(900))


@lru_cache(maxsize=1000)
def fibonacci(num):
    if 1 == num or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(500))
