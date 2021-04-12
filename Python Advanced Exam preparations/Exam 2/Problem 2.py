def create_board():
    matrix = []
    for _ in range(8):
        matrix.append(list(input().split()))
    return matrix


def find_king_on_the_board(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'K':
                return row, col


def look_down_for_queens(matrix, row, col):
    for r in range(row, len(matrix)):
        if matrix[r][col] == 'Q':
            result = [r, col]
            list_of_queens.append(result)
            return


def look_up_for_queens(matrix, row, col):
    for r in range(row, -1, -1):
        if matrix[r][col] == 'Q':
            result = [r, col]
            list_of_queens.append(result)
            return


def look_left_for_queens(matrix, row, col):
    for c in range(col, len(matrix[row])):
        if matrix[row][c] == 'Q':
            result = [row, c]
            list_of_queens.append(result)
            return


def look_right_for_queens(matrix, row, col):
    for c in range(col, -1, -1):
        if matrix[row][c] == 'Q':
            result = [row, c]
            list_of_queens.append(result)
            return


def look_up_right_diagonal_for_queens(matrix, row, col):
    for r in range(row-1, -1, -1):
        if col + 1 in range(len(matrix[row])):
            col += 1
            if matrix[r][col] == 'Q':
                result = [r, col]
                list_of_queens.append(result)
                return
        else:
            return


def look_up_left_diagonal_for_queens(matrix, row, col):
    for r in range(row-1, -1, -1):
        if col - 1 in range(len(matrix[row])):
            col -= 1
            if matrix[r][col] == 'Q':
                result = [r, col]
                list_of_queens.append(result)
                return
        else:
            return


def look_down_right_diagonal_for_queens(matrix, row, col):
    for r in range(row+1, len(matrix)):
        if col + 1 in range(len(matrix[row])):
            col += 1
            if matrix[r][col] == 'Q':
                result = [r, col]
                list_of_queens.append(result)
                return
        else:
            return


def look_down_left_diagonal_for_queens(matrix, row, col):
    for r in range(row+1, len(matrix)):
        if col - 1 in range(len(matrix[row])):
            col -= 1
            if matrix[r][col] == 'Q':
                result = [r, col]
                list_of_queens.append(result)
                return
        else:
            return


def find_queens_that_can_capture_the_king(board, list_of_queens, k_row, k_col):
    look_down_for_queens(board, k_row, k_col)
    look_up_for_queens(board, k_row, k_col)
    look_left_for_queens(board, k_row, k_col)
    look_right_for_queens(board, k_row, k_col)
    look_up_right_diagonal_for_queens(board, k_row, k_col)
    look_up_left_diagonal_for_queens(board, k_row, k_col)
    look_down_right_diagonal_for_queens(board, k_row, k_col)
    look_down_left_diagonal_for_queens(board, k_row, k_col)
    return list_of_queens


board = create_board()
k_row, k_col = find_king_on_the_board(board)
list_of_queens = []
find_queens_that_can_capture_the_king(board, list_of_queens, k_row, k_col)
if list_of_queens:
    for row in list_of_queens:
        print(row)
else:
    print('The king is safe!')
