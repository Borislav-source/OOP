jobs = list(map(int, input().split(', ')))
index_of_chosen_job = int(input())
value = jobs[index_of_chosen_job]
cycles_amount = 0
for num in sorted(jobs):
    if num <= value:
        cycles_amount += num
    else:
        break

print(cycles_amount)
