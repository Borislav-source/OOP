from collections import deque

customers = list(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))
customers = deque(customers)
total_time = 0

while customers and taxis:
    customer = customers.popleft()
    taxi = taxis.pop()
    if taxi >= customer:
        total_time += customer
    else:
        customers.insert(0, customer)

if not customers:
    print(f'''All customers were driven to their destinations
Total time: {total_time} minutes
''')
else:
    print(f'''Not all customers were driven to their destinations
Customers left: {", ".join(list(map(str, customers)))}
''')