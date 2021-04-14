def best_list_pureness(sequence, k):
    best_pureness = 0
    rotations = 0
    for rotation in range(k+1):
        current_result = 0
        for index in range(len(sequence)):
            current_result += index * sequence[index]
        if current_result > best_pureness:
            best_pureness = current_result
            rotations = rotation
        value = sequence.pop()
        sequence.insert(0, value)
    return f"Best pureness {best_pureness} after {rotations} rotations"


test = ([4, 3, 2, 6], 1)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
