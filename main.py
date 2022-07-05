import pygame
from anarchyChess.constants import WIDTH, HEIGHT

FPS = 60
WIN = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)  # width and height to be passed as a tuple
pygame.display.set_caption("anarchyChess")


def main():
    run = True

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

    pygame.quit()


main()
