import sys

import pygame


class MainWindow:
    def __init__(self, type="game"):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.running = True

    def update(self):
        # first handle game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit(0)
        # okay now draw the display
        pygame.display.flip()
