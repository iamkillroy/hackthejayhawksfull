

from .entity import Entity
from .entsignal import SIG
from cmath import log, e
import random


class WaveMaker(Entity):
    def __init__(self, x, y, screen) -> None:
        """This entity is supposed to make equally distributed logarithmic
        growth for enemy waves. Does it??"""
        self.entityName = "wavemaker"
        super().__init__(x, y, screen)
        self.currentWaveCounter = 0
        self.currentWaveTimer = 3
        self.waveEnemies = list()
    def update(self, dt):
        self.currentWaveTimer -= 1 * dt
        if self.currentWaveTimer < 0:
            print("got here")
            #reset the timer after each wave is done
            self.currentWaveTimer += 10 * (0.5 * self.currentWaveCounter + 1 )
            #okay now we finna do that stupid ahh shi where we have to make arbitrary logarithmic growth functions
            # we're gonna use that fancy smanczy signal system to transmit to make those
            # thanks godot! that concept is cool. sorry i don't love your engine so much to actually do it
            # in it
            redAmount = round(pow(e, self.currentWaveCounter)) if self.currentWaveCounter < 20 else 15 + random.randint(-5, 5)
            #return the signal amount for redfox
            print(f"red amount is {redAmount} ")
            return [SIG.NEWREDFOX for _ in range(redAmount)]
