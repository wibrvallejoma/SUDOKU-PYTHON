import sys
import pygame
from pygame.locals import QUIT

WIDTH = 800
HEIGHT = 800

# COLORS
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class Grid:
    # need algorithm to design a sudoku grid 9x9
    def __init__(self):
        super().__init__()


def main():
    pygame.display.set_caption("Sudoku Python")
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        draw_grid(screen)

        pygame.display.flip()


def draw_grid(screen):
    gap_y = 10
    for row in range(9):
        gap_x = 10
        if row % 3 == 0 and row > 0:
            gap_y += 5
        for col in range(9):
            if col % 3 == 0 and col > 0:
                gap_x += 5
            pygame.draw.rect(screen, WHITE, ((col * 85) + gap_x, (row * 85) + gap_y, 80, 80))

def draw_rect(screen, i, x, y):
    pygame.draw.rect(screen, WHITE, ((i * x) + 10, y, 80, 80))


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    main()
