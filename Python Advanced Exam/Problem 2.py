def matrix_generator():
    rows_count = 7
    matrix = []
    for _ in range(rows_count):
        column = input().split()
        matrix.append(column)
    return matrix


def calculate_points(matrix, r, c, mark):
    values = [board[0][c], board[-1][c], board[r][0], board[r][-1]]
    result = sum(list(map(int, values)))
    if mark == 'D':
        result *= 2
    else:
        result *= 3
    return result


player_1, player_2 = input().split(', ')
points_mapper = {
    player_1: 501,
    player_2: 501
}
board = matrix_generator()
player_1_turn = 0
player_2_turn = 0
turn = 0
points = 0

while points_mapper[player_1] > 0 < points_mapper[player_2]:
    row, col = list(map(int, input().strip('()').split(', ')))
    if row in range(len(board)) and col in range(len(board[row])):
        if board[row][col] == 'D':
            points = calculate_points(board, row, col, 'D')
        elif board[row][col] == 'T':
            points = calculate_points(board, row, col, 'T')
        elif board[row][col] == 'B':
            if turn % 2 == 0:
                points_mapper[player_1] = 0
                player_1_turn += 1
            else:
                points_mapper[player_2] = 0
                player_2_turn += 1
            break
        else:
            points = int(board[row][col])

    if turn % 2 == 0:
        points_mapper[player_1] -= points
        player_1_turn += 1
    else:
        points_mapper[player_2] -= points
        player_2_turn += 1
    turn += 1

for player in points_mapper:
    if points_mapper[player] <= 0:
        if player == player_1:
            print(f"{player} won the game with {player_1_turn} throws!")
        else:
            print(f"{player} won the game with {player_2_turn} throws!")
