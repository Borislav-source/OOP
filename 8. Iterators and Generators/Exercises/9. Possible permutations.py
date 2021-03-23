from itertools import permutations


def possible_permutations(seq):
    for lst in permutations(seq):
        yield list(lst)


[print(n) for n in possible_permutations([1, 2, 3])]


# def possible_permutations(seq, index=0):
#     if index == len(seq):
#         print(seq)
#         return
#     for i in range(index, len(seq)):
#         seq[i], seq[index] = seq[index], seq[i]
#         possible_permutations(seq, index+1)
#         seq[i], seq[index] = seq[index], seq[i]
#
#
# possible_permutations(list('abc'))