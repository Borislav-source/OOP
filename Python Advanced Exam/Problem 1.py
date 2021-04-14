from collections import deque

pizza_orders = list(map(int, input().split(', ')))
employees = list(map(int, input().split(', ')))
pizza_orders = [order for order in pizza_orders if 0 < order <= 10]
pizza_orders = deque(pizza_orders)
total_pizzas = 0

while employees and pizza_orders:
    order = pizza_orders.popleft()
    employee = employees.pop()
    if order <= employee:
        total_pizzas += order
        continue
    else:
        order -= employee
        pizza_orders.insert(0, order)
        total_pizzas += employee

if not pizza_orders:
    print(f'''All orders are successfully completed!
Total pizzas made: {total_pizzas}
Employees: {", ".join(list(map(str, employees)))}
''')
else:
    print(f'''Not all orders are completed.
Orders left: {", ".join(list(map(str, pizza_orders)))}
''')
