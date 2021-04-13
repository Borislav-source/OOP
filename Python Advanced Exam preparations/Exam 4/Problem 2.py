def matrix_generator():
    matrix = []
    rows_count = int(input())
    for _ in range(rows_count):
        matrix.append(list(input()))
    return matrix


def find_snake_on_the_board(matrix, symbol_to_look_for):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == symbol_to_look_for:
                return row, col


def snake_move(matrix, row, col):
    global eaten_food
    if matrix[row][col] == '*':
        matrix[row][col] = 'S'
        eaten_food += 1
        return row, col
    elif matrix[row][col] == 'B':
        matrix[row][col] = '.'
        row, col = find_snake_on_the_board(matrix, 'B')
        matrix[row][col] = 'S'
        return row, col
    return row, col


def play(matrix, row, col):
    while eaten_food < 10:
        command = input()
        matrix[row][col] = '.'
        if command == 'up':
            if row - 1 in range(len(matrix)):
                row, col = snake_move(matrix, row - 1, col)
            else:
                return
        elif command == 'down':
            if row + 1 in range(len(matrix)):
                row, col = snake_move(matrix, row + 1, col)
            else:
                return
        elif command == 'left':
            if col - 1 in range(len(matrix[row])):
                row, col = snake_move(matrix, row, col - 1)
            else:
                return
        elif command == 'right':
            if col + 1 in range(len(matrix[row])):
                row, col = snake_move(matrix, row, col + 1)
            else:
                return


def printing_result(matrix):
    if eaten_food < 10:
        print('Game over!')
    else:
        print('You won! You fed the snake.')
    print(f'Food eaten: {eaten_food}')
    for row in board:
        print(''.join(row))


global eaten_food
eaten_food = 0
board = matrix_generator()
s_row, s_col = find_snake_on_the_board(board, 'S')
play(board, s_row, s_col)
printing_result(board)