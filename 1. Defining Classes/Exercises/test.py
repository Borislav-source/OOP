a = [2, 4, 5, 6, 8]

for i in a:
    if i % 2 == 0:
        a.remove(i)
print(a)

# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         a[i] = None
# a = [i for i in a if i is not None]
# print(a)