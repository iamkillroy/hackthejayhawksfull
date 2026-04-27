from pathlib import Path

import pygame


class Entity:
    def __init__(self, x, y, screen) -> None:
        self.x = x
        self.y = y
        self.sprite = 0
        self.spriteState = 0
        self.visible = True
        # get all sprites and load within the class object itself
        self.sprites: pygame.Surface = []
        spriteInitIterator = 0
        self.screen = screen
        while True:
            # we have to use the .exists because reading allegedly corrupts
            # the pointer for pygame
            path = self.get_sprite_addr(spriteInitIterator)
            if not path.exists():
                break  # break, we're done looping
            self.sprites.append(pygame.image.load(str(path)))  # add to the path
            spriteInitIterator += 1  # increase by one

    def get_sprite_addr(self, spriteState):
        """Gets the current active sprite for the entity"""
        img_path = Path(__file__).parents[2] / (
            "assets/sprites/" + self.entityName + str(spriteState) + ".png"
        )
        print(img_path.exists())
        print(img_path)
        return img_path

    def display(self):
        """Draws the current sprite state at the current x and y of the entity"""
        self.screen.blit(self.sprites[self.spriteState], (self.x, self.y))

    def update(self, optionalArgumentList=list()):
        self.display()
