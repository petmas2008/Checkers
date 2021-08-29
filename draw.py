import pygame


def draw_board(screen):
    cell_size = screen.get_width() // 8, screen.get_height() // 8
    for y in range(8):
        for x in range(8):
            pass

    for cell in range(8):
        row_cell = cell * cell_size[0]

        pygame.draw.line(screen,
             (255, 255, 255),
             (row_cell, 0),
             (row_cell, screen.get_height()))

    for cell in range(8):
        col_cell = cell * cell_size[1]

        pygame.draw.line(screen,
            (255, 255, 255),
            (0, col_cell),
            (screen.get_height(), col_cell))


def draw_pieces(screen, board):
    cell_size = screen.get_width() // 8, screen.get_height() // 8
    circle_radius = cell_size[0] // 2
    white = (255, 255, 255)
    red = (255, 0, 0)
    for y in range(8):
        for x in range(8):
            circle_pos = (circle_radius + cell_size[0] * x, circle_radius + cell_size[1] * y)
            if board[y][x] == "p1":
                pygame.draw.circle(screen, white, circle_pos, circle_radius)
            elif board[y][x] == "p2":
                pygame.draw.circle(screen, red, circle_pos, circle_radius)
