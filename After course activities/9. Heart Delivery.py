neighborhood = list(map(int, input().split('@')))
data = input()
cupid_position_index = 0
while not data == 'Love!':
    length_of_jump = int(data.split()[1])
    cupid_position_index += length_of_jump
    if cupid_position_index not in range(len(neighborhood)):
        cupid_position_index = 0
    if neighborhood[cupid_position_index] is not 0:
        neighborhood[cupid_position_index] -= 2
        if neighborhood[cupid_position_index] <= 0:
            neighborhood[cupid_position_index] = 0
            print(f'Place {cupid_position_index} has Valentine\'s day.')
    else:
        print(f"Place {cupid_position_index} already had Valentine's day.")
    data = input()

print(f'Cupid\'s last position was {cupid_position_index}.')
neighborhood = [house for house in neighborhood if house > 0]
if neighborhood:
    print(f'Cupid has failed {len(neighborhood)} places.')
else:
    print('Mission was successful.')

