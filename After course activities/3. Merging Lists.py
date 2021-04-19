first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
result = []
for index in range(len(first_list) + len(second_list)):
    try:
        result.append(first_list[index])
    except:
        pass
    try:
        result.append(second_list[index])
    except:
        pass
print(result)