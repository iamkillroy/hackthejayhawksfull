import sys

import pygame

import src.entity.gamemap as gamemap
import src.entity.selectbar as selectbar
import src.entity.enemy as enemy
import src.entity.wavemaker as wm
from src.entity.entsignal import SIG
RESOLUTION = (1920, 1080)


class MainWindow:

    class LAYERS:
        BACKGROUND = 0
        USERINTERFACE = 4
        SPRITELAYER1 = 1
        SPRITELAYER2 = 2
        SPRITELAYER3 = 3
    def __init__(self, type="game"):
        pygame.init()
        info = pygame.display.Info()
        self.realScreen = pygame.display.set_mode(
            (info.current_w, info.current_h), pygame.FULLSCREEN
        )
        self.screen = pygame.Surface(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.dt = 0 #this is my deltatime in seconds

        pygame.display.set_caption("Jayhawk Bash")
        self.running = True
        self.type = type
        self.entities = [[] for _ in range(5)]  # create five lists within a list
        # the reason we're doing this is tier. each list will get drawn over the other
        # and has superceding abilities
        # (0) - background
        # (1-3) - entities of varying superiority
        # (4) - the UI
        if self.type == "game":  # main game add entity
            self.entities[self.LAYERS.BACKGROUND].append(gamemap.GameMap(0, 0, self.screen))
            self.entities[self.LAYERS.USERINTERFACE].append(
                selectbar.SelectBar(0, 0, self.screen)
            )  # highest level
            self.entities[self.LAYERS.BACKGROUND].append(wm.WaveMaker(0,0, self.screen))
    def update(self):
        self.dt = self.clock.tick(60) / 1000.0 #recalculate the deltatime every frame, 60fps is our max
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
        signalAccum = [] #store all signals accumulated
        for entityTier in self.entities:
            # i know i know it's O(n^2)
            # and in python but for small maps
            # it's gonna be alright
            for entity in entityTier:
                resp = entity.update(self.dt)
                if resp is not None: #resp can be None, (SIG.xxxx), or a tuple of (SIG.xxxx, SIG.yyyy.....SIG.zzz)
                        #handle multiple signals which is the new default
                        subsignalArray = [[], entity]
                        for subsignal in resp:
                            subsignalArray[0].append(subsignal)
                        signalAccum.append(subsignalArray)
        # cast that fat scaled version onto the screen
        info = pygame.display.Info()
        scaled = pygame.transform.scale(self.screen, (info.current_w, info.current_h))
        #now we gotta handle signals which get executed the next frame after update

        #PER FRAME VARIABLES
        enemySpacing = 0
        for signal, entityOfSignal in signalAccum:
            for subsignal in signal:
                match subsignal:
                    case SIG.NOOP:
                        pass
                    case SIG.KILLME:
                        for tier in self.entities:
                            if entityOfSignal in tier:
                                tier.remove(entityOfSignal)
                                break #only one instance so we can cut the loop short
                    case SIG.FINISHEDCOURSE:
                        #TODO, deincrement hearts
                        pass
                    case SIG.NEWREDFOX:
                        print("gotnew sig")
                        #this means to add a new redfox. for each time this is called in frame,
                        # the signal handler will offset the x by -20 to make sure that there's
                        # consistent spacing on them
                        enemySpacing -= 20
                        newEnemy = enemy.Enemy(0 + enemySpacing, 825, self.screen, 10)
                        self.entities[MainWindow.LAYERS.SPRITELAYER1].append(newEnemy)
        self.realScreen.blit(scaled, (0, 0))  # 00 for the top
        pygame.display.flip()
