import sys

import pygame


class MainWindow:
    def __init__(self, type="title"):
        pygame.init()
        info = pygame.display.Info()
        self.screen = pygame.display.set_mode(
            (info.current_w, info.current_h), pygame.FULLSCREEN
        )
        pygame.display.set_caption("Jayhawks Vs The Hackers")
        self.running = True
        self.type = type

    def update(self):
        # first handle game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit(0)
        # okay now draw the display

        pygame.display.flip()
