from collections import deque

males_sequence = [int(el) for el in input().split()]
females_sequence = [int(el) for el in input().split()]

matches = 0

for m in range(len(males_sequence)):
    if males_sequence[m] % 25 == 0:
        males_sequence[m] = 0
        if not m == 0:
            males_sequence[m-1] = 0
males_sequence = [i for i in males_sequence if not i == 0]

for f in range(len(females_sequence)):
    if females_sequence[f] % 25 == 0:
        females_sequence[f] = 0
        if not f + 1 == len(females_sequence):
            females_sequence[f+1] = 0
females_sequence = [i for i in females_sequence if not i == 0]
females_sequence = deque(females_sequence)


def chose_female_member(sequence):
    member = 0
    while member <= 0:
        try:
            member = sequence.popleft()
        except:
            return None
    member = validate_female_member(member)
    return member


def chose_male_member(sequence):
    member = 0
    while member <= 0:
        try:
            member = sequence.pop()
        except:
            return None
    member = validate_male_member(member)
    return member


def validate_female_member(member):
    if member % 25 == 0:
        for i in range(2):
            member = chose_female_member(females_sequence)
    return member


def validate_male_member(member):
    if member % 25 == 0:
        for i in range(2):
            member = chose_male_member(males_sequence)
    return member


while females_sequence and males_sequence:
    female = chose_female_member(females_sequence)
    if female is None:
        break
    male = chose_male_member(males_sequence)
    if male is None:
        break

    if female == male:
        matches += 1
    else:
        male -= 2
        if male > 0:
            males_sequence.append(male)

print(f'Matches: {matches}')
if not males_sequence:
    print('Males left: none')
else:
    print(f'Males left: {", ".join(list(map(str, reversed(males_sequence))))}')
if not females_sequence:
    print('Females left: none')
else:
    print(f'Females left: {", ".join(list(map(str, females_sequence)))}')


