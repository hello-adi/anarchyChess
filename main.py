from platform import win32_edition
import pygame
import os
from anarchyChess.board import Board
from anarchyChess.chess_pieces import Bishop
from anarchyChess.constants import RED, WIDTH, HEIGHT

rect = (0, 0, 592, 592)
# from anarchyChess.board import Board

board = pygame.image.load(os.path.join("images", "board400x400.png"))

FPS = 60
WIN = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)  # width and height to be passed as a tuple
pygame.display.set_caption("anarchyChess")


def redraw_pygame_window():
    global WIN
    WIN.blit(board, (0, 0))
    # chess_board = Board(8, 8)
    chess_board.draw(WIN)
    # pygame.draw.rect(WIN, RED, (0, 0, 592, 592), 3)
    pygame.display.update()


def click(pos):
    """
    :return: pos (x, y) in range 0-7 0-7
    """
    x = pos[0]
    y = pos[1]
    if rect[1] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            xDiv = x - rect[0]
            yDiv = y - rect[0]
            i = int(xDiv / (rect[2] / 8))
            j = int(yDiv / (rect[3] / 8))
            return i, j


def main():
    run = True
    chess_board = Board(8, 8)
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        redraw_pygame_window()

        for event in pygame.event.get():
            # quitting the game by making run false
            if event.type == pygame.QUIT:
                run = False
            # when mouse is clicked, check if a piece was selected, if we are moving
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
            chess_board[j][i].isSelected = True

        # board.draw_square(WIN)
        # # to update after drawing after every loop iteration

    pygame.quit()


main()
