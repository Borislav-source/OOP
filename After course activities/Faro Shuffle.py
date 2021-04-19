sequence = input().split()
k = int(input())

middle_of_sequence = len(sequence) // 2

for _ in range(k):
    list_one = sequence[:middle_of_sequence]
    list_two = sequence[middle_of_sequence:]
    result = []
    for index in range(middle_of_sequence):
        result.append(list_one[index])
        result.append(list_two[index])
    sequence = result
print(sequence)