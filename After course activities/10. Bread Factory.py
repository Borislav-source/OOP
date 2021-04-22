from collections import deque

events = deque(input().split('|'))
energy = 100
coins = 100
ingredients = []


while events:
    event_ingredient, value = events.popleft().split('-')
    value = int(value)
    if event_ingredient == 'rest':
        if energy + value > 100:
            print(f'You gained {100-energy} energy.')
            energy = 100
        else:
            energy += value
            print(f'You gained {value} energy.')
        print(f'Current energy: {energy}.')
    elif event_ingredient == 'order':
        energy -= 30
        if energy >= 0:
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 80
            print('You had to rest!')
    else:
        coins -= value
        if coins <= 0:
            print(f'Closed! Cannot afford {event_ingredient}.')
            break
        else:
            print(f'You bought {event_ingredient}.')

if not coins <= 0:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")