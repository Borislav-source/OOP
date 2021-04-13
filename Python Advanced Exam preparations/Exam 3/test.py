# a = '(1, 2)'
# # a = a[1:-1]
# # a = tuple(a.split(', '))
# # row, col = a
# # print(row)
# # print(col)
#
# row, col = [int(s) for s in a if s.isdigit()]
# print(row)
# print(col)
#
# for r in range(-1, 2):
#     if row + r in range(len(matrix)):
#         for c in range(-1, 2):
#             if col + c in range(len(matrix[row])):
#                 if matrix[row + r][col + c] == '*':
#                     bombs_count += 1