import sys

import pygame

import src.entity.gamemap as gamemap
import src.entity.selectbar as selectbar

RESOLUTION = (1920, 1080)


class MainWindow:
    def __init__(self, type="game"):
        pygame.init()
        info = pygame.display.Info()
        self.realScreen = pygame.display.set_mode(
            (info.current_w, info.current_h), pygame.FULLSCREEN
        )
        self.screen = pygame.Surface(RESOLUTION)

        pygame.display.set_caption("Jayhawk Bash")
        self.running = True
        self.type = type
        self.entities = [[] for _ in range(5)]  # create five lists within a list
        print(self.entities)
        # the reason we're doing this is tier. each list will get drawn over the other
        # and has superceding abilities
        # (0) - background
        # (1-3) - entities of varying superiority
        # (4) - the UI
        if self.type == "game":  # main game add entity
            self.entities[0].append(gamemap.GameMap(0, 0, self.screen))
            self.entities[4].append(
                selectbar.SelectBar(0, 0, self.screen)
            )  # highest level

    def update(self):
        # first handle game loop
        self.screen.fill((0, 0, 0))  # clear each frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit(0)
        # okay now draw the display
        # IMPORTANT for future headaches
        # by doing this method, we're making it so that entites that are higher up
        # (larger index) get drawn over and supercede the lower stuff (such as background)
        #
        for entityTier in self.entities:
            # i know i know it's O(n^2)
            # and in python but for small maps
            # it's gonna be alright
            for entity in entityTier:
                entity.update()
        # cast that fat scaled version onto the screen
        info = pygame.display.Info()
        scaled = pygame.transform.scale(self.screen, (info.current_w, info.current_h))

        self.realScreen.blit(scaled, (0, 0))  # 00 for the top
        pygame.display.flip()
