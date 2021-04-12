def create_matrix():
    rows_count = int(input())
    board = []
    for i in range(rows_count):
        board += [list(input())]
    return board


def find_player_on_the_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'P':
                return row, col


message = input()
matrix = create_matrix()
player_row, player_col = find_player_on_the_board(matrix)
moves_count = int(input())

for _ in range(moves_count):
    move = input()
    if move == 'up':
        if player_row - 1 in range(len(matrix)):
            matrix[player_row][player_col] = '-'
            player_row -= 1
            if not matrix[player_row][player_col] == '-':
                message += matrix[player_row][player_col]
                matrix[player_row][player_col] = 'P'
        else:
            if message:
                message = message[:-1]
    elif move == 'down':
        if player_row + 1 in range(len(matrix)):
            matrix[player_row][player_col] = '-'
            player_row += 1
            if not matrix[player_row][player_col] == '-':
                message += matrix[player_row][player_col]
                matrix[player_row][player_col] = 'P'
        else:
            if message:
                message = message[:-1]
    elif move == 'left':
        if player_col - 1 in range(len(matrix[player_row])):
            matrix[player_row][player_col] = '-'
            player_col -= 1
            if not matrix[player_row][player_col] == '-':
                message += matrix[player_row][player_col]
                matrix[player_row][player_col] = 'P'
        else:
            if message:
                message = message[:-1]
    elif move == 'right':
        if player_col + 1 in range(len(matrix[player_row])):
            matrix[player_row][player_col] = '-'
            player_col += 1
            if not matrix[player_row][player_col] == '-':
                message += matrix[player_row][player_col]
                matrix[player_row][player_col] = 'P'
        else:
            if message:
                message = message[:-1]
print(message)
for row in matrix:
    print(''.join(row))