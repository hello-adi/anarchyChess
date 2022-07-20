from platform import win32_edition
import pygame
import os
from anarchyChess.constants import WIDTH, HEIGHT

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
    pygame.display.update()


def main():
    run = True
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
                pass

        # board.draw_square(WIN)
        # # to update after drawing after every loop iteration

    pygame.quit()


main()
