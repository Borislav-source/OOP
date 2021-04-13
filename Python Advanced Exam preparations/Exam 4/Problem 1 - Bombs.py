from collections import deque

mapper = {
    40: [],
    60: [],
    120: [],
}
completed = False

bombs_effects = list(map(int, input().split(', ')))
bombs_casings = list(map(int, input().split(', ')))
bombs_effects = deque(bombs_effects)

while bombs_effects and bombs_casings:
    effect = bombs_effects.popleft()
    casing = bombs_casings.pop()
    result = effect + casing
    if result in mapper:
        mapper[result].append(1)
    else:
        casing -= 5
        bombs_effects.insert(0, effect)
        if casing >= 0:
            bombs_casings.append(casing)
    if all(len(mapper[key]) >= 3 for key in mapper):
        completed = True
        break


if completed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
print(f'Bomb Effects: {", ".join(set(map(str, bombs_effects))) if bombs_effects else "empty"}')
print(f'Bomb Casings: {", ".join(set(map(str, bombs_casings))) if bombs_casings else "empty"}')
print(f'''Cherry Bombs: {len(mapper[60])}
Datura Bombs: {len(mapper[40])}
Smoke Decoy Bombs: {len(mapper[120])}
''')