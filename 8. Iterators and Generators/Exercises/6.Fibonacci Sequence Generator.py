# def fibonacci(n=0):
#     sequence = []
#     n = 0
#     while True:
#         yield n
#         sequence.append(n)
#         if n == 0:
#             n += 1
#         else:
#             n += sequence[-2]
#
#
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))


def fibonacci():
    previous_num, current_num = 0, 1
    while True:
        yield current_num
        previous_num, current_num = current_num, previous_num + current_num


generator = fibonacci()
for i in range(5):
    print(next(generator))