from .entity import Entity
import pygame
from cmath import sin

class Heart(Entity):
    def __init__(self, x, y, screen):
        self.entityName = "hearts"
        super().__init__(x, y, screen)
        self.health = 5
        self.startX = x
        self.startY = y
        self.currentSin = 0
        # this is a carbon copy of the previous gamemap rescale, look for comments there
        self.sprites = list()
        scaledHeart = pygame.transform.scale_by(
            pygame.image.load(self.get_sprite_addr(0)), 3
        )
        self.sprites.append(scaledHeart)
    def fast_sin(self, x):
        #is this wholy necessary? not really, but i got frustrated with cmath and
        # wanted to have fun
        clampedx = self.clamp_to_fast_sin_range(x)
        return clampedx * (1-abs(clampedx))
    def clamp_to_fast_sin_range(self, x):
        #okay scary ahh function incoming
        fractionalRemainder = abs(x) - abs(int(x))
        if int(x) % 2 == 0: return fractionalRemainder
        oddDeterminant = ((int(x)-1) // 2) % 2
        if oddDeterminant == 0:
            return -1 + fractionalRemainder
        else:
            return 1 + fractionalRemainder

    def display(self):
        for i in range(self.health):
            self.screen.blit(
                self.sprites[self.spriteState], (self.x + (i * 60), self.y + round(30*self.fast_sin(self.currentSin+i*0.5)))
            )

    def update(self, dt):
        #i know i know
        # crucify him! he's using degrees in radians!
        # chill. 2pi is 6.28-- that's all ya need folks
        self.currentSin += 1 * dt if self.currentSin < 1 and self.currentSin > -1 else -1
        super().update(dt)
