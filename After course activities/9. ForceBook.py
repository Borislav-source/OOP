command = input()
forceBook = {}


def check_if_user_is_in_the_forcebook(user):
    for side, users in forceBook.items():
        if user in users:
            return side


def add_user(user, side):
    if side not in forceBook:
        forceBook[side] = []
    previous_side = check_if_user_is_in_the_forcebook(user)
    if not previous_side:
        forceBook[side].append(user)


def transfer_user(user, previous_side, side):
    forceBook[previous_side].remove(user)
    forceBook[side].append(user)


while not command == 'Lumpawaroo':
    if ' | ' in command:
        forceSide, forceUser = command.split(' | ')
        add_user(forceUser, forceSide)
    else:
        forceUser, forceSide = command.split(' -> ')
        previous_side = check_if_user_is_in_the_forcebook(forceUser)
        if previous_side:
            transfer_user(forceUser, previous_side, forceSide)
        else:
            add_user(forceUser, forceSide)
    command = input()

for side in dict(sorted(forceBook.items(), key=lambda x: (-len(x[1]), x[0]))):
    if len(forceBook[side]):
        print(f"Side: {side}, Members: {len(forceBook[side])}")
        for member in sorted(forceBook[side]):
            print(f'! {member}')

