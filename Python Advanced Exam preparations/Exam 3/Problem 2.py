def matrix_generator():
    rows_count = int(input())
    matrix = []
    for _ in range(rows_count):
        matrix.append(['-']*rows_count)
    return matrix


def place_bombs_on_the_board(matrix):
    bombs_count = int(input())
    for _ in range(bombs_count):
        row, col = input().strip('()').split(', ')
        matrix[int(row)][int(col)] = '*'
    return matrix


def check_for_surrounding_bombs(matrix, row, col):
    bombs_count = 0
    for r in range(-1, 2):
        if row + r in range(len(matrix)):
            for c in range(-1, 2):
                if col + c in range(len(matrix[row])):
                    if matrix[row + r][col + c] == '*':
                        bombs_count += 1
    return bombs_count


def calculate_each_cell_number(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not matrix[row][col] == '*':
                matrix[row][col] = check_for_surrounding_bombs(matrix, row, col)


def printing_results(matrix):
    for row in matrix:
        print(*row)


board = matrix_generator()
place_bombs_on_the_board(board)
calculate_each_cell_number(board)
printing_results(board)