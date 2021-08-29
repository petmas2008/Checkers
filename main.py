"""
This program is an attempt to recreate the game checkers.
It consists of a 8*8 board and each player has 12 pieces
which are arranged in an offset pattern. Pieces can only move
diagonally forward once. If the the oppositions piece is adjacent
to their piece and there is a space behind it in the same direction
they can then eliminate that piece. If there are multiple pieces lined up
they can do the same. If a piece reaches the opposing king row then
that piece becomes a king and can move diagonally in any direction.
"""
from pprint import pprint
import pygame

pygame.init()

screen = pygame.display.set_mode([400, 400])
running = True
cur_player = 2
board = [['e', 'p2', 'e', 'p2', 'e', 'p2', 'e', 'p2'],
         ['p2', 'e', 'p2', 'e', 'p2', 'e', 'p2', 'e'],
         ['e', 'p2', 'e', 'p2', 'e', 'p2', 'e', 'p2'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['p1', 'e', 'p1', 'e', 'p1', 'e', 'p1', 'e'],
         ['e', 'p1', 'e', 'p1', 'e', 'p1', 'e', 'p1'],
         ['p1', 'e', 'p1', 'e', 'p1', 'e', 'p1', 'e']
         ]


def check_start_pos(cur_player, start_pos):
    x, y = start_pos
    if cur_player == 1:
        if board[y][x] == "p1":
            return True
        else:
            return False
    else:
        if board[y][x] == "p2":
            return True
        else:
            return False


def check_end_pos(cur_player, start_pos, end_pos, current_casualties):
    sx, sy = start_pos
    ex, ey = end_pos
    print("Start pos: ", sx, sy, "-", board[sy][sx])
    print("End pos: ", ex, ey, "-", board[ey][ex])
    print(board[ey+1][ex-1])

    if cur_player == 1:
        if board[ey][ex] == "e":
            if (ex - 1, ey + 1) == (sx, sy):
                return True
            elif (ex + 1, ey + 1) == (sx, sy):
                return True
            elif board[ey+1][ex+1] == "p2":
                if (ex + 2, ey + 2) == (sx, sy):
                    current_casualties.append((ey+1, ex+1))
                    return True
            elif board[ey+1][ex-1] == "p2":
                print(ex + 2, ey - 2, sx, sy)
                if (ex - 2, ey + 2) == (sx, sy):
                    print("HEllo your reached me")
                    current_casualties.append((ey+1, ex-1))
                    return True
        elif board[ey][ex] == "p2":
            return False
        else:
            return False
    else:
        if board[ey][ex] == "e":
            if (ex - 1, ey - 1) == (sx, sy):
                return True
            elif (ex + 1, ey - 1) == (sx, sy):
                return True
            elif board[ey-1][ex-1] == "p1":
                if (ex - 2, ey - 2) == (sx, sy):
                    current_casualties.append((ey-1, ex-1))
                    return True
            elif board[ey-1][ex+1] == "p1":
                if (ex - 2, ey + 2) == (sx, sy):
                    current_casualties.append(ey-1, ex+1)
                    return True
        elif board[ey][ex] == "p1":
            return False
        else:
            return False


def execute_move(cur_player, start_pos, end_pos, current_casualties):
    sx, sy = start_pos
    ex, ey = end_pos
    if cur_player == 1:
        board[sy][sx] = "e"
        board[ey][ex] = "p1"
    else:
        board[sy][sx] = "e"
        board[ey][ex] = "p2"
    for (x, y) in current_casualties:
        board[y][x] = "e"


def return_error_message():
    print("Well that did not work")


def get_move(cur_player, current_casualties):
    while True:
        start_pos = input("Enter the starting piece that you want to move: ").split()
        start_pos = int(start_pos[0]), int(start_pos[1])
        if check_start_pos(cur_player, start_pos):
            end_pos = input("Enter where you want to move your piece: ").split()
            end_pos = int(end_pos[0]), int(end_pos[1])
            if check_end_pos(cur_player, start_pos, end_pos, current_casualties):
                execute_move(cur_player, start_pos, end_pos, current_casualties)
                return
            else:
                return_error_message()
        else:
            return_error_message()


# def players():
#     while True:
#         yield 1
#         yield 2
#
#
# def run():
#     for cur_player in players():
#         current_casualties = []
#         print("Current player:", str(cur_player))
#         get_move(cur_player, current_casualties)
#         pprint(board)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cur_player == 1:
        cur_player = 2
    elif cur_player == 2:
        cur_player = 1

    # current_casualties = []
    # print("Current player:", str(cur_player))
    # get_move(cur_player, current_casualties)
    # pprint(board)

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()
# run()