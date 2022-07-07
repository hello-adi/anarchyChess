import pygame
import os
from anarchyChess.constants import WIDTH, HEIGHT
from anarchyChess.board import Board

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
b = [b_bishop, b_king, b_knight, b_pawn, b_rook, b_queen]
w = [w_bishop, w_king, w_knight, w_pawn, w_rook, w_queen]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale2x(img))

for img in w:
    W.append(pygame.transform.scale2x(img))

FPS = 60
WIN = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)  # width and height to be passed as a tuple
pygame.display.set_caption("anarchyChess")


def redraw_pygame_window():
    pygame.display.update()


def main():
    run = True
    board = Board()
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            # quitting the game by making run false
            if event.type == pygame.QUIT:
                run = False
            # when mouse is clicked, check if a piece was selected, if we are moving
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_square(WIN)
        # to update after drawing after every loop iteration
        redraw_pygame_window()

    pygame.quit()


main()
