import numpy as np
import pygame
import sys

ROWS_COUNT = 7
COLUMNS_COUNT = 7
BLUE = (0, 0, 255)


# Todo Create the board
def create_board():
    return np.zeros((ROWS_COUNT, COLUMNS_COUNT))


# Todo Check and add piece
def is_valid(matrix, column):
    return matrix[1][column] == 0


def get_the_row(matrix, column):
    for row in range(len(matrix)-1, -1, -1):
        if matrix[row][column] == 0:
            return row


def add_piece(matrix, row, column, piece):
    matrix[row][column] = piece


# Todo Check for winning sequence
def is_winning(matrix, r, column, piece):
    horizontal = horizontal_check(matrix, r, column, piece)
    vertical = vertical_check(matrix, r, column, piece)
    opposite = opposite_diagonal(matrix, r, column, piece)
    main = main_diagonal(matrix, r, column, piece)
    check_list = [horizontal, vertical, opposite, main]
    return any(check_list)


def horizontal_check(matrix, r, column, piece):
    the_sum = 0
    # Right check
    for c in range(column, len(matrix[r])):
        if matrix[r][c] == piece:
            the_sum += 1
        else:
            break
    # Left check
    for c in range(column-1, -1, -1):
        if matrix[r][c] == piece:
            the_sum += 1
        else:
            break
    print(f'horizontal: {the_sum}')
    return the_sum >= 4


def vertical_check(matrix, r, column, piece):
    the_sum = 0
    for row in range(r, len(matrix)):
        if matrix[row][column] == piece:
            the_sum += 1
        else:
            print(f'vertical: {the_sum}')
            return the_sum == 4


def main_diagonal(matrix, r, column, piece):
    the_sum = 1
    col = column
    # Main diagonal UP-Left
    for row in range(r-1, -1, -1):
        col -= 1
        if matrix[row][col] == piece:
            the_sum += 1
        else:
            break
    # Main diagonal Down-Right
    for row in range(r+1, len(matrix)):
        column += 1
        if matrix[row][column] == piece:
            the_sum += 1
        else:
            break
    print(f'main diagonal: {the_sum}')
    return the_sum >= 4


def opposite_diagonal(matrix, r, column, piece):
    the_sum = 1
    col = column
    # Opposite diagonal Up-Right
    for row in range(r-1, -1, -1):
        col += 1
        if matrix[row][col] == piece:
            the_sum += 1
        else:
            break
    # Opposite diagonal Down-Left
    for row in range(r+1, len(matrix)):
        column -= 1
        if matrix[row][column] == piece:
            the_sum += 1
        else:
            break
    print(f'opposite diagonal: {the_sum}')
    return the_sum >= 4


# Todo draw the board
def draw_board(matrix):
    for r in range(1, ROWS_COUNT):
        for c in range(COLUMNS_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE, 100, 100))
            if matrix[r][c] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif matrix[r][c] == 1:
                pygame.draw.circle(screen, (255, 0, 0),
                                   (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif matrix[r][c] == 2:
                pygame.draw.circle(screen, (255, 255, 0),
                                   (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


board = create_board()
turn = 0
end_game = False

pygame.init()

SQUARESIZE = 100
RADIUS = (SQUARESIZE // 2) - 5

width = COLUMNS_COUNT * SQUARESIZE
height = ROWS_COUNT * SQUARESIZE

size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

# Todo Play
while not end_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Todo Ask player one for move
            if not turn:
                posx = event.pos[0]
                col = int(posx//SQUARESIZE)

                if is_valid(board, col):
                    row = get_the_row(board, col)
                    add_piece(board, row, col, 1)
                else:
                    print('Sorry! This column is full. Please choose another!')
                    continue

                if is_winning(board, row, col, 1):
                    end_game = True

            # Todo Ask player two for move
            else:
                posx = event.pos[0]
                col = int(posx // SQUARESIZE)

                if is_valid(board, col):
                    row = get_the_row(board, col)
                    add_piece(board, row, col, 2)
                else:
                    print('Sorry! This column is full. Please choose another!')
                    continue

                if is_winning(board, row, col, 2):
                    end_game = True
            draw_board(board)
            print(board)
            turn += 1
            turn %= 2

