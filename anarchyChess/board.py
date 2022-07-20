# board.py handles all the seperate pieces moving, deleting the pieces,
# drawing certain pieces and so on.

import pygame
from .constants import (
    BLACK,
    CREAM,
    GREEN,
    RED,
    ROWS,
    SQUARE_SIZE,
)  # dot constant for relative import


class Board:
    def __init__(self) -> None:
        # internal representaion in a  2D list
        self.board = []
        self.selected_piece = None
        # number of pieces left for red and white
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0

    # def draw_square(self, win):
    #     win.fill(GREEN)
    #     for row in range(ROWS):
    #         for col in range(row % 2, ROWS, 2):
    #             pygame.draw.rect(
    #                 win,
    #                 CREAM,
    #                 (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
    #             )

    def create_board(self):
        pass
