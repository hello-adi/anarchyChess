from .constants import RED, SQUARE_SIZE


class Piece:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0

    def calc_pos(self):
        pass
