import pygame
import os

# from .constants import RED, SQUARE_SIZE

# load images using pygame.image.load(os.path.join("images", "image-name.png"))
b_bishop = pygame.image.load(os.path.join("images", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("images", "black_king.png"))
b_knight = pygame.image.load(os.path.join("images", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("images", "black_pawn.png"))
b_rook = pygame.image.load(os.path.join("images", "black_rook.png"))
b_queen = pygame.image.load(os.path.join("images", "black_queen.png"))

w_bishop = pygame.image.load(os.path.join("images", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("images", "white_king.png"))
w_knight = pygame.image.load(os.path.join("images", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("images", "white_pawn.png"))
w_rook = pygame.image.load(os.path.join("images", "white_rook.png"))
w_queen = pygame.image.load(os.path.join("images", "white_queen.png"))


# scaling images
b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (74, 74)))

for img in w:
    W.append(pygame.transform.scale(img, (74, 74)))


class Piece:

    img_index = -1
    rect = (0, 0, 592, 592)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.selected = False

    # all possible pieces for the piece, knowing it's position in the grid and then figuring out
    # all other possible moves
    def move(self):
        pass

    # returns a boolean if the piece is selected
    def isSelected(self):
        return self.selected

    def draw(self, WIN):
        # img_index = -1
        if self.color == "w":
            draw_image = w[self.img_index]
        else:
            draw_image = b[self.img_index]

        x = 5 + round(self.startX + (self.col * self.rect[2] / 8))
        y = 7 + round(self.startY + (self.row * self.rect[2] / 8))

        WIN.blit(draw_image, (x, y))


class Bishop(Piece):
    img_index = 0


class King(Piece):
    img_index = 1


class Knight(Piece):
    img_index = 2


class Pawn(Piece):
    img_index = 3


class Queen(Piece):
    img_index = 4


class Rook(Piece):
    img_index = 5
